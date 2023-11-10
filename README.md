# WildDafny

To clone this repo with its submodules, execute the following:

`git clone --recurse-submodules https://github.com/ChloeL19/WildDafny.git`

### Dependencies

TODO

### Usage
To compile the modified Dafny compiler which will strip hints from Dafny files, run:

`dotnet build dafny/Source/Dafny.sln`

To run the hint striper on all of the downloaded submodules (dafny repos), run:

`dafny/Binaries/Dafny.exe index.dfy`

