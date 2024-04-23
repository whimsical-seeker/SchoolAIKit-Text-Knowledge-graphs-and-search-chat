

#Derived from **rahulnyk/knowledge_graph** and modified
import sys
from yachalk import chalk #might have to add reference here test and check
import os
print(os.getcwd())
import json
import os
import requests
print("updated")

# %% [code]
def generate( model_name=None,prompt=None, system=None, template=None, context=None, options=None, callback=None):
    try:
        url = f"{'http://localhost:11434/api/chat'}"#"/api/generate"
      
        payload = {
            "model": "zephyr",
            "temperature": 0.6,# value of 0.6 strikes a balance between creativity and coherence.
            "stream": False,
            "messages": [
                {"role": "system", "content":system},
                {"role": "user", "content": prompt}
            ]
        }

        
        # Remove keys with None values
      #  payload = {k: v for k, v in payload.items() if v is not None}
        
        with requests.post(url, json=payload, stream=True) as response:
            response.raise_for_status()
            
            # Creating a variable to hold the context history of the final chunk
            final_context = None
            
            # Variable to hold concatenated response strings if no callback is provided
            full_response = ""

            # Iterating over the response line by line and displaying the details
            for line in response.iter_lines():
                if line:
                    # Parsing each line (JSON chunk) and extracting the details
                    chunk = json.loads(line)
                    if callback:
                        callback(chunk)
                    else:
                        # If this is not the last chunk, add the "response" field value to full_response and print it
                        if  chunk.get("done"):
                            response_piece = chunk.get("message")['content']
                            full_response += response_piece
                          #  print(response_piece, end="", flush=True)
                    
                    # Check if it's the last chunk (done is true)
                    if chunk.get("done"):
                        final_context = chunk.get("context")
            
            # Return the full response and the final context
            return full_response, final_context
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None

def graphPrompt(input: str, metadata={}, model="mistral-openorca:latest"):
    if model == None:
        model = "zephyr"#"mistral-openorca:latest"

    SYS_PROMPT = (
    "You are a network graph maker who extracts terms and their relations from "
    "You are provided with a context chunk (delimited by ```) Your task is to extract the ontology "
    "of necessary key scientific and mathematical concepts mentioned in the given context.\n"
    "Thought 1: While traversing through each sentence, please list terms including entities, concepts, and topics within physics, math, and chemistry.\n "
        "\tTerms can be fundamental principles, laws, equations, constants, theories, formulas,theorems, elements, compounds, reactions, etc..\n"
        "\tTerms should be as atomistic as possible.\n\n"
    "Thought 2: let's determine the relationships between the identified entities within and across the domains.\n"
         "\tThink about dependencies, causal relationships, hierarchical relationships,mathematical relationships.\n"
         "\tFind relationship between terms leveraging semantic relationships such as 'is-a,' 'part-of,''derives-from,' 'is-related-to,' etc., to capture the semantics between different entities. \n\n"
    "Thought 3:Format your output as a list of json. Each element of the list contains a pair of terms,\n"
    "and the relation between them, like the follwing: \n"      
    "[\n"
    "   {\n"
    '       "concept_1": "A concept from extracted ontology",\n'
    '       "concept_2": "A related concept from extracted ontology",\n'
    '       "description": "relationship between the two concepts, concept_1 and concept_2 in one or two lines but keep it concise."\n'
    '       "edge":"semantic relationship between concepts such as is-a, part-of,derives-from,is-related-to, etc.,",\n'
          
    "   }, {...}\n"
    "]"
     )
         
    
    USER_PROMPT = f"context: ```{input}``` \n\n output: "
    response, _ = generate(model_name=model, system=SYS_PROMPT, prompt=USER_PROMPT)
    try:
          print(metadata)
          result = json.loads(response)
          result = [dict(item, **metadata) for item in result]
    except:
        print("\n\nERROR ### Here is the buggy response: ", response, "\n\n")
        result = None
    return result
