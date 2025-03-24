import sys
from PyQt6.QtWidgets import (QApplication, QGridLayout,
        QWidget, QLineEdit, QTextEdit, QVBoxLayout, QPushButton,
        QSizePolicy)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt


class Window(QWidget):
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



