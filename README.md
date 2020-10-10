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
  - [Service](#service)
- [Deployment](#deployment)
- [Built Using](#built-using)
- [Acknowledgements](#acknowledgements)

## About 


## Getting Started 


### Prerequisites


## Running Locally

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
    "title": "TypeScript Advanced Exam",
    "description": "Tricky questions about TypeScript."
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
