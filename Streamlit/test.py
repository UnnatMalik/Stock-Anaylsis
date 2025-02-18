import mplfinance as mpl
import streamlit as st 
import pandas as pd
import yfinance as yf

st.set_page_config(
    page_title="Stock Analysis",
    page_icon="chart_with_upwards_trend",
    
)

st.title("Stock Anaylsis 📈")
with st.container(border=True):
    if 'period' not in st.session_state:
        st.session_state.period = '1d'

    if 'interval' not in st.session_state:
        st.session_state.interval = '1m'

    symbol = st.text_input("Enter a ticker symbol")
    st.session_state.period = st.select_slider(label="Period",options=['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
    st.session_state.interval = st.select_slider(label="Interval",options=['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'])
    chart_type = st.selectbox(label="Chart Type",options=
        ['candle','ohlc', 'line','renko','pnf','hollow_and_filled']
    )
    def get_price(symbol):
        data = yf.Ticker(symbol)
        stock_data = data.history(period=st.session_state.period,interval=st.session_state.interval)
        stock_info = data.info
        return stock_data, stock_info

    if st.button("Get Details"):
        df, info = get_price(symbol)
        if df.empty:
            st.error("No data available for the selected period and interval.",icon=":material/error:")
        else:
            df.index = pd.to_datetime(df.index)
            st.subheader(f"Company Info for {symbol}")
            st.write(f'''
                Country :     {info.get("country")}\n
                Industry :    {info.get("industry")}\n
                Sector :      {info.get("sector")}\n
                Currency :    {info.get("financialCurrency")}\n
                Recommendation : {info.get("recommendationKey")}\n
                Type : {info.get("quoteType")}\n
        ''')
            st.markdown("### Summary : ")
            st.write(f"{info.get("longBusinessSummary")} ")
            col1 , col2 = st.columns(2)
            with col1:
                st.subheader(f"Histroy Price for {symbol}")
                st.write(df)
            with col2:
                st.subheader(f"Line Chart for {symbol}")
                fig, ax = mpl.plot(data=df,type=chart_type,volume=True,style='yahoo',returnfig=True, figsize=(15,10),)
                st.pyplot(fig,clear_figure=True,use_container_width=True)

st.markdown("""
        <br><br><hr>
        <div style='text-align: center;'>
            Developed by Unnat Malik
        </div>
    """, unsafe_allow_html=True)
# Add a footer
st.markdown(
    """
    <div style="text-align: center;">
    <br>
        &copy; 2025 Stock Analysis. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)            
