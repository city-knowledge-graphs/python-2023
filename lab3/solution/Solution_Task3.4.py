'''
Created on 20 Feb 2022

@author: ejimenez-ruiz
'''
from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS, FOAF, XSD

#DOCUMENTATION: 
#https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html
#https://rdflib.readthedocs.io/en/stable/rdf_terms.html

def Solution_Task3_4():
    
    #Empty graph
    g = Graph()
    
    #Special namspaces to create
    #The URI created for city is new created as example   
    city = Namespace("http://www.example.org/university/london/city#")
    
    #These URI namespaces exists in the DBPedia KG
    dbo = Namespace("http://dbpedia.org/ontology/")
    dbp = Namespace("http://dbpedia.org/property/")
    dbr = Namespace("http://dbpedia.org/resource/")
       
    #Prefixes
    g.bind("foaf", FOAF) #FOAF is given as default rdflib Namespace
    g.bind("city", city) #city is a newly created rdflib Namespace
    g.bind("dbo", dbo) #dbo is a newly created rdflib Namespace
    g.bind("dbp", dbp) #dbp is a newly created rdflib Namespace
    g.bind("dbr", dbr) #dbr is a newly created rdflib Namespace 
    
    #These lines are equivalent:    
    #ernesto = URIRef("http://www.example.org/university/london/city#ernesto")
    #city.ernesto
    
    #print(city.ernesto)
    
    bnode1 = BNode()  # a GUID is generated
    bnode2 = BNode()

    #We define literals
    family_name = Literal('Jiménez-Ruiz', datatype=XSD.string)  # lang="en" for language tags
    name = Literal('Ernesto', datatype=XSD.string)
    year = Literal('2021', datatype=XSD.gYear)  # lang="en" for language tags
    date = Literal('2019-09-23T00:00:00', datatype=XSD.Date)

    #The "," gives problems otherwise if added as dbr.City,_University_of_London
    city_university = URIRef('http://dbpedia.org/resource/City,_University_of_London')
    
    g.add((city.inm713, RDF.type, city.Module))
    g.add((city.ernesto, RDF.type, FOAF.Person))
    
    g.add((city.ernesto, FOAF.familyName, family_name))
    g.add((city.ernesto, FOAF.givenName, name))
    
    g.add((city.ernesto, city.speaks, dbr.Spanish_language))
    g.add((city.ernesto, city.speaks, dbr.Italian_language))
    g.add((city.ernesto, city.speaks, dbr.English_language))


    g.add((city.ernesto, dbo.birthPlace, dbr.Castellón_de_la_Plana))
    g.add((city.ernesto, dbo.nationality, dbr.Spain))
    
    
    
    #Triple to be annotated via reification
    g.add((city.ernesto, city.teaches, city.inm713))
    #Reification
    g.add((bnode1, RDF.type, RDF.Statement ))
    g.add((bnode1, RDF.subject, city.ernesto ))
    g.add((bnode1, RDF.predicate, city.teaches ))
    g.add((bnode1, RDF.object, city.inm713 ))
    g.add((bnode1, dbo.year, year ))
    
    #Triple to be annotated via reification
    g.add((city.ernesto, dbp.employer, city_university ))
    #Reification
    g.add((bnode2, RDF.type, RDF.Statement ))
    g.add((bnode2, RDF.subject, city.ernesto ))
    g.add((bnode2, RDF.predicate, dbp.employer ))
    g.add((bnode2, RDF.object, city_university ))
    g.add((bnode2, dbo.startDate, date ))
    
    print("Saving graph to 'Solution_Task3.4_rdflib.ttl':")
    
    #print(g.serialize(format="turtle").decode("utf-8"))    
    g.serialize(destination='Solution_Task3.4_rdflib.ttl', format='ttl')


Solution_Task3_4()

