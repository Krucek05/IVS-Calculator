############################################################################
## @file calculator_GUI.py
## @brief GUI for Calculator, IVS 2025
## @date 17.4.2025
## @author: Rastislav Šerý <xseryra00>
##
## Logic behind graphic user face and processing inputs
############################################################################


import math
import sys
from config import Configuration
from help import helpWindow

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QKeyEvent
from PyQt6.QtWidgets import (QApplication, QGridLayout,
                             QWidget, QLineEdit, QVBoxLayout, QPushButton,
                             QSizePolicy)

from math_library import add, sub, multiply, divide, power, n_root, factorial, modulo

class Window(QWidget):
    argumentProcessed = 1
    firstArgument = ""
    secondArgument = ""
    operation = ""
    result = ""
    fullText = ""
    wasError = False

    ############################################################################
    ## @brief Function to process second root
    ############################################################################

    def secondRoot(self):
        if self.secondArgument != "":
            self.makeNumSecArg()
            try:
                self.secondArgument = str(n_root(self.secondArgument, 2))
            except Exception as e:
                self.wasError = True
                self.firstArgument = f"Error: {e}"
        else:
            self.operation = ""
            self.makeNumFirstArg()
            try:
                self.firstArgument = str(n_root(self.firstArgument, 2))
            except Exception as e:
                self.wasError = True
                self.firstArgument = f"Error: {e}"

    ############################################################################
    ## @brief Function to process second power
    ############################################################################
    def secondPower(self):
        if self.secondArgument != "":
            self.makeNumSecArg()
            try:
                self.secondArgument = str(power(self.secondArgument, 2))
            except Exception as e:
                self.wasError = True
                self.firstArgument = f"Error: {e}"
        else:
            self.operation = ""
            self.makeNumFirstArg()
            try:
                self.firstArgument = str(power(self.firstArgument, 2))
            except Exception as e:
                self.wasError = True
                self.firstArgument = f"Error: {e}"

    ############################################################################
    ## @brief Converts first argument to int/float based on whether there is comma
    ############################################################################
    def makeNumFirstArg(self):
        if ('.' not in self.firstArgument) and ('.' not in self.secondArgument):
            self.firstArgument = int(self.firstArgument)
        else:
            self.firstArgument = float(self.firstArgument)

    ############################################################################
    ## @brief Converts first argument to int/float based on whether there is comma
    ############################################################################
    def makeNumSecArg(self):
        if ('.' not in str(self.firstArgument)) and ('.' not in self.secondArgument):
            self.secondArgument = int(self.secondArgument)
        else:
            self.secondArgument = float(self.secondArgument)

    ############################################################################
    ## @brief Updates display on calculator
    ############################################################################
    def displayUpdate(self):
        if len(self.firstArgument + self.operation + self.secondArgument) > 31:
            self.displayText.setFont(QFont(Configuration.font, 12))
        elif len(self.firstArgument + self.operation + self.secondArgument) > 15:
            self.displayText.setFont(QFont(Configuration.font, 15))
        else:
            self.displayText.setFont(QFont(Configuration.font, 30))

        if self.secondArgument != "":
            self.makeNumSecArg()
            if self.secondArgument < 0:
                self.secondArgument = str(self.secondArgument)
                self.displayText.setText(self.firstArgument + self.operation + "(" + self.secondArgument + ")")
            else:
                self.secondArgument = str(self.secondArgument)
                self.displayText.setText(self.firstArgument + self.operation + self.secondArgument)
        else:
            self.displayText.setText(self.firstArgument + self.operation + self.secondArgument)

        self.displayText.setCursorPosition(0)

    ############################################################################
    ## @brief Adds clicked number to processed argument
    ## @param number Clicked number
    ############################################################################
    def numberClicked(self, number):
        if self.argumentProcessed == 1:
            if self.firstArgument == "0":
                self.firstArgument = ""
            self.firstArgument += number
        else:
            if self.secondArgument == "0":
                self.secondArgument = ""
            self.secondArgument += number

    ############################################################################
    ## @brief Logic to get result after "=" is clicked
    ############################################################################
    def equalsClicked(self):
        if (self.operation != "") and (self.firstArgument != "") and (self.secondArgument != ""):
            self.makeNumFirstArg()
            self.makeNumSecArg()
            if self.operation == "+":
                try:
                    self.result = add(self.firstArgument, self.secondArgument)
                except Exception as e:
                    self.wasError = True
                    self.result = f"Error: {e}"
            elif self.operation == "-":
                try:
                    self.result = sub(self.firstArgument, self.secondArgument)
                except Exception as e:
                    self.wasError = True
                    self.result = f"Error: {e}"
            elif self.operation == "*":
                try:
                    self.result = multiply(self.firstArgument, self.secondArgument)
                except Exception as e:
                    self.wasError = True
                    self.result = f"Error: {e}"
            elif self.operation == "/":
                try:
                    self.result = divide(self.firstArgument, self.secondArgument)
                except Exception as e:
                    self.wasError = True
                    self.result = f"Error: {e}"
            elif self.operation == "^":
                try:
                    self.result = power(self.firstArgument, self.secondArgument)
                except Exception as e:
                    self.wasError = True
                    self.result = f"Error: {e}"
            elif self.operation == "√":
                try:
                    self.result = n_root(self.secondArgument, self.firstArgument)
                except Exception as e:
                    self.wasError = True
                    self.result = f"Error: {e}"
            elif self.operation == "%":
                try:
                    self.result = modulo(self.firstArgument, self.secondArgument)
                except Exception as e:
                    self.wasError = True
                    self.result = f"Error: {e}"

    ############################################################################
    ## @brief Processes result to first argument, so we can use it again for calculations
    ## @param newOperation operation to add after first argument
    ##
    ## Takes result after calculation and if instead "=" some other operation
    ## was used it adds it after the first argument
    ############################################################################
    def isResult(self, newOperation):
        try:
            self.firstArgument = str(self.result)
        except:
            self.wasError = True
            self.firstArgument = "Error: Result has too many digits"
        self.operation = newOperation
        self.secondArgument = ""
        self.result = ""

    ############################################################################
    ## @brief Logic to clear display of calculator after "C" is clicked
    ############################################################################
    def clearClicked(self):
        if self.argumentProcessed == 2:
            if self.secondArgument == "":
                self.clear()
            else:
                self.secondArgument = ""
        else:
            self.clear()

    ############################################################################
    ## @brief clears operation, first argument and number of processed argument
    ############################################################################
    def clear(self):
        self.argumentProcessed = 1
        self.firstArgument = ""
        self.operation = ""

    ############################################################################
    ## @brief Logic after some mathematical operation is clicked
    ############################################################################
    def operationClicked(self, operation):
        self.operation = operation
        self.argumentProcessed = 2

    ############################################################################
    ## @brief Logic to add comma at the end of processed argument
    ############################################################################
    def commaClicked(self):
        if self.argumentProcessed == 1 and ('.' not in self.firstArgument) and self.firstArgument != "":
            self.firstArgument += '.'
        elif self.argumentProcessed == 2 and ('.' not in self.secondArgument) and self.secondArgument != "":
            self.secondArgument += '.'

    ############################################################################
    ## @brief Logic to calculate factorial of number
    ############################################################################
    def factorial(self):
        if ('.' not in self.firstArgument) and (not self.secondArgument):
            self.makeNumFirstArg()
            try:
                self.firstArgument = str(factorial(self.firstArgument))
            except Exception as e:
                self.wasError = True
                self.firstArgument = f"Error: {e}"

        elif '.' not in self.secondArgument and self.secondArgument != "":
            self.makeNumSecArg()
            try:
                self.secondArgument = str(factorial(self.secondArgument))
            except Exception as e:
                self.wasError = True
                self.firstArgument = f"Error: {e}"

    ############################################################################
    ## @brief Function that makes from processed argument pi
    ############################################################################
    def pi(self):
        if self.argumentProcessed == 1:
            self.firstArgument = str(math.pi)
        else:
            self.secondArgument = str(math.pi)

    ############################################################################
    ## @brief Changes sign of processed argument
    ############################################################################
    def changeSign(self):
        if self.argumentProcessed == 2 and self.secondArgument != "":
            self.makeNumSecArg()
            self.secondArgument *= -1
            self.secondArgument = str(self.secondArgument)
        elif self.firstArgument != "":
            self.makeNumFirstArg()
            self.firstArgument *= -1
            self.firstArgument = str(self.firstArgument)

    ############################################################################
    ## @brief Checks what was clicked and call function for processing
    ############################################################################
    def buttonClick(self):
        buttonText = self.sender().text()
        self.processClickedCharacter(buttonText)
        self.setFocus()

    ############################################################################
    ## @brief processes character which was pressed and call right function based on that
    ##
    ## @param buttonText Text of the pressed button
    ############################################################################

    def processClickedCharacter(self, buttonText):
        if self.wasError:
            self.wasError = False
            self.firstArgument = ""
            self.secondArgument = ""
            self.operation = ""

        if '0' <= buttonText <= '9':
            self.numberClicked(buttonText)

        elif buttonText == '=':
            if (self.operation != "") and (self.secondArgument != ""):
                self.equalsClicked()
                self.isResult("")
                self.argumentProcessed = 1
        elif buttonText == ",":
            self.commaClicked()

        elif buttonText in ("C", "c"):
            self.clearClicked()

        elif buttonText == 'π':
            self.pi()
        elif self.firstArgument != "":
            if buttonText == "²√":
                self.secondRoot()
            elif buttonText == "a²":
                self.secondPower()
            elif buttonText == "!":
                self.factorial()
            elif buttonText == '±':
                self.changeSign()

            elif self.secondArgument == "":
                if buttonText == "aˣ":
                    buttonText = "^"
                elif buttonText == "ˣ√":
                    buttonText = "√"
                self.operationClicked(buttonText)
            elif buttonText != "aˣ" or buttonText != "ˣ√":
                self.equalsClicked()
                self.isResult(buttonText)
        self.displayUpdate()

    ############################################################################
    ## @brief Checks what was clicked and call function for processing
    ############################################################################
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            keyText = '='
        else:
            keyText = event.text()
        if keyText == '^':
            keyText = "aˣ"
        if (keyText in Configuration.buttons) or (keyText == "c"):
            self.processClickedCharacter(keyText)

    ############################################################################
    ## @brief Function that adds buttons to calculator
    ##
    ## @param colAmount Number of columns
    ## @param buttonList List of all buttons we want to be in there
    ############################################################################

    def buttonsCreation(self, colAmount, buttonList):
        row, col = 0, 0
        for symbol in buttonList:
            color = Configuration.bottomLineColor
            color2 = Configuration.bottomLineColorHovered
            if row < 1 and col > 2:
                color = Configuration.clearColor
                color2 = Configuration.clearColorHovered
            if '0' <= symbol <= '9':
                color = Configuration.numbersColor
                color2 = Configuration.numbersColorHovered
            if (row > 0 and col > 3) or (row == 0 and col < 3) or (col < 1 and row < 4):
                color = Configuration.operationColor
                color2 = Configuration.operationColorHovered

            button = self.buttonAttributes(symbol, color, color2)
            self.gridLayout.addWidget(button, row, col)
            col += 1
            if col > colAmount - 1:
                row += 1
                col = 0

    ############################################################################
    ## @brief Functions that gives buttons its attribute e.g. color, symbol...
    ##
    ## @param symbol Which symbol will be on the button
    ## @param color Which Color will normally be on the button
    ## @param color2 Color that will be on button when mouse is hovering over it
    ############################################################################
    def buttonAttributes(self, symbol, color, color2):
        button = QPushButton(symbol)
        button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button.setFont(self.font)
        button.clicked.connect(self.buttonClick)  # Connect to function
        button.setStyleSheet(Configuration.buttonStyle % (color, color2))
        return button

    ############################################################################
    ## @brief Function that is called when help button is pressed and shows help
    ############################################################################
    def showHelp(self):
        help = helpWindow()
        help.exec()

    ############################################################################
    ## @brief Initializes calculator window and builds all buttons
    ############################################################################
    def __init__(self):
        super().__init__()

        #Setup for window
        self.setWindowTitle(Configuration.windowTitle)
        self.setWindowIcon(QIcon(Configuration.icon))
        self.setGeometry(Configuration.windowSize[0], Configuration.windowSize[1], Configuration.windowSize[2], Configuration.windowSize[3])
        self.setStyleSheet("background: %s" % Configuration.background)
        self.font = QFont(Configuration.font, 22, QFont.Weight.Bold)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        layout = QVBoxLayout()

        #Setup of Help button
        helpButton = QPushButton("?")
        helpButton.setFixedSize(20, 20)
        helpButton.setStyleSheet(Configuration.helpButtonStyle)

        helpButton.clicked.connect(self.showHelp)
        layout.addWidget(helpButton)
        layout.setContentsMargins(7, 3, 7, 3)

        #Setup for text box
        self.displayText = QLineEdit()
        self.displayText.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.displayText.setFont(QFont(Configuration.font, 30))
        self.displayText.setReadOnly(True)
        self.displayText.setStyleSheet(Configuration.displayStyle % Configuration.background)
        self.displayText.setFixedHeight(Configuration.heightTextDisplay)

        layout.addWidget(self.displayText)

        #Setup for buttons
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.buttonsCreation(5, Configuration.buttons)
        layout.addLayout(self.gridLayout)

        self.setLayout(layout)


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()