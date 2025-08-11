# **📅 Slack Auto Message**
Planifiez automatiquement des messages dans un canal Slack à des horaires précis via une interface simple en Streamlit.


## **✅ Prérequis**
Windows
Python 3.8+ (à installer depuis python.org)
Un token Slack
L’ID du canal Slack (ex. C097N5F2FQD)


## **🚀 Installation**
Ouvrir PowerShell ou cmd
Aller dans le dossier du projet "cd C:\chemin\vers\slack_scheduler"
Lancer le script d’installation "python setup.py"


## **🎯 Lancer l’application (UI)**
Toujours dans le dossier du projet :

python -m streamlit run app.py
Cela ouvrira automatiquement une interface web dans ton navigateur.


## **🧠 Fonctionnement**
Renseigne :
    - Le channel ID
    - La date de l’examen
    - Le nom du cours

Écris tes messages avec un horaire, tu peux utiliser {course} dans le texte.
Clique sur ✅ Schedule messages dans la sidebar et sur le bouton 🚀 Schedule All.
Les messages sont planifiés avec l’API Slack si valides (heure future, format correct).


## **🛠️ Configuration Slack**
Crée un token Slack avec chat:write et chat:write.public dans une app personnalisée

Invite l’app dans le canal Slack

Remplace la variable token dans .env : SLACK_BOT_TOKEN="xoxb-votre-token-ici"