from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS, FOAF, XSD

#1. Load mappings
#http://www.semanticweb.org/city/in3067-inm713/2023/restaurants#AmericanPizza|http://www.co-ode.org/ontologies/pizza/pizza.owl#American|=|0.95|CLS

#2. Create triples with RDFLib

def transformMappings(filename):
    
    g = Graph()
    
    city = Namespace("http://www.semanticweb.org/city/in3067-inm713/2023/restaurants#")
    pizza = Namespace("http://www.co-ode.org/ontologies/pizza/pizza.owl#")
    
    g.bind("owl", OWL) #OWL is given as defaulty namespace
    g.bind("city", city) #city is a newly created namespace
    g.bind("pizza", pizza) #pizza is a newly created namespace
    
    
    with open(filename) as file:
        for line in file:
            elements=line.split("|")
            uri1=elements[0]
            uri2=elements[1]
            type=elements[4].strip()
            
            #print(uri1)
            #print(uri2)
            #print(type)
    
    
            if type == "CLS":
                g.add((URIRef(uri1), OWL.equivalentClass, URIRef(uri2)))
            elif type == "OPROP" or type == "DPROP":
                g.add((URIRef(uri1), OWL.equivalentProperty, URIRef(uri2)))
                
        
    file_out = filename.split(".")[0]+'.ttl'
    print(g.serialize(format="turtle").decode("utf-8"))    
    g.serialize(destination=file_out, format='ttl')



filename = "/home/ernesto/Documents/City_Teaching/2022-2023/mappings-logmap/reference-mappings-pizza.txt"
transformMappings(filename)