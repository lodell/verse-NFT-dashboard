# Using streamlit to create UI for dashboard
import streamlit as st
import requests, json

# With streamlits functions we can build a full web interface to display our data

# Add header
#st.header("Verse Intel NFT Tools")

# Add text to page
#st.write("Big_Cheek")

# Add text to sidebar
#st.sidebar.write("Sidebar_Cheek")

# To create a select box with a drop down menu we use streamlits 'selectbox' function
# We can add items to the box in list format
#st.selectbox("Events", ['Assets', 'Events', 'Rarity'])

# Add select box to sidebar
#st.sidebar.selectbox("Events", ['Assets', 'Events', 'Rarity'])

# To change to main page display from the select box we can save the selectbox call to a variable
# Then use an fstring in the header or write functions to call different variables

# Assign sidebar select box to a variable
endpoint = st.sidebar.selectbox("Events", ['Assets', 'Events', 'Rarity'])

# Add fstring to header to change the header based on endpoint selected
st.header(f"Verse Intel NFT Tools - {endpoint}")

# Add API request code
# Since we have endpoints defined above we can add incorporate into conditional statements
# Instead of printing to terminal or local file we can write to our dashboard with streamlit

if endpoint == 'Assets':

    params = {
        'collection': 'the-wanderers',
        'limit': 1
    }

    API = requests.get("https://api.opensea.io/api/v1/assets", params=params)

    st.write(API.json())
