import streamlit as st 


# The class `Pages_switch` contains sidebar page links for navigating to different pages such as Home,
# Stock Analysis, and Live Track.
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

class Pages_switch():
    st.sidebar.page_link("home.py", label="Home 🏠")
    st.sidebar.page_link("pages/Stock_analysis.py", label="Stock Analysis 🔍")
    st.sidebar.page_link("pages/Live_track.py", label="Live Track 📈")
    

st.title(" Welcome to the Stock Tracking and Anaylsis Protal 📈")

st.markdown(
    """
    <p style="text-align: left;">
    <br>
    This web application is designed to help you Study and Analyze a particular Stock based on it's summary, financials, Chart and News.
    </p>
    <br>
    """,
    unsafe_allow_html=True
)


titles = [
    "Stock analysis 🔍",
    "Live Chart and Tracking 📈",
    "News & Trends 📰",
]

descriptions = [
    "Helps in getting Stock information from various financials data rendered from Yfinance and visualization through Charts.",
    "Visualize the live stock tracking in market hours.",
    "Stay updated with the latest news and trends in the stock market.",
]

links = [
    "Stock_analysis",
    "Live_track",
    "Stock_analysis",
]

# Create a box for each feature
for title, description, link in zip(titles, descriptions, links):
    st.markdown(
        f"""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <a href="{link}" style="text-decoration: none; color: white;"><h4>{title}</h4></a>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
        <br><br><hr>
        <div style='text-align: center;'>
        Developed by Unnat Malik
        </div>
    """, unsafe_allow_html=True
    )
# Add a footer
st.markdown(
    """
    <div style="text-align: center;">
    <br>
        &copy; 2025 Stock Analysis. All rights reserved.
    </div>
    """, unsafe_allow_html=True
)            
