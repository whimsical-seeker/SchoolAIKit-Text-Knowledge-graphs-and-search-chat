# SchoolAIKit-Text-Knowledge-graphs-and-search-chat

# Motivation

The SchoolAIKit project is all about creating a smart tool that connects the dots between what you learn in Physics, Maths, and Chemistry from grades 8 to 12 in CBSE. It's like building a big map of knowledge by looking at how things in different subjects relate to each other. This way, students can learn from one subject and apply it to another, making it easier to understand everything.

Paul Lockhart once said in his book "A Mathematician's Lament" that just memorizing rules in math takes away the fun of exploring and being creative. It's like trying to see the whole picture through a tiny window.He likens this to teaching music by focusing solely on notation and theory, without ever letting students actually listen to or play music.

Back in ancient times, a guy named Apollonius figured out cool stuff about shapes like circles, ellipses, parabolas, and hyperbolas. Later on, smart folks like Galileo and Kepler used his ideas to understand how things move through space.

So, the idea behind this project is to make learning more exciting and connected. It's not just about memorizing facts, but about seeing how everything fits together like puzzle pieces. This way, you can explore and discover new things on your own, which is what makes learning really cool!

![image](https://github.com/whimsical-seeker/SchoolAIKit-Text-Knowledge-graphs-and-search-chat/assets/55318342/5f290b11-5178-451d-90d7-82514794de0a)

Source: Graph visualised on Neo4j browser by the author

![image](https://github.com/whimsical-seeker/SchoolAIKit-Text-Knowledge-graphs-and-search-chat/assets/55318342/6a025809-8eb7-44f3-a804-352e04019327)

Source: Graph visualised using Pvis and connection weights

# Methodology

Basically would like to connect ideas from different levels of classes and give comprehensive picture of the project.
These are the following steps that are followed:
1. Using Langchain to parse text from the books stored in the pdf format -Recursively split the text according to character length and define overlapping margins.
2. Cleaning the text corpus. Detecting the presence of keywords through Regex to remove "questions" and "activity" related content.
3. Scan the text for stopwords and remove the lines which have only variable names or figure names which would add noise to the system through word tokens .
4. Remove special characters strip unnecessary spaces
5. Engineer the system prompt for the LLM Zephyr to extract the entities and relationship from the corpus.
6. Instantiate a graph object and construct a graph.
7. Construct and display a graph using Neo4j,Pyvis and seaborn.


# Tech Framework

1. Ollama: Installed from https://ollama.ai

2. Zephyr: Zephyr beta is a fine-tuned  version of mistral model that was trained on on a mix of publicly available, synthetic datasets.
source: https://ollama.com/library/zephyr (Source:HuggingFaceH4/zephyr-7b-beta)

3. Neo4j desktop for non relational DBMS and cypher queries (https://neo4j.com/docs/desktop-manual/current/)

4. PyVis a python library for plotting the knowledge graph 

5. Networkx python library for handling graphs


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

Knowledge graphs (KGs) organise data from multiple sources, capture information about entities of interest in a given domain or task (like people, places or 
events), and forge connections between them. 

The term ‘knowledge graph’ has been introduced by Google in 2012 to refer to its general-purpose knowledge base, though similar approaches have been around since the beginning of modern AI in areas such as knowledge representation, knowledge acquisition, natural language processing, ontology engineering and the semantic web. Today, KGs are used extensively in anything from search engines and chatbots to product recommenders and autonomous systems.

source: https://www.turing.ac.uk/research/interest-groups/knowledge-graphs

# Prompting LLMs for entity and context
Ollama helps in running open-source large language models, such as Llama 2,Mistral locally. It bundles model weights, configuration, and data into a single package. It optimizes configuration including GPU usage.
All the loaded models are run locally and available on the port 11434. The web request is placed along with the payload and URL. The actual values of system and prompt depends would be specific to the context.

      payload = {
            "model": "zephyr",
            "temperature": 0.6,
            "stream": False, #return response as a single batch or streamed continuously
            "messages": [
                {"role": "system", "content":system},
                {"role": "user", "content": prompt}
            ]
        }


The "role": "system" message typically provides system-level instructions or context.
The "role": "user" message represents the user’s input or prompt.

source: https://python.langchain.com/docs/integrations/llms/ollama#:~:text=Ollama%20allows%20you%20to%20run,configuration%20details%2C%20including%20GPU%20usage.

Prompt engineering involves crafting clear and effective instructions or queries for language models. Steps include - clear instructions, persona adoption and decomposing complex tasks.


## Next Steps:
The following enhancements are planned for the project:
1. Improve entity recognition and reduce ambiguous terms.
2. Integrate the knowledge graph with external Wikipedia knowledge graphs.
3. Develop a chatbot for interactive learning.

The open source community has been helpful have been able to rely on github repositories and open licences as given below (rahulnayak, MIT license)



# References

1. https://support.google.com/knowledgepanel
2. https://github.com/AITwinMinds/Ollama-in-Google-Colab
3. https://github.com/rahulnyk/knowledge_graph.git
4. https://neo4j.com/docs/ogm-manual/current/reference/
5. https://neo4j.com/why-graph-databases/
6. https://huggingface.co/HuggingFaceH4/zephyr-7b-beta
   

