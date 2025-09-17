import random


def players(player1, player2):
    if player1 == player2:
        return "Egalité"



    elif ((player1 == "pierre " and player2 == "feuille") or
          (player1 == "feuille" and player2 == "pierre ") or
          (player1 == "ciseaux" and player2 == "feuille")):

        return "joueur 1  gagne "
    else:
        return "ordinateur gagne  "


options = ("pierre", " feuille", "ciseaux")

while True:

    players_choice = input(" Choisis pierre , feuille ou ciseaux : ").lower()
    if players_choice == 'Exit':
        print("Merci d'avoir joué")
        break

if players_choice not in options:
    print("il n'y a pas de choisi !")


else:
    computer_choice = random.choice(options)
    print("l'ordinateur a choisi : ", {computer_choice})
    result = players(players_choice, computer_choice)
    print(result)
