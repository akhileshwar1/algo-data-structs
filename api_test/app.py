from flask import Flask, abort, request, jsonify
from connection import conn
from sqlalchemy import text
app = Flask(__name__)


@app.route('/')
def welcome():
    return "<p>Hello, World!</p>"


@app.route('/api/Movies/')
def view():
    return jsonify(get_paginated_list(
        "Movies",
        'api/Movies/',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 5)
    ))


def get_paginated_list(klass, url, start, limit):
    results = conn.execute(text(f"SELECT * FROM {klass}")).fetchall()
    print(results)
    count = len(results)
    print(count)
    if(count < start):
        abort(404)

    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count

    if start == 1:
        obj['prev'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['prev'] = url + 'start=%d&limit=%d' % (start_copy, limit_copy)

    if(start + limit > count):
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    print(obj)
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj

