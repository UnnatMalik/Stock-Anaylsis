import streamlit as st 
import pandas as pd 
import numpy as np
import mplfinance as mpf
import os

st.title("My First App")

st.sidebar.header("Data Upload")

st.spinner("uploading")

uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=['csv'])

code_example = '''
    #include <stdio.h>

    int main(){
        printf("Hello World!");
        return 0;
    }
'''

st.code(code_example,language='c',line_numbers=True,wrap_lines=True)

st.image(os.path.join(os.getcwd(),"static","image.png"),)

st.subheader("Some Data")
df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Sue', 'Fred', 'Sally'],
    'Age': [23, 34, 29, 25, 23],
    'City': ['Mumbai', 'Delhi', 'Churchgate', 'Colaba', 'Borivali']
})
st.table(df)

st.subheader("Editable Data")
editable_df = st.data_editor(df)

st.subheader("Metrics")
st.metric("Total row",value=len(df))
st.metric("Total columns",value=len(df.columns))
st.metric(label="Mean age",value=df.get('Age').mode())