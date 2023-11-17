def process_jsonl(input_file_path, output_directory):
    """
    Processes a JSONL file, writing the content of the 'dafny' field from each line to a separate file.

    :param input_file_path: Path to the input JSONL file.
    :param output_directory: Path to the directory where output files will be saved.
    """
    import os
    import json

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

                # Write to a new file
                with open(os.path.join(output_directory, f"{i}.dfy"), 'w') as dafny_file:
                    dafny_file.write(dafny_code)

            except json.JSONDecodeError as e:
                # Log any JSON decode errors
                print(f"Error parsing line {i}: {e}")

    print("Processing complete.")

# Example usage:
# process_jsonl('/path/to/input/dafny.jsonl', '/path/to/output/directory/')
