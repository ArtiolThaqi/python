from fastapi import FastAPI
from models import Project,Developer

app = FastAPI()
@app.post('/developer')
def create_developer(developer: Developer):
    return {"message:":"Developer created","developer":developer}

@app.post("/project")
def create_project(project: Project):
    return {"message:":"Project created","project":project}

@app.get('/project')
def get_projects():
    developer=Developer(name="Artiol",experience=2)
    sample_project=Project(title="HR Management system", description="This is a sample project",
                           languages=["Python","Jvascript","SQL"],lead_developer=developer)

    return {"projects":[sample_project]}

