############################################################################
## @file help.py
## @brief GUI for Calculator, IVS 2025
## @date 29.4.2025
## @author: Rastislav Šerý <xseryra00>
##
## File for configuration of app
############################################################################

from config import Configuration
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QGridLayout, QVBoxLayout, QLabel, QDialog)

############################################################################
## @brief class that will popup window with help
############################################################################

class helpWindow(QDialog):
    def __init__(self):
        super().__init__() 

        self.setWindowTitle(Configuration.helpTitle)
        self.setWindowIcon(QIcon(Configuration.icon))
        self.setStyleSheet("background: %s" % Configuration.background)
        self.font = QFont(Configuration.font, 12)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        
        layout = QVBoxLayout()
        text = Configuration.helpText
        columns = Configuration.helpColumns
        grid = QGridLayout()
        for i in range(len(text)):
            textAdd = QLabel(text[i])
            textAdd.setStyleSheet("color: white")
            textAdd.setFont(self.font)
            grid.addWidget(textAdd, i // columns, i % columns)
        layout.addLayout(grid)
        self.setLayout(layout)


