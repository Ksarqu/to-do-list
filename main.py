import os
from time import sleep

if not os.path.isfile("list.txt"):
    open("list.txt", "x")

#clear command
if os.name == "nt":
    clear = "cls"
elif os.name == "posix":
    clear = "clear"
else:
    print("unsupported os, please contact me to fix it!")
    sleep(5)
    exit()

def read():
    with open("list.txt", "r") as f:
        list = f.read().split("|")
        return list


def remove(index):
    with open("list.txt", "r") as f:
        list = f.read().split("|")
        list.pop(index)
        separator = "|".join(list)
    with open("list.txt", "w") as new:
        new.write(separator)


def add(title):
    with open("list.txt", "a", encoding="utf-8") as f:
        f.write(f"|{title}")


while True:
    os.system(clear)
    for index, i in enumerate(read()):
        print(index, i)
    choice = int(input("\n1 - add\n2 - remove\n>>>"))
    if choice == 1:
        add(input("Title:"))
    elif choice == 2:
        remove(int(input("index: ")))
