
import streamlit as st
from streamlit_folium import st_folium
from streamlit_js_eval import streamlit_js_eval

def intro():
    import streamlit as st

    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


def WEAInBetrieb():
    with open("WEAInBetrieb.html",'r') as f: 
        html_data = f.read()
    st.components.v1.html(html_data, scrolling=True, height = page_height, width = page_width)

def WEAInPlanung():
    with open("WEAinPlanung.html",'r') as f: 
        html_data = f.read()
    st.components.v1.html(html_data, scrolling=True, height = page_height, width = page_width)

def SolarFrei():
    with open("solarFreiflaeche.html",'r') as f: 
        html_data = f.read()
    st.components.v1.html(html_data, scrolling=True, height = page_height, width = page_width)

# def SolarDach():
#     with open("solarHausdach.html",'r') as f: 
#         html_data = f.read()
#     st.components.v1.html(html_data, scrolling=True, height = page_height, width = page_width)

# def SolarBalkon():
#     with open("solarBalkon.html",'r') as f: 
#         html_data = f.read()
#     st.components.v1.html(html_data, scrolling=True, height = page_height, width = page_width)

def Kraftwerke():
    with open("kraftwerke.html",'r') as f: 
        html_data = f.read()
    st.components.v1.html(html_data, scrolling=True, height = page_height, width = page_width)

def Speicher():
    with open("speicher.html",'r') as f: 
        html_data = f.read()
    st.components.v1.html(html_data, scrolling=True, height = page_height, width = page_width)


page_names_to_funcs = {
    "—": intro,
    "WEA in Betrieb": WEAInBetrieb,
    "WEA in Planung": WEAInPlanung,
    "Solar Freifläche": SolarFrei,
    # "Solar Hausdach": SolarDach,
    # "Solar Balkonkraftwerk": SolarBalkon,
    "andere Kraftwerke": Kraftwerke,
    "Speicher": Speicher
    }

st.set_page_config(page_title="Temporitär", layout="wide")
page_width = streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH',  want_output = True,)
page_height = streamlit_js_eval(js_expressions='window.innerWidth', key='HEIGHT',  want_output = True,)
if (page_height < 400):
    page_height = 600
# print(str(page_width) + " " +str(page_height))
demo_name = st.sidebar.selectbox("Choose a map", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()