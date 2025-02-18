import streamlit as st

# st.title('Sessions')

# if 'counter' not in st.session_state:
#     st.session_state.counter = 0

# if st.button("Increment counter"):
#     st.session_state.counter += 1
#     st.write("Current counter value:", st.session_state.counter)

# if st.button("Reset counter"):
#     st.session_state.counter = 0
#     st.write("Counter reset to 0.")

# st.write(f"Session State: {st.session_state.counter}")

st.title('Callback')

if 'step' not in st.session_state:
    st.session_state.step = 1

if 'info' not in st.session_state:
    st.session_state.info = {}

def go_to_step(name):
    st.session_state.info['name'] = name
    st.session_state.step = 2

def go_to_back():
    st.session_state.step = 1

if st.session_state.step == 1: 

    st.header("Enter your name")

    name = st.text_input('Your Name:',value=st.session_state.info.get("name", ""))

    tab1 , tab2 ,tab3 = st.tabs(["Tab1","Tab2","Tab3"])

    with tab1:
        st.header("Tab 1")
        st.write("Tab1 content")
        Col1 , Col2 = st.columns(2)

        with Col1:
            st.subheader("Col 1")
            st.write("Col1 content")

        with Col2:
            st.subheader("Col 2")
            st.write("Col2 content")

    with tab2:
        st.header("Tab 2")
        st.write("Tab2 content") 
        Col1 , Col2 = st.columns(2)

        with Col1:
            st.subheader("Col 3")
            st.write("Col 3 content")

        with Col2:
            st.subheader("Col 4")
            st.write("Col 4 content")   

    with tab3:
        st.header("Tab 3")
        st.write("Tab3 content")    
        Col1 , Col2 = st.columns(2)

        with Col1:
            st.subheader("Col 5")
            st.write("Col 5 content")

        with Col2:
            st.subheader("Col 6")
            st.write("Col 6 content")
    st.button("Next",on_click=go_to_step,args=(name,))




if st.session_state.step == 2 :
    st.header("Review")


    st.subheader("Please review :")
    st.write(f"Name: {st.session_state.info.get('name')}")
    st.button("Back",on_click=go_to_back,)
    if st.button("submit"):
        st.success("Good")
        st.balloons()



