import random

global hp, xp, money


hp = 100
xp = 0
money = 0

def add_hp(amount):
    global hp
    hp += amount

    if hp > 100:
        hp = 100

def stats():
    print(f"### HP {hp} ### XP {xp} ### $$$ {money}###")

def welcome_screen():
    print("########################")
    print("     Vítej v RPG hře    ")
    print("########################")

    print("\nMenu:")
    print("1 - Zahájit hru")
    print("Cokoliv jiného - ukončit hru")

def tavern():
    global hp, xp, money
    print("-----------------------")
    print("      Jsi v krčmě      ")
    print("-----------------------")

    stats()

    print("\nMenu:")
    print("1 - Koupím si pivo")
    print("2 - Koupím si polévku")
    print("3 - Koupím si velké jídlo")

    choice = input("Výběr z menu: ")
    if int(choice) == 1:
        if money < 20:
            print("Nemáš dostatek peněz")
        else:
            print("Koupil sis báječné pivo")
            money -= 20
            add_hp(5)
    elif int(choice) == 2:
        if money < 35:
            print("Nemáš dostatek peněz")
        else:
            print("Koupil sis hnusnou polévku")
            money -= 35
            add_hp(6)
    elif int(choice) == 3:
        if money < 80:
            print("Nemáš dostatek peněz")
        else:
            print("Dostal jsi před sebe půlku divočáka")
            money -= 80
            add_hp(50)

    stats()
    crossroad()

def crossroad():
    print("-----------------------")
    print("   Jsi na křizovatce   ")
    print("-----------------------")

    print("\nMenu:")
    print("1 - Tréninkové hriště")
    print("2 - Krčma")
    print("3 - Souboj")
    print("4 - Konec hry")

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        training_course()

    elif int(choice) == 2:
        tavern()
    elif int(choice) == 3:
        real_fight()
    elif int(choice) == 4:
        print("Ukončil si hru. Ve tvé hře jsi dosáhl: ")
        stats()
        exit()
    else:
        crossroad()

def fight(win_under):
    random_chance = random.randint(1,100)

    if random_chance < win_under:
        return True
    else:
        return False

def training_course():
    global xp
    print("-------------------------------")
    print("   Jsi na Tréninkovém hřišti   ")
    print("-------------------------------")

    print("\nVyber si trénink")
    print("1 - Útok")
    print("2 - Obrana")


    if fight(50):
        xp += 1
        print("vyhrál jsi")
    else:
        print("prohrál jsi")

    crossroad()
def real_fight():
    global xp, hp, money
    print("-------------------------------")
    print("   Potkal jsi monstrum   ")
    print("-------------------------------")

    print("\nVyber si typ boje")
    print("1 - Útok")
    print("2 - Obrana")

    if fight(random.randint(40,60)):
        xp += random.randint(5,30)
        money += random.randint(10,40)
        print("vyhrál jsi")
    else:
        hp -= random.randint(5,20)
        print("prohrál jsi")

        crossroad()

def main():
    welcome_screen()

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        crossroad()
    else:
        print("Hra ukončena")


main()