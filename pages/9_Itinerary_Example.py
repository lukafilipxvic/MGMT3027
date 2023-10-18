import streamlit as st
from streamlit_extras.grid import grid
import datetime
import hide_st

st.set_page_config(
    layout="centered",
    page_title="Itinerary Example",
    page_icon="💡",
    initial_sidebar_state="auto",
)

st.header("💡 Itinerary Example", divider="grey")

grid = grid([1.5, 1, 1], [1, 1, 2], 3, vertical_align="bottom")


today = datetime.datetime.now()
todayplusweek = today + datetime.timedelta(weeks=1)

destination = grid.selectbox(
    "Select Destination",
    options=["Canberra", "Byron Bay"],
    index=None)

if destination != "":
    departure_date = grid.date_input("Select departure date",
        (today), today,format="DD/MM/YYYY")
    return_date = grid.date_input("Select return date",
        (todayplusweek), today,format="DD/MM/YYYY")

    colA, colB = st.columns([1, 1])

    people = grid.number_input(
        "Number of adults",
        1, 25,
        step=1)

    budget = grid.select_slider("Budget", options=["Free", "Cheap", "Average", "Expensive"])

    preferences = grid.multiselect("Your activity preferences",
        options=["Hiking", "Music festival", "Surfing", "Restaurants", "Museums"],
        placeholder="Your activity preferences",
        label_visibility="collapsed")


    if grid.button("🔍 Search the Horizon"):
        if destination == "Canberra":
           st.write(f"Here is your {destination} itinerary for {departure_date} to {return_date}:")
           st.image('images/itineraries/byron-surf.png', caption="")
        if destination == "Byron Bay":
            st.write(f"Here is your {destination} itinerary for {departure_date} to {return_date}:")
            st.image('images/itineraries/byron-surf.png', caption="")
    
    hide_st.footer()