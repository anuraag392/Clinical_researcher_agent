from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import time


def process_literature(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.2, convert_system_message_to_human=True)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Summarize relevant literature and prior trials for this clinical problem. Focus on evidence gaps."),
        ("user", "Background: {background}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"background": state["background"]})
    
    state["literature_summary"] = response.content
    time.sleep(0.5)
    return state
