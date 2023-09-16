import streamlit as st
from linkedin import linkedin_profiles
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
1.	**Focus on AI technology development.** Building sophisticated algorithms to power personalized itineraries and real-time recommendations.
2.	**Managing data harvesting**, server hosting and API scraping to ensure up-to-date information.
3.	**Marketing and customer acquisition** efforts to expand both supplier and consumer users.
4.  An **integrated booking system** to streamline flights, insurance, and accommodation transactions, enhancing the travel planning value capture.
5.  **Automated budget/cost estimator** based on duration, cost of destination and other key factors.
''', unsafe_allow_html=True)

st.write("")
st.subheader("APIs for Horizon", divider="grey")

col1, col2 = st.columns(2)

col1.markdown('''
<p style="margin-bottom:0; font-style: italic">Flights</p>\n
- <a href="https://developers.skyscanner.net/docs/intro" target="_blank">Skyscanner API</a>

<p style="margin-bottom:0; font-style: italic">Accomodation</p>\n
- <a href="https://developers.expediagroup.com/docs" target="_blank">Expedia API</a>
- <a href="https://www.tripadvisor.com/developers" target="_blank">TripAdvisor API</a>
- <a href="https://www.airbnb.com.au/partner" target="_blank">Airbnb API</a>
- <a href="https://developers.booking.com/api/" target="_blank">Booking.com API</a>

<p style="margin-bottom:0; font-style: italic">Events</p>\n
- <a href="https://developers.gadventures.com/docs/index.html" target="_blank">G Adventures API</a>
- <a href="https://www.predicthq.com/events/travel" target="_blank">PredictHQ API</a>

<p style="margin-bottom:0; font-style: italic">Destinations/Cities/Countries Content</p>\n
- <a href="https://www.roadgoat.com/business/cities-api" target="_blank">RoadGoat API</a>
- <a href="https://www.predicthq.com/events/travel" target="_blank">PredictHQ API</a>

<p style="margin-bottom:0; font-style: italic">Points of Interest (POIs) Content</p>\n
- <a href="https://www.yelp.com/developers" target="_blank">Yelp Fusion API</a>
''', unsafe_allow_html=True)

col2.markdown('''
<p style="margin-bottom:0; font-style: italic">Weather</p>\n
- <a href="https://api.windy.com" target="_blank">Weather forecast API</a>
- <a href="https://openweathermap.org/api" target="_blank">OpenWeather API</a>

<p style="margin-bottom:0; font-style: italic">Map Services</p>\n
- <a href="https://developer.apple.com/maps/" target="_blank">Apple Maps SDK</a>
- <a href="https://mapsplatform.google.com/" target="_blank"> Google Maps Platform</a>

<p style="margin-bottom:0; font-style: italic">Geolocation</p>\n
- <a href="https://ip-api.com/docs/api:json" target="_blank">Ip-api</a>

<p style="margin-bottom:0; font-style: italic">Currencies</p>\n
- <a href="https://exchangeratesapi.io/" target="_blank">Exchange Rates API</a>

<p style="margin-bottom:0; font-style: italic">Other</p>\n
- <a href="https://timezonedb.com/api" target="_blank">Time Zones API</a>
- <a href="https://developers.worldmate.com/" target="_blank">WorldMate Email Parsing API</a>
- <a href="http://sunrise-sunset.org/api" target="_blank">Sunset and Sunrise Times API</a>
- <a href="https://developer.transportapi.com" target="_blank">Transport data and development</a>
''', unsafe_allow_html=True)

st.write("")
st.subheader("The Horizon Team", divider=True)
linkedin_profiles("yamato-takahashi-a73b65231", "ben-scanlon-b13667227", "lukafilipxvic", "max-rupert-1812481b0")

st.write("#")
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