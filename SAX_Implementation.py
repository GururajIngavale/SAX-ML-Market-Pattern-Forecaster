import pandas as pd 
import numpy as np 
from scipy.stats import norm
from sklearn.cluster import KMeans
from collections import Counter

# Reading the File 
file = "nifty_fifty_OHLCV.csv"
read_file = pd.read_csv(file)

# Calculating Mid Prices  
# read_file['mid_price'] = ( read_file["High"] + read_file["Low"] ) / 2
# read_file.to_csv("nifty_fifty_OHLCV.csv" , index = False)
# print("done")

close_data = np.array(read_file["Close"])
mid_price_data = np.array(read_file["mid_price"])

# Create Windows

window_size = 30
sliding_window = 5
paa_segment = 10
paa_list = []

for i in range (0, len(close_data) - window_size + 1 , sliding_window) : 
    window = close_data[ i : i + window_size ]
    # print(window)

# Z - Normalization
    mean = np.mean(window)
    std_deviation = np.std(window)

    if std_deviation == 0 :
        window = np.zeros(len (window))
    normalization = (window - mean ) / std_deviation
    # print(normalization)

# PAA ( Piecewise Aggregate Approximation )

    segment_size = len(normalization) // paa_segment
    paa = []

    for i in range(0, len(normalization), segment_size):
        segment = normalization[i : i + segment_size]
        paa_mean = np.mean(segment)
        paa.append(paa_mean)

    paa_list.append(paa)   # <- THE ONLY CORRECT WAY
# print(paa_list)
    
# BreakPoint Generations 

alphabet_size = 5 

def generate_breakpoints(alphabet_size):
    return [norm.ppf(i / alphabet_size) for i in range(1, alphabet_size)]


breakpoints = generate_breakpoints(alphabet_size)
# print(breakpoints)

# SAX Defination 

alphabet = ["a","b","c","d","e"]
breakpoint = [-0.8416212335729142, -0.2533471031357997, 0.2533471031357997, 0.8416212335729143]
sax_words = []
count = 0
for paa_window in paa_list : 
    
    sax_word = ""

    for val in paa_window : 

        if val < breakpoint[0] : 
            sax_word += "a"
        
        elif val < breakpoint[1] : 
            sax_word += "b"
        
        elif val < breakpoint[2] : 
            sax_word += "c"
        
        elif val < breakpoint[3] : 
            sax_word += "d"

        else :  
            sax_word += "e"
    
    # print(sax_word)
    sax_words.append(sax_word)
# print(sax_words)

# Find Identical Patterns 

# 1. Recurring Complete SAX Patterns -----------
 
counts = Counter(sax_words)

for word , count in counts.items() :
    if count > 1 : 
        print(word ,"=", count)

# 2. SAX pattern of specific length  ----------- 

n = 3
n_gram = [] 


for word in sax_words : 
    for i in range (len(word) - n + 1) : 
        n_gram.append(word[i : i + n])

n_counts = Counter(n_gram)

for w , c in n_counts.items() : 
    if c > 3 : 
        print (w , "=" , c)

# 3. Clustering SAX Words -----------

a = 0 
b = 1
c = 2
d = 3
e = 4

alphabet_to_int = {"a" : 0 , "b" : 1 , "c" : 2 , "d" : 3 , "e" : 4}

alphabet_to_int = {'a':0,'b':1,'c':2,'d':3,'e':4}

def word_to_vector(word):
    return [alphabet_to_int[c] for c in word]
vectors = [word_to_vector(w) for w in sax_words]
kmeans = KMeans(n_clusters=5 , n_init="auto" )
labels = kmeans.fit_predict(vectors)
clusters = {}
for word, label in zip(sax_words, labels):
    clusters.setdefault(label, []).append(word)

print(clusters)