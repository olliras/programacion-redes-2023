'''
nombre: Samuel reynaldo olvera lira
fecha: 6 de octubre 2023
descripcion: laborartorios modulo 4
'''
from random import randrange

def DisplayBoard(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for cell in row:
            print(f"|   {cell}   ", end="")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def EnterMove(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento (un número del 1 al 9): "))
            if move < 1 or move > 9:
                raise ValueError("Número fuera de rango")
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] != " ":
                raise ValueError("Cuadro ocupado")
            board[row][col] = "O"
            break
        except ValueError as e:
            print(f"Error: {e}")
            continue

def MakeListOfFreeFields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                free_fields.append((row, col))
    return free_fields

def VictoryFor(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def DrawMove(board):
    free_fields = MakeListOfFreeFields(board)
    move = randrange(len(free_fields))
    row, col = free_fields[move]
    board[row][col] = "X"

board = [[" " for _ in range(3)] for _ in range(3)]
board[1][1] = "X"  

while True:
    DisplayBoard(board)
    EnterMove(board)
    if VictoryFor(board, "O"):
        DisplayBoard(board)
        print("¡Has Ganado!")
        break
    free_fields = MakeListOfFreeFields(board)
    if not free_fields:
        DisplayBoard(board)
        print("¡Empate!")
        break
    DrawMove(board)
    if VictoryFor(board, "X"):
        DisplayBoard(board)
        print("¡La Máquina ha Ganado!")
        break
