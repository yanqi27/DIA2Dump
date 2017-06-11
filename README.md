## Dia2Dump

Based on Windows Dia2Dump sample, this fork adds an option `-id` to print out pdb's debug identifier and code identifier if input is an exe or dll.

### Usage
You can invoke the program to print out a pdb's debug id. Or you can embed it in your script to search for a particular id (see file script/search_id.py)
```shell
Dia2Dump.exe -id Endeavor.pdb
Endeavor.pdb,CFC6A435CBCA43378B380045C2CB5A5C1

Dia2Dump.exe -id Endeavor.exe
Endeavor.pdb,CFC6A435CBCA43378B380045C2CB5A5C1
Endeavor.exe,5938895960F2000

python.exe search_id.py F:\pdbs CFC6A435CBCA43378B380045C2CB5A5C1
F:\pdbs\7.x\Endeavor.pdb
```
### Reference

* [DIA(Debug Interface Access)](https://docs.microsoft.com/en-us/visualstudio/debugger/debug-interface-access/debug-interface-access-sdk)
* [Breakpad dump_syms.exe](https://github.com/google/breakpad)
