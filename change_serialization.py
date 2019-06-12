import rdflib, os

try:
    gsource = rdflib.Graph()
    gdest = rdflib.Graph()
    fsource="filename.ttl"
    fdest = "filename.rdf"
    with open(fsource, "r") as f:
        gsource.parse(location = fsource, format="turtle")
        
        qres = gsource.query(
            """SELECT *
               WHERE {
                     ?s ?p ?o .
               }""")
   
        for row in qres:
                gdest.add(row)
                gdest.serialize(destination = fdest, format="xml")
        gdest.close()
        
except Exception as e:
    if hasattr(e, 'message'):
        print(e.message)
    else:
        print(e)
