import mplfinance as mpl
import streamlit as st 
import pandas as pd
import yfinance as yf
import time 

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
    chart_type = st.selectbox(label="Chart Type",options=['candle','ohlc', 'line','renko','pnf','hollow_and_filled'])
    def get_price(symbol):
        progress_bar = st.progress(0)
        progress_bar.progress(10)

        data = yf.Ticker(symbol)
        stock_data = data.history(period=st.session_state.period,interval=st.session_state.interval)
        stock_info = data.info
        stock_financials = data.financials
        Quarterly = data.quarterly_financials

        progress_bar.progress(100)
        time.sleep(2)
        progress_bar.empty()
        return stock_data, stock_info, stock_financials, Quarterly

    if st.button("Get Details"):
        df, info, financials, Quarterly = get_price(symbol)
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
            
            Tab1 , Tab2 = st.tabs(["Overview 🔍","Financials 💸",])

            with Tab1:
                st.subheader(f"Overview of {symbol.strip(".NS")}")
                with st.expander(label="Summary",icon="📜"):
                    st.write(f"{info.get("longBusinessSummary")} ")
                st.slider(label="Day's Range",min_value=info.get("dayLow"),max_value=info.get("dayHigh"),value=info.get("currentPrice"),disabled=True)
                st.write(f"Volume: {info.get("volume")}")
                st.write(f"Dividend Rate: {info.get('dividendRate')}")
                st.write(f"Dividend Yield : {info.get('dividendYield')}")
                st.write(f"Day High : :green[{info.get('dayHigh')}⬆]")
                st.write(f"Day Low : :red[{info.get('dayLow')}⬇]")
                price = info.get("currentPrice")
                eps = info.get("trailingEps")
                Pe = round(price / eps, 2)
                st.write(f"PE : {Pe}")
                st.markdown("### Chart ")
                fig, ax = mpl.plot(data=df,type=chart_type,volume=True,style='binance',returnfig=True, figsize=(15,10),)
                st.pyplot(fig,clear_figure=True,use_container_width=True)

            with Tab2:
                st.subheader(f"Chart for {symbol}")

                revenue24 = financials.loc['Operating Revenue'].get('2024-03-31')
                Tax_Provision_24 = financials.loc['Tax Provision'].get('2024-03-31')
                pre_tax_income_24 =  financials.loc['Pretax Income'].get('2024-03-31')
                profit_24 = round(pre_tax_income_24 - Tax_Provision_24, 5)

                revenue23 = financials.loc['Operating Revenue'].get('2023-03-31')
                Tax_Provision_23 = financials.loc['Tax Provision'].get('2023-03-31')
                pre_tax_income_23 =  financials.loc['Pretax Income'].get('2023-03-31')
                profit_23 = round(pre_tax_income_23 - Tax_Provision_23, 5)

                revenue22 = financials.loc['Operating Revenue'].get('2022-03-31')
                Tax_Provision_22 = financials.loc['Tax Provision'].get('2022-03-31')
                pre_tax_income_22 =  financials.loc['Pretax Income'].get('2022-03-31')
                profit_22 = round(pre_tax_income_22 - Tax_Provision_22, 5)


                profit_data = {
                    'Year': ['Profit 2023', 'Profit 2024', 'Profit 2022'],
                    'Profit': [profit_23, profit_24, profit_22],
                    'revenue': [revenue23, revenue24, revenue22]
                }
                df = pd.DataFrame(data=profit_data)

                st.bar_chart(df.set_index('Year'),stack=False,color=["#00FF00", "#0000FF"])
                st.table(Quarterly)

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
