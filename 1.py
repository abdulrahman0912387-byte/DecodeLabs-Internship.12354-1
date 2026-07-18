import streamlit as st
import pandas as pd
import numpy as np

dataset = pd.read_csv('movies (2).csv')
st.write("Available genres:", dataset['genre'].unique())

user = st.text_input("What type of movies do you like?")

if user:
    matches = dataset[dataset['genre'].str.lower() == user.lower()]
    matches = matches.sort_values("score", ascending=False)

    if len(matches) == 0:
        st.write("No movies found for that genre. Try: Action, Comedy, Drama, Horror, etc.")
    else:
        st.write(matches[['name','genre','score','director','year']].head(10))
        



