from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import time


def process_ethics(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.2, convert_system_message_to_human=True)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Address ethical considerations: informed consent, risk-benefit, vulnerable populations, data protection."),
        ("user", "Design: {design}\nEligibility: {eligibility}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "design": state["trial_design"],
        "eligibility": state["eligibility_criteria"]
    })
    
    state["ethics_considerations"] = response.content
    time.sleep(0.5)
    return state
