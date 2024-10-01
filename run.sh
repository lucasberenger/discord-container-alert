#! /bin/bash

# Loop to create and then delete containers
for i in `seq 5`; do docker run -d nginx; done; docker stop `docker ps -q`