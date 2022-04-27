# README

Our flask server connects the frontend with the Neo4j database.
The code takes reference from a template at https://github.com/neo4j-examples/neo4j-movies-template.
We just amended the Python/Flask backend at `/flask-api` from the template.
It includes both the Heroku deployable version and the development version that can be run at localhost. 

There are only some differences in their config files, so we separated them into two versions. Here are the files that each version has to use:  
- Heroku deployable version: `Procfile_heroku`, `requirements_heroku.txt`, `runtime.txt`
- Development version: `Procfile`, `requirements.txt`
 
## The Model

### Nodes

* `Document`
* `User`

### Relationships

* `(:User)-[:FAVOURITE]->(:Document)`


## Flask API

You can try to run with the developement version that can easily run on localhost.
From this subfolder:

```
cd flask-api
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=app.py
flask run
```



