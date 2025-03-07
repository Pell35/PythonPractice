board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print(f"{board[0]} | {board[1]} | {board[2]}")
print("-----------")
print(f"{board[3]} | {board[4]} | {board[5]}")
print("-----------")
print(f"{board[6]} | {board[7]} | {board[8]}")


xChoice = int(input("Choose a spot"))

board[xChoice-1] = "X"

print(f"{board[0]} | {board[1]} | {board[2]}")
print("-----------")
print(f"{board[3]} | {board[4]} | {board[5]}")
print("-----------")
print(f"{board[6]} | {board[7]} | {board[8]}")


oChoice = int(input("Choose an available spot"))

board[oChoice-1] = "O"

print(f"{board[0]} | {board[1]} | {board[2]}")
print("-----------")
print(f"{board[3]} | {board[4]} | {board[5]}")
print("-----------")
print(f"{board[6]} | {board[7]} | {board[8]}")

xChoice = int(input("Choose a spot"))

board[xChoice-1] = "X"

print(f"{board[0]} | {board[1]} | {board[2]}")
print("-----------")
print(f"{board[3]} | {board[4]} | {board[5]}")
print("-----------")
print(f"{board[6]} | {board[7]} | {board[8]}")


oChoice = int(input("Choose an available spot"))

board[oChoice-1] = "O"

print(f"{board[0]} | {board[1]} | {board[2]}")
print("-----------")
print(f"{board[3]} | {board[4]} | {board[5]}")
print("-----------")
print(f"{board[6]} | {board[7]} | {board[8]}")

xChoice = int(input("Choose a spot"))

board[xChoice-1] = "X"

print(f"{board[0]} | {board[1]} | {board[2]}")
print("-----------")
print(f"{board[3]} | {board[4]} | {board[5]}")
print("-----------")
print(f"{board[6]} | {board[7]} | {board[8]}")

if board[0] == "X" and board[1] == "X" and board[2] == "X" or  board[0] == "X" and board[4] == "X" and board[8] == "X" or board[0] == "X" and board[3] == "X" and board[6] == "X" or board[1] == "X" and board[5] == "X" and board[7] == "X" or board[2] == "X" and board[5] == "X" and board[8] == "X" or board[2] == "X" and board[4] == "X" and board[6] == "X" or board[3] == "X" and board[4] == "X" and board[5] == "X" or board[6] == "X" and board[7] == "X" and board[8] == "X":
    print("X wins!!!")
elif board[0] == "O" and board[1] == "O" and board[2] == "O" or  board[0] == "X" and board[4] == "X" and board[8] == "X" or board[0] == "X" and board[3] == "X" and board[6] == "X" or board[1] == "X" and board[5] == "X" and board[7] == "X" or board[2] == "O" and board[5] == "O" and board[8] == "O" or board[2] == "O" and board[4] == "O" and board[6] == "O" or board[3] == "O" and board[4] == "O" and board[5] == "O" or board[6] == "O" and board[7] == "O" and board[8] == "O" :
    print("O wins!!!")
else:


    oChoice = int(input("Choose an available spot"))

    board[oChoice-1] = "O"

print(f"{board[0]} | {board[1]} | {board[2]}")
print("-----------")
print(f"{board[3]} | {board[4]} | {board[5]}")
print("-----------")
print(f"{board[6]} | {board[7]} | {board[8]}")
