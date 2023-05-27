# Dependencies
import sys, cmath
import numpy as np

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# -










# Window
App = QApplication(sys.argv)

Window = QMainWindow()
Window.setWindowTitle("Nathan's Project #1")
Window.setGeometry(100, 100, 400, 200)
Window.setMaximumSize(Window.size())

CentralWidget = QWidget()
Window.setCentralWidget(CentralWidget)
Layout = QVBoxLayout(CentralWidget)

TabWidgets = QTabWidget()
MainWidget = QWidget()
ResultWidget = QWidget()


TabWidgets.addTab(MainWidget, "Main")
TabWidgets.addTab(ResultWidget, "Result")
Layout.addWidget(TabWidgets)
# -



# Main
MainLayout = QVBoxLayout(MainWidget)

HeaderQES = QLabel("Quadratic Equation  |  Solver")
HeaderQES.setStyleSheet("color: red; font-weight: bold;")
HeaderQES.setAlignment(Qt.AlignCenter)
MainLayout.addWidget(HeaderQES)

HeaderFormula = QLabel("a x ² + b x + c = 0")
HeaderFormula.setStyleSheet("color: blue; font-size: 15px; font-family: Arial;")
HeaderFormula.setAlignment(Qt.AlignCenter)
MainLayout.addWidget(HeaderFormula)


Divider1 = QFrame()
Divider1.setFrameShape(QFrame.HLine)
Divider1.setFrameShadow(QFrame.Sunken)
MainLayout.addWidget(Divider1)


InputALabel = QLabel("A:")
InputA = QLineEdit()
MainLayout.addWidget(InputALabel)
MainLayout.addWidget(InputA)

InputBLabel = QLabel("B:")
InputB = QLineEdit()
MainLayout.addWidget(InputBLabel)
MainLayout.addWidget(InputB)

InputCLabel = QLabel("C:")
InputC = QLineEdit()
MainLayout.addWidget(InputCLabel)
MainLayout.addWidget(InputC)


MainLayout.addSpacing(15)


CalculateInputButton = QPushButton("Calculate")
MainLayout.addWidget(CalculateInputButton)
# -


# Result
ResultLayout = QVBoxLayout(ResultWidget)
ResultGroupbox = QGroupBox("")
ResultLayout.addWidget(ResultGroupbox)

AnswerLabel = QLabel("...")
AnswerLabel.setStyleSheet("color: red; font-weight: bold;")
AnswerLabel.setAlignment(Qt.AlignCenter)
ResultLayout.addWidget(AnswerLabel)


ResultGivenLabel = QLabel("Given:  |  ")
ResultGivenLabel.setStyleSheet("color: blue;")
Divider1 = QFrame()
Divider1.setFrameShape(QFrame.HLine)
Divider1.setFrameShadow(QFrame.Sunken)
ResultRootsLabel = QLabel("Roots:  |  ")
ResultRootsLabel.setStyleSheet("color: blue;")
Divider2 = QFrame()
Divider2.setFrameShape(QFrame.HLine)
Divider2.setFrameShadow(QFrame.Sunken)
ResultRootsPairLabel = QLabel("Roots Pair:  |  ")
ResultRootsPairLabel.setStyleSheet("color: blue;")
Divider3 = QFrame()
Divider3.setFrameShape(QFrame.HLine)
Divider3.setFrameShadow(QFrame.Sunken)
ResultFactoredLabel = QLabel("Factored:  |  ")
ResultFactoredLabel.setStyleSheet("color: blue;")
Divider4 = QFrame()
Divider4.setFrameShape(QFrame.HLine)
Divider4.setFrameShadow(QFrame.Sunken)
ResultDiscriminantLabel = QLabel("Discriminant:  |  ")
ResultDiscriminantLabel.setStyleSheet("color: blue;")
Divider5 = QFrame()
Divider5.setFrameShape(QFrame.HLine)
Divider5.setFrameShadow(QFrame.Sunken)
ResultVertexLabel = QLabel("Vertex:  |  ")
ResultVertexLabel.setStyleSheet("color: blue;")
Divider6 = QFrame()
Divider6.setFrameShape(QFrame.HLine)
Divider6.setFrameShadow(QFrame.Sunken)
ResultSumOfRootsLabel = QLabel("Sum Of Roots:  |  ")
ResultSumOfRootsLabel.setStyleSheet("color: blue;")
Divider7 = QFrame()
Divider7.setFrameShape(QFrame.HLine)
Divider7.setFrameShadow(QFrame.Sunken)
ResultProductOfRootsLabel = QLabel("Product Of Roots:  |  ")
ResultProductOfRootsLabel.setStyleSheet("color: blue;")
Divider8 = QFrame()
Divider8.setFrameShape(QFrame.HLine)
Divider8.setFrameShadow(QFrame.Sunken)

