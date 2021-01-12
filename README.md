# CMP API Kubernetes test
## Description

Is a simple REST API. This API code  run in a Kubernetes cluster.

Is build with Python 3.9 and Sanic.

## How to use it

PreRequisits:

 * Python 3.9, Pytest, Requests
 * Create the new k8s namespace (kubectl create ns cmpapi)

 Commands:
```
- make build: : Build and push the image.

- make deploy : Deploy the app on your kubernetes cluster.

- make destroy : Destroy the app on your kubernetes cluster.

- make test : Run functional tests to check that the API is working.
```

## API Specification
``` 
GET /user/{id} - Retrieves a specific user

GET /allusers - Show all the users on the DB

POST /user - Creates a new user

DELETE /user/{id} - Deletes a specific user
``` 
Includes a Postman collection.

## Pipeline
For the pipeline i will use the typical GitFlow:
* Normal Braches: Will launch a new build & deploy & test on testing k8s clusters.
* Master Branch: Will launch a new build & deploy & test on staging/preproduction k8s clusters.
* Tags: Will launch a new build & deploy & test on production k8s clusters.
For CI/CD we can use Gitlab + Runners or Jenkins

## How to imporve it and move it to production
* Use a persistent DB: MySQL,Aurora,Postgre...
* On the K8s Cluster, deploy multiple replicas with horitzontal and vertical autoscaling.
* Use a nice ALB in front of the application.
* Access logs: it should be get from the ALB and saved to S3 with intelligent tiering, and then analize it with Athena if are needed.
* Application logs: deploying the Cloudwatch agent on the cluster and then with fluentbit put all the data to cloudwatch is the best practice, is not the most cheap but then we are able to easily setup alarms, and query the logs with container insights, you can do the same with prometheus but is harder to manage, a study case is needed.

