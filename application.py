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

# Interprétation des résultats
st.markdown("Le tableau présente les statistiques générales des variables numériques, offrant un aperçu de la répartition des salaires, du travail à distance et des années de travail. L’échantillon contient 3 755 observations, avec une moyenne de salaire locale de 190 695 et une moyenne de 137 570 USD, bien que l’écart-type élevé indique une forte dispersion des salaires. Les salaires varient de 6 000 à 30,4 millions dans la devise locale et de 5 132 à 450 000 USD, ce qui met en évidence des disparités importantes. La médiane des salaires est de 138 000 en monnaie locale et 135 000 USD, suggérant que la plupart des salaires sont inférieurs à la moyenne en raison de valeurs extrêmes élevées. Concernant le télétravail (remote_ratio), la médiane est de 0, indiquant que la majorité des emplois sont en présentiel, bien que 25 % des emplois offrent un ratio de télétravail de 100 %. L’année de travail s’étend de 2020 à 2023, avec une moyenne autour de 2022, reflétant des données récentes.")


### 3. Distribution des salairespar rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
st.subheader("📈 Distribution des salaires")

# Création d'un boxplot pour visualiser la distribution des salaires
fig = px.box(df, x='experience_level', y='salary') 
st.plotly_chart(fig)

# Interprétation des résultats
st.markdown("Le graphique montre la distribution des salaires en fonction du niveau d'expérience, révélant une forte variabilité selon les catégories. Les niveaux Mid-Level (MI) affichent des pics de rémunération plus élevés que les autres, avec des valeurs extrêmes, tandis que Senior (SE) et Entry-Level (EN) ont des salaires plus concentrés. On observe également des outliers marqués, notamment au niveau MI, suggérant que certains postes comme Data Science Manager ou Machine Learning Engineer peuvent atteindre des rémunérations exceptionnelles. La progression des salaires n’est pas strictement linéaire : certains niveaux bénéficient d’une hausse significative avant de stagner ou de diminuer aux niveaux supérieurs, ce qui indique que certaines fonctions sont mieux rémunérées à un stade intermédiaire de carrière, alors que d’autres suivent une évolution plus stable.")


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
st.markdown("Les graphiques montrent que la rémunération varie fortement selon l'expérience, le type d'emploi, l'intitulé du poste et la localisation de l'entreprise. Les Mid-Level (MI) et Executive (EX) ont les salaires moyens les plus élevés, tandis que les Senior (SE) gagnent moins en moyenne. Les Freelancers (FL) sont les mieux rémunérés, dépassant 300k, alors que les Part-Time (PT) ont les salaires les plus bas. Certains postes comme Head of Machine Learning ou Financial Data Analyst atteignent plusieurs millions, tandis que d’autres, comme Data Analyst ou Software Engineer, ont une rémunération plus stable. La localisation joue un rôle clé : la Suisse (CH) offre les salaires les plus élevés (jusqu'à 30M), suivie des États-Unis (US) et d’autres pays à forte demande en expertise. Ces tendances montrent que les opportunités financières dépendent fortement du marché, de la spécialisation et du niveau d’expérience.")


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
st.markdown("Le graphique représente la matrice de corrélation entre différentes variables numériques, indiquant la force et la direction des relations entre elles. On observe que l'année de travail (work_year) est positivement corrélée (+0.23) avec le salaire en USD, ce qui suggère une légère augmentation des salaires au fil du temps, tandis qu'elle est négativement corrélée (-0.24) avec le ratio de travail à distance, indiquant une diminution du télétravail avec les années. Le salaire en devise locale et en USD sont faiblement liés (-0.024), ce qui pourrait refléter des fluctuations monétaires ou des différences dans la conversion. Enfin, le ratio de télétravail a une très faible corrélation avec le salaire (+0.029), suggérant que le travail à distance n’influence pas significativement la rémunération.")


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
