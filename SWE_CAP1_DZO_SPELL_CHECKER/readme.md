# Dzongkha Spell Checker

## Project overview
This project implements a spell checker for Dzongkha, Bhutan’s national language. This code compares the Dzongkha words in the script file with the dzongkha dictionary and identifies spelling mistakes in the script. To do this, the first step is to filer out the dzongkha dictionary only then can we compare the words. 

## Table of Contents
-[Usage](#usage)
-[Implementation Details](#implementation-details)
-[Data Structures](#data-structure)
-[Algorithms](#algorithms)
-[Future Improvements](#future-improvements)
-[References](#references)

## Usage
The script is compared with the dictionary, then it is processed and identifies the words that do not match and prints out the incorrect words along with their line and positions.

```bash
python spell_check.py 365.txt
```
## Implementation Details
The spell checker reads the input file, splits the text into individual words and checks if each word exists in the Dzongkha dictionary or not.
The dictionary is then loaded from a file containing the correct Dzongkha words and incorrect words are identified with their line numbers and positions in the text and are printed.

## Data Structures
Sets: The Dzongkha dictionary is stored in a set to allow fast lookup of words.
Lists: The input text is split into a list of words, and incorrect words are stored in a list with their corresponding line numbers and positions.

## Algorithms
The algorithm used is a linear search for word matching.
Each word in the script file is compared against the dictionary.
Regular expressions are used to filter out non-Dzongkha(english) words and special characters.
The spell checker operates line by line to track word positions and line numbers of the script file

## Performance Analysis
Time Complexity: Comparing each word by word involves a constant-time lookup in a set, so the time complexity is O(n), where n is the number of words in the script file.
Space Complexity: The space complexity is determined by the size of the dictionary and the number of words in the script file.

## Challenges and Solutions
Challenge: First chanllenge faced is not being able to filter out the non-dzongkha(english, special chars) words from the dictionary. Secondly, couldn't comapre the script file and the dictionary to print out the incorrect words
Solution: Used regular expressions to filter out non-Dzongkha words and only check valid Dzongkha words.

## Future Improvements
Expand the dictionary to include more words.
Add support for checking grammar in addition to spelling.
Optimize the algorithm for larger files and spell checking.

## References
youtube=https://youtu.be/e7sX3nHjZ5Y
https://youtu.be/2SSr-RVAwIg
https://youtu.be/JE7qXaF806Q?si=lOPHpqc8iDMbA10E
chat gpt=https://chatgpt.com/c/67124a5a-c170-8004-a101-20b277c17fba#usage