from enum import Enum


class DefaultSchemas(Enum):
    DATASETS = {"entityType": "catalogs", "schema": "vp_catalogs-v1.0"}
    INDIVIDUALS = {"entityType": "individual", "schema": "ejp-individuals_v1.0"}
    ANALYSES = {"entityType": "analysis", "schema": "beacon-analysis-v2.0.0"}
    BIOSAMPLES = {"entityType": "biosample", "schema": "beacon-dataset-v2.0.0"}
    COHORTS = {"entityType": "cohort", "schema": "beacon-cohort-v2.0.0"}
    GENOMICVARIATIONS = {"entityType": "genomicVariation", "schema": "beacon-g_variant-v2.0.0"}
    RUNS = {"entityType": "run", "schema": "beacon-run-v2.0.0"}
