import random

def players(player1, player2):
    if player1 == player2:
        return "Égalité"
    elif ((player1 == "pierre" and player2 == "ciseaux") or
          (player1 == "feuille" and player2 == "pierre") or
          (player1 == "ciseaux" and player2 == "feuille")):
        return "Joueur gagne"
    else:
        return "Ordinateur gagne"

def main():
    options = ("pierre", "feuille", "ciseaux")
    rounds = 3
    for i in range(rounds):
        players_choice = input(f"Round {i+1} - Choisis pierre, feuille ou ciseaux (ou 'exit' pour quitter) : ").lower()
        if players_choice == 'exit':
            print("Merci d'avoir joué")
            break
        if players_choice not in options:
            print("Choix invalide !")
            continue
        computer_choice = random.choice(options)
        print("L'ordinateur a choisi :", computer_choice)
        result = players(players_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
