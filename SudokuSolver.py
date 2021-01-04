"""Summary: Automated sudoku solver
Description: This program does not have any access to the sudoku puzzle other than
what is visually displayed on the users screen. The program reads the screen using
OpenCV and determines the blank and numbered cells of the sudoku board. The cells
are then organized into their proper positions within a 2D list.  A recursive
function then tries all possible solutions. If the function works itself into a
dead end, it will back track. Once a solution is found, the cursor will enter the
correct values into the sudoku board on the website. This program is designed to
work on https://www.websudoku.com/

Author: Zennon Paul Weleschuk
"""

import pyautogui
import cv2 as cv
import numpy as np
from PIL import ImageGrab
from Cell import Cell
from Image import Image


def createImageList():
    # returns object list of images and its parameters
    imageList = []
    blank = cv.imread('photos/blank.png', 0)
    imageBlank = Image(blank, 0, 0.85, 255, 255, 153)
    imageList.append(imageBlank)
    one = cv.imread('photos/one.png', 0)
    imageOne = Image(one, 1, 0.85, 0, 0, 255)
    imageList.append(imageOne)
    two = cv.imread('photos/two.png', 0)
    imageTwo = Image(two, 2, 0.87, 65, 153, 255)
    imageList.append(imageTwo)
    three = cv.imread('photos/three.png', 0)
    imageThree = Image(three, 3, 0.87, 51, 255, 255)
    imageList.append(imageThree)
    four = cv.imread('photos/four.png', 0)
    imageFour = Image(four, 4, 0.85, 0, 255, 128)
    imageList.append(imageFour)
    five = cv.imread('photos/five.png', 0)
    imageFive = Image(five, 5, 0.87, 153, 255, 51)
    imageList.append(imageFive)
    six = cv.imread('photos/six.png', 0)
    imageSix = Image(six, 6, 0.85,255, 153, 51 )
    imageList.append(imageSix)
    seven = cv.imread('photos/seven.png', 0)
    imageSeven = Image(seven, 7, 0.87, 255, 0, 127)
    imageList.append(imageSeven)
    eight = cv.imread('photos/eight.png', 0)
    imageEight = Image(eight, 8, 0.84, 255, 51, 255)
    imageList.append(imageEight)
    nine = cv.imread('photos/nine.png', 0)
    imageNine = Image(nine, 9, 0.86, 0, 0, 0)
    imageList.append(imageNine)
    return imageList


def getFrame():
    # returns images of screen
    topOfScreen = 15
    leftSideOfScreen = 15
    screenWidth = 800
    screenHeight = 1000
    image = ImageGrab.grab(bbox=(topOfScreen, leftSideOfScreen, screenWidth, screenHeight))
    img_np = np.array(image)
    display = cv.cvtColor(img_np, cv.COLOR_BGR2RGB)
    frame = cv.cvtColor(img_np, cv.COLOR_BGR2GRAY)
    _, frame = cv.threshold(frame, 240, 255, cv.THRESH_BINARY)
    return frame, display


def findBlankTiles(frame, display):
    # returns list of blank cell objects
    unorderedCellList = []
    _, blankThres = cv.threshold(imageList[0].image, 240, 255, cv.THRESH_BINARY)
    w, h = imageList[0].image.shape[::-1]
    blankResult = cv.matchTemplate(frame, blankThres, cv.TM_CCOEFF_NORMED)
    blankLocation = np.where(blankResult >= imageList[0].threshold)
    rectangles = []
    for loc in list(zip(*blankLocation[::-1])):
        rect = [int(loc[0]), int(loc[1]), w, h]
        rectangles.append(rect)  # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)  # remove the duplicate results
    for i in range(len(rectangles)):
        cv.rectangle(display, (rectangles[i][0], rectangles[i][1]),
                 (rectangles[i][0] + rectangles[i][2], rectangles[i][1] + rectangles[i][3]),
                     (imageList[0].b, imageList[0].g, imageList[0].r), 2)
        cell = Cell(0, 0, rectangles[i][0], rectangles[i][1])
        unorderedCellList.append(cell)
    return unorderedCellList, display, frame


