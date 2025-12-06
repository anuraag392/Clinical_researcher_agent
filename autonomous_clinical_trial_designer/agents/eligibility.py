from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate


def process_eligibility(state):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Define inclusion and exclusion criteria for participant eligibility. Be specific and evidence-based."),
        ("user", "Trial design: {design}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"design": state["trial_design"]})
    
    state["eligibility_criteria"] = response.content
    return state
