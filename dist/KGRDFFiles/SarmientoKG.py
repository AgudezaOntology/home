from rdflib import *

SarmientoGraph = Graph()

AgudezaOntologyNamespaceString = "http://www.semanticweb.org/rjbea/ontologies/2022/5/AgudezaOntology#"
OwlNamespaceString = "http://www.w3.org/2002/07/owl#"
RdfNamespaceString = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
agdza = Namespace(AgudezaOntologyNamespaceString)
owl = Namespace(OwlNamespaceString)
rdf = Namespace(RdfNamespaceString)
SarmientoGraph.bind("agdza", agdza)
SarmientoGraph.bind("owl", owl)
SarmientoGraph.bind("rdf", rdf)

#Establish the scholarly source
SarmientoGraph.add((agdza.SarmientoArticle, rdf.type, agdza.Analysis))
SarmientoGraph.add((agdza.Sarmiento, rdf.type, agdza.Critic))
SarmientoGraph.add((agdza.Sarmiento, agdza.wrote, agdza.SarmientoArticle))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.writtenBy, agdza.Sarmiento))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.hasTitle, Literal("Gracián's Agudeza y arte de ingenio")))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.hasDate, Literal(1932)))

#KeyTerms considered by the critic
SarmientoGraph.add((agdza.SarmientoArticle, agdza.considers, agdza.agudeza))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.considers, agdza.wit))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.considers, agdza.concepto))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.considers, agdza.ingenio))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.considers, agdza.conceit))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.considers, agdza.reason))

SarmientoGraph.add((agdza.ingenio, rdf.type, agdza.IntellectualFaculty))
SarmientoGraph.add((agdza.reason, rdf.type, agdza.IntellectualFaculty))
SarmientoGraph.add((agdza.wit, rdf.type, agdza.IntellectualFaculty))

SarmientoGraph.add((agdza.agudeza, rdf.type, agdza.CentralConcept))
SarmientoGraph.add((agdza.concepto, rdf.type, agdza.CentralConcept))
SarmientoGraph.add((agdza.conceit, rdf.type, agdza.CentralConcept))

SarmientoGraph.add((agdza.IntellectualFaculty, owl.subClassOf, agdza.KeyTerm))
SarmientoGraph.add((agdza.CentralConcept, owl.subClassOf, agdza.KeyTerm))

#Links between KeyTerms
SarmientoGraph.add((agdza.agudeza, agdza.equivalentTo, agdza.wit))
SarmientoGraph.add((agdza.agudeza, agdza.equivalentTo, agdza.conceit))
SarmientoGraph.add((agdza.wit, agdza.equivalentTo, agdza.agudeza))
SarmientoGraph.add((agdza.conceit, agdza.equivalentTo, agdza.agudeza))
SarmientoGraph.add((agdza.agudeza, agdza.resultsFrom, agdza.concepto))
SarmientoGraph.add((agdza.concepto, agdza.resultsIn, agdza.agudeza))
SarmientoGraph.add((agdza.agudeza, agdza.belongsTo, agdza.parecer))
SarmientoGraph.add((agdza.concepto, agdza.belongsTo, agdza.ser))

#Other links
SarmientoGraph.add((agdza.reason, agdza.contributesTo, agdza.ConnectionMaking))
SarmientoGraph.add((agdza.ingenio, agdza.contributesTo, agdza.ConnectionMaking))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.hasPhilosophicalScope, agdza.Rhetoric))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.hasPhilosophicalScope, agdza.Aesthetics))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.usesSymbol, agdza.fire))
SarmientoGraph.add((agdza.SarmientoArticle, agdza.usesSymbol, agdza.light))
SarmientoGraph.add((agdza.fire, agdza.symbolises, agdza.agudeza))
SarmientoGraph.add((agdza.light, agdza.symbolises, agdza.ser))
SarmientoGraph.add((agdza.light, agdza.symbolises, agdza.concepto))
SarmientoGraph.add((agdza.agudeza, agdza.symbolisedBy, agdza.fire))
SarmientoGraph.add((agdza.ser, agdza.symbolisedBy, agdza.light))
SarmientoGraph.add((agdza.concepto, agdza.symbolisedBy, agdza.light))

SarmientoGraph.add((agdza.fire, rdf.type, agdza.SymbolicImagery))
SarmientoGraph.add((agdza.light, rdf.type, agdza.SymbolicImagery))

SarmientoGraph.add((agdza.Aesthetics, rdf.type, agdza.PhilosophicalScope))
SarmientoGraph.add((agdza.Rhetoric, rdf.type, agdza.PhilosophicalScope))

#Serialise graph in ttl format
print(SarmientoGraph.serialize(format="ttl"))



