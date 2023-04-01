'''
Modified on 1 April 2023

@author: ejimenez-ruiz
'''
from rdflib import Graph


def updateLocalGraph():
    
    dataset="./data/playground.ttl"
    format_data = "ttl"
    
    g = Graph()
    g.parse(dataset, format=format_data)#
    
    #If available ontology
    #g.parse(ontology_file, format=format_ontology)
    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
    
    
    ## Insert triples
    query_insert = """
       PREFIX ttr: <http://example.org/tuto/resource#>\n
       PREFIX tto: <http://example.org/tuto/ontology#>\n
       PREFIX dbo: <http://dbpedia.org/ontology/>\n
       PREFIX dbp: <http://dbpedia.org/property/>\n
       insert data {
           ttr:Bella dbp:name 'Bella' .\n
           ttr:Bella a tto:Cat .\n
           ttr:Ernesto a dbo:Person .\n
           ttr:Ernesto ttr:pet ttr:Bella .\n                
        }"""
    qres = g.update(query_insert)
    print("Triples after insert update: '" + str(len(g)) + "' triples.")
    
    
    
    ## Delete triples
    query_delete = """
       PREFIX ttr: <http://example.org/tuto/resource#>\n
       PREFIX tto: <http://example.org/tuto/ontology#>\n
       PREFIX dbo: <http://dbpedia.org/ontology/>\n
       PREFIX dbp: <http://dbpedia.org/property/>\n
       delete data {
           ttr:Bella dbp:name 'Bella' .\n
           ttr:Bella a tto:Cat .\n
           ttr:Ernesto a dbo:Person .\n
           ttr:Ernesto ttr:pet ttr:Bella .\n                
        }"""
    qres = g.update(query_delete)
    print("Triples after delete update: '" + str(len(g)) + "' triples.")



    ##Update labels
    query_update_labels = """
       PREFIX ttr: <http://example.org/tuto/resource#>\n
       PREFIX tto: <http://example.org/tuto/ontology#>\n
       PREFIX dbo: <http://dbpedia.org/ontology/>\n
       PREFIX dbp: <http://dbpedia.org/property/>\n
       PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n
         delete { ?x dbp:name ?y }\n
         insert { ?x rdfs:label ?y }\n
         where { ?x dbp:name ?y }                
    """
    qres = g.update(query_update_labels)
    print("Triples after update labels: '" + str(len(g)) + "' triples.")
    
    
    
    #Save new KG
    file_output = dataset.replace(".ttl", "-update-labels.ttl")
    g.serialize(destination=file_output, format='ttl')
    print("Created new file " + file_output)
    


updateLocalGraph()
    
    