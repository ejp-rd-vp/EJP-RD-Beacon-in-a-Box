from aiohttp import web

from beacon.db import analyses, biosamples, cohorts, datasets, g_variants, individuals, runs, filtering_terms
from beacon.request.handlers import collection_handler, generic_handler, filtering_terms_handler
from beacon.response import framework, info, service_info


routes = [

    ########################################
    # CONFIG
    ########################################
    web.get('/api/', info.handler),
    # Name added to redirect / -> /info
    web.get('/api/info/', info.handler, name="info"),
    web.get('/api/service-info/', service_info.handler),
       web.get('/api/filtering_terms/',
            filtering_terms_handler(db_fn=filtering_terms.get_filtering_terms)),

    web.get('/api/configuration/', framework.configuration),
    web.get('/api/entry_types/', framework.entry_types),
    web.get('/api/map/', framework.beacon_map),

    ########################################
    # GET
    ########################################

    web.get('/api/catalogs/',
            generic_handler(db_fn=datasets.get_datasets)),
    web.get('/api/individuals/',
            generic_handler(db_fn=individuals.get_individuals)),

    ########################################
    # POST
    ########################################

    web.post('/api/catalogs/',
             generic_handler(db_fn=datasets.get_datasets)),
    web.post('/api/individuals/',
             generic_handler(db_fn=individuals.get_individuals)),

]
