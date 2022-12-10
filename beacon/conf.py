"""Beacon Configuration."""

#
# Beacon general info
#
beacon_id = ''  # ID of the Beacon
beacon_name = ''  # Name of the Beacon service
api_version = 'v2.0.0'  # Version of the Beacon implementation
uri = ''
beacon_granularity = "record"
max_beacon_granularity = "record"

#
#  Organization info
#
org_id = ''  # Id of the organization
org_name = ''  # Full name
org_description = ()
org_adress = ('The University of Leicester',
              'University Road',
              'Leicester',
              'LE1 7RH',
              'United Kingdom') # filled in with a correctly formatted example
org_welcome_url = ''
org_contact_url = ''
org_logo_url = ''
org_info = ''

#
# Project info
#
description = (r"This <a href='https://beacon-project.io/'>Beacon</a> "
               r"is based on the GA4GH Beacon "
               r"<a href='https://github.com/ga4gh-beacon/specification-v2/blob/master/beacon.yaml'>v2.0</a>")
version = 'v2.0'
welcome_url = ''
alternative_url = ''
create_datetime = ''
update_datetime = ''
# update_datetime will be created when initializing the beacon, using the ISO 8601 format

#
# Service
#
service_type = 'org.ga4gh:beacon:1.0.0'  # service type
service_url = 'https://beacon.ega-archive.org/api/services'
entry_point = False
is_open = True
# Documentation of the service
documentation_url = 'https://github.com/EGA-archive/beacon-2.x/'
# Environment (production, development or testing/staging deployments)
environment = 'test'

# GA4GH
ga4gh_service_type_group = 'org.ga4gh'
ga4gh_service_type_artifact = 'beacon'
ga4gh_service_type_version = '1.0'

# Beacon handovers
beacon_handovers = [
]

#
# Database connection
#
database_host = '127.0.0.1'
database_port = 27017
database_user = 'vpbib'
database_name = 'beacon'
database_auth_source = 'admin'
database_password = 'vpbib'
# database_schema = 'public' # comma-separated list of schemas
# database_app_name = 'beacon-appname' # Useful to track connections

#
# Web server configuration
# Note: a Unix Socket path is used when behind a server, not host:port
#
beacon_host = '0.0.0.0'
beacon_port = 5050
beacon_tls_enabled = False
beacon_tls_client = False
beacon_cert = '/etc/ega/server.cert'
beacon_key = '/etc/ega/server.key'
CA_cert = '/etc/ega/CA.cert'

#
# Permissions server configuration
#
permissions_url = 'http://beacon-permissions'

#
# IdP endpoints (OpenID Connect/Oauth2)
#
# or use Elixir AAI (see https://elixir-europe.org/services/compute/aai)
#
idp_client_id = ''
idp_client_secret = ''  # same as in the test IdP
idp_scope = ''

idp_authorize = ''
idp_access_token = ''
idp_introspection = ''
idp_user_info = ''
idp_logout = ''

idp_redirect_uri = ''

#
# UI
#
autocomplete_limit = 16
autocomplete_ellipsis = '...'

#
# Ontologies
#
ontologies_folder = "deploy/ontologies/"
