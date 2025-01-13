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

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        training_course()

    elif int(choice) == 2:
        tavern()
    elif int(choice) == 3:
        print("Budeš bojovat")
    else:
        crossroad()


def training_course():
    print("-------------------------------")
    print("   Jsi na Tréninkovém hřišti   ")
    print("-------------------------------")

    print("\nVyber si trénink")
    print("1 - Útok")
    print("2 - Obrana")

    random_chance = random.randint(1, 100)

    if random_chance < 50:
        print("vyhral jsi")
    else:
        print("prohral jsi")

def main():
    welcome_screen()

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        crossroad()
    else:
        print("Hra ukončena")


main()