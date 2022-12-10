# EJP-RD-Beacon-in-a-Box

This repository is a modified version of the [Beacon2 Reference Implementation (B2RI)](https://github.com/EGA-archive/beacon-2.x) and contains a stand-alone Beacon instance designed to allow for
the sharing of metadata of datasets.

This repo contains: 

* The (Python 3.7+) [source code for beacon](beacon),
### Local installation instructions(Docker)
> [Instructions](deploy/README_Docker.md)
### Local installation instructions(Dockerless)
> [Instructions](deploy/README_Dockerless.md)

### Importing metadata into the Beacon-in-a-box

To import metadata into your Beacon instance please use the [Beacon-import-tools](https://github.com/Cafe-Variome/Beacon-Import-tools).

<h1 id="query">Query Endpoints</h2>

## Individuals endpoint
> Method : GET

```bash
http GET http://localhost:5050/api/individuals/
```
Querying this endpoit it should return all the variants of the beacon (paginated):

> Method : POST

```bash
http POST http://localhost:5050/api/individuals/ --json < request.json
```

You can use POST to make the previous query. With a `request.json` file like this one:

```json
{
    "meta": {
        "apiVersion": "2.0"
    },
    "query": {
        "filters": [
                {
                "id": "HP_0001252"
                }
        ],
        "includeResultsetResponses": "HIT",
        "pagination": {
            "skip": 0,
            "limit": 10
        },
        "testMode": false,
        "requestedGranularity": "record"
    }
}
```
Above request will return all the individuals with "HP_0001252" phenotype.

You can execute:



But you can also use complex filters:

```json
{
    "meta": {
        "apiVersion": "2.0"
    },
    "query": {
        "filters": [
            {
                "id": "obo:NCIT_C28421",
                "value": "obo:NCIT_C16576"
            }
        ],
        "includeResultsetResponses": "HIT",
        "pagination": {
            "skip": 0,
            "limit": 10
        },
        "testMode": false,
        "requestedGranularity": "record"
    }
}
```
## Catalogs endpoint
> Method : GET

```bash
http GET http://localhost:5050/api/catalogs/ --json < request.json
```
Above request return all records.
> Method : POST

```bash
http POST http://localhost:5050/api/catalogs/ --json < request.json
```

<h5 id="request_body"> Query Request Body: </h5>

```JSON
{ 
"$schema": "https://json-schema.org/draft/2020-12/schema",
 "meta":{},
 "query": {
      "filters": [
        {
          "id": "description",
          "value": "%genome comparison%",
        },
        {
          "id": "resourceTypes",
          "value": " BiobankDataset"

        }
      ]
    }
}
```

**RESPONSE**
```JSON
{
  "meta": {},

  "responseSummary": 
  {
    "exists": true,
    "numTotalResults": 1
  },
  "response": {
    "resultSets": [
      {
        "resultsCount": 1,
        "results": [
          {
          "createDateTime": "2017-04-30T00:00:00+00:00",
          "description": "The Genome in a Bottle Consortium, hosted by the National Institute of Standards and Technology (NIST) is creating reference materials and data for human genome sequencing, as well as methods for genome comparison and benchmarking. ",
          "externalUrl": "https://www.nature.com/articles/sdata201625, https://jimb.stanford.edu/giab-resources",
          "id": "EGAD00001008097",
          "name": "The Genome in a Bottle Consortium (GIAB)",
          "updateDateTime": "2017-04-30T00:00:00+00:00",
          "resourceTypes": ["BiobankDataset"],
          "organisation": ["UOL"]

          }
        ],
        "resultsHandover": null
      }
    ]
  },
  "beaconHandovers": []
  }
```


