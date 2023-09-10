import streamlit as st
import hide_st

st.set_page_config(
    layout="centered",
    page_title="References",
    page_icon="📑",
    initial_sidebar_state="auto",
)

st.header("📑 References", divider="grey")
st.markdown('''
Amazon Web Servers, 2023. Subscription Cost Calculator. [Online] Available at: https://calculator.aws/#/addService/Lambda\n
Capgemini Research Institute, 2023. WHY CONSUMERS LOVE GENERATIVE AI. [Online] Available at: https://prod.ucwe.capgemini.com/wp-content/uploads/2023/06/Final-Infographic-Creative-Gen-AI.pdf\n
Huang, M.H. and Rust, R.T., 2021. A strategic framework for artificial intelligence in marketing. Journal of the Academy of Marketing Science, 49, pp.30-50. Available at: https://link.springer.com/article/10.1007/s11747-020-00749-9\n
ICN.Gateway, 2023. Subscription Pricing. [Online] Available at: https://gateway.icn.org.au/subscription/campaign/boost\n
Market.us, 2023. Travel Planner App market., [Online] Available at: https://market.us/report/travel-planner-app-market/\n
MarketResearch, 2023. Generative AI In Travel Market. [Online] Available at: https://marketresearch.biz/report/generative-ai-in-travel-market/\n
''')

hide_st.footer()