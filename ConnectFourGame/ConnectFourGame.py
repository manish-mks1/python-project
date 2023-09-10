import random

print("****Welcome to Connect Four****")
print("-----------------------")

letters = ["A","B","C","D","E","F","G"]
board= [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

rows = 6
cols = 7

def printboard():
  print("\n     A    B    C    D    E    F    G  ", end="")
  for x in range(rows):
    print("\n   +----+----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(cols):
      if(board[x][y] == "🔵"):
        print("",board[x][y], end=" |")
      elif(board[x][y] == "🔴"):
        print("", board[x][y], end=" |")
      else:
        print(" ", board[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
  board[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
  for y in range(rows):
    for x in range(cols - 3):
      if board[x][y] == chip and board[x+1][y] == chip and board[x+2][y] == chip and board[x+3][y] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  for x in range(rows):
    for y in range(cols - 3):
      if board[x][y] == chip and board[x][y+1] == chip and board[x][y+2] == chip and board[x][y+3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  for x in range(rows - 3):
    for y in range(3, cols):
      if board[x][y] == chip and board[x+1][y-1] == chip and board[x+2][y-2] == chip and board[x+3][y-3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  for x in range(rows - 3):
    for y in range(cols - 3):
      if board[x][y] == chip and board[x+1][y+1] == chip and board[x+2][y+2] == chip and board[x+3][y+3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True
  return False

def coordinateParser(inputString):
  coordinate = [None] * 2
  if(inputString[0] == "A"):
    coordinate[1] = 0
  elif(inputString[0] == "B"):
    coordinate[1] = 1
  elif(inputString[0] == "C"):
    coordinate[1] = 2
  elif(inputString[0] == "D"):
    coordinate[1] = 3
  elif(inputString[0] == "E"):
    coordinate[1] = 4
  elif(inputString[0] == "F"):
    coordinate[1] = 5
  elif(inputString[0] == "G"):
    coordinate[1] = 6
  else:
    print("Invalid")
  coordinate[0] = int(inputString[1])
  return coordinate

def isSpaceAvailable(intendedCoordinate):
  if(board[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
    return False
  elif(board[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵'):
    return False
  else:
    return True

def gravityChecker(intendedCoordinate):
  spaceBelow = [None] * 2
  spaceBelow[0] = intendedCoordinate[0] + 1
  spaceBelow[1] = intendedCoordinate[1]
  if(spaceBelow[0] == 6):
    return True
  if(isSpaceAvailable(spaceBelow) == False):
    return True
  return False

leaveLoop = False
turnCounter = 0
while(leaveLoop == False):
  if(turnCounter % 2 == 0):
    printboard()
    while True:
      spacePicked = input("\nChoose a space: ")
      coordinate = coordinateParser(spacePicked)
      try:
        if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
          modifyArray(coordinate, '🔵')
          break
        else:
          print("Not a valid coordinate")
      except:
        print("Error occured. Please try again.")
    winner = checkForWinner('🔵')
    turnCounter += 1
  else:
    while True:
      cpuChoice = [random.choice(letters), random.randint(0,5)]
      cpuCoordinate = coordinateParser(cpuChoice)
      if(isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate)):
        modifyArray(cpuCoordinate, '🔴')
        break
    turnCounter += 1
    winner = checkForWinner('🔴')

  if(winner):
    printboard()
    break