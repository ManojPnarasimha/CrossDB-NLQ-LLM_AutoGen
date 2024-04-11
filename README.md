# Autogen Group Chat Application

This application demonstrates how to use the `autogen` library to create a group chat system that interacts with multiple databases using SQLDatabaseChain. The system is designed to query product information, sales transactions, and product reviews from separate databases.

## Features

- **Multi-database Querying**: The application can query product information, sales transactions, and product reviews from separate databases.
- **Agent-based Interaction**: Utilizes `autogen` agents to manage interactions with the databases and process user queries.
- **Automatic Conversation Stopping**: Implements a custom logic to stop the conversation after a specified number of rounds.

## Prerequisites

- Python 3.6 or higher
- PostgreSQL databases for product information, sales transactions, and product reviews
- An Azure OpenAI account with access to the GPT-4 model

## Setup

0. **environment variable** Copy .env.local to .env and replace with your secret values

1. **Environment Variables**: Create a `.env` file in the root directory of your project. Add your Azure OpenAI API key and any other necessary environment variables.

    ```
    AZURE_OPENAI_KEY=your_azure_openai_key_here
    ```

2. **Database Configuration**: Ensure your PostgreSQL databases are set up and accessible. Update the database URIs in `database_config.py` with your database connection details.

3. **Install Dependencies**: Install the required Python packages.

    ```
    pip install -r requirements.txt
    ```

4. **Run the Application**: Execute `main.py` to start the group chat application.

    ```
    python main.py
    ```

## Usage

The application initiates a group chat with a user proxy and three agents: `ProductInfoAgent`, `ProductSalesAgent`, and `ProductReviewsAgent`. Each agent is capable of querying its respective database.

The conversation is automatically stopped after 20 rounds to prevent excessive processing.

## Customization

- **Database Queries**: Modify the `query_db1`, `query_db2`, and `query_db3` functions in `database_config.py` to customize the queries executed against each database.
- **Agent Descriptions**: Update the descriptions and system messages in `agent_config.py` to better reflect the capabilities and behavior of each agent.
- **Conversation Limit**: Adjust the `max_rounds` variable in `main.py` to change the maximum number of rounds before the conversation is automatically stopped.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to improve the application.
