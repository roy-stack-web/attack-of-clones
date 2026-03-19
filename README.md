# Attack of the Clones (GSoC 2026)

## Overview
This project focuses on detecting duplicated vulnerable code across codebases using security patches.

## Current Progress
- Implemented a patch parser in Python
- Extracts:
  - Removed (potentially vulnerable) code
  - Added (fixed) code

## Example
- Input: Patch file  
- Output: Separated vulnerable and fixed code segments

## Next Steps
- Convert extracted code into generalized patterns (regex)
- Detect similar vulnerable code across codebases
- Automate reporting of potential clone attacks

## Tech Stack
- Python
- Git

## Recent Progress

- Implemented basic regex pattern generation from vulnerable code
- Performed pattern matching on sample code snippets
- Successfully detected multiple variations of vulnerable function usage

## Sample Output

Pattern: strcpy\s*\(.*\)  
Matched: strcpy(buf, data);  
Matched: strcpy(user, input);  

Pattern: printf\s*\(.*\)  
Matched: printf('hello');  
Matched: printf(user);
