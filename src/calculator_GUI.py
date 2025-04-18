############################################################################
# @file calculator_GUI.py
# @brief GUI for Calculator, IVS 2025
# @date 17.4.2025
# @author: Rastislav Šerý <xseryra00>
#
#Logic behind graphic user face and processing inputs
############################################################################


import sys, math
from PyQt6.QtWidgets import (QApplication, QGridLayout,
        QWidget, QLineEdit, QVBoxLayout, QPushButton,
        QSizePolicy)
from PyQt6.QtGui import QIcon, QFont, QKeyEvent
from PyQt6.QtCore import Qt
from math_library import add, sub, multiply, divide, power, n_root, factorial, modulo


# ked je float tak nesmie a^b sa pouzit, to iste root


#ked je rovnasa bez operacie tak to vycisti idk ci to tak nehat


class Window(QWidget):

    buttons = [
        '²√', 'a²', 'aˣ', 'C', '⌫',
        'ˣ√', '7', '8', '9', '/',
        '%', '4', '5', '6', '*',
        '!', '1', '2', '3', '-',
        'π', ',', '0', '=', '+',
    ]


    argumentProcessed = 1
    firstArgument = ""
    secondArgument = ""
    operation = ""
    result = ""

############################################################################
# @brief Function to process second root
############################################################################
    def secondRoot(self):
        if self.secondArgument != "":
            self.makeNumSecArg()
            self.secondArgument = str(power(self.secondArgument), 2)
        else:
            self.operation = ""
            self.makeNumFirstArg()
            self.firstArgument = str(power(self.firstArgument, 2))

############################################################################
# @brief Function to process second power
############################################################################
    def secondPower(self):
        if self.secondArgument != "":
            self.makeNumSecArg()
            self.secondArgument = str(power(self.secondArgument), 2)
        else:
            self.operation = ""
            self.makeNumFirstArg()
            self.firstArgument = str(power(self.firstArgument, 2))

############################################################################
# @brief Converts first argument to int/float based on whether there is comma
############################################################################
    def makeNumFirstArg(self):
        if ('.' not in self.firstArgument) and ('.' not in self.secondArgument):
            self.firstArgument = int(self.firstArgument)
        else:
            self.firstArgument = float(self.firstArgument)

############################################################################
# @brief Converts first argument to int/float based on whether there is comma
############################################################################
    def makeNumSecArg(self):
        if ('.' not in str(self.firstArgument)) and ('.' not in self.secondArgument):
            self.secondArgument = int(self.secondArgument)
        else:
            self.secondArgument = float(self.secondArgument)

############################################################################
# @brief Updates display on calculator
############################################################################
    def displayUpdate(self):
        self.displayText.setText(self.firstArgument + self.operation + self.secondArgument)
        self.displayText.setCursorPosition(0)

############################################################################
# @brief Adds clicked number to processed argument
# @param number Number that was clicked
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
# @brief Logic to get result after "=" is clicked
############################################################################
    def equalsClicked(self):
        if (self.operation != "") and (self.firstArgument != "") and (self.secondArgument != ""):
            self.makeNumFirstArg()
            self.makeNumSecArg()
            if self.operation == "+":
                self.result = add( self.firstArgument, self.secondArgument)
            elif self.operation == "-":
                self.result = sub(self.firstArgument, self.secondArgument)
            elif self.operation == "*":
                self.result = multiply(self.firstArgument, self.secondArgument)
            elif self.operation == "/":
                self.result = divide(self.firstArgument, self.secondArgument)
            elif self.operation == "^":
                print(self.firstArgument)
                print(self.secondArgument)
                self.result = power(self.firstArgument, self.secondArgument)
            elif self.operation == "ˣ√":
                self.result == n_root(self.firstArgument, self.secondArgument)
            elif self.operation == "%":
                self.result = modulo(self.firstArgument, self.secondArgument)

############################################################################
# @brief Processes result to first argument, so we can use it again for calculations
# @param newOperation operation to add after first argument
#
# Takes result after calculation and if instead "=" some other operation
# was used it adds it after the first argument
############################################################################
    def isResult(self, newOperation):
        self.firstArgument = str(self.result)
        self.operation = newOperation
        self.secondArgument = ""
        self.result = ""

############################################################################
# @brief Logic to clear dislpay of calculator after "C" is clicked
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
# @brief clears operation, first argument and number of processed argument
############################################################################
    def clear(self):
        self.argumentProcessed = 1
        self.firstArgument = ""
        self.operation = ""

############################################################################
# @brief Logic after some mathematical operation is clicked
############################################################################
    def operationClicked(self, operation):
        self.operation = operation
        self.argumentProcessed = 2

