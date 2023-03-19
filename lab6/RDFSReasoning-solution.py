from rdflib import Graph

import owlrl


def RDFSInference():
    
    g = Graph()
    
    g.parse("data/lab6-rdfs.ttl", format="ttl")    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
    #Performs RDFS reasoning
    owlrl.DeductiveClosure(owlrl.RDFS_Semantics, axiomatic_triples=True, datatype_axioms=False).expand(g)
    
    
    print("After inference rules: '" + str(len(g)) + "' triples.")
    
    
    #Check if entailments hold
    checkEntailments(g)

    
    print("\nSaving extended graph")
    g.serialize(destination='data/lab6-rdfs-extended.ttl', format='ttl')

    


def checkEntailments(g):
    
    print("\nChecking entailments: ")
    
    triple1 = ":Father rdfs:subClassOf :Person ." 
    triple2 = ":Woman rdfs:subClassOf :Person ."
    triple3 = ":Juliet a :Person ."
    triple4 = ":Ann a :Child ."
    triple5 = ":Ann :isChildOf :Carl ."
    triple6 = ":Ann :hasParent :Juliet ."
    triple7 = "rdfs:range rdf:type rdfs:Resource ."
    triple8 = ":Mother rdfs:subClassOf :Person ."
    
    
    checkEntailment(g, triple1)
    checkEntailment(g, triple2)
    checkEntailment(g, triple3)
    checkEntailment(g, triple4)
    checkEntailment(g, triple5)
    checkEntailment(g, triple6)
    checkEntailment(g, triple7)
    checkEntailment(g, triple8)
    
    
    
def checkEntailment(g, triple):
    
    #We use an ASK query instead of a select. It could be done with SELETCT and then checking that the results are not empty 
    qres = g.query(
    """ASK {""" + triple + """ }""")

    #Single row with one boolean vale
    for row in qres:
        print("Does '" + triple + "' hold? " + str(row))
    
    
RDFSInference()

