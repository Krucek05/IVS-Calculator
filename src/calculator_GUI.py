import sys
from PyQt6.QtWidgets import (QApplication, QGridLayout,
        QWidget, QLineEdit, QTextEdit, QVBoxLayout, QPushButton,
        QSizePolicy)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt


class Window(QWidget):

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
                self.displayText.clear()
            else:
                self.secondArgument = ""
                self.displayText.setText(self.firstArgument + self.operation)
        else:
            self.firstArgument = ""
            self.displayText.clear()

    def operationClicked(self, operation):
        self.operation = operation
        self.argumentProcessed = 2
        self.displayText.setText(self.firstArgument + self.operation)
    def buttonClick(self):
        buttonText = self.sender().text()

        if buttonText == "C":
            self.clearClicked()

        elif '0' <= buttonText and buttonText <= '9':
           self.numberClicked(buttonText)

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