def findNumber(image, value, threshold, frame, display, b, g, r, unorderedCellList):
    # returns list of the numbers found in the image and print results
    _, frame = cv.threshold(frame, 240, 255, cv.THRESH_BINARY)
    w, h = image.shape[::-1]
    _, imageThres = cv.threshold(image, 240, 255, cv.THRESH_BINARY)
    imageResult = cv.matchTemplate(frame, imageThres, cv.TM_CCOEFF_NORMED)
    imageLocation = np.where(imageResult >= threshold)
    count = 0
    for pt in zip(*imageLocation[::-1]):
        cv.rectangle(display, pt, (pt[0] + w, pt[1] + h), (b, g, r), 2)
        cell = Cell(value,value, pt[0], pt[1])
        unorderedCellList.append(cell)
        count += 1
    if value == 1:
        print("Numbers Found")
        print("-" * 13)
    print(value, "'s: ", count, sep="")
    return unorderedCellList


def OrganizeCells(unorderedCellList):
    # returns a 9x9 2D list with the values in the correct position
    sudokuMatrix = []
    temp = []
    for j in range(9):
        unorderedCellList = sorted(unorderedCellList, key= lambda Cell: Cell.ypixel)
        for i in range(9):
            temp.append(unorderedCellList[i])  # takes the nine cells with the lowest y pixel values
        for i in range(9):
            del unorderedCellList[0]
        sortedRow = sorted(temp, key=lambda Cell: Cell.xpixel)  # sorting the nine cells by x pixel value
        temp = []
        sudokuMatrix.append(sortedRow)
    return sudokuMatrix


def printMatrix(matrix):
    # prints the original and solved sudoku Matrix
    for y in range(len(matrix)):
        print(" ")
        for x in range(len(matrix)):
            print(matrix[y][x].originalValue, end=" ")
    print("\nStarting Sudoku Grid")
    print(" ")
    for y in range(len(matrix)):
        print(" ")
        for x in range(len(matrix)):
            print(matrix[y][x].newValue, end=" ")
    print("\nSolved Sudoku Grid")


def possibleValue(y, x, n):
    # return True if value is not found in the row, column, or sub-grid
    for i in range(9):
        if sudokuMatrix[y][i].originalValue == n:  # check rows
            return False
    for i in range(9):
        if sudokuMatrix[i][x].originalValue == n:  # check column
            return False
    xSubMatrix = (x // 3) * 3
    ysubMatrix = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudokuMatrix[ysubMatrix + i][xSubMatrix + j].originalValue == n:  # check 3x3 sub-grid
                return False
    return True


def solve():
    # brute force recursive function that will back track if it gets into a dead end
    for y in range(9):
        for x in range(9):
            if sudokuMatrix[y][x].originalValue == 0:
                for n in range(1, 10):
                    if possibleValue(y, x, n):
                        sudokuMatrix[y][x].originalValue = n
                        solve()
                        sudokuMatrix[y][x].originalValue = 0
                return
    #once the solution is found assign the new values
    for y in range(len(sudokuMatrix)):
        for x in range(len(sudokuMatrix)):
            sudokuMatrix[y][x].newValue = sudokuMatrix[y][x].originalValue


def completeTheSudoku(sudokuMatrix):
    # clicks on the tiles and enters the correct number
    for y in range(9):
        for x in range(9):
            if sudokuMatrix[y][x].originalValue == 0:
                pyautogui.click(sudokuMatrix[y][x].xpixel + 25, sudokuMatrix[y][x].ypixel + 25)
                #there is a bug that occurs when using both openCV and pyautogui in that the pixel locations are offset
                tempValue = str(sudokuMatrix[y][x].newValue)
                pyautogui.typewrite(tempValue)


frame, display = getFrame()
imageList = createImageList()
unorderedCellList, display, frame = findBlankTiles(frame, display)
for i in range(1, len(imageList)):
    unorderedCellList = findNumber(imageList[i].image, imageList[i].value, imageList[i].threshold, frame, display,
              imageList[i].b, imageList[i].g, imageList[i].r, unorderedCellList)
cv.imshow("display", display)
cv.moveWindow("display", 1000, 0)
cv.waitKey(1)
sudokuMatrix = OrganizeCells(unorderedCellList)
solve()
printMatrix(sudokuMatrix)
completeTheSudoku(sudokuMatrix)
cv.waitKey(0)
cv.destroyAllWindows()
