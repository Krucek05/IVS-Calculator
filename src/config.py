############################################################################
## @file config.py
## @brief GUI for Calculator, IVS 2025
## @date 29.4.2025
## @author: Rastislav Šerý <xseryra00>
##
## File for configuration of app
############################################################################

############################################################################
## @brief Class with all the settings to configure application
##
##  All of the varibles like color, window, size, font...
############################################################################


class Configuration:
    buttons = ['²√', 'a²', 'aˣ', 'C', '±',
               'ˣ√', '7', '8', '9', '/',
               '%', '4', '5', '6', '*',
               '!', '1', '2', '3', '-',
               'π', ',', '0', '=', '+']

    windowSize = 300, 150, 375, 480
    heightTextDisplay = 50
    icon = "icon.png"
    windowTitle = 'Calculator'

    font = "Consolas"

    background = "#191919"

    operationColor = "#2e4053"
    operationColorHovered = "#5d6d7e"

    numbersColor = "#424949"
    numbersColorHovered = "#7f8c8d"

    clearColor = "#212f3d"
    clearColorHovered = "#34495e"

    bottomLineColor = "#333333"
    bottomLineColorHovered = "#656565"

    displayStyle = ("background-color: %s; "
                    "color: white;"
                    "border-radius: 4px;"
                    "border: none;")

    buttonStyle = ("QPushButton {"
                   "background-color: %s; color: white;"
                   "border-radius: 4px; border:none;}"
                   "QPushButton:hover {"
                   "background-color: %s; color: white;}")

    helpButtonStyle = """
                    QPushButton {
                                border-radius: 10px; border: none;
                                background-color: #191919;
                                font-size: 15px;
                                font-weight: bold;
                                }
            QPushButton:hover {
                            background-color: #5E5E5E;
                            }"""

    helpText = ("ˣ√ - xth root of given number (x√a)\t/ - Division\n"
                "²√ - Second root of given number\t* - Multiplication\n"
                "aˣ - xth power of given number (a^x)\t− - Subtraction\n"
                "a² - Second power of given number\t+ - Addition\n"
                "% - Remaining after division\t\t!  - Factorial\n"
                "C - Clears the display\t\t\t= - Result of math operation\n"
                "± - Changes sign of number\t\tπ - Makes argument pi")

    helpStyle = """
                QMessageBox {
                            background-color: #222;
                            color: white;
                            font-size: 13px;
                            }
                QPushButton {
                            background-color: #444;
                            color: white;
                            border-radius: 5px;
                            padding: 4px 10px;
                            }
            QPushButton:hover {
                            background-color: #666;
                            }
                        """