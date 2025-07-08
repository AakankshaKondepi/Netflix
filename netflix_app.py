import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Netflix Dashboard", layout="wide")

# Title
st.title("Netflix Dataset Dashboard")
st.markdown("Visualizing from Netflix titles dataset")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("netflix_cleaned.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")
selected_type = st.sidebar.multiselect("Select Content Type", df['type'].unique(), default=df['type'].unique())
selected_country = st.sidebar.multiselect("Select Country", df['country'].dropna().unique(), default=df['country'].dropna().unique())

filtered_df = df[(df['type'].isin(selected_type)) & (df['country'].isin(selected_country))]

# 1. Movies vs TV Shows
st.subheader(" Distribution of Movies vs TV Shows")
type_counts = filtered_df['type'].value_counts()
fig1, ax1 = plt.subplots()
sns.barplot(x=type_counts.index, y=type_counts.values, palette="pastel", ax=ax1)
ax1.set_ylabel("Count")
st.pyplot(fig1)

# 2. Top 10 Countries
st.subheader("Top 10 Countries by Number of Titles")
top_countries = filtered_df['country'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(y=top_countries.index, x=top_countries.values, palette="rocket", ax=ax2)
ax2.set_xlabel("Count")
st.pyplot(fig2)

# 3. Genre Distribution
st.subheader("Genre Distribution")
genres = df['listed_in'].str.split(', ', expand=True).stack().value_counts().head(10)
fig3, ax3 = plt.subplots()
sns.barplot(y=genres.index, x=genres.values, palette="muted", ax=ax3)
ax3.set_xlabel("Count")
st.pyplot(fig3)

# 4. Top Actors (Optional: if you have actors cleaned and exploded)
st.subheader("Top 10 Appearing Actors")
if 'cast' in filtered_df.columns:
    exploded_cast = filtered_df['cast'].dropna().str.split(', ').explode()
    top_actors = exploded_cast.value_counts().head(10)
    fig4, ax4 = plt.subplots()
    sns.barplot(y=top_actors.index, x=top_actors.values, palette="magma", ax=ax4)
    ax4.set_xlabel("Number of Titles")
    st.pyplot(fig4)

# 5. Year-wise trend
st.subheader("Content Release Over the Years")
yearly_trend = filtered_df['release_year'].value_counts().sort_index()
fig5, ax5 = plt.subplots(figsize=(12, 4))
sns.lineplot(x=yearly_trend.index, y=yearly_trend.values, marker='o', ax=ax5)
ax5.set_xlabel("Release Year")
ax5.set_ylabel("Number of Titles")
st.pyplot(fig5)
