command = 'home/ubuntu/rest-kaffka/Kaffka-REST/env/bin/gunicorn'
pythonpath = '/home/ubuntu/rest-kaffka/Kaffka-REST/config'
bind = '127.0.0.1:8000'
worker = 3
user = 'ubuntu'
limir_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
