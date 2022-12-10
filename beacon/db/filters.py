from ast import Str
from collections import defaultdict
from typing import List, Union
import re
import dataclasses
from copy import deepcopy

from beacon.request import ontologies
from beacon.request.model import AlphanumericFilter, CustomFilter, NumericFilter, OntologyFilter, Operator, Similarity
from beacon.db.filtering_terms import get_filtering_terms

import logging

LOG = logging.getLogger(__name__)

CURIE_REGEX = r'^([a-zA-Z0-9]*):\/?[a-zA-Z0-9]*$'


def apply_filters(query: dict, filters: List[dict]) -> dict:
    LOG.debug("Filters len = {}".format(len(filters)))
    if len(filters) > 0:
        query["$and"] = []
        partial_query = {}
        for filter in filters:
            if type(filter["id"]) == list:
                partial_query = format_array_filter(filter["id"])
            # if filter["id"].startswith('HP_') or filter["id"].startswith('Orphanet_'):
            #     filter = OntologyFilter(**filter)
            #     LOG.debug("Ontology filter: %s", filter.id)
            #     partial_query = {"$text": defaultdict(str)}
            #     partial_query = apply_ontology_filter(partial_query, filter)

            elif "value" in filter:
                filter = AlphanumericFilter(**filter)
                value = format_value(filter.value)
                LOG.info(type(value))
                if(isinstance(value, int)):
                    LOG.debug("Numeric filter: %s %s %s",filter.id, filter.operator, filter.value)
                    partial_query = apply_numeric_filter(partial_query, filter)
                else:
                    LOG.debug("Alphanumeric filter: %s %s %s",filter.id, filter.operator, filter.value)
                    partial_query = apply_alphanumeric_filter(partial_query, filter)
            elif "similarity" in filter or "includeDescendantTerms" in filter or re.match(CURIE_REGEX, filter["id"]):
                filter = OntologyFilter(**filter)
                LOG.debug("Ontology filter: %s", filter.id)
                partial_query = {"$text": defaultdict(str)}
                partial_query = apply_ontology_filter(partial_query, filter)
            else:
                filter = CustomFilter(**filter)
                LOG.debug("Custom filter: %s", filter.id)
                partial_query = apply_custom_filter(partial_query, filter)
        query["$and"].append(partial_query)
    else:
        query={}
    return query

 
def apply_ontology_filter(query: dict, filter: OntologyFilter) -> dict:
    LOG.debug("QUERY: %s", query)
    is_filter_id_required = True
    q =""
    # Search similar
    if filter.similarity != Similarity.EXACT:
        is_filter_id_required = False
        similar_terms = ontologies.get_similar_ontology_terms(
            filter.id, filter.similarity)
        LOG.debug("Similar: {}".format(similar_terms))
        for term in similar_terms:
            if query["$text"]["$search"]:
                query["$text"]["$search"] += '\"' + term + '\"'

    # Apply descendant terms
    if filter.include_descendant_terms:
        is_filter_id_required = False
        descendants = ontologies.get_descendants(filter.id)
        LOG.debug("Descendants: {}".format(descendants))
        for descendant in descendants:
            if query["$text"]["$search"]:
                query["$text"]["$search"] += '\"' + descendant + '\"'

    if is_filter_id_required:
        q ={"$text":{"$search": filter.id}}
        # if filter.id.startswith('Orphanet_'):
        #    LOG.debug("QUERY: %s", query)
        #    q = {"sio:SIO_001003": {'$regex': filter.id }}
        # elif filter.id.startswith('HP_'):
        #     q = {"sio:SIO_010056": {'$regex':  filter.id }}
    
    return q


def format_value(value: Union[str, List[int]]) -> Union[List[int], str, int, float]:
    if isinstance(value, list):
        return value
    elif value.isnumeric():
        if float(value).is_integer():
            return int(value)
        else:
            return float(value)
    else:
        return value


def format_operator(operator: Operator, value: Str) -> str:
    if operator == Operator.EQUAL:
        if "%" in value:
            return "$regex"
        else:
            return "$eq"
    elif operator == Operator.NOT:
        return "$ne"
    elif operator == Operator.GREATER:
        return "$gt"
    elif operator == Operator.GREATER_EQUAL:
        return "$gte"
    elif operator == Operator.LESS:
        return "$lt"
    else:
        # operator == Operator.LESS_EQUAL
        return "$lte"


def apply_alphanumeric_filter(query: dict, filter: AlphanumericFilter) -> dict:
    formatted_value = format_value(filter.value)
    formatted_operator = format_operator(filter.operator, filter.value)
    if formatted_operator == "$regex":
        query[filter.id] = {
            formatted_operator: "^"+formatted_value.replace("%", ".*")+"$"}
    else:
        query[filter.id] = {formatted_operator: formatted_value}
    LOG.debug("QUERY: %s", query)
    return query


def apply_numeric_filter(query: dict, filter: NumericFilter) -> dict:
    formatted_operator = format_operator(filter.operator, filter.value)
    formatted_value = int(filter.value)
    query[filter.id] = {formatted_operator: formatted_value}
    return query


def apply_custom_filter(query: dict, filter: CustomFilter) -> dict:
    LOG.info(query)
    if "$text" in query:
        LOG.info(query)
        query["$text"]["$search"] += " "+'\"' + filter.id + '\"'
    else:
         query ={"$text":{"$search": filter.id}}
    return query

def format_array_filter(filterId:list):

    search =""
    for i in filterId:
        search += " "+ i
    q ={"$text":{"$search": search}}
    return q
