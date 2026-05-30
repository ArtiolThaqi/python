import streamlit as st
import requests
import pandas as pd

st.title("Project Managment App")

st.header("Add a Developer")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Developer Experience(Years)",min_value=0,max_value=50,value=0)

if st.button("Create Developer"):
    dev_data = {"name":dev_name,"experience":dev_experience}
    response = requests.post("http://localhost:8501/developers/",data=dev_data)
    st.json(response.json())

st.header("Add a Project")
proj_title = st.text_input("Project Title")
proj_description = st.text_area("Project Description")
proj_langs = st.text_input("Language Used(Comma Seperated)")
lead_dev_name = st.text_input("Lead Developer Name")
lead_dev_exp = st.number_input("Lead Developer Experience(Years)",min_value=0,max_value=50,value=0)

if st.button("Create Project"):
    lead_dev_data = {"name":lead_dev_name,"experience":lead_dev_exp}
    proj_data = {"title":proj_title,"description":proj_description,"languages":proj_langs,"lead_developer":lead_dev_data}

    response = requests.post("http://localhost:8501/projects/", json=proj_data)
    st.json(response.json())

st.header("Project Dashboard")

if st.button("Get Projects"):
    response = requests.get("http://localhost:8501/projects/")
    projects_data = response.json()['projects']

   if projects_data:
       projects_df = pd.DataFrame(projects_data)
       st.subheader("Project Dashboard")
       for project in projects_data:
           st.markdown(projects_data[project]['title'],unsafe_allow_html=True)
           st.markdown(projects_data[project]['description'],unsafe_allow_html=True)
           st.markdown(projects_data[project]['languages'],unsafe_allow_html=True)
           st.markdown(projects_data[project]['lead_developer'],unsafe_allow_html=True)
           st.markdown(projects_data[project]['experience'],unsafe_allow_html=True)
       else:
           st.warning("No Project Found")