ResultLayout = QVBoxLayout()
ResultLayout.addWidget(ResultGivenLabel)
ResultLayout.addWidget(Divider1)
ResultLayout.addWidget(ResultRootsLabel)
ResultLayout.addWidget(Divider2)
ResultLayout.addWidget(ResultRootsPairLabel)
ResultLayout.addWidget(Divider3)
ResultLayout.addWidget(ResultFactoredLabel)
ResultLayout.addWidget(Divider4)
ResultLayout.addWidget(ResultDiscriminantLabel)
ResultLayout.addWidget(Divider5)
ResultLayout.addWidget(ResultVertexLabel)
ResultLayout.addWidget(Divider6)
ResultLayout.addWidget(ResultSumOfRootsLabel)
ResultLayout.addWidget(Divider7)
ResultLayout.addWidget(ResultProductOfRootsLabel)
ResultLayout.addWidget(Divider8)

ResultGroupbox.setLayout(ResultLayout)
# -










# Core
def Calculate():
    A = float(InputA.text())
    B = float(InputB.text())
    C = float(InputC.text())


    Discriminant = B ** 2 - 4 * A * A

    if Discriminant > 0:
        Root_1 = (-B + np.sqrt(Discriminant)) / (2 * A)
        Root_2 = (-B - np.sqrt(Discriminant)) / (2 * A)
        RootsPair = f"({Root_1}, {Root_2})"
    elif Discriminant == 0:
        Root_1 = -B / (2 * A)
        Root_2 = Root_1
        RootsPair = f"({Root_1}, {Root_2})"
    else:
        Root_1 = (-B + cmath.sqrt(Discriminant)) / (2 * B)
        Root_2 = (-B - cmath.sqrt(Discriminant)) / (2 * B)
        RootsPair = f"({Root_1.real} + {Root_1.imag}j, {Root_2.real} + {Root_2.imag}j)"



    ResultGivenLabel.setText(f"Given:  a = {A}, b = {B}, c = {C}")
    ResultRootsLabel.setText(f"Roots:  1 = {Root_1}, 2 = {Root_2}")
    ResultRootsPairLabel.setText(f"Roots Pair:  {RootsPair}")
    ResultFactoredLabel.setText(f"Factored:  (x - {Root_1})(x - {Root_2})")
    ResultDiscriminantLabel.setText(f"Discriminant:  {Discriminant}")
    ResultVertexLabel.setText(f"Vertex:  ({-B / (2 * A)}, {-(B ** 2 - 4 * A * C) / (4 * A)})")
    ResultSumOfRootsLabel.setText(f"Sum of Roots:  {Root_1 + Root_2}")
    ResultProductOfRootsLabel.setText(f"Product of Roots:  {Root_1 * Root_2}")
    AnswerLabel.setText(f"{A}x² + {B}x + {C} = 0")

CalculateInputButton.clicked.connect(Calculate)
# -















# Execution
Window.show()
App.exec()
