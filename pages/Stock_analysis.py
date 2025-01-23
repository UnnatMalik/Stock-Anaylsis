import mplfinance as mpl
import streamlit as st 
import pandas as pd
import yfinance as yf
import time 

st.set_page_config(
    page_title="Stock Analysis",
    page_icon="🔍",
)

st.title("Stock Anaylsis 🔍")

class Pages_switch():
    st.sidebar.page_link("home.py", label="Home 🏠")
    st.sidebar.page_link("pages/Stock_analysis.py", label="Stock Analysis 🔍")
    st.sidebar.page_link("pages/Live_track.py", label="Live Track 📈")

# The code block you provided is creating a container using `st.container(border=True)` in Streamlit.
# Within this container, the code is checking if the keys 'period' and 'interval' are present in the
# `st.session_state`. If they are not present, it initializes them with default values ('1d' and '1m'
# respectively).
with st.container(border=True):
    if 'period' not in st.session_state:
        st.session_state.period = '1d'

    if 'interval' not in st.session_state:
        st.session_state.interval = '1m'
    
    symbol = st.text_input("Enter a ticker symbol")
    st.markdown(
    """
        <div>
            📈. The ticker symbol input should be all Caps.<br> 
            📈. For Indian stalks after the symbol name add '.NS' example: " PNB.NS ".<br> 
        </div>
    """, unsafe_allow_html=True
    )
    st.markdown(
    """ 
        <div>
        <br>
        </div>

    """, unsafe_allow_html=True
    )
    st.session_state.period = st.select_slider(label="Period",options=['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
    st.session_state.interval = st.select_slider(label="Interval",options=['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'])
    chart_type = st.selectbox(label="Chart Type",options=['candle','ohlc', 'line','renko','pnf','hollow_and_filled'])
    def get_price(symbol):
        """
        The function `get_price` retrieves stock data, information, financials, and quarterly financials
        for a given stock symbol using the yfinance library, while displaying a progress bar.
        
        :param symbol: The `symbol` parameter in the `get_price` function is used to specify the stock
        symbol for which you want to retrieve data. This symbol is typically a unique identifier for a
        particular stock listed on a stock exchange, such as "AAPL" for Apple Inc. or "GOOGL"
        :return: The `get_price` function is returning four variables: `stock_data`, `stock_info`,
        `stock_financials`, and `Quarterly`.
        """
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
            
            Tab1 , Tab2, Tab3 = st.tabs(["Overview 🔍","Financials 💸","News and Events 📰"])

            # The `with Tab1:` block in the code you provided is creating a tab within the Streamlit
            # interface. Inside this tab, various components are being displayed to show an overview
            # of the stock symbol entered by the user.
            with Tab1:
                st.subheader(f"Overview of {symbol.strip(".NS")}")
                with st.expander(label="Summary",icon="📜"):
                    st.write(f"{info.get("longBusinessSummary")} ")
                st.slider(label="52W Range",min_value=info.get("fiftyTwoWeekLow"),max_value=info.get("fiftyTwoWeekHigh"),value=info.get("currentPrice"),disabled=True)

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

           # The `with Tab2:` block in the code you provided is creating a tab within the Streamlit
           # interface. Inside this tab, there are two sub-tabs created using
           # `st.tabs(["Yearly","Quarterly",])`.
            with Tab2:
                st.subheader(f"Financial Summary for {symbol}")
                Tab1 , Tab2 = st.tabs(["Yearly","Quarterly",])
                with Tab1:
                    st.subheader(f"Yearly Statistic for {symbol}")
                    
                    revenue24 = financials.loc['Operating Revenue'].get('2024-03-31')
                    profit_24 = financials.loc['Normalized Income'].get('2024-03-31')

                    revenue23 = financials.loc['Operating Revenue'].get('2023-03-31')
                    profit_23 = financials.loc['Normalized Income'].get('2023-03-31')

                    revenue22 = financials.loc['Operating Revenue'].get('2022-03-31')
                    profit_22 = financials.loc['Normalized Income'].get('2022-03-31')

                    # quarter24 = financials.loc['']

                    profit_data = {
                        'Year': ['Profit 2023', 'Profit 2024', 'Profit 2022'],
                        'revenue': [revenue23, revenue24, revenue22],
                        'Profit': [profit_23, profit_24, profit_22],
                    }
                    df = pd.DataFrame(data=profit_data)

                    st.bar_chart(df.set_index('Year'),stack=False,color=["#00FF00", "#0000FF"])
                
                with Tab2:
                    st.subheader(f"Quarterly Statistic for {symbol}")
                    
                    revenue24 = Quarterly.loc['Operating Revenue'].get('2024-09-30')
                    profit_24 = Quarterly.loc['Normalized Income'].get('2024-09-30')

                    revenue23 = Quarterly.loc['Operating Revenue'].get('2024-06-30')
                    profit_23 = Quarterly.loc['Normalized Income'].get('2024-06-30')

                    revenue22 = Quarterly.loc['Operating Revenue'].get('2023-09-30')
                    profit_22 = Quarterly.loc['Normalized Income'].get('2023-09-30')

                    # quarter24 = financials.loc['']

                    profit_data = {
                        'Month': ['Profit 2023', 'Profit 2024', 'Profit 2022'],
                        'revenue': [revenue23, revenue24, revenue22],
                        'Profit': [profit_23, profit_24, profit_22],
                    }
                    df = pd.DataFrame(data=profit_data)

                    st.bar_chart(df.set_index('Month'),stack=False,color=["#00FF00", "#0000FF"])

           # The above Python code is using the Streamlit library to display news and events related
           # to a given stock symbol. It fetches news data using the Yahoo Finance API, then iterates
           # through the news articles to display each article's title, publication date, source,
           # summary, and optionally an image if available. The code formats the news content using
           # HTML and CSS styles to create a visually appealing display for the user. If no news is
           # available for the given symbol, it shows an informational message.
            with Tab3:
                df = yf.Ticker(symbol)
                data = df.get_news(tab='all')

                st.subheader(f'News and Events about {symbol} 📰')
                theme_color = st.get_option("theme.primaryColor")
                if not data:
                    st.info(f"No news available for the {symbol}.")
                else:
                    with st.container():
                        for i in range(0, len(data)):
                            news = data[i]
                            content = news['content']
                            title = content["title"]
                            url = content.get('provider')['url']
                            pub_date = content['pubDate'].split("T")[0]
                            source = content.get('provider')['displayName']
                            summary = content['summary']
                            thumbnail = content.get('thumbnail', {})
                            image_url = ''
                            caption = ''

                            if thumbnail:
                                image_url = thumbnail.get('originalUrl', '')
                                caption = thumbnail.get('caption', '')

                            st.markdown(f"<h3 style='text-align: justify;color: {theme_color};'><a href='{url}' style='text-decoration: none;color: {theme_color};'>{title}</a></h3>", unsafe_allow_html=True)
                            st.markdown(f"<p style='text-align: justify;'><strong>Published:</strong> {pub_date}</p>", unsafe_allow_html=True)
                            st.markdown(f"<p style='text-align: justify;'><strong>Source:</strong> {source}</p>", unsafe_allow_html=True)
                            if image_url:
                                st.image(image_url, width=400, caption=caption)
                            st.markdown(f"<p style='text-align: justify;'>{summary}</p>", unsafe_allow_html=True)
                            st.markdown("<hr style='border:1px solid #e0e0e0;'>", unsafe_allow_html=True)
        

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
