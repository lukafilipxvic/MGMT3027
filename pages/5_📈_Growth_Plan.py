import streamlit as st
import hide_st

st.set_page_config(
    layout="centered",
    page_title="Growth Plan",
    page_icon="📈",
    initial_sidebar_state="auto",
)

st.header("📈 Growth Plan", divider="grey")
st.markdown('''
The first 6-months of growth targets the development of the Horizon’s AI IP, pilot locations to test the app within set parameters, and marketing to two key customer segmentations to gauge interest in the Horizon product. This is detailed in the 6 Month Operation Plan below.
''')
st.image('images/6-month-plan.png')
st.divider()
st.subheader("Exit Stategies")
st.markdown('''
The IP development is the most valuable asset of this business. A successful Travel AI is most likely to still be purchased even if Horizon’s business model fails to be profitable. Potential buyers include, Flight Centre, Booking.com, Trivago and Google – as they seek to expand and improve the AI suggestion capabilities of Bard. Luka has key expertise in merger and acquisition transactions.\n
In the event of a successful launch the Horizon team will aim to expand to all Australian travel markets, and limited international markets for additional pilot programs. Such a market would be Ibiza for example. This would require a review of marketing strategies for differing regional markets.\n
''')
st.divider()
st.subheader("Potential growth markets")
st.markdown('''
Both market size of travel planner apps and Generative AI in travel market are expected to dramatically grow by 2032. This is due to the technological development of AI, which allows for personalized travel plans, people of all ages highly trust AI recommendations. About 73% of users trust content provided by AI.''')
st.image('images/travel-app-market.png', caption="Global Travel Planner App Market")
st.image('images/gen-ai-market.png', caption="Generative AI in Travel Market")
st.divider()
st.subheader("Investor Offer")
st.markdown('''
Our initial offer is a 20% private equity stake in Horizon in exchange for an $80,000 investment. This seed money will enable LYMB Innovations to engage in six months of operations, including developing an active Travel AI and pilot studies within three target locations.\n
If our initial pilot proves successful, partnership grants from local councils and regional governments should help us recoup most of this investment during the early rollout stages. In the event of liquidation, the initial private equity investment of $80,000 will be prioritized for repayment with fixed interest from the contract’s signing day, reducing risk for our founding seed investors. 
''')
hide_st.footer()