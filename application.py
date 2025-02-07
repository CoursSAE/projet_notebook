"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données à partir du fichier csv Kaggle
df = pd.read_csv("ds_salaries.csv")


### 2. Exploration visuelle des données
# Affiche le titre
st.title("📊 Visualisation des Salaires en Data Science")

# Affiche le texte d'introduction
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")

# Affiche les 5 premières lignes du jeu de données si la case est cochée.
if st.checkbox("Afficher un aperçu des données"):
    st.write(df.head())


#Statistique générales avec describe pandas  
st.subheader("📌 Statistiques générales")
st.write(df.describe())


### 3. Distribution des salairespar rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
st.subheader("📈 Distribution des salaires")

# Création d'un boxplot pour visualiser la distribution des salaires
fig = px.bar(df, x='job_title', y='salary') 
st.plotly_chart(fig)


### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 
st.subheader("📊 Salaire moyen par catégorie")

# Sélection de la catégorie pour l'analyse du salaire moyen
selection = st.selectbox('Choisir une catégorie', options=['experience_level', 'employment_type', 'job_title', 'company_location'])

# Calcul du salaire moyen par la catégorie sélectionnée
salaire_moyen = df.groupby(selection)['salary'].mean().reset_index()

# Création d'un graphique à barres
fig_bar = px.bar(salaire_moyen, x=selection, y='salary', title=f"Salaire moyen par {selection}")
st.plotly_chart(fig_bar)

# Interprétation des résultats
st.markdown("")


### 5. Corrélation entre variables
st.subheader("🔗 Corrélations entre variables numériques")

# Sélectionner uniquement les colonnes numériques pour la corrélation
numeric_df = df.select_dtypes(include=[np.number])

# Calcul de la matrice de corrélation
correlation_matrix = numeric_df.corr()

# Affichage du heatmap avec sns.heatmap
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Interprétation des résultats
st.markdown("")


### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
# utilisez px.line
st.subheader("📈 Évolution des salaires pour les 10 postes les plus courants")

# Sélection des 10 postes les plus fréquents
job_10 = df['job_title'].value_counts().nlargest(10).index
df_job_10 = df[df['job_title'].isin(job_10)]

# Calcul du salaire moyen en fonction du niveau d'expérience
salaire_moyen_an = df_job_10.groupby(['job_title', 'experience_level'])['salary'].mean().reset_index()

# Création d'un graphique en ligne
fig_line = px.line(salaire_moyen_an, x='experience_level', y='salary', color='job_title', title="Salaire moyen par expérience")
st.plotly_chart(fig_line)

# Interprétation des résultats
st.markdown("Le graphique montre l'évolution des salaires moyens pour les 10 postes les plus courants en fonction du niveau d'expérience. On observe que certains postes, comme Data Science Manager et Data Scientist, affichent des variations importantes, avec des pics de rémunération pour les niveaux intermédiaires (MI) avant de redescendre pour les seniors (SE). À l’inverse, des postes comme Applied Scientist ou Machine Learning Engineer connaissent une progression plus stable avec l'expérience. Cette tendance suggère que certaines fonctions offrent des opportunités financières plus élevées à un moment donné de la carrière, tandis que d’autres bénéficient d’une croissance salariale plus linéaire.")


### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
st.subheader("📊 Salaire médian par expérience et taille d'entreprise")

# Calcul du salaire médian selon l'expérience et la taille de l'entreprise
salaire_median = df.groupby(['experience_level', 'company_size'])['salary'].median().reset_index()

# Création d'un graphique à barres
fig_median = px.bar(salaire_median, x='experience_level', y='salary', color='company_size', barmode='group', title="Salaire médian par expérience et taille d'entreprise")
st.plotly_chart(fig_median)

# Interprétation des résultats
st.markdown("Le graphique montre que le salaire médian augmente avec l'expérience, les employés expérimentés (EX) et seniors (SE) gagnant significativement plus que les débutants (EN) et intermédiaires (MI). On observe également que la taille de l'entreprise influence les salaires : les grandes entreprises (L) offrent les rémunérations les plus élevées, suivies des moyennes (M), tandis que les petites entreprises (S) proposent les salaires les plus bas, quel que soit le niveau d'expérience. Cette tendance souligne l'importance de l'expérience et de la structure de l'entreprise dans la rémunération des employés.")


### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages  
st.subheader("🎚️ Filtrer les données par salaire")

# Sélection d'une plage de salaires avec un slider
min_salaire, max_salaire = int(df['salary'].min()), int(df['salary'].max())
plage_salaire = st.slider("Sélectionnez une plage de salaire", min_value=min_salaire, max_value=max_salaire, value=(min_salaire, max_salaire))

# Filtrage des données en fonction de la plage de salaires sélectionnée
df_filtre = df[(df['salary'] >= plage_salaire[0]) & (df['salary'] <= plage_salaire[1])]
st.write(df_filtre)


### 9.  Impact du télétravail sur le salaire selon le pays
st.subheader("🏠 Impact du télétravail sur le salaire selon le pays")

# Calcul du salaire moyen en fonction du télétravail et de la localisation
remote_salary = df.groupby(['remote_ratio', 'company_location'])['salary'].mean().reset_index()

# Création d'un graphique à barres
fig_remote = px.bar(remote_salary, x='company_location', y='salary', color='remote_ratio', barmode='group', title="Impact du télétravail sur le salaire")
st.plotly_chart(fig_remote)

# Interprétation des résultats
st.markdown("")


### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
st.subheader("🔍 Filtrage avancé des données")

# Création des filtres pour le niveau d'expérience et la taille d'entreprise
select_exp = st.multiselect("Sélectionnez le niveau d'expérience", options=df['experience_level'].unique())
select_taille = st.multiselect("Sélectionnez la taille d'entreprise", options=df['company_size'].unique())

df_filtre = df.copy()

# Utilisation des filtres
if select_exp:
    df_filtre = df_filtre[df_filtre['experience_level'].isin(select_exp)]
if select_taille:
    df_filtre = df_filtre[df_filtre['company_size'].isin(select_taille)]
st.write(df_filtre)
