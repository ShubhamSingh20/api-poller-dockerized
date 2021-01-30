# TechStax assignemnt

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# Installation

**NOTE**
create a `.env` file and add the variables present in `env.example` which will be used by the application

### 1. Clone repo
    git clone https://github.com/ShubhamSingh20/techstax-assignment.git

### 2. Docker build
    docker build . -t worker:latest

### 3. Docker compose workers and beat
    docker-compose up -d 
    
### 4. Scale the number of readers (consumers)
    docker-compose up -d --scale worker=3




