from fastapi import FastAPI
from model import Developer, Projects
app = FastAPI()

@app.post("/developers/")  #post shton ne aplikacion
def create_developer(developer: Developer):
    return {"message":"Developer created","developer":developer}

@app.post("/projects/")  #post shton ne aplikacion
def create_project(project: Projects):
    return {"message":"Projects created","project":project}

@app.get("/projects/")   #get me i shfaq prej app me i lexu
def get_projects():
    sample_project = Projects
    title = "Sample Project"
    description = "This is a Sample description"
    language = ["Python","JavaScript","C++"]
    lead_developer = Developer(name="John Doe",experience=5)

    return {"projects":[sample_project]}
