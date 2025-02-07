"# Projet Jupyter Notebook" 
Librairies

Données
Kaggle

Installation et configuration de l'environnement

Avant de commencer, il est nécessaire de configurer un environnement conda pour exécuter le projet.

1. Lancer Anaconda Prompt sous Windows

Ouvrez Anaconda Prompt (sous Windows) ou un terminal (sous macOS/Linux).

Saisissez la commande suivante pour créer un environnement conda nommé projet avec les dépendances nécessaires :

conda create -n projet python pandas numpy matplotlib jupyterlab kagglehub seaborn streamlit plotly

Lorsqu'il vous demande "Proceed ([y]/n)?", appuyez sur "y" puis Entrée.

L'installation prendra quelques minutes.

2. Activer l'environnement

Une fois l'environnement installé, activez-le avec la commande :


Expliquer conda

conda activate projet
streamlit run "H:/"
Procédure à réaliser avant les séances de TD (nous utiliserons désormais jupyter lab)

    Lancer Anaconda Prompt sous Windows
    Saisissez dans Anaconda Prompt : conda create -n projet python pandas numpy matplotlib jupyterlab kagglehub seaborn streamlit plotly

=> à la demande "Proceed ([y]/n)?" saisissez y (ou juste pressez sur la touche "entrée") => "Executing transaction" prend du temps, c'est normal Saisissez dans Anaconda Prompt : conda activate projet
