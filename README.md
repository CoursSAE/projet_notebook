# 📌 Projet Jupyter Notebook

## 📊 Données utilisées
Les données exploitées dans ce projet proviennent de **Kaggle** :

### 🔗 [Data Science Salaries 2023](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023)
Ce dataset fournit des informations sur les **salaires dans le domaine de la science des données** et contient **11 colonnes** principales :

- **`work_year`** : L'année où le salaire a été versé.
- **`experience_level`** : Niveau d'expérience dans le poste.
- **`employment_type`** : Type d'emploi (temps plein, temps partiel, etc.).
- **`job_title`** : Titre du poste.
- **`salary`** : Salaire brut total en devise locale.
- **`salary_currency`** : Devise du salaire.
- **`salary_in_usd`** : Salaire converti en dollars américains.
- **`employee_residence`** : Pays de résidence de l'employé.
- **`remote_ratio`** : Proportion de travail à distance.
- **`company_location`** : Pays où se trouve l'entreprise.
- **`company_size`** : Taille de l'entreprise.

---

## 🛠️ Librairies utilisées

### 📌 Librairies Jupyter
Dans un environnement **Jupyter Notebook**, certaines **commandes magiques** et bibliothèques sont utilisées pour optimiser l’expérience interactive et la visualisation :

- **`%matplotlib inline`** : Affiche les graphiques Matplotlib directement sous les cellules du notebook.
- **`%matplotlib notebook`** : Similaire à `%matplotlib inline`, mais avec des graphiques interactifs (zoom, panoramique, etc.).

### 📌 Librairies Python
Ces bibliothèques sont essentielles pour **l'analyse et la visualisation des données** :

- **`os`** : Interagit avec le système d’exploitation (gestion des fichiers et répertoires).
- **`shutil`** : Opérations avancées sur les fichiers (copie, suppression, etc.).
- **`pandas`** : Manipulation et analyse des données avec les DataFrames.
- **`numpy`** : Gestion des tableaux et matrices multidimensionnels.
- **`matplotlib.pyplot`** : Création de visualisations statiques.
- **`seaborn`** : Génération de visualisations statistiques attractives.
- **`streamlit`** : Création d’applications web interactives pour la visualisation des données.
- **`plotly.express`** : Génération de visualisations interactives avancées.

---

## ⚙️ Installation et configuration de l'environnement

Avant de commencer, il est nécessaire de **configurer un environnement conda** pour exécuter ce projet.

### 1️⃣ Lancer Anaconda Prompt sous Windows

1. **Ouvrir** Anaconda Prompt (sous Windows) ou un terminal (macOS/Linux).
2. **Créer un environnement `conda`** avec les dépendances requises :

   ```sh
   conda create -n projet python pandas numpy matplotlib jupyterlab kagglehub seaborn streamlit plotly

Lorsqu'il vous demande "Proceed ([y]/n)?", appuyez sur y puis Entrée.
L’installation prendra quelques minutes.

### 2️⃣ Activer l’environnement
Une fois l'environnement installé, activez-le avec la commande :

   ```sh
   conda activate projet

   
### 3️⃣ Lancer Jupyter Lab
Activer l’environnement (si ce n’est pas encore fait) :
   sh
   conda activate projet

Lancer Jupyter Lab en spécifiant le répertoire de travail :
   sh
   jupyter lab --notebook-dir="H:/"

Ouvrir le fichier du projet :
Dans Jupyter Lab, ouvrez Projet_SAE.ipynb pour analyser les données.
## 🚀 Exécution de l'application Streamlit

Une application interactive a été développée avec Streamlit pour visualiser les résultats d’analyse.

🔹 Lancer l'application
Activer l’environnement :
   sh
   conda activate projet
Exécuter l'application Streamlit :
   sh
   streamlit run "H:/application.py"

L'application se lancera dans votre navigateur et affichera des visualisations interactives basées sur les données analysées.
