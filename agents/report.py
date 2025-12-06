from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import time


def process_report(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.2, convert_system_message_to_human=True)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Compile structured markdown report with sections: Background, Objectives, Design, Eligibility, Endpoints, Sample Size, Ethics, Feasibility, Limitations."),
        ("user", """Background: {background}
Literature: {literature}
Design: {design}
Eligibility: {eligibility}
Endpoints: {endpoints}
Sample Size: {sample_size}
Ethics: {ethics}
Feasibility: {feasibility}""")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "background": state["background"],
        "literature": state["literature_summary"],
        "design": state["trial_design"],
        "eligibility": state["eligibility_criteria"],
        "endpoints": state["trial_endpoints"],
        "sample_size": state["sample_size"],
        "ethics": state["ethics_considerations"],
        "feasibility": state["feasibility_assessment"]
    })
    
    state["final_report"] = response.content
    time.sleep(0.5)
    return state
