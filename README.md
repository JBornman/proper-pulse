<!-- Logo provided by Tailor Brands -->
<h1 align="center">
  <br>
    <a href="" rel="noopener">
 <img width=300px height=137px src="./documentation/logo.png" alt="Project logo"></a>
  <br>
  <br>
  <b>Proper Pulse</b>
</h1>

<!-- Shields -->
<div align="center">

[![Size](https://img.shields.io/github/repo-size/JBornman/proper-pulse)]()
[![License](https://img.shields.io/badge/license-GPL%20v3-blue.svg)](/LICENSE)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=JBornman_proper-pulse&metric=alert_status&style=flat-square)](https://sonarcloud.io/dashboard?id=JBornman_proper-pulse)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=JBornman_proper-pulse&metric=bugs)](https://sonarcloud.io/dashboard?id=JBornman_proper-pulse)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/nacl115/proper_pulse_service?label=Service%20Container)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/nacl115/proper_pulse_ui?label=UI%20Container)

</div>

<p align="center"> Proper Pulse is an application for logging and tracking your blood pressure.
</p>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About](#about)
- [Containers](#containers)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Running Locally](#running-locally)
  - [Database](#database)
  - [Service](#service)
  - [Front end](#front-end)
- [Local Deployment](#local-deployment)
  - [Running the stack](#running-the-stack)
  - [Shutdown the stack](#shutdown-the-stack)
  - [Cleanup](#cleanup)
- [Remote Deployment](#remote-deployment)
  - [Running the stack](#running-the-stack-1)
- [Using the application](#using-the-application)
  - [Adding more entries](#adding-more-entries)
- [Creating your Certificate](#creating-your-certificate)
- [Acknowledgements](#acknowledgements)

## About
This is a simple application used to store and display blood pressure data. The application consists of a python service that retrieves and stores the data from postgres and an Angular front end that displays the records stored in the database. The design as it stands currently will look like this: 
![Architecture diagram for Proper Pulse](./documentation/Architecture%20diagram.jpeg) 

## Containers
- [Python Container](https://hub.docker.com/r/nacl115/proper_pulse_service)
- [UI Container](https://hub.docker.com/r/nacl115/proper_pulse_ui)

## Getting Started

### Prerequisites

- [pip](https://www.tecmint.com/install-pip-in-linux/)
- [NPM](https://github.com/nodesource/distributions)
- [Python](https://www.python.org/downloads/source/)
- [Angular](https://angular.io/cli)
- [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)
- [docker-compose](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)
- [Postman](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-linux)
- [OpenSSL](https://cloudwafer.com/blog/installing-openssl-on-ubuntu-16-04-18-04/)

## Running Locally

### Database

- open a terminal
- execute the following docker command

```bash
docker run --name postgres \
    -p 5432:5432 \
    -e POSTGRES_DB=postgres \
    -e POSTGRES_PASSWORD=Pr0p3r-Pu1s3 \
    -d postgres
```

### Service

- browse the /service folder
- Open a new terminal window
- Make the script executable

```bash
chmod u+x bootstrap.sh
```

- Execute the script in the background

```bash
./bootstrap.sh &
```

- Create dummy measurement

```bash
    curl -X POST -H 'Content-Type: application/json' -d '{
    "title": "Test measurement",
    "description": "Normal relaxed measurement",
    "systolic" : 130,
    "diastolic" : 87,
    "pulse" : 96
    }' http://0.0.0.0:5000/measurements
```

- Retrieve measurements

```bash
curl http://0.0.0.0:5000/measurements
```

### Front end

- Browse to the /ui/frontend/ folder
- Open a new terminal window
- Install all the packages

```bash
npm install
```

- Run the front end on the default 4200 port

```bash
ng serve
```

- Browse to [localhost:4200](localhost:4200)

## Local Deployment

### Running the stack

Navigate to where the repository was cloned. Open a new terminal. Type the following to quick run the stack locally:

```bash
docker-compose up -d
```

### Shutdown the stack

Navigate to where the repository was cloned. Open a new terminal. Type the following to shutdown the stack we started up:

```bash
docker-compose down
```

### Cleanup

In order to clean-up all the containers and volumes we created that are still there after shutdown run the following command:

```bash
docker system prune
```

## Remote Deployment

### Running the stack

In order to deploy your stack to another machine execute the following command and change the `user` and the `hostmachine` values:

```bash
DOCKER_HOST="ssh://user@hostmachine" docker-compose up -d
```

## Using the application

### Adding more entries
There are two main ways of adding new records
- Curl
```Bash
    curl -X POST -H 'Content-Type: application/json' -d '{
    "title": "Test measurement",
    "description": "Normal relaxed measurement",
    "systolic" : 130,
    "diastolic" : 87,
    "pulse" : 96
    }' http://0.0.0.0:5000/measurements
```
- Postman (using the linked [postman collection](./Proper%20Pulse.postman_collection.json))








## Creating your Certificate
In order to have a working self signed certificate please follow the steps indicated below:
- In your repo create a certs folder as follows:
```bash
mkdir certs
```
- Open the certs folder in a terminal
- Generate your root certificate:
```bash
openssl genrsa -out rootCA.key 4096
```
- Self sign the key we just created: 
```bash
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt
```
- Create a certificate for our front end:
```bash
openssl genrsa -out properpulse.localhost.key 2048
```
- Sign the key we just created:
```bash
openssl req -new -sha256 -key properpulse.localhost.key -out properpulse.localhost.csr
```
- Create the following file `properpulse.localhost.v3.ext` and add the following contents: 
```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = properpulse.localhost
```
- Sign our certificate with the root CA:
```bash
openssl x509 -req -in properpulse.localhost.csr -CA properpulse.localhost.crt -CAkey properpulse.localhost.key -CAcreateserial -out properpulse.localhost.crt -days 1024 -sha256 -extfile properpulse.localhost.v3.ext
```

## Acknowledgements

- Logo provided by Tailor Brands
- Diagram made with lucidchart
