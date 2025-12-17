from flask import Flask, request, render_template, jsonify
from elasticsearch import Elasticsearch
from time import time
import os

# Configuration from environment variables
ES_HOST = os.environ.get('ELASTICSEARCH_HOST', 'http://localhost:9200')

es_client = Elasticsearch(hosts=ES_HOST)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'City and It is population data'

@app.route('/health')
def health():
    """Health check endpoint."""
    try:
        if es_client.ping():
            return jsonify({"status": "healthy", "elasticsearch": "connected"})
        return jsonify({"status": "unhealthy", "elasticsearch": "disconnected"}), 503
    except Exception:
        return jsonify({"status": "unhealthy", "elasticsearch": "error"}), 503


@app.route('/population/', methods=['GET', 'POST'])
def create_population_index():
    """Create a new Elasticsearch index."""
    index_name = request.form.get('index_name')
    
    if request.method == 'POST' and index_name:
        try:
            resp = es_client.indices.create(index=index_name)
            print(f'Index {index_name} created')
            return render_template('indexing_population.html', response=resp)
        except Exception as e:
            return render_template('indexing_population.html', response={'error': str(e)})
    
    return render_template('indexing_population.html')


@app.route('/read', methods=['GET', 'POST'])
def read_data():
    """Read a document from Elasticsearch by ID."""
    id_number = request.form.get('id_number')
    index_name = request.form.get('index_name')
    
    if request.method == 'POST' and index_name and id_number:
        try:
            resp = es_client.get(index=index_name, id=id_number)
        except Exception:
            resp = {'_source': {'text': 'Data not found'}}
        return render_template('read_population.html', result=resp)
    
    return render_template('read_population.html', result={})


@app.route('/insert', methods=['GET', 'POST'])
def insert_data():
    """Insert a new document into Elasticsearch."""
    if request.method == 'POST':
        doc = {
            'city': request.form.get('city'),
            'population': request.form.get('population'),
        }
        id_number = request.form.get('id_number')
        index_name = request.form.get('index_name')

        try:
            resp = es_client.index(index=index_name, body=doc, id=id_number)
        except Exception:
            resp = {'error': 'Failed to insert data'}
        return render_template('insert_population.html', response=resp)
    
    return render_template('insert_population.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    """Update an existing document in Elasticsearch."""
    if request.method == 'POST':
        id_number = request.form.get('id_number')
        index_name = request.form.get('index_name')
        field_name = request.form.get('field_name')
        field_value = request.form.get('field_value')

        timestamp = int(time())
        doc = {
            'doc': {
                field_name: field_value,
                'timestamp': timestamp
            }
        }
        try:
            resp = es_client.update(index=index_name, body=doc, id=id_number)
        except Exception:
            resp = {'error': 'Failed to update data'}
        return render_template('update_population.html', response=resp)
    
    return render_template('update_population.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    """Search documents in Elasticsearch."""
    if request.method == 'POST':
        index_name = request.form.get('index_name')
        search_string = request.form.get('search_string')

        try:
            resp = es_client.search(
                index=index_name,
                body={'query': {'match': {'name': search_string}}}
            )
        except Exception:
            resp = {'hits': {'total': {'value': 0}, 'hits': []}}
        return render_template('search_population.html', result=resp)
    
    return render_template('search_population.html', result={'hits': {'total': {'value': 0}, 'hits': []}})


@app.route('/delete_document', methods=['GET', 'POST'])
def delete_document():
    """Delete a document from Elasticsearch by ID."""
    if request.method == 'POST':
        id_number = request.form.get('id_number')
        index_name = request.form.get('index_name')
        try:
            if es_client.exists(index=index_name, id=id_number):
                resp = es_client.delete(index=index_name, id=id_number)
            else:
                resp = {'status': 'Document not found'}
        except Exception:
            resp = {'status': 'Document not found'}
        return render_template('delete_document.html', response=resp)
    
    return render_template('delete_document.html')


@app.route('/delete_index', methods=['GET', 'POST'])
def delete_index():
    """Delete an Elasticsearch index."""
    if request.method == 'POST':
        index_name = request.form.get('index_name')
        try:
            resp = es_client.indices.delete(index=index_name)
        except Exception:
            resp = {'status': 'Failed to delete index. Check if index name is valid.'}
        return render_template('delete_index.html', response=resp)
    
    return render_template('delete_index.html')


if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, port=port, host='0.0.0.0')