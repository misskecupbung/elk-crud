from flask import Flask, request, render_template, jsonify
from elasticsearch import Elasticsearch
from time import sleep, time
import json
import os
import requests

pd = Elasticsearch(hosts='http://kibana.dwiananda.click:9200')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'City and It is population data'

@app.route('/health')
def health():
    return {"message": "Health OK!"}


@app.route('/population/', methods=['GET', 'POST'])
def create_population_index():
    index_name = request.form.get('index_name')
    doc_type = request.form.get('doc_type')
    if index_name and doc_type is not None:
        r = requests.get('http://elasticsearch.dwiananda.click:9200/')
        i = 1
        while r.status_code == 200:
            if i != 17:
                r = requests.get('http://swapi.co/api/people/' + str(i))
                resp = pd.index(index=index_name, doc_type=doc_type, id=i, body=json.loads(r.content))
            i = i + 1
        return render_template('indexing_population.html', data=i, response=resp)

    print('index {} create'.format(index_name))
    return render_template('indexing_population.html')


@app.route('/read', methods=['GET', 'POST'])
def read_data():
    id_number = request.form.get('id_number')  # substitute with args to work with postman as in: request.args.get
    doc_type = request.form.get('doc_type')
    index_name = request.form.get('index_name')
    try:
        resp = pd.get(index=index_name, doc_type=doc_type, id=id_number)

    except:
        resp = {'_source': {'text': 'Data not found'}}
    return render_template('read_population.html', result=resp)


@app.route('/insert', methods=['GET', 'POST'])
def insert_data():
    doc1 = {'city': request.form.get("city"),
            'population': request.form.get("population"),
            }
    id_number = request.form.get('id_number')  # substitute with args to work with postman as in: request.args.get
    doc_type = request.form.get('doc_type')
    index_name = request.form.get('index_name')

    try:
        resp = pd.index(index=index_name, doc_type=doc_type, body=doc1, id=id_number)
    except:
        resp = {'estado': 'Data not agregate'}

    return render_template('insert_demo.html', response=resp)


@app.route('/update', methods=['GET', 'POST'])
def update():
    id_number = request.form.get('id_number')  # substitute with args to work with postman as in: request.args.get
    doc_type = request.form.get('doc_type')
    index_name = request.form.get('index_name')

    timestamp = int(time())
    source_to_update = {

        "doc": {
            "year": 2014,
            "grade": "Grade 3",
            "timestamp": timestamp  # integer of epoch time
        }
    }

    doc1 = {"doc": {
                    request.form.get("field_name"): request.form.get("field_value"),
                    "timestamp": timestamp
                  }
    }
    try:
        resp = pd.update(index=index_name, doc_type=doc_type, body=doc1, id=id_number)
    except:
        resp = {'city': 'Data not update'}
    return render_template('update_demo.html', response=resp)


@app.route('/search', methods=['GET', 'POST'])
def search():
    index_name = request.form.get('index_name')
    search_string = request.form.get('search_string')

    try:
        resp = pd.search(index=index_name,
                         # body={"query": {"query_string": {"query": search_string, "default_field": "name"}}}
                         body={"query":{"match":{"name":search_string}}}
                         )

    except:
        resp = {'hits': {'total': {'value': 0}, 'hits': {'_id': '404', '_source': {'name': 'NOBODY'}}}}
    return render_template('search_demo.html', result=resp)


@app.route('/delete_document', methods=['GET', 'POST'])
def delete_document():
    id_number = request.form.get('id_number')
    index_name = request.form.get('index_name')
    try:
        if pd.exists(index=index_name, id=id_number):
            resp = pd.delete(index=index_name, id=id_number)

        else:
            resp = {'Status': 'document not found.'}
    except:
        resp = {'Status': 'document not found.'}
    return render_template('delete_document.html', response=resp)


@app.route('/delete_index', methods=['GET', 'POST'])
def delete_index():
    index_name = request.form.get('index_name')
    try:
        resp = pd.indices.delete(index=index_name)

    except:
        resp = {'Status': 'Type an index name please'}
    return render_template('delete_index.html', response=resp)


if __name__ == '__main__':
    app.run(debug=True, port=5000)