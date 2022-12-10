from pymongo.mongo_client import MongoClient
import conf

client = MongoClient(
    "mongodb://{}:{}@{}:{}/{}?authSource={}".format(
        conf.database_user,
        conf.database_password,
        conf.database_host,
        conf.database_port,
        conf.database_name,
        conf.database_auth_source,
    )
)
client.beacon.datasets.create_index([("$**", "text")])
client.beacon.individuals.create_index([("$**", "text")])
