from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import time


def process_feasibility(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.2, convert_system_message_to_human=True)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Assess feasibility: recruitment timeline, site requirements, budget estimates, potential barriers."),
        ("user", "Sample size: {sample_size}\nDesign: {design}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "sample_size": state["sample_size"],
        "design": state["trial_design"]
    })
    
    state["feasibility_assessment"] = response.content
    time.sleep(0.5)
    return state
