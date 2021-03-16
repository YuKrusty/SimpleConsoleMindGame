import shutil

def save(user, level, lifes):
    source = "save.yureiSave"
    target = "sv/save.yureiSave"
    with open("save.yureiSave", "a+") as save:
        save.write("{\n")
        save.write("Name : " + user + "\nLevel : " + str(level) + "\nLifes : " + str(lifes) + "\n")
        save.write("}\n")
    shutil.move(source, target)