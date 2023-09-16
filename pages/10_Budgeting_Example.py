import streamlit as st
import hide_st
import pandas as pd

st.set_page_config(
    layout="centered",
    page_title="Budgeting Example",
    page_icon="💡",
    initial_sidebar_state="auto",
)

@st.cache_data
def read_cities(ttl=3600):
    ''' Read data extracted
        from numbeo-city.py
    '''
    df = pd.read_csv("data/cost_of_living.csv", encoding="latin-1")
    cities = df['City'].tolist()
    return cities


df = pd.read_csv("data/cost_of_living.csv", encoding="latin-1")
cities = read_cities()

st.header("💡 Budgeting Example", divider="grey")

city_origin = st.selectbox('Select origin', options=cities, placeholder="Select origin", help="If city not found, select the nearest applicable one.")
city_destination = st.multiselect('Select destination', options=cities, default=None, placeholder="Select destination/s", help="If city not found, select the nearest applicable one.")
st.write("")

# Assuming `df` is the DataFrame containing the data
selected_cities = [city_origin] + city_destination
comparison_df = df[df['City'].isin(selected_cities)][['City', 'Groceries Index', 'Restaurant Price Index']]


# Calculate the differences in prices
groceries_index_origin = df[df['City'] == city_origin]['Groceries Index'].values[0]
restaurant_index_origin = df[df['City'] == city_origin]['Restaurant Price Index'].values[0]

for city in city_destination:
    groceries_index_destination = df[df['City'] == city]['Groceries Index'].values[0]
    restaurant_index_destination = df[df['City'] == city]['Restaurant Price Index'].values[0]

    groceries_difference = groceries_index_destination - groceries_index_origin
    restaurant_difference = restaurant_index_destination - restaurant_index_origin

    st.markdown(f'''
    In {city.split(',')[0]}:\n
    Groceries are **{groceries_difference:.2f}% {'more' if groceries_difference > 0 else 'less'} expensive** than in {city_origin.split(',')[0]}.\n
    Restaurants are **{restaurant_difference:.2f}% {'more' if restaurant_difference > 0 else 'less'} expensive** than in {city_origin.split(',')[0]}.\n
    ''')
    st.write("")

hide_st.footer()
