import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from duckduckgo_search import DDGS
import os

# Set Google Gemini API Key (Replace with your actual key)
os.environ["GOOGLE_API_KEY"] = "AIzaSyBwCjIbg7VFJss14VNtGq5PaPeB70NA4W4" # I know that i have uploaded this on github 

# Initialize Language Model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7, google_api_key=os.getenv("GOOGLE_API_KEY"))

# Wikipedia Tool
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# Web Search Tool
def search_duckduckgo(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    return "\n".join([res["body"] for res in results]) if results else "No results found."

search_tool = Tool(name="Web Search", func=search_duckduckgo, description="Search the web for latest information.")

# Initialize LangChain Agent
agent = initialize_agent(
    tools=[wikipedia, search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def generate_blog(topic, focus):
    """Generates a well-structured blog post using LangChain Agent."""
    research_data = agent.run(f"Research about {topic} with a focus on {focus} and summarize key points.")
    
    prompt = f"""
    Write a well-structured blog on '{topic}' with the main focus on '{focus}', including the following sections:
    
    # {topic}
    
    ## Introduction
    Provide an engaging introduction that aligns with the main focus.
    
    ## Content
    Present detailed and informative content with research-based support, emphasizing {focus}.
    
    ## Summary
    Summarize the main points with insights into {focus}.
    
    Use this research data:
    {research_data}
    """
    
    blog_content = llm.invoke(prompt)
    return blog_content.content.strip()

# Streamlit UI
st.title("AI Blog Generator")
topic = st.text_input("Enter Blog Topic:")
focus = st.text_input("Enter Main Focus of the Blog:")
if st.button("Generate Blog") and topic and focus:
    with st.spinner("Generating Blog..."):
        blog = generate_blog(topic, focus)
    st.markdown("## Generated Blog")
    st.markdown(blog)
