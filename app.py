import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration basique
st.set_page_config(
    page_title="ONU Haïti Data",
    page_icon="🇺🇳",
    layout="wide"
)

# Titre principal
st.title("🇺🇳 ONU Data Visualization - Haïti 🇭🇹")
st.markdown("Application de visualisation des données des Nations Unies en Haïti")

# Données des départements d'Haïti
def load_data():
    haiti_data = {
        'Département': ['Ouest', 'Artibonite', 'Nord', 'Nord-Est', 'Nord-Ouest', 
                       'Centre', 'Sud', 'Sud-Est', 'Grand\'Anse', 'Nippes'],
        'Population': [4029705, 1727524, 1067177, 393967, 728807, 
                      746236, 774976, 632601, 468301, 342525],
        'Projets_ONU': [45, 28, 32, 18, 22, 25, 30, 20, 15, 12],
        'Taux_Pauvrete': [65, 78, 72, 82, 85, 75, 70, 68, 80, 78],
        'Acces_Eau': [72, 58, 65, 45, 40, 55, 68, 62, 48, 52]
    }
    
    un_data = {
        'Thème': ['Développement', 'Paix et Sécurité', 'Droits Humains', 'Environnement', 'Santé', 'Éducation'],
        'Budget_Million_USD': [45, 35, 25, 20, 32, 18],
        'Projets': [120, 85, 60, 45, 95, 55]
    }
    
    return pd.DataFrame(haiti_data), pd.DataFrame(un_data)

# Chargement des données
haiti_df, un_df = load_data()

# Sidebar
st.sidebar.title("Filtres")
department_filter = st.sidebar.selectbox(
    "Sélectionnez un département:",
    ["Tous"] + list(haiti_df['Département'].unique())
)

# Métriques
st.header("📊 Indicateurs Clés")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Population Totale", f"{haiti_df['Population'].sum():,}")

with col2:
    st.metric("Total Projets ONU", haiti_df['Projets_ONU'].sum())

with col3:
    st.metric("Pauvreté Moyenne", f"{haiti_df['Taux_Pauvrete'].mean():.1f}%")

with col4:
    st.metric("Budget Total", f"${un_df['Budget_Million_USD'].sum()}M")

# Graphique 1: Projets par département
st.header("📈 Projets ONU par Département")
fig1 = px.bar(
    haiti_df,
    x='Département',
    y='Projets_ONU',
    color='Projets_ONU',
    title="Nombre de projets ONU par département"
)
st.plotly_chart(fig1, use_container_width=True)

# Graphique 2: Budget par thème
st.header("💰 Budget ONU par Thème")
fig2 = px.pie(
    un_df,
    values='Budget_Million_USD',
    names='Thème',
    title="Répartition du budget par thème"
)
st.plotly_chart(fig2, use_container_width=True)

# Graphique 3: Corrélation
st.header("🔗 Projets ONU vs Taux de Pauvreté")
fig3 = px.scatter(
    haiti_df,
    x='Projets_ONU',
    y='Taux_Pauvrete',
    size='Population',
    color='Département',
    title="Relation entre les projets ONU et le taux de pauvreté",
    size_max=40
)
st.plotly_chart(fig3, use_container_width=True)

# Tableaux de données
st.header("📋 Données Détailées")

tab1, tab2 = st.tabs(["Départements Haïti", "Thèmes ONU"])

with tab1:
    st.subheader("Données par Département")
    st.dataframe(haiti_df)
    
    # Téléchargement
    csv = haiti_df.to_csv(index=False)
    st.download_button(
        label="Télécharger CSV",
        data=csv,
        file_name="haiti_data.csv",
        mime="text/csv"
    )

with tab2:
    st.subheader("Données par Thème ONU")
    st.dataframe(un_df)

# Footer
st.markdown("---")
st.markdown("**Application développée avec Streamlit** | Données de démonstration")
