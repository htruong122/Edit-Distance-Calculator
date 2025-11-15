# Edit Distance Calculator

A Python program that calculates the edit distance (Levenshtein distance) between two words and displays the calculation matrix and alignment. Available in both command-line and graphical user interface (GUI) versions.

## Assignment Requirements

Programming Assignment (due Nov 21): Write a program to calculate the edit distance between two words and output both the matrix of distance calculation and an alignment that demonstrates the result.

## Features

- Calculates edit distance using dynamic programming
- Displays the complete calculation matrix with separators
- **Graphical user interface** (edit_distance_gui.py)

## How to Run
Simply run the GUI version from the command line:

```bash
python edit_distance_gui.py
```

A window will pop up looking like this:
- Input fields for two words
- "Calculate" button to compute edit distance
- "Clear" button to reset all fields
- Scrollable results area showing the matrix and alignment

![pop up image](ex_img/popup_screen.png)


## Example Output Inside Result Box

For the words "evaluation" and "elution":

```
The matrix:

     0   1   2   3   4   5   6   7
   --------------------------------
0 |  0:  1:  2:  3:  4:  5:  6:  7:
   --------------------------------
1 |  1:  0:  1:  2:  3:  4:  5:  6:
   --------------------------------
2 |  2:  1:  1:  2:  3:  4:  5:  6:
   --------------------------------
3 |  3:  2:  2:  2:  3:  4:  5:  6:
   --------------------------------
4 |  4:  3:  2:  3:  3:  4:  5:  6:
   --------------------------------
5 |  5:  4:  3:  2:  3:  4:  5:  6:
   --------------------------------
6 |  6:  5:  4:  3:  3:  4:  5:  6:
   --------------------------------
7 |  7:  6:  5:  4:  3:  4:  5:  6:
   --------------------------------
8 |  8:  7:  6:  5:  4:  3:  4:  5:
   --------------------------------
9 |  9:  8:  7:  6:  5:  4:  3:  4:
   --------------------------------
10 | 10:  9:  8:  7:  6:  5:  4:  3:
   --------------------------------

The edit distance is: 3

Alignment is:
evaluation
e__lu_tion
```

## Implementation Details

- Uses O(mn) space and time complexity where m and n are the lengths of the two words
- Traceback algorithm finds an optimal alignment path through the matrix
- Input is case-insensitive (converted to lowercase)
- Non-alphabetic characters are automatically filtered out

## Testing

To test with different word pairs:

### Using GUI:
1. Run `python edit_distance_gui.py`
2. Type first word in the "The first word:" field
3. Type second word in the "The second word:" field
4. Click "Calculate" button (or press Enter)
5. View results in the scrollable area below


## Files Included

- **edit_distance_gui.py** - GUI version with graphical interface 
- **README.md** - This documentation file

## Requirements

- Python 3.6 or higher
- tkinter (for GUI version - usually included with Python)

### Setting Up Your Environment:

**For Windows:**
1. Download and install Python from [python.org](https://www.python.org/downloads/)
2. During installation, make sure to check "Add Python to PATH"
3. Verify installation by opening Command Prompt (cmd) and typing:
   ```bash
   python --version
   ```
4. tkinter should be included by default. To verify, run:
   ```bash
   python -m tkinter
   ```
   A small window should appear if tkinter is properly installed.

### Running the Program:

1. Open a terminal/command prompt
2. Navigate to the directory containing `edit_distance_gui.py`
3. Run the command:
   ```bash
   python edit_distance_gui.py
   ```
   or on some systems:
   ```bash
   python3 edit_distance_gui.py
   ```
4. A graphical window will appear. Enter your two words and click "Calculate" or press Enter.

### Development Environment:

This program was developed and tested using:
- Python 3.8+
- tkinter 8.6+
- Windows 11, but is cross-platform compatible

No additional external libraries or packages are required beyond the Python standard library.

## Author

Helen Truong
Created for Programming Assignment due Nov 21
