#!/bin/python3
from datetime import datetime


def cur_time(environ, start_response):
    data = list()

    data.append("Now is {}".format(datetime.now()))

    data.append("REQUEST_METHOD: {}".format(environ['REQUEST_METHOD']))
    data.append("RAW_URI: {}".format(environ['RAW_URI']))
    data.append("HTTP_USER_AGENT: {}".format(environ['HTTP_USER_AGENT']))

    data = str.encode("\n".join(data))

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

# gunicorn --workers 4 ./sarvar/main:cur_time
