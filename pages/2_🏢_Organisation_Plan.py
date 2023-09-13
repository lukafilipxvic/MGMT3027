import streamlit as st
import hide_st

st.set_page_config(
    layout="centered",
    page_title="Organisation Plan",
    page_icon="🏢",
    initial_sidebar_state="auto",
)

st.header("🏢 Organisation Plan", divider="grey")
st.subheader("Key Value Creation and Management Structure")
st.markdown('''
Horizon’s key value activities:
1.	Focus on AI technology development. Building sophisticated algorithms to power personalized itineraries and real-time recommendations.
2.	Managing data harvesting, server hosting and API scraping to ensure up-to-date information.
3.	Marketing and customer acquisition efforts to expand both supplier and consumer users.
4.	An integrated booking system to streamline flights, insurance, and accommodation transactions, enhancing the travel planning value capture.
''')
st.divider()
st.image('images/org-structure.png', caption="Horizon Organisational Structure")

st.markdown('''
While we possess key skills as shown in the organizational structure, we recognize the need for industry-specific commercial experience. To address this, we are open to offering an increased equity stake to individuals who can guide Horizon through the post-pilot stages and with Travel industry experience.
''')
st.divider()
st.markdown('''
:blue[Luka KR:] Coding and API Scraping Web Server cost mitigation \n
:orange[Ben KR:] SEO knowledge and implementation experience Professional Market Research Consultant \n
:red[Yamato KR:] International Travel Planner Experience \n
:green[Max KR:] Financial Documentation and invoicing experience
''')
st.divider()
st.markdown('''
Strategically, we intend to target regional travel networks like Visit Canberra. This will allow us to apply for government grants, increasing revenue and reducing pilot costs. Partnering with local tourism hubs, such as hotels and locally owned businesses, will help rapidly expand Horizon's brand awareness.\n
This approach positions our product as a complementary product, encouraging interactions and data sharing, like how pubs and cafes display labels to signify their relationship with local Australian products.
''')
st.divider()

hide_st.footer()