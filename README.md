# Scheduling-partner

An Application to be used by HR manager to schedule interviews and view them. This is a variant from the main project where i implemented an nginx container to serve as a reverse proxy and a loadbalancer for multiple backend service replicas. For now this runs locally as a Docker app.<br />

## Requirements: <br />

 -Docker (version 20.10.22) <br />
 -Docker Compose (version v2.15.1)<br />
 
## How to run:<br />
Clone the repository and navigate to the folder<br />
run "docker-compose up -d --scale api=<no of backend containers>"<br />
 
## Build-time - 5 mins approx<br />

Frontend - Angular<br />
Backend - Flask(live reload enabled)<br />
Database - MongoDB<br />

All three components run as a docker app(multi-container)

![alt text](https://github.com/Scheduling-Squad/Scheduling-partner/blob/main/snipping%20tool.PNG)

