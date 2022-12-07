"""
Beacon Framework Configuration Endpoints.
"""

# import logging

from beacon import conf

# LOG = logging.getLogger(__name__)
from beacon.db.schemas import DefaultSchemas

from beacon.utils.stream import json_stream


def get_entry_types():
    return {
        "dataset": {
            "id": "dataset",
            "name": "EJP dataset entry",
            "ontologyTermForThisType": {
                "id": "ABC:123",
                "label": "dataset"
            },
            "partOfSpecification": "Beacon v2.0.0",
            "description": "A dataset available for use within EJP, this may be a catalogue, a biobank, patient registry, knowledgebase or other",
            "defaultSchema": {
                "id": "ejp_dataset_v1.0",
                "name": "EJP dataset",
                "referenceToSchemaDefinition": "",
                "schemaVersion": "v1.0"
            },
            "additionalSupportedSchemas": []
        }

    }


async def configuration(request):
    meta = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/responses/sections/beaconInformationalResponseMeta.json',
        'beaconId': conf.beacon_id,
        'apiVersion': conf.api_version,
        'returnedSchemas': []
    }

    response = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/configuration/beaconConfigurationSchema.json',
        'maturityAttributes': {
            'productionStatus': 'DEV'
        },
        'securityAttributes': {
            'defaultGranularity': 'record',
            'securityLevels': ['PUBLIC', 'REGISTERED', 'CONTROLLED']
        },
        'entryTypes': get_entry_types()
    }

    configuration_json = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/responses/beaconConfigurationResponse.json',
        'meta': meta,
        'response': response
    }

    return await json_stream(request, configuration_json)


async def entry_types(request):
    meta = {
        'beaconId': conf.beacon_id,
        'apiVersion': conf.api_version,
        'returnedSchemas': []
    }

    response = {
        "entryTypes": get_entry_types()
    }

    entry_types_json = {
        'meta': meta,
        'response': response
    }

    return await json_stream(request, entry_types_json)


async def beacon_map(request):
    meta = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/responses/sections/beaconInformationalResponseMeta.json',
        'beaconId': conf.beacon_id,
        'apiVersion': conf.api_version,
        'returnedSchemas': []
    }

    response = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/configuration/beaconMapSchema.json',
        "endpointSets": {
            "datasets": {
                "entryType": "datasets",
                "openAPIEndpointsDefinition": "",
                "rootUrl": conf.uri + "/api/datasets",
                "endpoints": {
                }
            }
        }
    }

    beacon_map_json = {
        'meta': meta,
        'response': response
    }

    return await json_stream(request, beacon_map_json)
