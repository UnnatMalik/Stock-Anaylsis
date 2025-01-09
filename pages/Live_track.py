import mplfinance as mpf
import streamlit as st 
import yfinance as yf
import time 
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Live Track",
    page_icon="chart_with_upwards_trend",
)

class Pages_switch():
    st.sidebar.page_link("home.py", label="Home 🏠")
    st.sidebar.page_link("pages/Stock_analysis.py", label="Stock Analysis 🔍")
    st.sidebar.page_link("pages/Live_track.py", label="Live Track 📈")
st.title('Live Stock Price Tracker and Indices Monitor 📈')

# Input field for the stock ticker symbol

tab1, tab2 = st.tabs(tabs=['Essential Stock and Indices 💹', 'Live Chart 📈'])

with tab1:
    def get_stock_metrics(ticker):
        ticker_data = yf.Ticker(ticker)
        history = ticker_data.history(period='1y')
        
        if len(history) < 2:
            return None, None  # Return None if there's not enough data
        
        current_price = history['Close'].iloc[-1]
        prev_close = history['Close'].iloc[-2]
        fluctuation = ((current_price - prev_close) / prev_close) * 100
        return current_price, fluctuation

    random_stocks = ['TATASTEEL.NS', 'MRF.NS', 'TCS.NS','JIOFIN.NS','INFY.NS','NESTLEIND.NS'] 

    # Display metrics for random stocks
    st.subheader('Current Price and Fluctuation for TOP Stocks')
    num_columns = 3
    for i in range(0, len(random_stocks), num_columns):
        stocks_in_row = random_stocks[i:i+num_columns]  # Get the next 3 stocks for the row
        columns = st.columns(len(stocks_in_row)) 
        for col, stock in zip(columns, stocks_in_row,):
            price, fluctuation = get_stock_metrics(stock)
            if price is not None and fluctuation is not None:
                    col.metric(label=f"{stock.strip('.NS')}", value=f"₹{price:.2f}", delta=f"{fluctuation:.2f}%",border=True)
            else:
                col.write(f"Not enough data for {stock}.")
    st.divider()

    st.subheader("Current Price and Fluctuation for Key Indices")

    indices = {
        'Bank Nifty': '^NSEBANK',
        'Nifty 50': '^NSEI',
        'Nifty IT': '^CNXIT',
        'Nifty FMCG': '^CNXFMCG',
        'Nifty Energy': '^CNXENERGY',
        'Nifty Auto': '^CNXAUTO',
        'Nifty Metal': '^CNXMETAL',
        "NIFTY 500": "^CRSLDX"
    }

    num_indices = len(indices)
    rows = (num_indices // 3) + (1 if num_indices % 3 > 0 else 0)

    for i in range(rows):
        start_idx = i * 3
        end_idx = min(start_idx + 3, num_indices)
        selected_indices = list(indices.items())[start_idx:end_idx]
        
        # Create columns for this row
        columns = st.columns(3)  # Always 3 columns per row
        for col, (index_name, ticker) in zip(columns, selected_indices):
            price, fluctuation = get_stock_metrics(ticker)
            if price is not None and fluctuation is not None:
                col.metric(label=f"{index_name}", value=f"₹{price:.2f}", delta=f"{fluctuation:.2f}%",border=True)
            else:
                col.write(f"Not enough data for {index_name}.")
    st.divider()
with tab2:
    st.subheader('Live Stock Price Tracker 📈')

    ticker_symbol = st.text_input('Enter the stock ticker symbol:',)

    chart_type = st.selectbox(label="Chart Type",options=['candle','ohlc', 'line','pnf','hollow_and_filled'])

    start_button = st.button('Get Live chart')
    # Function to fetch the live data
    def get_live_data(ticker):
        ticker_data = yf.Ticker(ticker)
        data = ticker_data.history(period='1d', interval='1m')
        return data

    if start_button:
        st.subheader(f'Chart for {ticker_symbol.strip('.NS')}')
        chart_placeholder = st.empty()
        while True:
            data = get_live_data(ticker_symbol)
            fig, (ax, ax_volume) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})
            mpf.plot(data, type=chart_type, ax=ax, volume=ax_volume, style='yahoo')
            chart_placeholder.pyplot(fig)
            time.sleep(60)  

            


