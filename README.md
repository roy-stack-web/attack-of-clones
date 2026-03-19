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
