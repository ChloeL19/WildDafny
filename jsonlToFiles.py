import os
import json
import requests

def process_jsonl(input_file_path, output_directory):
    """
    Processes a JSONL file, writing the content of the 'dafny' field from each line to a separate file.

    :param input_file_path: Path to the input JSONL file.
    :param output_directory: Path to the directory where output files will be saved.
    
    # TODO: filter out the standalone files that do not compile, and test hint stripping with only those first
    
    
    # NEXT STEPS: how many loop invariants can GPT4 figure out? (first step) --> count how many I actually remove (grep for these things)
    (next step): are calc blocks a good thing to remove?
    then remove asserts (probably quite hard for the model to figure out, just so that code passes verifier)
    figure out lemmas entirely (remove entire body of a lemma)
    
    professor amin suggestion: 
    - filename.dfy 
    - filename_no_loop_invariants.dfy
    - filename_no_asserts.dfy [only generate if needed]
    
    *don't push yet, test ideas
    *when push, do proper dataset that follows licensing etc
    """
    def dafnyc(v):
        r = requests.post("https://dafny.livecode.ch/check", data = { 'v': v })
        r.raise_for_status()
        r = r.json()
        return r['status'] == 0
    
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each line in the JSONL file
    with open(input_file_path, 'r') as file:
        for i, line in enumerate(file):
            try:
                # Parse the JSON line
                data = json.loads(line)

                # Extract the 'dafny' field
                dafny_code = data.get('dafny', '')
                dafny_name = data.get('file', '')
                dafny_name = dafny_name[dafny_name.rindex("/")+1:]

                if not dafnyc(dafny_code):
                    continue
                # Write to a new file
                with open(os.path.join(output_directory, f"{dafny_name}"), 'w') as dafny_file:
                    dafny_file.write(dafny_code)
            

            except json.JSONDecodeError as e:
                # Log any JSON decode errors
                print(f"Error parsing line {i}: {e}")

    print("Processing complete.")

# Example usage:
if __name__ == "__main__":
    process_jsonl('standalone/dafny.jsonl', 'standalone/unpacked/')
