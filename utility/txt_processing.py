
# Script for performing pre-processing of text corpus

import re
import os

from nltk.tokenize import word_tokenize

def clean_text(text):
    # Remove non-textual elements
    #text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\n', ' ', text)   # Replace \n character
    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespaces with single space
   # text= re.sub(r'[^\w\s",.!]', ' ', text)
    text = text.strip()  # Removing trailing or extra spaces
    return text.lower() # Normalising the text by converting it to lower case

def count_stopwords(tokens): # Also remove those elements whose length is equal to 1
    # Define a custom list of redundant stopwords
    custom_stopwords = set([
        "a", "an", "the", "this", "that", "these", "those", "it", "its",
        "is", "are", "was", "were", "am", "be", "being", "been", "have",
        "has", "had", "do", "does", "did", "will", "would", "should",
        "can", "could", "may", "might", "must", "shall", "to", "in", "on",
        "at", "by", "with", "for", "of", "about", "as", "but", "if", "so",
        "not", "or", "and", "yet", "from", "up", "down", "out", "over",
        "under", "into", "onto", "off", "away", "just", "only", "really",
        "very", "too", "much", "many", "more", "most", "least", "even",
        "still", "also", "almost", "nearly", "though",
        "although", "however", "unless", "until", "while", "where", "when",
        "why", "what", "which", "who", "whom", "whose", "how","fig.","fig .","fig . .","fig"
    ])

    # Filter out tokens that are not in the custom list of stopwords
    stopword_count = sum(1 for token in tokens if token in custom_stopwords)

    # Calculate the percentage of stopwords
    total_tokens = len(tokens)
    stopword_percentage = (stopword_count / total_tokens) * 100 if total_tokens > 0 else 0

    return stopword_percentage

def count_numbers_in_text(text):
    # Count the number of characters that are numbers
    number_count = sum(1 for char in text if char.isdigit())
    text_len = len(text)
    num_percentage = (number_count / text_len) * 100 if text_len > 0 else 0
    return num_percentage

def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

def clean_elem(tokens): # Also remove those elements whose length is equal to 1
    # Define a custom list of redundant stopwords
   
    #filtered_tokens = [token for token in tokens if token not in custom_stopwords]
    filtered_tokens=[token for token in tokens if len(token)>1]
    return filtered_tokens


def rm_q_exam(df,source):
    """
    Removing the exercise questions from the text corpus using regex
    
    """
    try:
            temp=df.loc[df["source"]==source]#'/katempggle/input/ncert-textbook/CBSE_TextBook_pdf/9_Maths/iemh101.pdf'] 
            temp["prev_text"]=temp["text"]

            if "Math" in source:
                pattern1="\nEXERCISE"
                pattern2 = r"\n\d+\.\d+ [A-Z][a-z]+"
                index=temp.loc[temp["text"].str.contains(pattern1)].index 

        # Find the index of rows in 'temp' where the 'text' column contains the pattern
                index2 = temp.loc[temp["text"].str.contains(pattern2)].index

                for i in range(0,len(index)):
                #    print("index",index[i])
                    text=temp.loc[temp["text"].str.contains(pattern1)]["text"][index[i]]
                    temp["text"][index[i]]=text.split(pattern1)[0]
                    sel_ind=[ x for x in index2 if x>index[i] and x<index[i+1]] if i<(len(index)-1) else [ x for x in index2 if x>index[i]]
                 #   print("index",sel_ind)
                    for j in sel_ind:
                        temp["text"][j]=re.split( pattern2,temp["text"][j])[1]

            else:
                pattern1="\nEXERCISES"
                index=temp.loc[temp["text"].str.contains(pattern1)].index 
                #print("index1:",index)
                if len(index)<1:
                    pattern1="EXERCISES"
                    index=temp.loc[temp["text"].str.contains(pattern1)].index 
                 #   print("index2:",index)
                temp=temp.loc[temp.index<index[0]]



            return temp
    except:
            print("Nothing to process")
            return temp
        

            

    
    