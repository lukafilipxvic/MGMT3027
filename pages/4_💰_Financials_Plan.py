import streamlit as st
import hide_st

st.set_page_config(
    layout="centered",
    page_title="Financials Plan",
    page_icon="💰",
    initial_sidebar_state="auto",
)

st.header("💰 Financials Plan", divider="grey")
st.subheader("Key Resources", divider=True)
st.markdown('''
The first priority is server space, obtainable through a **free 12-month trial** with Amazon Web Services (AWS) in Australia, estimated at a conservative \$0.2 per month for 100,000 active requests post-trial. This server space is crucial, offering over 2GB of requests per user. The risk is when AWS increases the cost per user as Horizon grows.\n
Another key activity will be **hiring AI engineer(s)** with a budgeted cost of around \$80,000 AUD. Additionally, we will invest \$24,000 in GPU and hardware acquisition, including four AI engineering-level PCs necessary for product development.\n
To effectively launch our pilot product, we have allocated a **\$30,000 marketing budget to target specific locations** in line with our growth plan. This includes collaboration with local government departments and business suppliers. Our budgeting is conservative, estimated at \$6 per user cost, through API scraping costs and payment charges that include GST.\n
''')
st.write("#")
st.subheader("Budget and Pricing", divider=True)
st.markdown('''
An **initial raising of \$200,000** in capital for the **first 12 months of operations** would meet the \$134,000 fixed budget cost and allow for upfront cashflow as we generate users. This is crucial for establishing competitiveness in the travel market, and understanding subscription models require a high amount of seed capital before they are cash flow positive.\n
To monetise our venture, we plan to offer a free model to attract younger segments, like students and adults. They will explore our AI assistant’s capabilities, increasing our active user base and conversions to paid users. For long-term subscriptions, users can pay \$7.99 AUD monthly or opt for six or 12-month advance payments at \$6.99 AUD. These pricing options enhance our cash flow and increase our expansion budgeting.\n
Additionally, we plan to offer a ‘per trip’ one-off payment option at \$25.99 AUD upfront, active for seven days, and extendable for \$4.99 AUD per week. This option is expected to be the most profitable, especially for older segments with a higher income. This option will be reviewed as we expand beyond pilot locations.\n
In terms of funding sources, we have identified multiple avenues, including \$80,000 AUD from angel investors, a \$80,000 matching grant from Visit Canberra Tourism, with potential grants from Visit NSW and Tourism Queensland for future pilots. We will offer a \$4.99 per month business advertisement subscription which will increase their priority within the AI itinerary. This is based off the ICN Gateway model that operates to attract suppliers.\n
''')
st.write("#")
st.subheader("First Year Financial Funding Allocation", divider=True)
st.markdown('''
First year is broken down into 2 stages. The initial seed capital. Angel Investors capital can be evenly matched by the ACT tourism fund, to develop the Horizon Product and test the pilot capabilities.

This is shown by the orange and blue in the figure below. The remaining revenue is earned through premium users and a fraction by promoted suppliers as seen by the grey, silver and yellow:
''')
st.image('images/year-one-rev.png')
st.markdown('''
We estimate revenue of **$231,000 AUD** after the first year.

This would meet the operational requirements for the second year of operations. It also guarantees ownership of AI engineering hardware and IP without needing to rely on outside patents.

This is important for future mergers and acquisitions, in line with our proposed exit strategy within this report.''')
hide_st.footer()