from pymongo import MongoClient
import streamlit as st

@st.cache_resource
def connect_to_client():
    return MongoClient(st.secrets['mongo_uri'])

@st.cache_resource
def connect_to_database():
    client=connect_to_client()
    return client[st.secrets['database']]

@st.cache_resource
def connect_to_collection(collection_name):
    db=connect_to_database()
    return db[collection_name]

def get_personal_info(personal_info_id):
    collection = connect_to_collection('personal_info')
    return collection.find_one({'_id':personal_info_id})

def get_employment_info(employment_info_id):
    collection = connect_to_collection('employment_info')
    return collection.find_one({'_id':employment_info_id})

def get_salary_info(salary_info_id):
    collection = connect_to_collection('salary_info')
    return collection.find_one({'_id':salary_info_id})

def get_government_benefit_info(government_benefit_id):
    collection = connect_to_collection('benefits_government')
    return collection.find_one({'_id':government_benefit_id})