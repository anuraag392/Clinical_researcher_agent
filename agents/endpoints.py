from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import time


def process_endpoints(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.2, convert_system_message_to_human=True)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Define primary and secondary endpoints. Include measurement methods and timepoints."),
        ("user", "Trial design: {design}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"design": state["trial_design"]})
    
    state["trial_endpoints"] = response.content
    time.sleep(0.5)
    return state
