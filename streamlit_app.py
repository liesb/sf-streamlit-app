import streamlit
import pandas as pd
import requests

# DATA

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt").set_index("Fruit")

# APP

streamlit.title("My Mom's new healthy diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# picklist of fruits to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruit_list_filtered = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruit_list_filtered)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_input = streamlit.text_input("Which fruit would you like information about?", "Kiwi")
streamlit.write("The user entered" + fruityvice_input)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruityvice_input)
fruityvice_normalised = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalised)

