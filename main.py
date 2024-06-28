import pingip
import pingurl

def afficher_banniere():
    print("""
░█▀▄▒▄▀▄░█░░▒█▒▄▀▄░░▒█▀▄░█░█▄░█░▄▀▒
▒█▄▀░█▀█░▀▄▀▄▀░█▀█▒░░█▀▒░█░█▒▀█░▀▄█
    """)

def menu_principal():
    afficher_banniere()
    while True:
        # Afficher les options du menu principal
        print("\nMenu Principal")
        print("1. Ping une adresse IP")
        print("2. Ping une URL")
        print("3. Quitter")

        # Demander à l'utilisateur de faire un choix
        choix = input("Que voulez-vous faire ? (1, 2 ou 3) ")

        # Traiter le choix de l'utilisateur
        if choix == '1':
            pingip.ping_ip()
        elif choix == '2':
            pingurl.ping_url()
        elif choix == '3':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

# Démarrer le programme
if __name__ == "__main__":
    menu_principal()
