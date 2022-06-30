from rdflib import *

ParkerGraph = Graph()

AgudezaOntologyNamespaceString = "http://www.semanticweb.org/rjbea/ontologies/2022/5/AgudezaOntology#"
OwlNamespaceString = "http://www.w3.org/2002/07/owl#"
RdfNamespaceString = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
agdza = Namespace(AgudezaOntologyNamespaceString)
owl = Namespace(OwlNamespaceString)
rdf = Namespace(RdfNamespaceString)
ParkerGraph.bind("agdza", agdza)
ParkerGraph.bind("owl", owl)
ParkerGraph.bind("rdf", rdf)

#Establish the scholarly source
ParkerGraph.add((agdza.ParkerArticle, rdf.type, agdza.Analysis))
ParkerGraph.add((agdza.Parker, rdf.type, agdza.Critic))
ParkerGraph.add((agdza.Parker, agdza.wrote, agdza.ParkerArticle))
ParkerGraph.add((agdza.ParkerArticle, agdza.writtenBy, agdza.Parker))
ParkerGraph.add((agdza.ParkerArticle, agdza.hasTitle, Literal("'Concept' and 'Conceit': An Aspect of Comparative Literary History")))
ParkerGraph.add((agdza.ParkerArticle, agdza.hasDate, Literal(1982)))

#KeyTerms considered by the critic
ParkerGraph.add((agdza.ParkerArticle, agdza.considers, agdza.agudeza))
ParkerGraph.add((agdza.ParkerArticle, agdza.considers, agdza.concepto))
ParkerGraph.add((agdza.ParkerArticle, agdza.considers, agdza.ingenio))
ParkerGraph.add((agdza.ParkerArticle, agdza.considers, agdza.wit))
ParkerGraph.add((agdza.ParkerArticle, agdza.considers, agdza.conceptus))
ParkerGraph.add((agdza.ParkerArticle, agdza.considers, agdza.conceit))
ParkerGraph.add((agdza.ParkerArticle, agdza.considers, agdza.reason))

ParkerGraph.add((agdza.ingenio, rdf.type, agdza.IntellectualFaculty))
ParkerGraph.add((agdza.wit, rdf.type, agdza.IntellectualFaculty))
ParkerGraph.add((agdza.reason, rdf.type, agdza.IntellectualFaculty))

ParkerGraph.add((agdza.agudeza, rdf.type, agdza.CentralConcept))
ParkerGraph.add((agdza.concepto, rdf.type, agdza.CentralConcept))
ParkerGraph.add((agdza.conceptus, rdf.type, agdza.CentralConcept))
ParkerGraph.add((agdza.conceit, rdf.type, agdza.CentralConcept))

ParkerGraph.add((agdza.parecer, rdf.type, agdza.OntologicalRealm))

ParkerGraph.add((agdza.IntellectualFaculty, owl.subClassOf, agdza.KeyTerm))
ParkerGraph.add((agdza.CentralConcept, owl.subClassOf, agdza.KeyTerm))
ParkerGraph.add((agdza.OntologicalRealm, owl.subClassOf, agdza.KeyTerm))

#Links between KeyTerms
ParkerGraph.add((agdza.agudeza, agdza.equivalentTo, agdza.wit))
ParkerGraph.add((agdza.agudeza, agdza.equivalentTo, agdza.conceit))
ParkerGraph.add((agdza.wit, agdza.equivalentTo, agdza.agudeza))
ParkerGraph.add((agdza.conceit, agdza.equivalentTo, agdza.agudeza))
ParkerGraph.add((agdza.agudeza, agdza.resultsFrom, agdza.concepto))
ParkerGraph.add((agdza.concepto, agdza.resultsIn, agdza.agudeza))
ParkerGraph.add((agdza.agudeza, agdza.belongsTo, agdza.parecer))
ParkerGraph.add((agdza.concepto, agdza.notComponentOf, agdza.conceptus))
ParkerGraph.add((agdza.agudeza, agdza.notComponentOf, agdza.conceptus))
ParkerGraph.add((agdza.conceptus, agdza.notComposedOf, agdza.agudeza))
ParkerGraph.add((agdza.conceptus, agdza.notComposedOf, agdza.concepto))
ParkerGraph.add((agdza.Ingenio, agdza.separateFrom, agdza.reason))

#Other links
ParkerGraph.add((agdza.reason, agdza.contributesTo, agdza.ConnectionMaking))
ParkerGraph.add((agdza.ParkerArticle, agdza.hasPhilosophicalScope, agdza.Rhetoric))
ParkerGraph.add((agdza.ParkerArticle, agdza.usesSymbol, agdza.lips))
ParkerGraph.add((agdza.ParkerArticle, agdza.usesSymbol, agdza.rose))
ParkerGraph.add((agdza.ParkerArticle, agdza.usesSymbol, agdza.lion))
ParkerGraph.add((agdza.lips, agdza.symbolises, agdza.parecer))
ParkerGraph.add((agdza.rose, agdza.symbolises, agdza.parecer))
ParkerGraph.add((agdza.lion, agdza.symbolises, agdza.parecer))
ParkerGraph.add((agdza.parecer, agdza.representedBy, agdza.lips))
ParkerGraph.add((agdza.parecer, agdza.representedBy, agdza.rose))
ParkerGraph.add((agdza.parecer, agdza.representedBy, agdza.lion))
ParkerGraph.add((agdza.ParkerArticle, agdza.references, agdza.SarmientoArticle))

ParkerGraph.add((agdza.lips, rdf.type, agdza.SymbolicImagery))
ParkerGraph.add((agdza.rose, rdf.type, agdza.SymbolicImagery))
ParkerGraph.add((agdza.lion, rdf.type, agdza.SymbolicImagery))

ParkerGraph.add((agdza.SarmientoArticle, rdf.type, agdza.Analysis))
ParkerGraph.add((agdza.SarmientoArticle, agdza.writtenBy, agdza.Sarmiento))
ParkerGraph.add((agdza.Sarmiento, agdza.wrote, agdza.SarmientoArticle))
ParkerGraph.add((agdza.Sarmiento, rdf.type, agdza.Critic))

#Serialise graph in ttl format
print(ParkerGraph.serialize(format="ttl"))