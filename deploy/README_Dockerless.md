# Deployment instructions

[![](https://mermaid.ink/img/pako:eNp1U01vgzAM_Ssop01qdtiRw6RRWm1SD91WJk2lhxRMGw0SFEg_VvW_z4EE2pX15Lz3bD_b9EQSmQLxyUaxcuvN3mPh4S-qQC0z5meMagyb98pSr5bYc5HKPS3YgRf8B5Cwiue5k2DWDrNfFou5QS0fBneWT1nN1qwCL7TB6j4WVoTI8ktq5RmRzRzLotR1Zy2F6ruWZQdb1eSQQG4lGc-BggFa2Eo-x1NXQzDzsngwnV4kmufKGar0ut3RmwZ1bDG3Ko_SJ5y_B52jhsDJe6aPuoJrYIkU9PHh0JN2j01-GFzjYXBbFkTqjA7VrhXjgosN1fy6VvR_jei2u-0cDc5j9WYfPehmcAtpmYtOnVNzcG8mWYo2Lzoa1BRorjc0YJbRHcs5fiVSXc_WpDTJeMfBTeLhHf9nDTYgI1KAKhhP8S9yMnBM6i0UEBMfQwEaN5vHJBZnlOoSXcAk5WiF-LXSMCJM1_LjKBL3bjUhZ2i_aMHzL0zOAvw)](https://mermaid.live/edit#pako:eNp1U01vgzAM_Ssop01qdtiRw6RRWm1SD91WJk2lhxRMGw0SFEg_VvW_z4EE2pX15Lz3bD_b9EQSmQLxyUaxcuvN3mPh4S-qQC0z5meMagyb98pSr5bYc5HKPS3YgRf8B5Cwiue5k2DWDrNfFou5QS0fBneWT1nN1qwCL7TB6j4WVoTI8ktq5RmRzRzLotR1Zy2F6ruWZQdb1eSQQG4lGc-BggFa2Eo-x1NXQzDzsngwnV4kmufKGar0ut3RmwZ1bDG3Ko_SJ5y_B52jhsDJe6aPuoJrYIkU9PHh0JN2j01-GFzjYXBbFkTqjA7VrhXjgosN1fy6VvR_jei2u-0cDc5j9WYfPehmcAtpmYtOnVNzcG8mWYo2Lzoa1BRorjc0YJbRHcs5fiVSXc_WpDTJeMfBTeLhHf9nDTYgI1KAKhhP8S9yMnBM6i0UEBMfQwEaN5vHJBZnlOoSXcAk5WiF-LXSMCJM1_LjKBL3bjUhZ2i_aMHzL0zOAvw)

## Prerequisites

You should have installed:

- [MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/installation/installation/)
- [Python 3](https://www.python.org/downloads/)

## Installation

### Light up the database

#### Up the DB

Install mongoDB following the instructions found here:
[https://www.mongodb.com/try/download](https://www.mongodb.com/try/download)

> *optional*: Install a program to interact with your mongoDB to view and edit the DB contents, such as [MongoDB Compass](https://www.mongodb.com/try/download/compass))


#### Load the data

Data is stored in mongoDB within collections of related JSON objects. For the use case of this implementation we will be storing metadata using following schema within the "datasets" collection and individuals in "individuals" collection.

**Beaacon_Catalog schema**
```JSON
{
	"$schema": "http://json-schema.org/draft-07/schema",
	"title": "Beacon Catalog",
	"$comment": "Beacon model",
	"description": "Schema for a Beacon Catalog .",
	"type": "object",
	"required": ["id", "name"],
	"properties": {
		"id": {
			"description": "Unique identifier of the dataset",
			"type": "string",
			"examples": ["dataset01"]
		},
		"name": {
			"description": "Name of the dataset/resource",
			"type": "string",
			"examples": ["Cardiovascular events in over 70s"]
		},
		"description": {
			"description": "Brief description of the dataset",
			"type": "string",
			"examples": ["Project for inferring relationships between cardiovascular events and age"]
		},

		"resourceType": {
			"description": "The primary resource type for this resource.",
			"type": "string",
			"example" : "PatientRegistryDataset",
			"enum": [
			  "PatientRegistryDataset", "BiobankDataset", "KnowledgeBase"
			]
		},
        "createDateTime": {
            "$ref": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/common/commonDefinitions.json#/definitions/Timestamp",
            "description": "The time the dataset was created (ISO 8601 format)",
            "examples": [
                "2017-01-17T20:33:40Z"
            ]
        },
        "updateDateTime": {
            "$ref": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/common/commonDefinitions.json#/definitions/Timestamp",
            "description": "The time the dataset was updated in (ISO 8601 format)",
            "examples": [
                "2017-01-17T20:33:40Z"
            ]
        },
        "version": {
            "type": "string",
            "description": "Version of the dataset",
            "examples": [
                "v1.1"
            ]
        },
        "externalUrl": {
            "type": "string",
            "format": "uri",
            "description": "URL to an external system providing more dataset information (RFC 3986 format).",
            "examples": [
                "http://example.org/wiki/Main_Page"
            ]
        },
		
		"organisations": {
			"description": "Organisation(s) responsible for the processing of data access requests made to this dataset",
			"type": "array",
			"items": {
				"description": "Organisation responsible for the processing of data access requests made to this dataset",
				"type": "string",
				"examples": ["University of Leicester"]
			},
			"examples": [["University of Leicester", "University Hospitals of Leicester"]]
		},
		
	
	},
	"additionalProperties": true
}

```



For this implementation there is no translation of the received query into fields used by the underlying DB, the data is stored within the metadata model format and all defined filters can act upon this model directly without translation.

To keep the commands simple, the commands below are provided assuming no security has been added to your mongoDB installation. Adding basic security is highly recommended.

```bash
mongoimport --jsonArray --uri "mongodb://127.0.0.1:27017/beacon" --file data/datasets*.json --collection datasets
mongoimport --jsonArray --uri "mongodb://127.0.0.1:27017/beacon" --file data/individual*.json --collection individuals
```


This loads the JSON files inside of the `data` folder into the MongoDB database.

> You can also use `make load` as a convenience alias.


### Light up the beacon

#### Up the beacon

Once the database is setup you can clone this repo onto your system and install all requirements.

```
cd EJP-RD-Beacon-in-a-Box
pip install -r requirements.txt
```

You can then start the beacon with the following command:

```bash
python -m beacon
```
This command will print the logs and any errors to screen. Once you are happy that your installation is working then you can redirect the logs to a log file and restart the beacon server using a shell script or by disconnecting the process from the terminal window using "&" at the end of the command.

```
python -m beacon &> logfile.log &
```

