import sys, math
from PyQt6.QtWidgets import (QApplication, QGridLayout,
        QWidget, QLineEdit, QTextEdit, QVBoxLayout, QPushButton,
        QSizePolicy)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from math_library import add, sub, multiply, divide, power, n_root, factorial, modulo


# potom pouzit float(arg.replace(",",".")),
#ale asi to nesmie fungovat pre mocninu odmocninu a factorial
# vymyslet ako zobrazit
#a^x a odm(x,a)

class Window(QWidget):

    isFactorial = False
    argumentProcessed = 1
    firstArgument = ""
    secondArgument = ""
    operation = ""
    result = "123"

    def displayUpdate(self):
        self.displayText.setText(self.firstArgument + self.operation + self.secondArgument)
        self.displayText.setCursorPosition(0)

    def equalsClicked(self):

        if ('.' in self.firstArgument) or ('.' in self.secondArgument):
            self.firstArgument = float(self.firstArgument)
            self.secondArgument = float(self.secondArgument)
        else:
            self.firstArgument = int(self.firstArgument)
            self.secondArgument = int(self.secondArgument)

        if self.operation == "+":
            self.result = add( self.firstArgument, self.secondArgument)
        elif self.operation == "-":
            self.result = sub(self.firstArgument, self.secondArgument)
        elif self.operation == "*":
            self.result = multiply(self.firstArgument, self.secondArgument)
        elif self.operation == "/":
            self.result = divide(self.firstArgument, self.secondArgument)
        elif self.operation == "^":
            self.result = power(self.firstArgument, self.secondArgument)
        elif self.operation == "ˣ√":
            self.result == n_root(self.firstArgument, self.secondArgument)
        elif self.operation == "!":
            self.result = factorial(self.firstArgument)
        else:
            self.result = modulo(self.firstArgument, self.secondArgument)

    def numberClicked(self, number):
        if self.argumentProcessed == 1:
            if self.firstArgument == "0":
                self.firstArgument = ""
            self.firstArgument += number
        elif not self.isFactorial:
            if self.secondArgument == "0":
                self.secondArgument = ""
            self.secondArgument += number

    def clear(self):
        self.argumentProcessed = 1
        self.firstArgument = ""
        self.operation = ""

    def clearClicked(self):
        if self.argumentProcessed == 2:
            if self.secondArgument == "":
                self.clear()
            else:
                self.secondArgument = ""
        else:
            self.clear()


    def operationClicked(self, operation):
        self.operation = operation
        self.isFactorial = False
        self.argumentProcessed = 2

    def commaClicked(self):
        if self.argumentProcessed == 1 and ('.' not in self.firstArgument) and self.firstArgument != "":
            self.firstArgument += '.'
        elif self.argumentProcessed == 2 and ('.' not in self.secondArgument) and self.secondArgument != "":
            self.secondArgument += '.'

    def isResult(self, newOperation):
        self.firstArgument = str(self.result)
        self.operation = newOperation
        self.isFactorial = False
        self.secondArgument = ""
        self.result = ""

    def zero(self, buttonText):
        if self.argumentProcessed == 1 and buttonText != self.firstArgument:
            self.numberClicked(buttonText)
        elif self.argumentProcessed == 2 and buttonText != self.secondArgument:
            self.numberClicked(buttonText)

    def factorial(self, buttonText):
        if '.' not in self.firstArgument and not self.secondArgument:
            self.isFactorial = True
            self.operation = buttonText
            self.argumentProcessed = 2

    def pi(self):
        if self.argumentProcessed == 1:
            self.firstArgument = str(math.pi)
        else:
            self.secondArgument = str(math.pi)

    def backspace(self):
        if self.argumentProcessed == 1:
            self.firstArgument = self.firstArgument[:-1]
        else:
            if self.secondArgument == "":
                self.operation = ""
                self.argumentProcessed = 1
            else:
                self.secondArgument = self.secondArgument[:-1]


    def buttonClick(self):
        buttonText = self.sender().text()

        if '0' < buttonText and buttonText <= '9':
           self.numberClicked(buttonText)

        elif buttonText == "C":
            self.clearClicked()

        elif buttonText == '⌫':
            self.backspace()

        elif buttonText == '0':
            self.zero(buttonText)

        elif buttonText == ",":
            self.commaClicked()

        elif buttonText == "!":
            self.factorial(buttonText)

        elif buttonText == "=":
            self.equalsClicked()
            self.isResult("")

        elif buttonText == "²√":
#            self.result = n_root(int(self.firstArgument), 2)
            self.isResult("")

        elif buttonText == "a²":
#           self.reult = power(self.firstArgument, 2)
            self.isResult("")

        elif buttonText == 'π':
            self.pi()

        elif buttonText == "aˣ":
            self.operation = "^"
            self.isFactorial = False
            self.argumentProcessed = 2

        else:
            if self.secondArgument == "":
                self.operationClicked(buttonText)
            elif buttonText != "aˣ" or buttonText != "ˣ√":
                self.equalsClicked()
                self.isResult(buttonText)

        self.displayUpdate()




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


    def buttonAtributes(self, symbol, color, color2):
        button = QPushButton(symbol)
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button.setFont(self.font)
        button.clicked.connect(self.buttonClick)  # Connect to function
        button.setStyleSheet("QPushButton {"
                                "background-color: %s; color: white;"
                                "border-radius: 4px; border:none;}"
                                "QPushButton:hover {"
                                "background-color: %s; color: white;}" %(color, color2))
        return button



    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 150, 375, 480)
        self.setStyleSheet('background: #191919')
        self.font = QFont("Consolas", 22, QFont.Weight.Bold)

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

        buttons = [
            '²√', 'a²', 'aˣ', 'C', '⌫',
            'ˣ√', '7', '8', '9', '/',
            '%', '4', '5', '6', '*',
            '!', '1', '2', '3', '-',
            'π', ',', '0', '=', '+',
        ]

        self.buttonsCreation(5, buttons)

        simpleLayout.addLayout(self.gridLayout)
        self.setLayout(simpleLayout)




def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':

    main()



