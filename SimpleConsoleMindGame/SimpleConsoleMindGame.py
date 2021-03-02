# IMPORT
import sys
import shutil
from functions.SaveCreate import*

user=input("Name : ")
lifes=5
level=0

print(
    "Welcome to the ConsoleMindGame " + user + "!"
    )


save(user, level, lifes)