import streamlit as st
from linkedin import linkedin_profiles
import hide_st

st.set_page_config(
    layout="centered",
    page_title="MGMT3027",
    page_icon="🌐",
    initial_sidebar_state="auto",
)

st.header("🌐 Horizon - Travel Itinerary and Budget App", divider="grey")
st.subheader(":red[Problem : ] Travel planning and budgeting is hard with current apps.")
st.markdown('''The problem is:\n
1. affecting +10M travellers (potential customers)
2. growing at a fast pace (+18.2% CAGR) 
3. trying to be solved it right now
''')
st.subheader(":blue[Solution : ] Horizon is a personalised AI itinerary and budget agent for travellers.")

st.divider()

st.subheader("What is Horizon?")
st.markdown('''
Horizon is an **AI travel assistant and budgeting app.** It researches destinations *on the horizon* and provides a structured itinerary that adapts to customer preferences.\n
The app will use API scraping and web-sharing technology to allow subscribed users to book experiences, find value deals for their travel budget, and change those bookings through the central AI.
''')
st.divider()

st.subheader("Our insight / Unfair Advantages related to growth")
st.write("Why our company will growth faster than other companies and competitors:")
st.markdown('''
**:blue[Founders : ]** The team of four share prior experience in developing software and know what is needed for the consumers \n
**:green[Market : ]** The problem is in the right space, high growth = high demand \n
**:orange[Product : ]** 10x better than the competition due to underlying intellectual property \n
**:red[Acquisition :]** Will we spend ~$0 in acquiring customers due our to strong value proposition \n
**:violet[Monopoly :]** The more users using Horizon, the stronger our data and recommendations become
''')
st.divider()

st.subheader("The Horizon Team", divider=True)


linkedin_profiles("yamato-takahashi-a73b65231", "ben-scanlon-b13667227", "lukafilipxvic", "max-rupert-1812481b0")

hide_st.footer()