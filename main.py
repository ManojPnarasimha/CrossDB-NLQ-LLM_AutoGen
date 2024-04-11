import os
from dotenv import load_dotenv
from database_config import initialize_databases, setup_database_chains, setup_azure_llm
from agent_config import setup_agents
from autogen import GroupChat, GroupChatManager, UserProxyAgent

load_dotenv()

# Initialize the databases
db1, db2, db3 = initialize_databases()

# Setup the Azure LLM
azure_llm = setup_azure_llm()

# Setup the database chains
db1_chain, db2_chain, db3_chain = setup_database_chains(azure_llm, db1, db2, db3)

# Define functions for database operations using the chains
def query_db1(query):
    return db1_chain.invoke(query)

def query_db2(query):
    return db2_chain.invoke(query)

def query_db3(query):
    return db3_chain.invoke(query)

# Setup the agents
config_list = [
    {
        "model": "gpt-4",
        "api_key": os.getenv("AZURE_OPENAI_KEY"),
        "azure_endpoint": "https://applied-ai-gpt-4.openai.azure.com/",
        "api_type": "azure",
        "api_version": "2023-12-01-preview"
    }
]

llm_config = {
    "model": "gpt-4",
    "config_list": config_list,
    "seed": 42,
    "functions": [
        {
            "name": "query_db1",
            "description": "Queries the ProductInfo database for product details, categories, and inventory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query to execute on the ProductInfo database"
                    }
                },
                "required": ["query"]
            }
        },
        {
            "name": "query_db2",
            "description": "Queries the ProductSales database for sales transactions and customer information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query to execute on the ProductSales database"
                    }
                },
                "required": ["query"]
            }
        },
        {
            "name": "query_db3",
            "description": "Queries the ProductReviews database for product reviews and related information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query to execute on the ProductReviews database"
                    }
                },
                "required": ["query"]
            }
        }
    ]
}

db1_agent, db2_agent, db3_agent = setup_agents(llm_config)

# Register the functions with the agents
db1_agent.register_function(
    function_map={
        "query_db1": query_db1,
    }
)

db2_agent.register_function(
    function_map={
        "query_db2": query_db2,
    }
)

db3_agent.register_function(
    function_map={
        "query_db3": query_db3,
    }
)

# Create the group chat with the user proxy and the new agents
user_proxy = UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 2,
        "work_dir": "groupchat",
        "use_docker": False,
    },
    human_input_mode="TERMINATE",
)

groupchat = GroupChat(agents=[user_proxy, db1_agent, db2_agent, db3_agent], messages=[], max_round=20)
manager = GroupChatManager(groupchat=groupchat)

# Initiate the chat
user_proxy.initiate_chat(manager, message="List the products which are comes under the price range 500 and has highest rating?")
