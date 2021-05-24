####################
# Import libraries #
####################

from altair.vegalite.v4.api import sequence
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

####################
# Page Title       #
####################

image = Image.open('dna_logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

####################
# Input textbox    #
####################

# st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = 'DNA >\n'

# sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
# Skips the secuence name(first line)
sequence = sequence[1:]
# Concatenate list to string
sequence = ''.join(sequence)

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA QUERY)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')
