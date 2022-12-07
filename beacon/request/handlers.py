import json
import logging
from aiohttp import web
from aiohttp.web_request import Request
from bson import json_util
from beacon.request.validate_filters import validate_filters

from beacon.request import ontologies
from beacon.request.model import Granularity, RequestParams
from beacon.response.build_response import (
    build_beacon_resultset_response,
    build_beacon_collection_response,
    build_beacon_boolean_response,
    build_beacon_count_response,
    build_error_response,
    build_filtering_terms_response
)
from beacon.utils.stream import json_stream

LOG = logging.getLogger(__name__)


def collection_handler(db_fn, request=None):
    async def wrapper(request: Request):

        # Get params
        json_body = await request.text() if request.method == "POST" and request.has_body and request.can_read_body else {}
        qparams = RequestParams(**json_body).from_request(request)
        entry_id = request.match_info["id"] if "id" in request.match_info else None

        # Get response
        entity_schema, count, records = db_fn(entry_id, qparams)
        response_converted = (
            [r for r in records] if records else []
        )
        response = build_beacon_collection_response(
            response_converted, count, qparams, lambda x, y: x, entity_schema
        )
        return await json_stream(request, response)

    return wrapper


def generic_handler(db_fn, request=None):
    async def wrapper(request: Request):

        # Get params
        LOG.debug(request.url)
        json_body = await request.json() if request.method == "POST" and request.can_read_body else {}
        qparams = RequestParams(**json_body).from_request(request)

        ############
        # Check for any filters which are not part of this beacon instance and return an error
        ############
        # invalid_filters = validate_filters(json_body)
        # if invalid_filters != set():
        #     error = {
        #         "errorCode": "400",
        #         "errorMessage": F"invalid Filters provided: {', '.join(invalid_filters)}"
        #     }
        #     response = build_error_response(error, qparams, None)
        #     return await json_stream(request, response)
        # ##############
        # else:
        entry_id = request.match_info.get('id', None)

        # Get response
        entity_schema, count, records = db_fn(entry_id, qparams)
        response_converted = records

        response = None
        if qparams.query.requested_granularity == Granularity.BOOLEAN:
            response = build_beacon_boolean_response(
                response_converted, count, qparams, lambda x, y: x, entity_schema)
        elif qparams.query.requested_granularity == Granularity.COUNT:
            response = build_beacon_count_response(
                response_converted, count, qparams, lambda x, y: x, entity_schema)
        else:
            response = build_beacon_resultset_response(
                response_converted, count, qparams, lambda x, y: x, entity_schema)
        return await json_stream(request, response)

    return wrapper


def filtering_terms_handler(db_fn, request=None):
    async def wrapper(request: Request):
        # Get params
        json_body = await request.json() if request.method == "POST" and request.has_body and request.can_read_body else {}
        qparams = RequestParams(**json_body).from_request(request)
        entry_id = request.match_info.get('id', None)

        # Get response
        _, _, records = db_fn(entry_id, qparams)
        response_converted = (
            [r for r in records] if records else []
        )
        resources = [{"id": onto.name, "url": onto.base_iri}
                     for onto in ontologies.ONTOLOGIES.values()]
        response = build_filtering_terms_response(
            response_converted, resources, qparams)
        return await json_stream(request, response)

    return wrapper
