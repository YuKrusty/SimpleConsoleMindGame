import shutil

def save(user, level, lifes):
    source = "save.json"
    target = "sv/save.json"
    with open("save.json", "a+") as save:
        save.write("{\n")
        save.write("Name : " + user + "\nLevel : " + str(level) + "\nLifes : " + str(lifes) + "\n")
        save.write("}\n")
    shutil.move(source, target)