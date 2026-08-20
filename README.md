
# CAP 931 – AI Sales Assistant

## Project Overview

This project is a multi-agent AI Sales Assistant prototype created for CAP 931.

The application helps a sales representative research a prospective company, understand company strategy, identify competitors, review leadership information, and generate a concise sales account brief.

The application uses Python, LangChain, Groq, Streamlit, and public web data.

---

## Project Objective

The goal of this project is to build a Sales Assistant Agent that can:

- Collect sales information from a user
- Research a prospective company
- Analyze company strategy and technology needs
- Identify competitor information
- Identify leadership information
- Generate potential sales opportunities
- Produce a final one-page sales account brief
- Provide source URLs used during research

---

## Technologies Used

- Python 3.12
- uv
- LangChain
- LangChain Groq
- Groq API
- Streamlit
- BeautifulSoup
- Requests
- python-dotenv
- Pydantic

---

## Project Architecture

The application uses a multi-agent workflow.

User Input  
↓  
Web Research Tool  
↓  
Sales Agent  
↓  
Research Agent  
↓  
Analysis Agent  
↓  
Report Agent  
↓  
Final Sales Account Brief

### Sales Agent

The Sales Agent receives the user's sales information and organizes the opportunity.

It processes:

- Product name
- Company URL
- Product category
- Competitors
- Value proposition
- Target customer
- Optional product overview

### Research Agent

The Research Agent receives the Sales Agent output and public website information.

It identifies relevant information about:

- Company strategy
- Technology strategy
- Competitors
- Leadership
- Products and services
- Company news
- Technology indicators
- Potential sales opportunities

### Analysis Agent

The Analysis Agent evaluates the research and identifies:

- Company strategy
- Technology strategy
- Competitor activity
- Leadership information
- Business needs
- Sales opportunities
- Risks and missing information

### Report Agent

The Report Agent combines the analysis into a concise sales account brief.

The report includes:

- Company Strategy
- Technology Strategy
- Competitor Mentions
- Leadership Information
- Business Needs
- Sales Opportunity
- Recommended Next Steps
- Sources

---

## Web Research

The application can read multiple public webpages.

The user provides a primary company URL and may also provide additional research URLs such as:

- Company homepage
- Investor relations page
- News or press release page
- Leadership page
- Careers page

The web research tool extracts readable text from these pages and sends the information to the Research Agent.

---

## Streamlit Interface

The Streamlit interface allows users to enter:

- Product Name
- Company URL
- Product Category
- Competitors
- Value Proposition
- Target Customer
- Additional Research URLs
- Optional Product Overview

The user clicks **Generate Sales Brief** to start the workflow.

---

## Installation

Clone or download the project.

Navigate to the project directory:

```powershell
cd C:\Users\kasin\Documents\capstone_sales_agent
## Time Management

I divided the project into four major phases:

- Environment setup and dependency configuration: 20%
- Agent development and prompt engineering: 35%
- Web research and Streamlit integration: 30%
- Testing, debugging, documentation, and GitHub submission: 15%

More time was allocated to agent development and integration because the multi-agent workflow was the core functionality of the project.


## Prompt Experiments

During development, I refined the prompts used by each agent.

Initial prompts produced broad and generic responses.

The prompts were improved by:

- Assigning each agent a specific role
- Providing structured input fields
- Specifying required output sections
- Adding instructions not to invent facts
- Providing public website content as context
- Passing source URLs through the workflow
- Separating research, analysis, and report generation

The final multi-agent approach produced more structured and relevant sales insights than using a single general prompt.


## Production Deployment Plan

For production deployment, the application could be containerized and hosted on a cloud platform.

Production considerations include:

- Store API keys in a secure secrets manager
- Add user authentication and authorization
- Validate URLs and uploaded files
- Add logging and monitoring
- Handle API failures and rate limits
- Cache web research where appropriate
- Add automated testing
- Use HTTPS
- Monitor LLM cost and token usage
- Scale application instances based on demand
- Regularly review prompts and model performance