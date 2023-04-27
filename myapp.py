import streamlit as st
import time

st.title('Outil de recommandation de films')

  
  
st.write("Please select what kind of movie, you wanna watch")
# multi select box
 
# first argument takes the box title
# second argument takes the options to show
genres = st.multiselect("Genres: ",
                         ['Drama',
                          'Action', 
                          'Fantasy',
                          'Comedy',
                          'Romance', 'Thriller', 'Crime', 'Adventure', 'Horror', 'Mystery', 'Biography', 'Family', 'History', 'Animation','Sci-Fi', 'Documentary'])



# write the selected options
st.write("You selected", len(genres), 'genres')


# slider
 
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Sélectionnez une note minimale de film", 1, 10)
 
# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))

col1, col2, col3 = st.columns([1,2,1])

text = col1.st.selectbox('Pick a title:', ['Avengers: Endgame', 'The Batman', 'Avatar'])
if 'photo' not in st.session_state:
  st.session_state['photo']='not done'

def change_photo_state():
  st.session_state['photo']='done'

camera_photo = col2.camera_input('take a photo', on_change=change_photo_state)

if st.session_state['photo'] == 'done':
  progress_bar = col2.progress(0)

  for perc_completed in range(100):
    time.sleep(0.05)
    progress_bar.progress(perc_completed+1)

    col2.success('photo uploaded successfully!')

col3.metric(label='Movie Revenue', value=15000, delta='30')

