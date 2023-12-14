from art import logo
import os
import time


def Add(n1,n2):
    return n1 + n2
def Subtract(n1,n2):
    return n1 - n2
def Multiply(n1,n2):
    return n1 * n2
def Divide(n1,n2):
    return n1 / n2
def Power(n1,n2):
    return n1 ** n2
def Modulus(n1,n2):
    return n1 % n2

global operation 
operation = {
    '+':Add,
    '-':Subtract,
    '*':Multiply,
    '/':Divide,
    '**':Power,
    '%':Modulus,
    }


def calculator():
    print(logo)
    EOF = False
    num1 = float(input("Enter the first number : "))
    for opr in operation:
            print(opr,end=' ')
    while not EOF:
        
        opr_symbol = input("\nPick an operation from above : ")

        num2 = float(input("Enter the second number : "))

        answer = operation[opr_symbol](num1,num2)
        print(f"{num1} {opr_symbol} {num2} = {answer}")
        save = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart calculator.: ")
        if save == 'y':
            num1 = answer
        elif save =='n':
            EOF = True
            calculator()
        else:
            print("ERROR!!")
            time.sleep(4)
            exit()

calculator()

