'''
Created on 29 Mar 2021
Modified 2023 

@author: ejimenez-ruiz
'''

from SPARQLWrapper import SPARQLWrapper, JSON, XML
from pprint import pprint
import time
import os



def loadingData(endpoint_url, file, format="ttl"):
    #https://graphdb.ontotext.com/documentation/free/quick-start-guide.html#load-data-through-sparql-or-rdf4j-api
    print("Uploading file: " + file)
    if format=="trig":
        curl_command = "curl '" + endpoint_url + "/statements' -X POST -H \"Content-Type:application/x-trig\" -T '" + file + "'"
    else:
        curl_command = "curl '" + endpoint_url + "/statements' -X POST -H \"Content-Type:application/x-turtle\" -T '" + file + "'"
    #Other formats: https://librdf.org/raptor/api/raptor-formats-types-by-parser.html
    #print(curl_command)
    
    status = os.system(curl_command)

    #print(status)
    
    

def queryGraphDBRepo(endpoint_url, query, attempts=3):
    
       
    try:
        
        sparql_web = SPARQLWrapper(endpoint_url)
        # Default is XML:
        # https://sparqlwrapper.readthedocs.io/en/latest/SPARQLWrapper.Wrapper.html
        sparql_web.setReturnFormat(JSON)
            
        sparql_web.setQuery(query)
            
        results = sparql_web.query().convert()
        
        #Raw results in json format
        #print("RAW RESULTS IN JSON FORMAT:")
        #pprint(results)
        
        print("\tRetrieved tuples: " + str(len(results["results"]["bindings"])))
                   
        #Processed results
        #print("Processed results in CSV format:")
        for result in results["results"]["bindings"]:
            row =""
            for out_var in results["head"]["vars"]:
                #print(out_var)
                #print(result[out_var]['value'])        
                row = row + "\"" + result[out_var]['value'] + "\"," 
                
            print(row)
        
        
    except Exception as e:
        print(e)
        
        print("Query '%s' failed. Attempts: %s" % (query, str(attempts)))
        time.sleep(1) #to avoid limit of calls, sleep 1s
        attempts-=1
        if attempts>0:
            return queryGraphDBRepo(endpoint_url, query, attempts)
        else:
            return None




test="world-cities"
test="nobel-prizes" 
test="named-graphs" 

loadData = True
#loadData = False  #If already loaded
path_to_onto_file=None

localhost = "http://127.0.0.1:7200"

if test=="world-cities":

    ##REPOSITORY URL AND SPARQL ENDPOINT
    ##To be updated with your local Endpoint URL
    graphdb_endpoint = localhost + "/repositories/lab_graphdb"
    
    #PATH TO DATA
    path_to_data_file = "./data/worldcities-free-100-task2.ttl"
    path_to_onto_file = "./data/ontology_lab5.ttl"
    
    format="ttl"
    
    
    #QUERY DATA
    query = """
            PREFIX lab5: <http://www.semanticweb.org/ernesto/in3067-inm713/lab5/>
            SELECT DISTINCT ?country (COUNT(?city) AS ?num_cities) WHERE { 
                  ?country lab5:hasCity ?city .
            }
            GROUP BY ?country
            ORDER BY DESC(?num_cities)
            LIMIT 10
            """

elif test=="nobel-prizes":
    
    graphdb_endpoint = localhost + "/repositories/NobelPrize"
    path_to_onto_file = "../files/nobel-prize-ontology.rdf"
    path_to_data_file = "../files/nobelprize_kg.nt"
    
    query_file="./data/query_nobel-prize.txt"
    #query_file="./solution/query7.5_nobel-prize.txt"
    query = open(query_file, 'r').read()
    
    format="ttl"
    

else:
    graphdb_endpoint = localhost + "/repositories/namedGraphs"    
    path_to_data_file = "named_graphs.ttl"
    format="trig"
    
    #query_file="./data/query_named_simple.txt"
    query_file="./data/query_named1.txt"
    #query_file="./data/query_named2.txt"
    #query_file="./data/query_named_all.txt"
    #query_file="./data/query_named_from.txt"    
    query = open(query_file, 'r').read()




if loadData:
    print("\nLoading data to GraphDB:")
    if path_to_onto_file is not None: 
        loadingData(graphdb_endpoint, path_to_onto_file, format)
    
    loadingData(graphdb_endpoint, path_to_data_file, format)


print("\nQuerying GraphDB Endpoint:")
queryGraphDBRepo(graphdb_endpoint, query)



