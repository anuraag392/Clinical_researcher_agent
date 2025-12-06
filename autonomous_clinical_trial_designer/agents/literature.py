from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate


def process_literature(state):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Summarize relevant literature and prior trials for this clinical problem. Focus on evidence gaps."),
        ("user", "Background: {background}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"background": state["background"]})
    
    state["literature_summary"] = response.content
    return state
