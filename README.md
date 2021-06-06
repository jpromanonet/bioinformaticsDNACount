# bioinformaticsDNACount

A simple bioinformatics DNA counter web application

## DNA Sequence Sample

 ```
GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC
TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT
 ```
 ---

## Development Journal

1. Install streamlit using:

   ```
   pip3 install streamlit
   ```

2. If when trying to use the "streamlit hello" command you get an error, try this

   ```
   pip3 install protobuf --upgrade
   ```

   Then run "streamlit hello" again and it should work just fine.

3. Now we should install pandas and yfinance, which we are going to use in the python file.

   ```
   pip3 install pandas
   pip3 install yfinance
   ```

## How to run the bioinformatics DNA count

```
streamlit run dna_app.py
```

It will open a browser tab at:

```
http://localhost:8502
```

Remember! you can change the DNA Sequence to everyone you want to study.