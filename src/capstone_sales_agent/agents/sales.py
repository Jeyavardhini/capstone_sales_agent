from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from the .env file
load_dotenv()

# Connect to the Groq AI model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# Create the prompt for the Sales Agent
sales_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a Sales Intake Agent.

        Your job is to understand the sales opportunity
        from the information provided by the user.

        Do not research the company yet.
        Do not invent facts.

        Organize the information clearly so that another
        research agent can use it.
        """
    ),
    (
        "human",
        """
        Product Name: {product_name}

        Company URL: {company_url}

        Product Category: {product_category}

        Competitors: {competitors}

        Value Proposition: {value_proposition}

        Target Customer: {target_customer} 
        Product Overview Document:
        {product_document}

        Return the following:

        1. Product
        2. Prospect Company
        3. Product Category
        4. Competitors
        5. Value Proposition
        6. Target Customer
        7. Important product Details from the uploaded document
        8. Important Research Questions

        If no product document was provided, state:
        "No product overview document provided." 
        """
    )
    
])

# Connect the prompt, AI model, and output parser
sales_chain = sales_prompt | model | StrOutputParser()


# Function used by workflow.py
def run_sales_agent(data):
    return sales_chain.invoke(data)
