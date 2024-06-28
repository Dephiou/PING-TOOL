# pingurl.py
from ping3 import ping
import time

def afficher_banniere_ping_url():
    print("""
░█▒█▒█▀▄░█▒░░░▒█▀▄░█░█▄░█░▄▀▒
░▀▄█░█▀▄▒█▄▄▒░░█▀▒░█░█▒▀█░▀▄█
    """)

def ping_url():
    afficher_banniere_ping_url()
    # Demander à l'utilisateur l'URL à pinguer
    adresse = input("Entrez l'URL à pinguer : ")
    
    # Demander à l'utilisateur combien de pings il veut faire
    nombre_de_pings = int(input("Combien de pings voulez-vous effectuer ? (Entrez 0 pour un ping infini) "))
    
    # Demander à l'utilisateur le délai entre chaque ping
    delay = float(input("Entrez le délai entre chaque ping (en secondes) : "))

    # Effectuer les pings
    if nombre_de_pings <= 0:
        print(f"Ping infini pour {adresse}. Appuyez sur Ctrl+C pour arrêter.")
        i = 1
        try:
            while True:
                temps_de_reponse = ping(adresse)
                if temps_de_reponse is not None:
                    print(f"Ping {i}: Temps de réponse pour {adresse}: {temps_de_reponse * 1000:.2f} ms")
                else:
                    print(f"Ping {i}: {adresse} est injoignable.")
                i += 1
                time.sleep(delay)
        except KeyboardInterrupt:
            print("\nPing infini interrompu par l'utilisateur.")
    else:
        for i in range(nombre_de_pings):
            temps_de_reponse = ping(adresse)
            if temps_de_reponse is not None:
                print(f"Ping {i+1}: Temps de réponse pour {adresse}: {temps_de_reponse * 1000:.2f} ms")
            else:
                print(f"Ping {i+1}: {adresse} est injoignable.")
            time.sleep(delay)
