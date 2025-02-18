import streamlit as st 
import yfinance as yf
import numpy as np
import pandas as pd
import mplfinance as mpf
from datetime import datetime

# ticker = yf.Ticker("PNB.NS")

# data = ticker.history(period='1d',interval='1h')
# pd.DataFrame(data).to_csv('trail.csv')

# high = pd.DataFrame(data['Open'])
# # low = pd.DataFrame(data['Close'])

# st.text("Hello world!")

# st.title("My First App")

# # x = mpf.plot(data,type='candle',style='charles',volume=True)

# fig, ax = mpf.plot(
#     data,
#     type='candle',
#     volume=True,
#     figsize=(15,10),
#     style='yahoo',
#     returnfig=True
# )

# # plot = [high,low]
# x=pd.DataFrame(high)

# st.pyplot(fig,clear_figure=True,use_container_width=True)
# # st.line_chart(low)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [19.0760, 72.8777],
#     columns=['lat', 'lon']
#     )
# st.map(map_data)



# st.text_input("Your name",key="name")

# st.session_state.name

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# st.sidebar.title(
#     "test1"
# )

# st.sidebar.write(
#     "This sidebar is fixed."
# )

# right_column, left_column = st.columns(2)

# with st.sidebar:
#     st.write("This sidebar is also fixed.")
#     st.text_input("Text input")
#     st.button("Press me")
#     st.checkbox("Check me out")
#     st.selectbox("Select", ["A", "B", "C"])
#     st.slider("Slide me", 0, 100)

# with right_column:
#     st.write("This column will be on the right.")
#     st.write("It's not fixed, so it will scroll with the page.")

# with left_column:
#     st.write("This column will be on the left.")
#     st.write("It's not fixed, so it will scroll with the page.")

st.set_page_config(
    page_title="Sign Up",
    page_icon="envelope_with_arrow",
    
)

st.title("User Sign-up")

Min_date = datetime(1960,1,1)
Max_date = datetime.now()

form = {
    "name": None,
    "height": None,
    "age": None,
    "gender": None,
    "birth_date": None
}


with st.form(key="Sing-up" , clear_on_submit=True):

    form["name"] = st.text_input("Enter your username")
    form["height"] = st.number_input("enter your height ")
    form["age"] = st.slider("Age")
    form["gender"]=st.selectbox("Gender",["Male","Female"],placeholder="Select your gender")
    form["birth_date"]=st.date_input("Enter your birth date",max_value=Max_date,min_value=Min_date)
    
    button = st.form_submit_button(icon=":material/login:")
    
    if button:
        if not all(form.values()):
            st.warning("Please fill in all of the fields",icon=":material/warning:")
        else:
            st.balloons()
            st.write("### info")
            for i in form.items():
                st.write(f"{i[0]}: {i[1]}")
