# IMPORT
import sys
import shutil
from functions.messages import*
from functions.questions_model import*
from functions.save_create import*

user=input("Name : ")
lifes=5
level=0

welcome(user)
presentation()

# Question 1
text = "What's the name of the LinkIt developer ?"
answer1 = "Maxime"
answer2 = "Thomas"
model(text, answer1, answer2)
if text!="1":
    while text!="1":
        lifes=lifes-1
        print("\nYou lost 1 life.")
        text = input("\nRetry : ")
level=level+1
print("\nGG! You won 1 level. Next question !")

save(user, level, lifes)