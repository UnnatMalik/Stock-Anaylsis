import streamlit as st 


st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

class Pages_switch():
    st.sidebar.page_link("home.py", label="Home 🏠")
    st.sidebar.page_link("pages/Stock_analysis.py", label="Stock Analysis 🔍")
    st.sidebar.page_link("pages/Live_track.py", label="Live Track 📈")
    

st.title(" Welcome to the Stock Tracking and Anaylsis Protal 📈")


st.divider()

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

# Create a box for each feature
for title, description in zip(titles, descriptions):
    st.markdown(
        f"""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
        <br><br><hr>
        <div style='text-align: center;'>
            Developed by Unnat Malik, Seher Sarik, Teerth lalwani, Ojas Singwi
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
