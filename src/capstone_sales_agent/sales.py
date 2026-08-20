from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env
load_dotenv()

# Connect to the Groq model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# Create the Sales Agent prompt
sales_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a Sales Intake Agent.

        Your job is to understand the sales opportunity
        from the information provided by the user.

        Do not research the company yet.
        Do not invent facts.

        Organize the information clearly so another
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

        Return the following:

        1. Product
        2. Prospect Company
        3. Product Category
        4. Competitors
        5. Value Proposition
        6. Target Customer
        7. Important Research Questions
        """
    )
])

# Create the LangChain chain
sales_chain = sales_prompt | model | StrOutputParser()


def run_sales_agent(data):
    """Run the Sales Intake Agent."""
    return sales_chain.invoke(data)