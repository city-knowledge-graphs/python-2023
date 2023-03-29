'''
Created on 19 Jan 2021

@author: ejimenez-ruiz
'''
import requests


def getEmbeddings():
    
    #Check http://www.kgvec2go.org/
    
    print("\nVector embedding for the resource 'Chicago Bulls':")
    
    #http://dbpedia.org/resource/Chicago_Bulls
    kg_entity = "Chicago_Bulls"
    
    r = requests.get('http://www.kgvec2go.org/rest/get-vector/dbpedia/' + kg_entity) 
    
    print(r.text)

    

#Query pre-computed knowledge graph embeddings
getEmbeddings()

print("\nTests successful!!")
