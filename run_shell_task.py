import os
import time

# Remplacez par le chemin de votre projet Django
project_dir = r"C:\Users\arthu\github\Geoportail_test"

# Accéder au répertoire du projet
os.chdir(project_dir)

print("Démarrage de la tâche")

# Lancer le shell Django et exécuter une commande personnalisée
try:
    # Ouvrir le shell Django
    os.system('CALL conda.bat activate geoenv && python manage.py shell < commands.py')
    print("Tâche terminée, fermeture du shell.")
    # Attendre 10 secondes
    time.sleep(10)
except Exception as e:
    print(f"Erreur : {e}")
