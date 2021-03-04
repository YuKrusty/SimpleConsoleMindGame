# IMPORT
import sys
import shutil
from functions.Messages import*
from functions.QuestionsModel import*
from functions.SaveCreate import*

user=input("Name : ")
lifes=5
level=0

welcome(user)
presentation()

text = "test"
answer1 = "test1"
answer2 = "test2"

model(text, answer1, answer2)

save(user, level, lifes)