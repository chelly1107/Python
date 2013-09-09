import os

face = [[7,8,9],[4,5,6],[1,2,3]]
mask = [["*","*","*"],["*","*","*"],["*","*","*"]]
counter = 0

def screen():
   print "Gameboard:\t\tControls:"
   print mask[0],"\t",["7","8","9"]
   print mask[1],"\t",["4","5","6"]
   print mask[2],"\t",["1","2","3"],"\n"

def token(j):
   if j%2==0:
      return "1(X)"
   else:
      return "2(O)"

def endGame():
   os.system("clear")
   print "\t**** Round ",(counter)," ****\n"
   screen()
   print "Game Over! Player "+token(counter+1)+" wins!\n"
   return False

def checkGame(face):
      for i in range(0,3):
         if face[i][0] == face[i][1] == face[i][2] or face[0][i] == face[1][i] == face[2][i]:
            return endGame()
      if face[0][0] == face[1][1] == face[2][2] or face[0][2] == face[1][1] == face[2][0]:
         return endGame()
      else:
         return True

def takeAnswer(counter):
   userInput = int(raw_input("Player "+token(counter)+" move: "))
   for j in range(0,3):
         for i in range(1+(j*3),4+(j*3)):
            if userInput == i:
               mask[2-j][i-(1+(j*3))] = face[2-j][i-(1+(j*3))] = token(counter)[2:-1]

while checkGame(face) == True:
   os.system("clear")
   print "\t**** Round ",(counter)," ****\n"
   screen()
   takeAnswer(counter)
   counter += 1