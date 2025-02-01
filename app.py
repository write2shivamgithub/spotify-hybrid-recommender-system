import streamlit as st # Used to build the web app interface.
from content_based_filtering import recommend
from scipy.sparse import load_npz # load_npz: Loads the preprocessed song data stored in a sparse matrix.
import pandas as pd
# transformed data path
transformed_data_path = "data/transformed_data.npz"
# cleaned data path
cleaned_data_path = "data/cleaned_data.csv"
# load the data
data = pd.read_csv(cleaned_data_path)
# load the transformed data
transformed_data = load_npz(transformed_data_path)
# Title
st.title('Welcome to the Spotify Song Recommender!')
# Subheader
st.write('### Enter the name of a song and the recommender will suggest similar songs 🎵🎧')
# Text Input
song_name = st.text_input('Enter a song name:')
st.write('You entered:', song_name)
# k recommndations
k = st.selectbox('How many recommendations do you want?', [5,10,15,20], index=1) #Default value: 10 recommendations.
# Button
if st.button('Get Recommendations'):
    st.write('Recommendations for', f"**{song_name}**")
    recommendations = recommend("Hips Don't Lie",data,transformed_data,k)
    
    # Display Recommendations
    for ind , recommendation in recommendations.iterrows():
        song_name = recommendation['name'].title()
        artist_name = recommendation['artist'].title()
        
        if ind == 0:
            st.markdown("## Currently Playing")
            st.markdown(f"#### **{song_name}** by **{artist_name}**")
            st.audio(recommendation['spotify_preview_url'])
            st.write('---')
        elif ind == 1:   
            st.markdown("### Next Up 🎵")
            st.markdown(f"#### {ind}. **{song_name}** by **{artist_name}**")
            st.audio(recommendation['spotify_preview_url'])
            st.write('---')
        else:
            st.markdown(f"#### {ind}. **{song_name}** by **{artist_name}**")
            st.audio(recommendation['spotify_preview_url'])
            st.write('---')