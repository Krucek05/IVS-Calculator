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

    isFloat = False
    argumentProcessed = 1
    firstArgument = ""
    secondArgument = ""
    operation = ""
    result = ""

    def numberClicked(self, number):
        if self.argumentProcessed == 1:
            self.firstArgument += number
            self.displayText.setText(self.firstArgument + self.operation)
        else:
            self.secondArgument += number
            self.displayText.setText(self.firstArgument + self.operation + self.secondArgument)
    def clearClicked(self):
        if self.argumentProcessed == 2:
            if self.secondArgument == "":
                self.argumentProcessed = 1
                self.firstArgument = ""
                self.operation = ""
                self.isFloat = False
                self.displayText.clear()
            else:
                self.secondArgument = ""
                self.displayText.setText(self.firstArgument + self.operation)
        else:
            self.firstArgument = ""
            self.isFloat = False
            self.displayText.clear()

    def operationClicked(self, operation):
        self.operation = operation
        self.argumentProcessed = 2
        self.displayText.setText(self.firstArgument + self.operation)

    def commaClicked(self):
        self.isFloat = True
        if self.argumentProcessed == 1:
            self.firstArgument += ','
            self.displayText.setText(self.firstArgument)
        else:
            self.secondArgument += ','
            self.displayText.setText(self.firstArgument + self.operation + self.secondArgument)

    def factorialClicked(self):
        if self.secondArgument == "":
            if self.isFloat:
                print("")
                #self.result = factorial(float(self.firstArgument.replace(",", ".")))
            else:
                print("")
                #self.result = factorial(int(self.firstArgument))

    def isResult(self, newOperation):
        self.firstArgument = self.result
        self.operation = newOperation
        self.secondArgument = ""
        self.result = ""


    def buttonClick(self):
        buttonText = self.sender().text()

        if buttonText == "C":
            self.clearClicked()

        elif '0' <= buttonText and buttonText <= '9':
           self.numberClicked(buttonText)

        elif buttonText == ",":
            self.commaClicked()

        elif buttonText == "!":
            self.factorialClicked()


        else:
            if self.secondArgument == "":
                self.operationClicked(buttonText)







    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 150, 290, 440)
        self.setStyleSheet('background: #191919; font-size:25px')
        font = QFont("Segoe UI Symbol", 16, QFont.Weight.Bold)

        simpleLayout = QVBoxLayout()

        self.displayText = QLineEdit()
        self.displayText.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.displayText.setFont(QFont("Arial", 20))  # Set font size
        self.displayText.setReadOnly(True)  # Prevent user typing manually
        self.displayText.setStyleSheet("background-color: #4c4c4c; color: white;"
                                       "border-radius: 4px; border: none;")
        self.displayText.setFixedHeight(70)
        simpleLayout.addWidget(self.displayText)

        gridLayout = QGridLayout()
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setSpacing(3)
        buttons = [
            'aˣ', '√', '!', 'C',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            ',', '0', '=', '+'
        ]

        row, col = 0, 0
        for buttonText in buttons:
            button = QPushButton(buttonText)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.setFont(font)
            # noinspection PyUnresolvedReferences
            button.clicked.connect(self.buttonClick)
            button.setStyleSheet("QPushButton {"
                                 "background-color: #333333; color: white;"
                                 "border-radius: 4px; border:none;}"
                                 "QPushButton:hover {"
                                 "background-color: #656565; color: white;}")
            gridLayout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        simpleLayout.addLayout(gridLayout)
        self.setLayout(simpleLayout)




def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':

    main()



