# Elasticsearch CRUD Application

A simple Python Flask application that provides CRUD (Create, Read, Update, Delete) operations for managing city population data using Elasticsearch as the database.

## Features

- Create Elasticsearch indices
- Insert, read, update, and delete documents
- Search functionality
- Health check endpoint
- Docker support
- Helm chart for Kubernetes deployment

## Tech Stack

- **Python 3.11+** - Programming language
- **Flask** - Web framework
- **Elasticsearch** - NoSQL database
- **Docker** - Containerization
- **Helm** - Kubernetes package manager

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/health` | GET | Health check with Elasticsearch status |
| `/population/` | GET, POST | Create a new index |
| `/insert` | GET, POST | Insert a document |
| `/read` | GET, POST | Read a document by ID |
| `/update` | GET, POST | Update a document |
| `/search` | GET, POST | Search documents |
| `/delete_document` | GET, POST | Delete a document |
| `/delete_index` | GET, POST | Delete an index |

## Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/elk-crud.git
cd elk-crud

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export ELASTICSEARCH_HOST=http://localhost:9200
export FLASK_DEBUG=true

# Run the application
python app.py
```

### Using Docker

```bash
# Build the image
docker build -t elk-crud .

# Run the container
docker run -p 5000:5000 -e ELASTICSEARCH_HOST=http://your-es-host:9200 elk-crud
```

### Deploy using Helm Chart

```bash
helm repo add elk-crud-chart https://elasticsearch-chart.dwiananda.click/
helm repo update
helm search repo elk-crud-chart
helm install elk-crud elk-crud-chart/elk-crud-chart
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ELASTICSEARCH_HOST` | `http://localhost:9200` | Elasticsearch server URL |
| `FLASK_DEBUG` | `false` | Enable debug mode |
| `PORT` | `5000` | Application port |

## Infrastructure (AWS)

This application can be deployed on AWS using the following services:

- **Amazon EKS** - Kubernetes cluster for container orchestration
- **Amazon EC2** - Worker nodes for the Kubernetes cluster
- **Amazon VPC** - Network isolation and security
- **Amazon Route 53** - DNS management
- **Amazon ECR** - Container image registry
- **AWS Certificate Manager** - SSL/TLS certificates
- **Application Load Balancer** - Traffic distribution
- **AWS IAM** - Access management

## Project Structure

```
elk-crud/
├── app.py                 # Main Flask application
├── Dockerfile             # Container configuration
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── indexing_population.html
│   ├── insert_population.html
│   ├── read_population.html
│   ├── update_population.html
│   ├── search_population.html
│   ├── delete_document.html
│   └── delete_index.html
└── elk-crud-chart/        # Helm chart
    ├── Chart.yaml
    ├── values.yaml
    └── templates/
```

## References

- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Helm Documentation](https://helm.sh/docs/)
- [Docker Documentation](https://docs.docker.com/)