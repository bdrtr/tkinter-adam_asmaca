import os
from PIL import Image, ImageTk

gameSet = {}
ImStates = {}


current_dir = os.path.dirname(__file__)
#icon_path = os.path.dirname(__file__)+"/pictures/icon.png"

with open(current_dir+"/settings.txt") as fl:
    experision = fl.readline()
    while experision:
        key, value = experision.strip().split("=")
        gameSet[key.strip()] = value.strip()
        experision = fl.readline()

for i in range(1,6):
    img = Image.open(current_dir+f"/pictures/state{i}.png")
    ImStates[f"state{i}"] = img

@staticmethod
def openPic(name, size=(300,300)):
        return (ImageTk.PhotoImage(Image.open(current_dir+"/pictures/"+name),size=(size)),size)
