#!/usr/bin/env python3
"""
Edit Distance Calculator with GUI
Calculates the edit distance (Levenshtein distance) between two words
and displays the calculation matrix and alignment in a graphical interface.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox


def calculate_edit_distance(word1, word2):
    """
    Calculate edit distance using dynamic programming.
    Returns the distance matrix and the final edit distance.
    """
    m, n = len(word1), len(word2)
    
    # Create matrix with dimensions (m+1) x (n+1)
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # Characters match, no operation needed
                matrix[i][j] = matrix[i-1][j-1]
            else:
                # Take minimum of insert, delete, or substitute
                matrix[i][j] = 1 + min(
                    matrix[i-1][j],      # deletion
                    matrix[i][j-1],      # insertion
                    matrix[i-1][j-1]     # substitution
                )
    
    return matrix, matrix[m][n]


def format_matrix(matrix, word1, word2):
    """
    Format the edit distance matrix as a string for display.
    """
    output = "The matrix:\n\n"
    
    # Print column numbers header
    header = "  "
    for j in range(len(word2) + 1):
        header += f"{j:4}"
    output += header + "\n"
    
    # Print separator line
    output += "   " + "-" * (len(header)-3) + "\n"
    
    # Print first row (empty string with row number 0)
    row = "0 |"
    for j in range(len(word2) + 1):
        row += f"{matrix[0][j]:3}:"
    output += row + "\n"
    output += "   " + "-" * (len(row) - 3) + "\n"
    
    # Print remaining rows with row numbers
    for i in range(1, len(word1) + 1):
        row = f"{i} |"
        for j in range(len(word2) + 1):
            row += f"{matrix[i][j]:3}:"
        output += row + "\n"
        output += "   " + "-" * (len(row) - 3) + "\n"
    
    return output


def traceback_alignment(matrix, word1, word2):
    """
    Trace back through the matrix to find an optimal alignment.
    Returns the aligned strings.
    """
    i, j = len(word1), len(word2)
    aligned_word1 = []
    aligned_word2 = []
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            # Characters match
            aligned_word1.insert(0, word1[i-1])
            aligned_word2.insert(0, word2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + 1:
            # Substitution
            aligned_word1.insert(0, word1[i-1])
            aligned_word2.insert(0, word2[j-1])
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or matrix[i][j] == matrix[i][j-1] + 1):
            # Insertion (gap in word1)
            aligned_word1.insert(0, '_')
            aligned_word2.insert(0, word2[j-1])
            j -= 1
        elif i > 0:
            # Deletion (gap in word2)
            aligned_word1.insert(0, word1[i-1])
            aligned_word2.insert(0, '_')
            i -= 1
    
    return ''.join(aligned_word1), ''.join(aligned_word2)


class EditDistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Helen Truong - Edit Distance Calculator")
        self.root.geometry("700x600")
        
        # Configure style
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Verdana', 14, 'bold'))
        style.configure('Header.TLabel', font=('Verdana', 10, 'bold'))
        style.configure('TLabelframe.Label', font=('Verdana', 11, 'bold'))  # LabelFrame title font
        
        # Main container
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Welcome to Helen's Edit Distance", 
                                style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Input Words For The Edit Distance", padding="10")
        input_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # First word
        ttk.Label(input_frame, text="The first word:", font=('Verdana', 11, 'italic')).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.word1_entry = ttk.Entry(input_frame, width=30, font=('Verdana', 10, 'bold'))
        self.word1_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Second word
        ttk.Label(input_frame, text="The second word:", font=('Verdana', 11, 'italic')).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.word2_entry = ttk.Entry(input_frame, width=30, font=('Verdana', 10, 'bold'))
        self.word2_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Buttons frame
        buttons_frame = ttk.Frame(input_frame)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # Configure button style
        style.configure('Big.TButton', font=('Verdana', 11, 'italic'))
        
        # Calculate button
        self.calculate_btn = ttk.Button(buttons_frame, text="Calculate ", 
                                        command=self.calculate, style='Big.TButton', width=10)
        self.calculate_btn.grid(row=0, column=0, padx=(0, 1))
        
        # Clear button
        self.clear_btn = ttk.Button(buttons_frame, text="Clear", 
                                    command=self.clear_all, style='Big.TButton', width=10)
        self.clear_btn.grid(row=0, column=1)
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Scrolled text for output
        self.results_text = scrolledtext.ScrolledText(results_frame, width=70, height=25, 
                                                       font=('Courier', 9), wrap=tk.NONE)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for resizing
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Bind Enter key to calculate
        self.word1_entry.bind('<Return>', lambda e: self.calculate())
        self.word2_entry.bind('<Return>', lambda e: self.calculate())
        
        # Focus on first entry
        self.word1_entry.focus()
    
    def calculate(self):
        """Calculate and display edit distance results."""
        # Get input
        word1 = self.word1_entry.get().strip().lower()
        word2 = self.word2_entry.get().strip().lower()
        
        # Remove non-alphabetic characters
        word1 = ''.join(c for c in word1 if c.isalpha())
        word2 = ''.join(c for c in word2 if c.isalpha())
        
        # Validate input
        if not word1 or not word2:
            messagebox.showerror("Error", "Both words must be non-empty!")
            return
        
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        
        # Calculate edit distance
        matrix, distance = calculate_edit_distance(word1, word2)
        
        # Format and display matrix
        matrix_output = format_matrix(matrix, word1, word2)
        self.results_text.insert(tk.END, matrix_output)
        
        # Display edit distance
        self.results_text.insert(tk.END, f"\nThe edit distance is: {distance}\n\n")
        
        # Display alignment
        aligned1, aligned2 = traceback_alignment(matrix, word1, word2)
        self.results_text.insert(tk.END, "Alignment is:\n")
        self.results_text.insert(tk.END, f"{aligned1}\n")
        self.results_text.insert(tk.END, f"{aligned2}\n")
        
        # Scroll to top
        self.results_text.see(1.0)
    
    def clear_all(self):
        """Clear all input fields and results."""
        self.word1_entry.delete(0, tk.END)
        self.word2_entry.delete(0, tk.END)
        self.results_text.delete(1.0, tk.END)
        self.word1_entry.focus()


def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = EditDistanceGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
