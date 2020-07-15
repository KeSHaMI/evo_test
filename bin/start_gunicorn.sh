#!/bin/bash
source /home/ubuntu/rest-kaffka/Kaffka-REST/env/bin/activate
exec gunicorn -c "/home/ubuntu/rest-kaffka/Kaffka-REST/gunicorn_config.py" config.wsgi




