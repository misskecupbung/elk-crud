# Simple Python CRUD Application with Elasticsearch as a database

This repo contains simple code using python programming language that able to create, read, update, and delete populations of specific city that using several Amazon Web Service (AWS) stacks.

### Components
- Python
- Flask
- Elasticsearch
- Docker

### Endpoints

- http://elasticsearch.dwiananda.click:5000/health : GET health status
- http://elasticsearch.dwiananda.click:5000/population/: GET populations for population_city index
- http://elasticsearch.dwiananda.click:5000/population/: PUT -> input the index name and the document type
- http://elasticsearch.dwiananda.click:5000/insert/: PUT -> input some data in an index and document type.
- http://elasticsearch.dwiananda.click:5000/read/: GET: retrieve the information stored of a specific id in index.
- http://elasticsearch.dwiananda.click:5000/update/: UPDATE: change the information of a specific id in an index
- http://elasticsearch.dwiananda.click:5000/delete_index/: DELETE -> delete an existing document
- http://elasticsearch.dwiananda.click:5000/delete_document/: delete an existing document


### Deploy using Helm Chart
```bash
helm repo add elk-crud-chart https://elasticsearch-chart.dwiananda.click/
helm repo list
helm search repo elk-crud-chart
helm install elk-crud-chart/elk-crud-chart --generate-name
```

### Infrastructure Stacks
- **Amazon EC2 (Elastic Compute Cloud)**
  <br> This service is for the worker node of the Kubernetes cluster. 
- **Amazon VPC (Virtual Private Cloud)**
  <br> Networking service for most of all resources.
- **Amazon Route 53**
  <br> This service is for managing the DNS server including its record. 
- **Amazon ECR (Elastic Container Registry)**
  <br> This service is to store  images.
- **AWS Certificate Manager (ACM)**
  <br> This service is for provision manage certificates of applications
- **ELB using Application Load Balancer (ALB)**
  <br> This service is a load balancer for the application deployed on Amazon EKS
- **AWS IAM (Identity and Access Management)**
  <br> This service is for configuring and managing access between the resources (e.g: access push the image from EC2 to Amazon ECR)
- **GitHub & GitHub Actions**

#### TODOs
- Migrate to microservices applications (e.g using Amazon EKS)

### References

- https://opster.com/guides/elasticsearch/glossary/elasticsearch-index/
- https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html
- https://www.linuxcapable.com/how-to-install-elasticsearch-8-on-ubuntu-22-04-lts/
- https://www.elastic.co/guide/en/cloud/current/ec-api-deployment-crud.html
- https://medium.com/geekculture/crud-operations-in-elasticsearch-1b5ff37bfb40
- https://www.elastic.co/guide/en/elasticsearch/client/net-api/current/examples.html
- https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
- https://medium.com/geekculture/how-to-dockerize-a-python-flask-app-cf98df24775d
