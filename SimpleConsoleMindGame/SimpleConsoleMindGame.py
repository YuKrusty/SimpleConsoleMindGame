# IMPORT
import sys
import shutil
from functions.Messages import*
from functions.SaveCreate import*

user=input("Name : ")
lifes=5
level=0

welcome(user)
presentation()
save(user, level, lifes)