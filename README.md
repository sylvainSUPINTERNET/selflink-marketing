# Setup 

```` bash

conda create --name selflink python=3.11

conda activate selflink

pip install -e .

python ./src/main.py
 
````

# neo4j setup 


```` bash

docker run --restart always --publish=7474:7474 --publish=7687:7687 --env NEO4J_AUTH=none --volume=E:\selflink-db:/data neo4j:5.12.0

# Go to http://localhost:7474/browser/

````