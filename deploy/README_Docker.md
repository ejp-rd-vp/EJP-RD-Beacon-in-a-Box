# Deployment instructions

[![](https://mermaid.ink/img/pako:eNp1U01vgzAM_Ssop01qdtiRw6RRWm1SD91WJk2lhxRMGw0SFEg_VvW_z4EE2pX15Lz3bD_b9EQSmQLxyUaxcuvN3mPh4S-qQC0z5meMagyb98pSr5bYc5HKPS3YgRf8B5Cwiue5k2DWDrNfFou5QS0fBneWT1nN1qwCL7TB6j4WVoTI8ktq5RmRzRzLotR1Zy2F6ruWZQdb1eSQQG4lGc-BggFa2Eo-x1NXQzDzsngwnV4kmufKGar0ut3RmwZ1bDG3Ko_SJ5y_B52jhsDJe6aPuoJrYIkU9PHh0JN2j01-GFzjYXBbFkTqjA7VrhXjgosN1fy6VvR_jei2u-0cDc5j9WYfPehmcAtpmYtOnVNzcG8mWYo2Lzoa1BRorjc0YJbRHcs5fiVSXc_WpDTJeMfBTeLhHf9nDTYgI1KAKhhP8S9yMnBM6i0UEBMfQwEaN5vHJBZnlOoSXcAk5WiF-LXSMCJM1_LjKBL3bjUhZ2i_aMHzL0zOAvw)](https://mermaid.live/edit#pako:eNp1U01vgzAM_Ssop01qdtiRw6RRWm1SD91WJk2lhxRMGw0SFEg_VvW_z4EE2pX15Lz3bD_b9EQSmQLxyUaxcuvN3mPh4S-qQC0z5meMagyb98pSr5bYc5HKPS3YgRf8B5Cwiue5k2DWDrNfFou5QS0fBneWT1nN1qwCL7TB6j4WVoTI8ktq5RmRzRzLotR1Zy2F6ruWZQdb1eSQQG4lGc-BggFa2Eo-x1NXQzDzsngwnV4kmufKGar0ut3RmwZ1bDG3Ko_SJ5y_B52jhsDJe6aPuoJrYIkU9PHh0JN2j01-GFzjYXBbFkTqjA7VrhXjgosN1fy6VvR_jei2u-0cDc5j9WYfPehmcAtpmYtOnVNzcG8mWYo2Lzoa1BRorjc0YJbRHcs5fiVSXc_WpDTJeMfBTeLhHf9nDTYgI1KAKhhP8S9yMnBM6i0UEBMfQwEaN5vHJBZnlOoSXcAk5WiF-LXSMCJM1_LjKBL3bjUhZ2i_aMHzL0zOAvw)

## Prerequisites

You should have installed:

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/installation/installation/) (specifically `mongoimport` to add the dummy data to the database)
- [Python 3](https://www.python.org/downloads/)

## Installation

All of the commands should be executed from the deploy directory.

```bash
cd deploy
```

### Light up the database

#### Up the DB

```bash
docker-compose up -d db
docker-compose up -d mongo-express
```

With `mongo-express` we can see the contents of the database at [http://localhost:8081](http://localhost:8081).

#### Load the data

To load the database we execute the following commands:

```bash
mongoimport --jsonArray --uri "mongodb://vpbib:vpbib@127.0.0.1:27017/beacon?authSource=admin" --file data/datasets*.json --collection datasets
mongoimport --jsonArray --uri "mongodb://vpbib:vpbib@127.0.0.1:27017/beacon?authSource=admin" --file data/individuals*.json --collection individuals
```

This loads the JSON files inside of the `data` folder into the MongoDB database.

> You can also use `make load` as a convenience alias.

#### Create the indexes

You can create the necessary indexes running the following Python script:

```bash
# Install the dependencies
pip3 install pymongo

python3 reindex.py
```

### Light up the beacon

#### Up the beacon

Once the database is setup, you can up the beacon with the following command:

```bash
docker-compose up -d beacon
```

#### Check the logs

Check the logs until the beacon is ready to be queried:

```bash
docker-compose logs -f beacon
```
