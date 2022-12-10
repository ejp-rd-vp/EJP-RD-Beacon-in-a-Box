from pymongo.mongo_client import MongoClient
from beacon import conf
import logging

LOG = logging.getLogger(__name__)

# client = MongoClient("mongodb://{}:{}@{}:{}/{}?authSource={}".format(
#     conf.database_user,
#     conf.database_password,
#     conf.database_host,
#     conf.database_port,
#     conf.database_name,
#     conf.database_auth_source
# ))
# LOG.info(client)
# userSection = F"{conf.database_user}:{conf.database_password}@" if conf.database_user else ""
# dbSection = F"{conf.database_host}:{conf.database_port}/{conf.database_name}{'?authSource='+ conf.database_auth_source if conf.database_auth_source else ''}"

# client = MongoClient(F"mongodb://{userSection}{dbSection}")

client = MongoClient("mongodb://vpbib:vpbib@beacon_db:27017/beacon?authSource=admin")


