# README

Our flask server connects the frontend with the Neo4j database.
The code takes reference from a template at https://github.com/neo4j-examples/neo4j-movies-template.
We just amended the Python/Flask backend at `/flask-api` from the template.
It includes both the Heroku Deployable version and the development version that can be run at localhost.  
Feel encouraged to fork and update this repo!

## The Model

### Nodes

* `Document`
* `User`

### Relationships

* `(:User)-[:FAVOURITE]->(:Document)`


## Flask API

First, configure your `flask-api/.env` file to point to your database. 

Then, from the root directory of this project:

```
cd flask-api
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=app.py
flask run
```



