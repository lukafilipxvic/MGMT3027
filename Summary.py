import streamlit as st
import hide_st

st.set_page_config(
    layout="centered",
    page_title="MGMT3027",
    page_icon="🌐",
    initial_sidebar_state="auto",
)

st.header("🌐 Horizon - Travel Itinerary and Budget App", divider="grey")
st.subheader(":red[Problem : ] Travel planning and budgeting is hard with current apps.")
st.write("It affects +10M travellers, A Growing Problem, People are trying to solve it right now.")
st.subheader(":blue[Solution : ] Horizon is a personalised itinerary and budget agent for travellers.")
st.divider()
st.subheader("what is Horizon?")
st.markdown('''
Horizon is an AI travel assistant app. It researches destinations on the horizon and provides a structured itinerary that adapts to customer preferences. The app will use API scraping and web-sharing technology to allow subscribed users to book experiences, find value deals for their travel budget, and change those bookings through the central AI.
''')

hide_st.footer()