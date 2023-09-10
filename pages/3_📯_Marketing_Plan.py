import streamlit as st
import hide_st

st.set_page_config(
    layout="centered",
    page_title="Marketing Plan",
    page_icon="📯",
    initial_sidebar_state="auto",
)

st.header("📯 Marketing Plan")
st.subheader("Target Segmentations and Value Propositions")
st.markdown('''
Among our identified customer segments, university students and student backpackers stand out as those most likely to embark on spontaneous trips, seeking the convenience of an adjustable itinerary. They are the demographic most likely to spread the word of a new AI product and benefit from an interactive itinerary app. Their input into the Pilot versions of the algorithm will benefit the R&D of the application the most due to diverse interests and willingness to engage with new products.
''')
st.image('images/customer-vp.png')

st.markdown('''
Our secondary and most profitable market segmentation is young double-income households, often comprised of families with children. The value proposition of an application that can streamline itinerary creation and bookings is justified to the Gen X demographic
''')
st.divider()
st.subheader("Horizon Customer and Supplier Positioning")
st.markdown('''
Our positioning strategy revolves around offering a complementary service to travel rather than a substitute for their current travel planning. Marketing research has found that emphasising an AI’s ability to interact with customers’ emotional drivers enhances marketing retention (Huang, 2021). The personal nature of the tailored AI itinerary it generates creates a sunk cost proposition in the user's mind.
''')
st.markdown('''
The feeling of the itinerary aligning with the individual’s tastes and preferences increases retention and perceived value. This approach generates high customer satisfaction by eliminating the friction often associated with misunderstandings or discomfort in sharing personal preferences and experiences with a person (Huang, 2021).
''')
st.markdown('''
The app is a dynamic ecosystem where consumers actively contribute to value co-creation, enriching the travel experience for all users through past uses. As we move forward, user feedback and validation, particularly during the pilot phase, will refine and enhance the central algorithm. This feedback loop will be instrumental in shaping our ongoing development efforts and guiding our marketing strategies. 
''')
st.divider()
st.subheader("Evaluation of Market Competitors")
st.image('images/competitors.png')
st.markdown('''
Horizons brand must become synonymous with fast travel information and AI booking assistance. This is a market gap identified in the competitor analysis table above. The flexibility of AI assistance will allow Horizons to position itself as more accessible and streamlined than specialised travel websites. Further, booking functions and a payment portal will allow Horizon AI to edge out AI competitors that are restricted from these tasks.
''')
hide_st.footer()