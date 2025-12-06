from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate


def process_design(state):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Propose trial design: type (RCT, observational, etc), phases, arms, blinding, duration, and intervention details."),
        ("user", "Background: {background}\nLiterature: {literature}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "background": state["background"],
        "literature": state["literature_summary"]
    })
    
    state["trial_design"] = response.content
    return state
