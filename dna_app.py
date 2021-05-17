####################
# Import libraries #
####################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import image

####################
# Page Title       #
####################

image = Image.open('dna_logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

""")

