# -*- coding: utf-8 -*-
"""Practical1AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SNUAPRRI8KhC9ZlFhkIHd2UDBhFmPW-5
"""

import random as r

mat = [[" ","|"," ","|"," "],
       ["-","-","-","-","-"],
       [" ","|"," ","|"," "],
       ["_","_","_","_","_"],
       [" ","|"," ","|"," "],
       ]

matSize = 0

def startMat():
  global mat
  mat = [[" ","|"," ","|"," "],
       ["-","-","-","-","-"],
       [" ","|"," ","|"," "],
       ["_","_","_","_","_"],
       [" ","|"," ","|"," "],
       ]

arr = [0,2,4] # used as a map

def Display(mat):
  print()
  for i in range(0,5):
    for j in range(0,5):
      print(mat[i][j],end=" ")
    print()
  print()

def computer(matrix):
  global matSize
  while(1):
    a = r.choice(arr)
    b = r.choice(arr)
    if(matrix[a][b] == " "):
      matrix[a][b] = "X"
      matSize = matSize + 1
      break

def user(matrix):
  global matSize
  print("Enter Position : ")
  int1 = int(input())
  int2 = int(input())
  int1 = arr[int1]
  int2 = arr[int2]
  if(matrix[int1][int2] == " "):
    matrix[int1][int2] = "0"
    matSize = matSize + 1
  else:
    print("Dekh Ke Khel bhai...., Try again")
    user(matrix)

def validateStateRow(mat):
  # checking all the rows
  flag = True

  for i in arr:
    prev = mat[i][0]
    kyaPooraChala = 1
    for j in arr:
      if(prev != mat[i][j]):
        #check for next row
        kyaPooraChala = False
        break

    #agar ye loop poora chal gaya means ye row m sab same hai
    if(kyaPooraChala):
      flag = prev
      break

  if(flag == "0"):
    print("User Won")
    return True
  elif (flag == "X"):
    print("Computer Won , you looser")
    return True
  else:
    return False

def validateStateColumn(mat):
  # checking all the rows
  flag = True

  for i in arr:
    prev = mat[0][i]
    kyaPooraChala = 1
    for j in arr:
      if(prev != mat[j][i]):
        #check for next row
        kyaPooraChala = False
        break

    #agar ye loop poora chal gaya means ye row m sab same hai
    if(kyaPooraChala):
      flag = prev
      break

  if(flag == "0"):
    print("User Won")
    return True
  elif (flag == "X"):
    print("Computer Won , you looser")
    return True
  else:
    return False

def validateStateDiagonal(mat):
  flag = "empty"
  prev = mat[0][0]
  if(prev == mat[2][2] and prev == mat[4][4]):
    flag = prev

  prev = mat[0][4]
  if(prev == mat[2][2] and prev == mat[4][0]):
    flag = prev

  if(flag == "0"):
    print("User Won")
    return True
  elif (flag == "X"):
    print("Computer Won , you looser")
    return True
  else:
    return False

def validate(mat):
  if(validateStateRow(mat)):
    return True
  elif(validateStateColumn(mat)):
    return True
  elif(validateStateDiagonal(mat)):
    return True
  return False

import time
def play():
  print("Enter any key to start the game")
  a = (input())

  startMat()

  #game loop
  while(not validate(mat)):

    if(matSize == 10):
      print("TIEEE : No Possible Moves ")
      break

    user(mat)
    print("You Played : ")
    Display(mat)
    print()
    if(validate(mat)):
      break

    time.sleep(0.5)

    computer(mat)
    print("Computer Played")
    Display(mat)
    print()

play()