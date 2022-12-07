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

> *optional*: Install a program to interact with your mongoDB to view and edit the DB contents, such as [mongo-express](https://github.com/mongo-express/mongo-express)


#### Load the data

Data is stored in mongoDB within collections of related JSON objects. For the use case of this implementation we will be storing metadata using the [LeHMR](https://lehmr.le.ac.uk/) [metadata model](https://www567.lamp.le.ac.uk/LeHMR_Dev/LeHMR/BeaconAPI/schema) within the "datasets" collection.

For this implementation there is no translation of the received query into fields used by the underlying DB, the data is stored within the metadata model format and all defined filters can act upon this model directly without translation.

To keep the commands simple, the commands below are provided assuming no security has been added to your mongoDB installation. Adding basic security is highly recommended.

```bash
mongoimport --jsonArray --uri "mongodb://127.0.0.1:27017/beacon" --file data/metadata*.json --collection datasets
```

The above command assumes that you have a single JSON file which contains a list of dataset objects, each of which conforms to the LeHMR metadata model.

This loads the JSON files inside of the `data` folder into the MongoDB database.

> You can also use `make load` as a convenience alias.


### Light up the beacon

#### Up the beacon

Once the database is setup you can clone this repo onto your system and install all requirements.

```
cd beacon-2.x
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

### Setting the Informational endpoints data content

Beacon utilises a set of Informational endpoints to describe the Beacon instance itself, the contents for these endpoints
can be set in the [conf.py](../beacon/conf.py), [filtering_terms.py](../db/filtering_terms.py) and [framework.py](../response/framework.py)



