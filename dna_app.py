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

### 1. Print dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
        ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

### 2. Print Text
st.subheader('2. Print Text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' adenine (Guanine)')
st.write('There are ' + str(X['C']) + ' adenine (Cytosine)')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)