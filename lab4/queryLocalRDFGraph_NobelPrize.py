'''
Created on 17 Feb 2022

@author: ejimenez-ruiz
'''
from rdflib import Graph

def queryLocalGraph():

    #Example from  https://www.stardog.com/tutorials/data-model/
  

    #Loads KG
    g = Graph()
    g.parse("../files/nobelprize_kg.nt", format="nt")
  
    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
    #for s, p, o in g:
    #    print((s.n3(), p.n3(), o.n3()))
    
        
    print("Female laureates:")
    
    nobelprize_query = """
    SELECT DISTINCT ?name_laur WHERE { 
    ?laur <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://data.nobelprize.org/terms/Laureate> . 
    ?laur <http://www.w3.org/2000/01/rdf-schema#label> ?name_laur . 
    ?laur <http://xmlns.com/foaf/0.1/gender> "female" . }
    """
    
    #Same query with prefixes     
    nobelprize_query = """
    PREFIX nobel: <http://data.nobelprize.org/terms/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT DISTINCT ?name_laur WHERE { 
    ?laur rdf:type nobel:Laureate . 
    ?laur rdfs:label ?name_laur . 
    ?laur foaf:gender "female" . }
    """
    
    
    qres = g.query(nobelprize_query)

    for row in qres:
        #Row is a list of matched RDF terms: URIs, literals or blank nodes
        print("'%s'" % (str(row.name_laur))) #Same name as in sparql query SELECT variable
        
        
queryLocalGraph()
