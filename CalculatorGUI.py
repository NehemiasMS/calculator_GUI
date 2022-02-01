# pip install ttkthemes :))

import tkinter
from tkinter import StringVar, ttk
import ttkthemes


# Main
AFlag = True
numeroA = ""
numeroB = ""

operator = "A"

resultado = 0


def addNumber(number):
    global numeroA, numeroB, resLabel
    number = str(number)
    if(AFlag):
        numeroA = numeroA + number
        resLabel.set(numeroA)

    else:
        numeroB = numeroB + number
        resLabel.set(numeroB)



def operation(op):
    global operator, AFlag
    AFlag = False
    operator = op

# GUI

main_Window = ttkthemes.ThemedTk(theme='breeze', background=True)
main_Window.geometry("315x285")
main_Window.resizable(False, False)

main_Window.title("Calculadora Los Tres Mosqueteros")

separacion = 4

resLabel = tkinter.StringVar()
resLabel.set("0")

Resultado = ttk.Label(main_Window, textvariable = resLabel, font = ('Arial', 25)).grid(row = 0, column = 0)


def enter():
    global Resultado, resLabel, numeroA, numeroB, operator, AFlag
    a = float(numeroA)
    b = float(numeroB)

    if(operator == "/"):
        resultado = a/b
    elif(operator == "x"):
        resultado = a*b
    elif(operator == "-"):
        resultado = a-b
    elif(operator == "+"):
        resultado = a+b

    resLabel.set(str(resultado))
    numeroA = "0"
    numeroB = "0"
    AFlag = True

tabla = ttk.Frame(main_Window, width = 180, height = 180)
tabla.grid(row = 1, column = 0, ipady = 10)
buttonWidth = 8
buttonLength = 15
numberSeven = ttk.Button(tabla, text = "7",width = buttonWidth, command = lambda: addNumber(7)).grid(row = 0, column = 0, ipady = buttonLength)
numberEight = ttk.Button(tabla, text = "8",width = buttonWidth, command = lambda: addNumber(8)).grid(row = 0, column = 1, ipady = buttonLength)
numberNine = ttk.Button(tabla, text = "9",width = buttonWidth, command = lambda: addNumber(9)).grid(row = 0, column = 2, ipady = buttonLength)

numberFour = ttk.Button(tabla, text = "4",width = buttonWidth, command = lambda: addNumber(4)).grid(row = 1, column = 0, ipady = buttonLength)
numberFive = ttk.Button(tabla, text = "5",width = buttonWidth, command = lambda: addNumber(5)).grid(row = 1, column = 1, ipady = buttonLength)
numberSix = ttk.Button(tabla, text = "6",width = buttonWidth, command = lambda: addNumber(6)).grid(row = 1, column = 2, ipady = buttonLength)

numberOne = ttk.Button(tabla, text = "1",width = buttonWidth, command = lambda: addNumber(1)).grid(row = 2, column = 0, ipady = buttonLength)
numberTwo = ttk.Button(tabla, text = "2",width = buttonWidth, command = lambda: addNumber(2)).grid(row = 2, column = 1, ipady = buttonLength)
numberThree = ttk.Button(tabla, text = "3",width = buttonWidth, command = lambda: addNumber(3)).grid(row = 2, column = 2, ipady = buttonLength)

numberZero = ttk.Button(tabla, text = "0",width = buttonWidth, command = lambda: addNumber(0)).grid(row = 3, column = 1, ipady = buttonLength)

divisionKey = ttk.Button(tabla, text = "/",width = buttonWidth, command = lambda: operation("/")).grid(row = 0, column = 3, ipady = buttonLength)
multiplyKey = ttk.Button(tabla, text = "x",width = buttonWidth, command = lambda: operation("x")).grid(row = 1, column = 3, ipady = buttonLength)
sumKey = ttk.Button(tabla, text = "+",width = buttonWidth, command = lambda: operation("+")).grid(row = 2, column = 3, ipady = buttonLength)
substractKey = ttk.Button(tabla, text = "-",width = buttonWidth, command = lambda: operation("-")).grid(row = 3, column = 3, ipady = buttonLength)
enterKey = ttk.Button(tabla, text = "=",width = buttonWidth, command = lambda: enter()).grid(row = 3, column = 2, ipady = buttonLength)
pointKey = ttk.Button(tabla, text = ".",width = buttonWidth, command= lambda: addNumber(".")).grid(row = 3, column = 0, ipady = buttonLength)

main_Window.mainloop()