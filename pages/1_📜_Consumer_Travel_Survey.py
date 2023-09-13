import streamlit as st
import hide_st
import streamlit.components.v1 as components


st.set_page_config(
    layout="centered",
    page_title="Consumer Travel Survey",
    page_icon="📜",
    initial_sidebar_state="auto",
)

st.header("📜 Consumer Travel Survey", divider="grey")
st.subheader("We started with finding the :red[problem], not the :blue[solution.]")
st.markdown('''
The team first surveyed travel consumers to find a problem worth solving.\n
Findings of the survey **shows demand** for simpler budgeting tools and a more personalised itinerary planner.
Hence, we persuit solving the problem.
''')

# embed streamlit docs in a streamlit app
components.iframe("https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=r7DZdv9X6Gm7YhW2cFiQ0CEJQ3xjVsro&id=XHJ941yrJEaa5fBTPkhkN5wgu1_g9GhKvAJIeN8y6h5UMUhLNEM2Uk5UMDNMMUxFSzkzUUNRRVlJUi4u", height=5270)

hide_st.footer()