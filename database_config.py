from langchain_community.utilities.sql_database import SQLDatabase
from langchain_experimental.sql.base import SQLDatabaseChain
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
import os

load_dotenv()

def initialize_databases():
    db1_uri = "postgresql+psycopg2://postgres:admin%40123@localhost:5432/productinfo"
    db2_uri = "postgresql+psycopg2://postgres:admin%40123@localhost:5432/productsales"
    db3_uri = "postgresql+psycopg2://postgres:admin%40123@localhost:5432/productreviews"

    db1 = SQLDatabase.from_uri(db1_uri)
    db2 = SQLDatabase.from_uri(db2_uri)
    db3 = SQLDatabase.from_uri(db3_uri)

    return db1, db2, db3

def setup_database_chains(llm, db1, db2, db3):
    db1_chain = SQLDatabaseChain(llm=llm, database=db1, verbose=True)
    db2_chain = SQLDatabaseChain(llm=llm, database=db2, verbose=True)
    db3_chain = SQLDatabaseChain(llm=llm, database=db3, verbose=True)

    return db1_chain, db2_chain, db3_chain

def setup_azure_llm():
    azure_llm = AzureChatOpenAI(
        azure_endpoint="https://applied-ai-gpt-4.openai.azure.com/",
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2024-02-15-preview",
        deployment_name="gpt-4",
    )
    return azure_llm
