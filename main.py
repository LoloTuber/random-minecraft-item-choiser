from backend import getrandomelement,settings,savefile
from time import sleep
import os
from random import randint
#state=-1 выход
#state=0 главное меню
#state=1 рулетка рандома
#state=2 настройки

state=0

def rollitems():
    os.system('cls' if os.name == 'nt' else 'clear')
    item = ""
    if settings["rollingtype"]=="Linear":
        for i in range(randint(5,17)):
            item=getrandomelement()
            print(item+"\n")
            sleep(0.32)
        item=getrandomelement()
        print(item+" <- ваш предмет")
    if settings["rollingtype"]=="Rolling":
        for i in range(randint(5,17)):
            os.system('cls' if os.name == 'nt' else 'clear')
            item=getrandomelement()
            print(item)
            sleep(0.46)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(item+" <- ваш предмет")
    if settings["rollingtype"]=="RollingThree":
        i1=getrandomelement()
        i2=getrandomelement()
        i3=getrandomelement()
        for i in range(randint(1,20)):
            os.system('cls' if os.name == 'nt' else 'clear')
            item=i2
            col1 = i1.center(35)
            col2 = i2.center(35)
            col3 = i3.center(35)
            line = col1 + col2 + col3
            print(line)
            arrow_pos = 35 + len(col2) // 2
            print(" " * arrow_pos + "^")
            print(" " * arrow_pos + "|")
            print(" " * arrow_pos + "|")
            print(" " * arrow_pos + "|")
            i1 = i2
            i2=i3
            i3=getrandomelement()
            sleep(1.5)
        print(item+" <- ваш предмет")
    global state
    state=0

def validateinput(input:str):
    global state
    if state==0:
        if input == "2":
            return 2
        if input == "1":
            return 1
        elif input == "0":
            return -1
    elif state==2:
        if input == "1":
            if settings["rollingtype"]=="Linear":
                settings["rollingtype"]="Rolling"
                savefile(os.path.dirname(os.path.abspath(__file__))+"/settings.json",settings)
            elif settings["rollingtype"]=="Rolling":
                settings["rollingtype"]="RollingThree"
                savefile(os.path.dirname(os.path.abspath(__file__))+"/settings.json",settings)
            elif settings["rollingtype"]=="RollingThree":
                settings["rollingtype"]="Linear"
                savefile(os.path.dirname(os.path.abspath(__file__))+"/settings.json",settings)
        if input == "0":
            return 0


    if input=="":
        return state
    else:
        return state

def settingsmenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    if settings["rollingtype"]=="Linear":
        print("1. Изменить прокрутку(сейчас линейное)")
    elif settings["rollingtype"]=="Rolling":
        print("1. Изменить прокрутку(сейчас крутящаесе)")
    elif settings["rollingtype"]=="RollingThree":
        print("1. Изменить прокрутку(сейчас выбор из трёх)")
    print("0. Выйти из настроек")

def printmenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Начать крутить")
    print("2. Настройки")
    print("0. Выйти")

def main():
    while True:
        global state
        if state==0:
            printmenu()
        elif state==1:
            rollitems()
        elif state==2:
            settingsmenu()
        elif state==-1:
            return 0
        state = validateinput(input())

if __name__ == "__main__":
    main()