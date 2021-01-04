# Automated_Sudoku_Solver
Summary: Automated sudoku solver

Description: This program does not have any access to the sudoku puzzle other than
what is visually displayed on the users screen. The program reads the screen using
OpenCV and determines the blank and numbered cells of the sudoku board. The cells
are then organized into their proper positions within a 2D list.  A recursive
function then tries all possible solutions. If the function works itself into a
dead end, it will back track. Once a solution is found, the cursor will enter the
correct values into the sudoku board on the website. This program is designed to
work on https://www.websudoku.com/

Author: Zennon Paul Weleschuk

![gif of program solving sudoku]( ZennonWeleschuk/Automated_Sudoku_Solver/demos/sudokuGif.gif)
