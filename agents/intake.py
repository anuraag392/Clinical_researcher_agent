from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import time


def process_intake(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.2, convert_system_message_to_human=True)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract the clinical problem and background from the user query. Output concise background context."),
        ("user", "{query}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]})
    
    state["background"] = response.content
    time.sleep(0.5)
    return state
