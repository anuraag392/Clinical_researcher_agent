from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate


def process_intake(state):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract the clinical problem and background from the user query. Output concise background context."),
        ("user", "{query}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]})
    
    state["background"] = response.content
    return state
