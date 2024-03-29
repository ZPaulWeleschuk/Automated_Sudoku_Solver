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

Author: Z. Paul Weleschuk

![gif of program solving sudoku](https://github.com/ZennonWeleschuk/Automated_Sudoku_Solver/blob/main/demos/sodukoGif.gif "Figure 1: GIF of program entering the solution into the sudoku on the website")<br/>Figure 1: GIF of program entering the solution into the sudoku on the website<br/><br/>
![image detection of blank and numbered cells](https://github.com/ZennonWeleschuk/Automated_Sudoku_Solver/blob/main/demos/visionOutput.PNG)![number detected on nefw sudoku](https://github.com/ZennonWeleschuk/Automated_Sudoku_Solver/blob/main/demos/numbersFound.PNG)<br/>Figure 2: Image recognition of blank and numbered cells<br/><br/>
![starting matrix and solution](https://github.com/ZennonWeleschuk/Automated_Sudoku_Solver/blob/main/demos/sudokuMatrixs.PNG "Figure 3: Starting matrix and solution")
<br/>Figure 3: Starting matrix and solution

# Complete code walk through presentation
PDF [Simplified Guide to Computer Vision: Sodoku Solver](https://github.com/ZPaulWeleschuk/Automated_Sudoku_Solver/raw/main/demos/ZPWeleschuk_OpenCV_SudokuSolver.pdf)


![pdf guide](https://github.com/ZPaulWeleschuk/Automated_Sudoku_Solver/blob/main/demos/ZPW-OpenCV-SudokuSolver-TitlePage.PNG)


# Accompanying video walk through
[Watch video here](https://www.youtube.com/watch?v=CXCErJgHIHg)
