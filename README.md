# SchoolAIKit-Text-Knowledge-graphs-and-search-chat
# Motivation behind the project:

The motivation behind the project is to create a knowledge graph from the text corpus of Physics, Maths and Chemistry curriculum from 8 to 12 in CBSE. The idea is to create a knowledge repostiory by exploring the relationshp between the entities that are addressed under different disciplines. This tool will be helpful in encouraging students to appreciate cross-learning. This reminds me of a gripe from a mathematician who passionately talks about how we are failing to convey the beauty of studying feometry, ellipse etc. More from this article.  This is to enable students to with a GPT or chatbot that operates within certain boundaries and KG  will be helful in guiding the chatbot.

Take a node on thermodynamics and expand further:


From the knowledge graph h it can be deciphered below that the conic sections (bring relationship through connections). How tiying with these ideas led to bigger questions related to planetary motions etc.


The generations of hand me down knowlegde between the scientists are explored in this graph


The notebook text pre -processing simply deals with the broad text corpus processing steps andembedding short phrases extracted across the books. Steps taken are as follow.

"graph_gen_nb.ipnb"

Basically would like to connect ideas from different levels of classes and give comprehensive picture of the project.
These are the following steos that are followed:
1. Using Langchain to parse text from the books stored in the pdf format -Recursively split the text according to character length and define overlapping margins
2. Cleaning the text corpus. Detecting the presence of keywords through Regex to remove "questions" and "activity" related content
3. Scan the text for stopwords and remove the lines which have only variable names or figure names which would add noise to the system through word tokens .
4. Remove special characters strip unnecessary spaces
5. Engineer the prompts for the LLM Zephyr to extract the entities and relationship from the corpus
6. Instantiate a graph object and construct a graph
7. Construct and display a graph using Pyvis and seaborn.

Next steps:

1. Improve the enitity recognition and reduce terns like closed curve,positive origin etc.
2. Connect the knowledge graph with external Wikipedia KG
3. Create a chatbot 

The open source community has been helpful have been able to rely on github repositories and open licences as given below (rahulnayak, MIT license)


Installation guides:
1. Ollama set up 
2. 


Please note that 
1. Text reading
2. Cleaning -removal of stopwords, le
3. Scan the text for stopwords and remove the lines which have only variable names or figure names which would add noise to the system through word tokens .
4. Remove special characters strip unnecessary spaces
5. Glive Embedding

# Tech Framework

Ollama: Installed from https://ollama.ai

Zephyr: Zephyr beta is a fine-tuned  version of mistral model that was trained on on a mix of publicly available, synthetic datasets.
source: https://ollama.com/library/zephyr (Source:HuggingFaceH4/zephyr-7b-beta)

PyVis a python library for plotting the knowledge graph 

Networkx python library for handling graphs





# Feature Engineering in NLP

## Tokenisation
Divide the sentence into smaller language units such as words (tokens), subwords, characters

It can exist at different levels -  into characters or subword tokens or phrase tokens

## Preprocessing

Remove the punctuation and retain only the root words
1. Lowercasing
2. Stemming - keep words in the root form
3. Stopword removal
4. Normalization -  transform a word to standard form ( correcting spelling mistakes)


## Text Representation

The computer understands text in addition to reading - vectors

How to turn text into numbers to retain meaning?
 e.g. ASCII or Morse code vectors generated could be huge and don't include a relationship between words

- One hot encoding - doesn't include the relationship between words and gives a sparse representation (high dimensional)
- Bag-of -words -collect the words to form a vocabulary or dictionary. It captures some semantic similarities of texts. It is high dimensional and provides sparse representation
- The two major problems with OHE and BAg of words are associated with sparse representation matrix and lack of relationship between the words
- Word Embedding-  describing a word based on quantitative measurements
  for instance the word "Mirror" - can be described by the word properties nature, origin, sense of belonging, excitement, trust.
The technique used to encode text into meaningful vectors - low dimensional and dense vectors.
Vectors convey the semantic similarity between the words.

##  Elaborating on Word2Vec

Word2vec is a family of model architectures and optimization can be used to learn word embeddings from large datasets.

Continuous bag of words - given the context fill the sentence.
A dog is ----- a person
The window shifting is performed to learn from

The goal is to learn the embedding matrix 

# Model training in NLP using DNN

The activation function is used to prevent linearity. Without the activation function, the output will be a linear combination of inputs and bias from the previous layer.

Used in layers in between ReLU, Sigmoid (link), tanh 

The output of Softmax is probability.

If the difference between the actual and predicted is high that means the 

## Cost Functions

MSE, cross-entropy (calculate the difference between probability distribution)

Gradient descent - decide the direction based on the sign of the derivative. The step size determines how long steps are taken to traverse.

# Knowledge Graph 

#Prompting through Ollama and language models
Running LLMs locally.

Write about prompt engineering and the syntax for posting the web-request 

#Guiding how to use the code notebook

# References

1.  https://github.com/AITwinMinds/Ollama-in-Google-Colab
2. https://github.com/rahulnyk/knowledge_graph.git

