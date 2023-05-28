import random
import sys
import pandas as pd


def guess_password():
    while True:
        restart = input("Czy chcesz zagrać ponownie (TAK/NIE)? ")
        if restart == "TAK" or restart == "tak":
            break

        elif restart == "NIE" or restart == "nie":
            sys.exit(0)

        else:
            print("Wpisz TAK lub NIE")
            continue


while True:
    category = input("Wybierz kategorię gry - kuchnia (K), zwierzeta (Z) lub "
                     "rośliny (R): ")
    category_list = ['K', 'k', 'Z', 'z', 'R', 'r']
    if category in category_list:
        df = pd.read_csv(f"{category.lower()}.csv")
        words = list(df["word"])
        category_name = df["category"][0]
        break
    else:
        print("Wybierz K, Z lub R!")
        print()

while True:
    while True:
        print("""Dostępne poziomy gry: 
            A) Poziom podstawowy - 5 prób na odgadnięcie. 
            B) Poziom średniozaawansowany - 7 prób. 
            C) Poziom zaawansowany - 10 prób.""")
        level = input("Który poziom wybierasz (A/B/C)? ")

        if level == "A" or level == "a":
            lives = 5
            break
        elif level == "B" or level == "b":
            lives = 7
            break
        elif level == "C" or level =="c":
            lives = 10
            break
        else:
            print("Wybierz A, B lub C!")
            print()

    search_word = random.choice(words)
    words.remove(search_word)
    underlines = "_" * len(search_word)
    hint = df.loc[df["word"] == search_word]["hint"].squeeze()
    print()
    print("Kategoria:", category_name)
    print("SZUKANE SŁOWO: ", " ".join(underlines))
    board = list(underlines)

    used_letters = []
    used_hint = []

    while lives > 0:
        if len(used_letters) > 0:
            print("Kategoria:", category_name)
            if len(used_hint) > 0:
                print("Wskazówka:", hint)
            print("Wykorzystane litery/słowa: ", ", ".join(used_letters))
            print("SZUKANE SŁOWO: ", " ".join(board))

        if len(used_hint) == 0:
            letter = input("Podaj literę, odgadnij hasło lub poproś o "
                           "podpowiedź (HELP): ")
        else:
            letter = input("Podaj literę lub odgadnij hasło: ")

        if letter == search_word:
            print("Brawo! Odgadłeś hasło!")
            guess_password()
            lives = 0

        if letter == "HELP" or letter == "help":
            used_hint.append(1)
            print("Wskazówka: ", hint)
            print()

        elif letter in search_word:
            # Change the underline to the guessed letter
            for i in range(len(search_word)):
                if search_word[i] == letter:
                    board[i] = letter
            print(" ".join(board))
            print()

            if "".join(board) == search_word:
                print("Brawo! Odgadłeś hasło!")
                guess_password()
                lives = 0

        else:
            print("Niestety, nie trafiłeś.")
            used_letters.append(letter)
            lives -= 1
            print("Pozostała liczba prób: ", lives)
            print()
            if lives == 0:
                print("Koniec gry, Przegrałeś :(")
                print("Szukane słowo:", search_word.upper())

                guess_password()





