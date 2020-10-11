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

[![Size](https://img.shields.io/github/repo-size/JBornman/proper-pulse?style=flat-square)]() 
[![License](https://img.shields.io/badge/license-GPL%20v3-blue.svg?style=flat-square)](/LICENSE)

</div>

<p align="center"> Proper Pulse is an application for logging and tracking your blood pressure.
    <br> 
Completed for a Kartoza technical assessment.
</p>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Running Locally](#running-locally)
  - [Database](#database)
  - [Service](#service)
- [Deployment](#deployment)
- [Built Using](#built-using)
- [Acknowledgements](#acknowledgements)

## About 


## Getting Started 


### Prerequisites


## Running Locally

### Database
- open a terminal
- execute the following docker command
```bash
docker run --name online-pulse-db \
    -p 5432:5432 \
    -e POSTGRES_DB=postgres \
    -e POSTGRES_PASSWORD=Pr0p3r-Pu1s3 \
    -d postgres
```

### Service
- cd into the 'service' folder
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




## Deployment 


## Built Using 

- [Docker](https://www.docker.com/) - Orchestration Tool
- [Python](https://www.python.org/) - Service
- [Angular](https://angular.io/) - UI

## Acknowledgements 

- Logo provided by Tailor Brands
