import logging

LOG = logging.getLogger(__name__)


def get_filtering_terms():
    filtering_terms = [
        {
            "type":"alphanumeric",
            "id": "obo:NCIT_C28421",
            "label": "Sex. Permitted values: obo:NCIT_C16576, obo:NCIT_C20197, obo:NCIT_C124294, obo:NCIT_C17998"
        },
        {
            "type":"alphanumeric",
            "id": "edam:data_2295",
            "label": "Causative Genes"
        },
        {
            "type":"alphanumeric",
            "id": "availableMaterials",
            "label": "Available Materials"

        },
        {
            "type":"alphanumeric",
            "id": "id",
            "label": "Id of resource/dataset",
            "scope": "Catalog"
        },
        {
            "type":"alphanumeric",
            "id": "name",
            "label": "Name of resource/dataset",
            "scope": "Catalog"
        },
        {
            "type":"alphanumeric",
            "id": "	organisation",
            "label": "Organisation of resource/dataset",
            "scope": "Catalog"
        },
        {
            "type":"alphanumeric",
            "id": "resourceTypes",
            "label": "Resource Types of resource/dataset. Permitted values: PatientRegistryDataset, BiobankDataset , KnowledgeBase ",
            "scope": "Catalog"
        },
    #                       Ontology Filters 
        {
            "type":"ontologyTerm",
            "id": "obo:NCIT_C2991",
            "label": "Disease or Disorder"
        },
        {
            "type":"ontologyTerm",
            "id": "Orphanet_558",
            "label": "Disease or Disorder"
        },
        {
            "type":"ontologyTerm",
            "id": "sio:SIO_010056",
            "label": "Phenotype"
        },
    #                   Numeric Filters
        {
            "type":"numeric",
            "id":"obo:NCIT_C25150",
            "label":"Age this year"
        },
        {
            "type":"numeric",
            "id":"obo:NCIT_C83164",
            "label":"Birth Year"
        },
        {
            "type":"numeric",
            "id":"obo:NCIT_C124353",
            "label":"Symptom Onset"

        },
        {
            "type":"numeric",
            "id":"obo:NCIT_C156420",
            "label":"Age at diagnosis"

        }

        
    ]
    return filtering_terms