############################################################################
# @brief Logic to add comma at the end of processed argument
############################################################################
    def commaClicked(self):
        if self.argumentProcessed == 1 and ('.' not in self.firstArgument) and self.firstArgument != "":
            self.firstArgument += '.'
        elif self.argumentProcessed == 2 and ('.' not in self.secondArgument) and self.secondArgument != "":
            self.secondArgument += '.'

############################################################################
# @brief Logic to calculate factorial of number
############################################################################
    def factorial(self):
        if ('.' not in self.firstArgument) and (not self.secondArgument):
             self.firstArgument = str(factorial(int(self.firstArgument)))
        elif '.' not in self.secondArgument :
            self.secondArgument = str(factorial(int(self.secondArgument)))

############################################################################
# @brief Function that makes from processed argument pi
############################################################################
    def pi(self):
        if self.argumentProcessed == 1:
            self.firstArgument = str(math.pi)
        else:
            self.secondArgument = str(math.pi)

############################################################################
# @brief Logic done after clicking backspace
############################################################################
    def backspace(self):
        if (self.argumentProcessed == 1) and (self.firstArgument != ""):
            self.firstArgument = self.firstArgument[:-1]
        else:
            if self.secondArgument == "":
                self.operation = ""
                self.argumentProcessed = 1
            else:
                self.secondArgument = self.secondArgument[:-1]

############################################################################
# @brief Function that processes click of some button
#
# Checks what was clicked and based on that calls right functions
############################################################################
    def buttonClick(self):
        buttonText = self.sender().text()
        self.processClickedCharacter(buttonText)
        self.setFocus()

    def processClickedCharacter(self, buttonText):

        if '0' <= buttonText and buttonText <= '9':
            self.numberClicked(buttonText)

        elif buttonText == '=':
            self.equalsClicked()
            self.isResult("")
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
            elif buttonText == '⌫':
                self.backspace()

            elif self.secondArgument == "":
                if buttonText == "aˣ":
                    buttonText = "^"
                self.operationClicked(buttonText)
            elif buttonText != "aˣ" or buttonText != "ˣ√":
                self.equalsClicked()
                self.isResult(buttonText)
        self.displayUpdate()


    def keyPressEvent(self, event:QKeyEvent):
        keyText = ''
        stuff = event.key()
        print(stuff)

        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            keyText = '='
        elif event.key() in (Qt.Key.Key_Backspace, Qt.Key.Key_Delete):
            keyText = '⌫'
        else:
            keyText = event.text()
        if keyText == '^':
            keyText = "aˣ"
        if (keyText in self.buttons) or (keyText == "c"):
            self.processClickedCharacter(keyText)


############################################################################
# @brief Function that adds buttons to calculator
#
# @param colAmount Number of columns
# @param buttonList List of all buttons we want to be in there
############################################################################
    def buttonsCreation(self, colAmount, buttonList):
        row, col = 0, 0
        for symbol in buttonList:
            color = "#333333"
            color2 = "#656565"
            if row < 1 and col > 2:
                color = " #212f3d"
                color2 =  "#34495e"
            if '0' <= symbol and symbol <= '9':
                color = "#424949"
                color2 = "#7f8c8d"
            if (row > 0 and col > 3) or (row == 0 and col <3) or (col < 1 and row < 4):
                color = "#2e4053"
                color2 = "#5d6d7e"

            button = self.buttonAtributes(symbol, color, color2)
            self.gridLayout.addWidget(button, row, col)
            col += 1
            if col > colAmount - 1:
                row += 1
                col = 0

############################################################################
# @brief Functions that gives buttons its attribute e.g. color, symbol...
#
# @param symbol Symbol that will be on the button
# @param color Color that will normally be on the button
# @param color2 Color that will be on button when mouse is hovering over it
############################################################################
    def buttonAtributes(self, symbol, color, color2):
        button = QPushButton(symbol)
        button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button.setFont(self.font)
        button.clicked.connect(self.buttonClick)  # Connect to function
        button.setStyleSheet("QPushButton {"
                                "background-color: %s; color: white;"
                                "border-radius: 4px; border:none;}"
                                "QPushButton:hover {"
                                "background-color: %s; color: white;}" %(color, color2))
        return button


############################################################################
# @brief Initializes calculator window and builds all buttons
############################################################################
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 150, 375, 480)
        self.setStyleSheet('background: #191919')
        self.font = QFont("Consolas", 22, QFont.Weight.Bold)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)


        simpleLayout = QVBoxLayout()

        self.displayText = QLineEdit()
        self.displayText.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.displayText.setFont(QFont("Consolas", 30))
        self.displayText.setReadOnly(True)
        self.displayText.setStyleSheet("background-color: #191919; color: white;"
                                       "border-radius: 4px; border: none;")
        self.displayText.setFixedHeight(70)
        simpleLayout.addWidget(self.displayText)

        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)

        self.buttonsCreation(5, self.buttons)

        simpleLayout.addLayout(self.gridLayout)
        self.setLayout(simpleLayout)


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':

    main()