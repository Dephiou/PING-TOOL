#!/bin/bash

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "Python 3 n'est pas installé. Veuillez l'installer et réessayer."
    exit 1
fi

# Installer le module ping3 s'il n'est pas déjà installé
if ! python3 -c 'import ping3' &> /dev/null; then
    echo "Installation du module ping3..."
    pip3 install ping3
    if [ $? -ne 0 ]; then
        echo "Erreur lors de l'installation du module ping3. Veuillez installer manuellement."
        exit 1
    fi
fi

# Lancer le fichier main.py
echo "Lancement de l'application..."
python3 main.py

# Fin du script
echo "Fin du script."
