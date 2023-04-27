import streamlit as st


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

text = st.selectbox('Pick a title:', ['Avengers: Endgame', 'The Batman', 'Avatar'])

if text == 'Avengers: Endgame':
    st.image("https://github.com/sbourganel/Streamlit_project/blob/main/Avengers.jpg")
elif text == 'The Batman':
    st.image("https://github.com/sbourganel/Streamlit_project/blob/main/The%20Batman.jpg")
else:
    st.image("https://github.com/sbourganel/Streamlit_project/blob/main/Avatar.jpg")
