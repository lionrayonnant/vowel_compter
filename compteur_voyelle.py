#tp fonctions
compteur = 0
restart = ''
text = "voyelle"

def main():
    global compteur
    compteur = 0
    mot = input("Saisissez votre mot : ")
    get_vowels_numbers(mot)
    voyelle_ou_voyelles(compteur)
    print("Le mot", mot, "contient", compteur, text)
    restart_prog()

def restart_prog():
    restart = input("Voulez vous recommencer avec un autre mot ? ( y / n ) : ")
    if restart == "y":
        main()
    elif restart == "n":
        exit()
    else:
        print("Veuillez répondre oui ou non.")
        restart_prog()

def get_vowels_numbers(mot):
    global compteur
    for letter in mot:
            if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
                compteur += 1

def voyelle_ou_voyelles(compteur):
    global text
    if compteur <= 1:
        text = "voyelle"
    else:
        text = "voyelles"
main()


