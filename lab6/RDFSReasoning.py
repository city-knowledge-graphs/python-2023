from rdflib import Graph

import owlrl


def RDFSInference():
    
    g = Graph()
    
    g.parse("data/lab6-rdfs.ttl", format="ttl")    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
    #Performs RDFS reasoning
    owlrl.DeductiveClosure(owlrl.RDFS_Semantics, axiomatic_triples=True, datatype_axioms=False).expand(g)
    
    
    print("After inference rules: '" + str(len(g)) + "' triples.")
    

    
    print("\nSaving extended graph")
    g.serialize(destination='data/lab6-rdfs-extended.ttl', format='ttl')

        
    
RDFSInference()

