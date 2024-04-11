from autogen import AssistantAgent

def setup_agents(llm_config):
    db1_agent = AssistantAgent(
        name="ProductInfoAgent",
        llm_config=llm_config,
        description="Queries the ProductInfo database for product details, categories, and inventory.",
        system_message="This agent retrieves product details, categories, and inventory information. If the complete answer isn't found here, it will inform Agent2 (sales transactions) to search for related information using the product ID."
    )

    db2_agent = AssistantAgent(
        name="ProductSalesAgent",
        llm_config=llm_config,
        description="Queries the ProductSales database for sales transactions and customer information.",
        system_message="This agent retrieves sales transactions and customer information. If product information is provided in the user query, it will search for matching IDs in the sales data."
    )

    db3_agent = AssistantAgent(
        name="ProductReviewsAgent",
        llm_config=llm_config,
        description="Queries the ProductReviews database for product reviews and related information.",
        system_message="This agent retrieves product reviews and related information. If necessary, it collaborates with other agents to provide comprehensive answers."
    )

    return db1_agent, db2_agent, db3_agent
