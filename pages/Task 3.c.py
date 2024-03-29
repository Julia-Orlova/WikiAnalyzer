import streamlit as st
from st_tasks import task3c

st.set_page_config(page_title="Task3c")

st.markdown("# Task3.c. Retrieve a statistic of a particular user which include "
            "type of contribution (typos editing | content addition).")

if st.button('Rerun script'):
    st.experimental_rerun()

user = st.text_input('Enter a username:')
nums = int(st.number_input('Enter the number of days:', min_value=1, max_value=1000))

if st.button('Retrieve a statistic'):
    task3c(user, nums)
