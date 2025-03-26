import sys
from PyQt6.QtWidgets import (QApplication, QGridLayout,
        QWidget, QLineEdit, QTextEdit, QVBoxLayout, QPushButton,
        QSizePolicy)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
#from math_library import add, sub, multiply, divide, power, n_root, factorial


#treba osetrit ze nemoze byt 0233, potom pouzit float(arg.replace(",",".")), osetrit ked niekto stlaci , ako prvu vec
#pravdepodobne by som zacal auto 0 a ked cosi ine klknes sa premeni
#potom este ked mas 12345+54321 a znovu das + tak ti to vypocita a vysledok da jak prvy argument
#ale asi to nesmie fungovat pre mocninu odmocninu a factorial
# vymyslet ako zobrazit
#a^x a odm(x,a)

class Window(QWidget):

    isFactorial = False
    firstArgComma = False
    secondArgComma = False
    argumentProcessed = 1
    firstArgument = ""
    secondArgument = ""
    operation = ""
    result = "123"


    def equalsClicked(self):
        if self.operation == "+":
           #self.result = add(self.firstArgument, self.secondArgument)
            print("add")
        elif self.operation == "-":
            #self.result = sub(self.firstArgument, self.secondArgument)
            print("sub")
        elif self.operation == "*":
            #self.result = multiply(self.firstArgument, self.secondArgument)
            print("multiply")
        elif self.operation == "/":
            #self.result = divide(self.firstArgument, self.secondArgument)
            print("divide")
        elif self.operation == "aˣ":
            #self.result = power(self.firstArgument, self.secondArgument)
            print("power")
        elif self.operation == "√":
            #self.result == n_root(self.firstArgument, self.secondArgument)
            print("root")
        elif self.operation == "!":
            #self.result = factorial(self.firstArgument)
            print("factorial")


    def numberClicked(self, number):
        if self.argumentProcessed == 1:
            self.firstArgument += number
            self.displayText.setText(self.firstArgument + self.operation)
        elif not self.isFactorial:
            self.secondArgument += number
            self.displayText.setText(self.firstArgument + self.operation + self.secondArgument)


    def clearClicked(self):
        if self.argumentProcessed == 2:
            if self.secondArgument == "":
                self.argumentProcessed = 1
                self.firstArgument = ""
                self.operation = ""
                self.firstArgComma = False
                self.displayText.clear()
            else:
                self.secondArgument = ""
                self.secondArgComma = False
                self.displayText.setText(self.firstArgument + self.operation)
        else:
            self.firstArgument = ""
            self.firstArgComma = False
            self.displayText.clear()


    def operationClicked(self, operation):
        self.operation = operation
        self.argumentProcessed = 2
        self.displayText.setText(self.firstArgument + self.operation)


    def commaClicked(self):
        if self.argumentProcessed == 1 and not self.firstArgComma:
            self.firstArgComma = True
            self.firstArgument += ','
            self.displayText.setText(self.firstArgument)
        elif self.argumentProcessed == 2 and not self.secondArgComma:
            self.secondArgComma = True
            self.secondArgument += ','
            self.displayText.setText(self.firstArgument + self.operation + self.secondArgument)

    def isResult(self, newOperation):
        self.firstArgument = self.result
        self.operation = newOperation
        self.secondArgument = ""
        self.result = ""
        self.displayText.setText(self.firstArgument + self.operation)





    def buttonClick(self):
        buttonText = self.sender().text()

        if buttonText == "C":
            self.clearClicked()

        elif '0' <= buttonText and buttonText <= '9':
           self.numberClicked(buttonText)

        elif buttonText == ",":
            self.commaClicked()

        elif buttonText == "!":
            if not self.firstArgComma:
                self.isFactorial = True
                self.operation = buttonText
                self.argumentProcessed = 2
                self.displayText.setText(self.firstArgument + self.operation)

        elif buttonText == "=":
            self.equalsClicked()
            self.isResult("")

        else:
            if self.secondArgument == "":
                self.operationClicked(buttonText)
            else:
                self.equalsClicked()
                self.isResult(buttonText)







    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 150, 365, 440)
        self.setStyleSheet('background: #191919')
        font = QFont("Consolas", 22, QFont.Weight.Bold)

        simpleLayout = QVBoxLayout()

        self.displayText = QLineEdit()
        self.displayText.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.displayText.setFont(QFont("Consolas", 35))
        self.displayText.setReadOnly(True)
        self.displayText.setStyleSheet("background-color: #191919; color: white;"
                                       "border-radius: 4px; border: none;")
        self.displayText.setFixedHeight(70)
        simpleLayout.addWidget(self.displayText)

        gridLayout = QGridLayout()
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setSpacing(3)

        buttons = [
            '²√', 'a²', 'aˣ', 'C', '⌫',
            'ˣ√', '7', '8', '9', '/',
            '%', '4', '5', '6', '*',
            '!', '1', '2', '3', '-',
            'π', ',', '0', '=', '+',
        ]

        row, col = 0, 0
        for symbol in buttons:
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

            button = QPushButton(symbol)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.setFont(font)
            button.clicked.connect(self.buttonClick)  # Connect to function
            button.setStyleSheet("QPushButton {"
                                 "background-color: %s; color: white;"
                                 "border-radius: 4px; border:none;}"
                                 "QPushButton:hover {"
                                 "background-color: %s; color: white;}" %(color, color2))

            gridLayout.addWidget(button, row, col)  # Add button to the layout
            col += 1
            if col > 4:
                row += 1
                col = 0




        simpleLayout.addLayout(gridLayout)
        self.setLayout(simpleLayout)




def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':

    main()



