import streamlit as st
import streamlit.components.v1 as components

# Page ko wide mode me set karna (optional)
st.set_page_config(layout="wide")

# Apni HTML file ka naam yahan likhein
html_file_path = "accessToken.html" 

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_data = f.read()
    
    # HTML content ko Streamlit par show karna
    # Height aap apne hisaab se adjust kar sakte hain
    components.html(html_data, height=800, scrolling=True)

except FileNotFoundError:
    st.error(f"File {html_file_path} nahi mili. Kripya check karein.")
