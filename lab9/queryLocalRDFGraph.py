'''
Modified on 1 April 2023

@author: ejimenez-ruiz
'''
from rdflib import Graph

import owlrl


def queryLocalGraph(ontology_file, format_ontology, data_file, format_data, query_file):

    g = Graph()
    g.parse(data_file, format=format_data)#
    if ontology_file is not None: 
        g.parse(ontology_file, format=format_ontology)
    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
        
    #for s, p, o in g:
    #    print((s.n3(), p.n3(), o.n3()))
    
    #Do reasoning!
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics, axiomatic_triples=True, datatype_axioms=False).expand(g)
    print("After reasoning '" + str(len(g)) + "' triples.")
    
    #Load query
    query = open(query_file, 'r').read()    
    
    qres = g.query(query)

    print("\nQuery: ")
    print(query)
    
    print("Results: ")

    #Print results
    for row in qres:        
        #Row is a list of matched RDF terms: URIs, literals or blank nodes
        row_str =""
        for element in row:
            row_str += str(element) + ", "
        
        print("'%s'" % (str(row_str))) 



#Script
test="playground"
test="world-cities"
test="nobel-prizes" 


if test=="playground":
    #Playground
    ontology_file=None
    format_onto=None
    dataset="./data/playground.ttl"
    format_data = "ttl"
    query="./data/query_playground.txt"
    #query="solution/query7.1_playground.txt"
    #query="solution/query7.2_playground.txt"
    #query="solution/query7.3_playground.txt"
elif test=="world-cities":
    #World-cities
    dataset = "./data/worldcities-free-100-task2.ttl"
    format_data = "ttl"
    ontology_file = "./data/ontology_lab5.ttl"
    format_onto = "ttl"
    query = "./data/query_world-cities.txt"
    #query = "solution/query7.4_world-cities.txt"; 
else:
    #Nobel prize
    #Reasoning takes a bit
    ontology_file = "../files/nobel-prize-ontology.rdf"
    format_onto = "xml"
    dataset= "../files/nobelprize_kg.nt"
    format_data = "nt"
    query = "./data/query_nobel-prize.txt"    
    #query = "query_nobel-prize-service.txt";
    #query = "solution/query7.5_nobel-prize.txt";
    #query = "solution/query7.6_nobel-prize.txt";



queryLocalGraph(ontology_file, format_onto, dataset, format_data, query)

