# Beacon v2.x

This repository is a modified version of the [Beacon2 Reference Implementation (B2RI)](https://github.com/EGA-archive/beacon-2.x) and contains a stand-alone Beacon instance designed to allow for
the sharing of metadata of datasets.

This repo contains: 

* The (Python 3.9+) [source code for beacon](beacon),
* **A docker-less version of the B2RI**

> [Local installation instructions](deploy/README_Dockerless.md)

### Importing metadata into the Beacon-in-a-box

To import metadata into your Beacon instance please use the [Beacon-import-tools](https://github.com/Cafe-Variome/Beacon-Import-tools).


## Usage

You can query the beacon using GET or POST. Below, you can find some examples of usage:

> For simplicity (and readability), we will be using [HTTPie](https://github.com/httpie/httpie).

### Using GET

Querying this endpoit it should return the 13 variants of the beacon (paginated):

```bash
http GET http://localhost:5050/api/g_variants/
```

You can also add [request parameters](https://github.com/ga4gh-beacon/beacon-v2-Models/blob/main/BEACON-V2-Model/genomicVariations/requestParameters.json) to the query, like so:

```bash
http GET http://localhost:5050/api/g_variants/?start=9411499,9411644&end=9411609
```

This should return 3 genomic variants.

### Using POST

You can use POST to make the previous query. With a `request.json` file like this one:

```json
{
    "meta": {
        "apiVersion": "2.0"
    },
    "query": {
        "requestParameters": {
            "start": [ 9411499, 9411644 ],
            "end": [ 9411609 ]
        },
        "filters": [],
        "includeResultsetResponses": "HIT",
        "pagination": {
            "skip": 0,
            "limit": 10
        },
        "testMode": false,
        "requestedGranularity": "count"
    }
}
```

You can execute:

```bash
http POST http://localhost:5050/api/g_variants/ --json < request.json
```

But you can also use complex filters:

```json
{
    "meta": {
        "apiVersion": "2.0"
    },
    "query": {
        "filters": [
            {
                "id": "UBERON:0001256",
                "scope": "biosamples",
                "includeDescendantTerms": false
            }
        ],
        "includeResultsetResponses": "HIT",
        "pagination": {
            "skip": 0,
            "limit": 10
        },
        "testMode": false,
        "requestedGranularity": "count"
    }
}
```

You can execute:

```bash
http POST http://localhost:5050/api/biosamples/ --json < request.json
```

And it will use the ontology filter to filter the results.


### Version notes

* Fusions (`mateName`) are not supported.

