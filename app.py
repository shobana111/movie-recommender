import streamlit as st
import requests

API_KEY = "2e71c640af446bff83f2574840309f9b"

def get_movie_id(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    data = requests.get(url).json()
    if data["results"]:
        return data["results"][0]["id"]
    return None

def get_recommendations(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}"
    data = requests.get(url).json()
    return [movie["title"] for movie in data["results"][:5]]

st.title("🎬 Movie Recommendation App")

movie = st.text_input("Enter a movie name")

if st.button("Recommend"):
    movie_id = get_movie_id(movie)
    if movie_id:
        recs = get_recommendations(movie_id)
        st.write("### Recommended Movies:")
        for r in recs:
            st.write("👉", r)
    else:
        st.error("Movie not found")


