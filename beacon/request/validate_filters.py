import logging
from beacon.db.filtering_terms import get_filtering_terms

LOG = logging.getLogger(__name__)


def validate_filters(json_body=None):
    if "query" not in json_body:
        return set()
    if "filters" not in json_body["query"]:
        return set()
    supported = [filter["id"] for filter in get_filtering_terms()]
    LOG.info(set(supported))
    supplied = [filter["id"] for filter in json_body["query"]["filters"]]
    LOG.info(set(supplied) - set(supported))
    return set(supplied) - set(supported)
