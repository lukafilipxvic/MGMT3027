import streamlit as st
from streamlit_extras.grid import grid
import hide_st
import datetime
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
canberra_index = cities.index("Canberra, Australia")

today = datetime.datetime.now()
todayplusweek = today + datetime.timedelta(weeks=1)

st.header("💡 Budgeting Example", divider="grey")

grid = grid([1, 1.5], [1, 1], [0.6, 1, 1], vertical_align="bottom")

col1, col2 = st.columns([1, 1])

city_origin = grid.selectbox('Select origin', index=canberra_index,
    options=cities, placeholder="Select origin",
    help="If city not found, nearest suitable alternative.")
city_destination = grid.multiselect('Select destination',
    options=cities, default=None,
    placeholder="Select destination/s",
    help="If city not found, nearest suitable alternative.")

departure_date = grid.date_input("Select departure date",
    (today), today,format="DD/MM/YYYY")
return_date = grid.date_input("Select return date",
    (todayplusweek), today,format="DD/MM/YYYY")

people = grid.number_input("Number of adults", 1, 25, step=1)

flights = grid.number_input(label="Flight costs ($)", step=1)

if grid.button("🔍 Budget the horizon") and city_destination != []:
    # Assuming `df` is the DataFrame containing the data
    selected_cities = [city_origin] + city_destination
    comparison_df = df[df['City'].isin(selected_cities)][['City', 'Groceries Index', 'Restaurant Price Index']]

    # Calculate the differences in prices
    groceries_index_origin = df[df['City'] == city_origin]['Groceries Index'].values[0]
    restaurant_index_origin = df[df['City'] == city_origin]['Restaurant Price Index'].values[0]

    # 

    for city in city_destination: # Get the indexes
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
else:
    st.toast("No destination selected.")
hide_st.footer()
