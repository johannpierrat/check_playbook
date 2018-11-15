#!/usr/bin/python2.7

import os.path
import sys
from datetime import (datetime, timedelta)
from multiprocessing import pool
import requests
import json

global conf

def process_file(name):
    pass

def get_token():
    delta = datetime.now() - timedelta(hours=1)
    if conf.version < 3.1:
        api_version = "/api//v1/"
    else:
        api_version = "/api/v2/"

    try:
        r = requests.post("{}{}authtoken",
                json='{"username":"{}", "password":"{}"}'.format(
                        conf.user, conf.password))
        if r != 200:
            return None

        token = json.loads(r.text)['token']
        return token
    except:
        return None


def get_list_job():
    token = get_token()

    if conf.version < 3.1:
        api_version = "/api/v1/"
    else:
        api_version = "/api/v2/"

    delta = datetime.now() - timedelta(hours=1)

    header = {'Authorization': 'token {}'.format(token)}
    url = '{}{}/?last_updated__gte={}-{}-{} {}:{}'.format(
            conf.tower,
            api_version,
            delta.year,
            delta.month,
            delta.day,
            delta.hour,
            delta.minute
    )
    response = requests.get(url, headers=header)

    if r.requests != 200:
        return None

    jq = json.loads(r.text)
    count = jq['count']
    paths = [result['local_path'] for result in jq['results']]


