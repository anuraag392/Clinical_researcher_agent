from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import time


def process_samplesize(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.2, convert_system_message_to_human=True)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Calculate sample size with power analysis. Include effect size, alpha, beta, and dropout assumptions."),
        ("user", "Endpoints: {endpoints}\nDesign: {design}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "endpoints": state["trial_endpoints"],
        "design": state["trial_design"]
    })
    
    state["sample_size"] = response.content
    time.sleep(0.5)
    return state
