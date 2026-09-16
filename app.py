import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬"
)

@st.cache_data
def load_data():
    return pd.read_csv("movies.csv")

movies = load_data()


def recommend_movies(data, genre, language, movie_type):
    results = data.copy()

    results["Similarity Score"] = 0

    results.loc[
        results["Genre"] == genre,
        "Similarity Score"
    ] += 2

    results.loc[
        results["Language"] == language,
        "Similarity Score"
    ] += 1

    results.loc[
        results["Type"] == movie_type,
        "Similarity Score"
    ] += 1

    results = results.sort_values(
        by=["Similarity Score", "Rating"],
        ascending=False
    )

    return results


st.title("🎬 AI Movie Recommendation System")

st.write(
    "Get personalized movie recommendations "
    "based on your preferences."
)

st.divider()

st.subheader("👤 Select Your Preferences")

genre = st.selectbox(
    "Choose your favorite genre:",
    sorted(movies["Genre"].unique())
)

language = st.selectbox(
    "Choose your preferred language:",
    sorted(movies["Language"].unique())
)

movie_type = st.selectbox(
    "Choose movie type:",
    sorted(movies["Type"].unique())
)


if st.button("🔍 Get Recommendations"):

    recommendations = recommend_movies(
        movies,
        genre,
        language,
        movie_type
    )

    st.subheader("🎯 Recommended Movies")

    top_movies = recommendations.head(5)

    for _, movie in top_movies.iterrows():

        st.markdown(
            f"""
            ### 🎬 {movie['Movie']}
            **Genre:** {movie['Genre']}  
            **Language:** {movie['Language']}  
            **Type:** {movie['Type']}  
            **Rating:** ⭐ {movie['Rating']}  
            **Similarity Score:** {movie['Similarity Score']}
            """
        )

        st.divider()

    st.success("Recommendations generated successfully!")