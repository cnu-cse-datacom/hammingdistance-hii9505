 import random
  2 import numpy as np
  3 import pandas as pd
  4 from hamming_practice import hamming
  5 
  6 df = pd.read_csv('sample.csv', names=['word', 'bin'])
  7 
  8 count = 1
  9 min = 10
 10 
 11 for i in range(len(df)):
 12         for j in range(i+1, len(df)):
 13                 hd =hamming(df.iloc[i,1], df.iloc[j,1])
 14                 print(count, "(", df.iloc[i,0], df.iloc[j,0], ")")
 15                 count = count + 1
 16                 if(min > hd):
 17                         min = hd
 18 
 19 
 20 
 21 
 22 
 23 
 24 print("min hamming distance", min)
 25 
