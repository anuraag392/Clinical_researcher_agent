from langgraph.graph import StateGraph, END
from state import TrialState
from agents.intake import process_intake
from agents.literature import process_literature
from agents.design import process_design
from agents.eligibility import process_eligibility
from agents.endpoints import process_endpoints
from agents.samplesize import process_samplesize
from agents.ethics import process_ethics
from agents.feasibility import process_feasibility
from agents.report import process_report


def create_graph():
    workflow = StateGraph(TrialState)
    
    workflow.add_node("intake", process_intake)
    workflow.add_node("literature", process_literature)
    workflow.add_node("design", process_design)
    workflow.add_node("eligibility", process_eligibility)
    workflow.add_node("endpoints", process_endpoints)
    workflow.add_node("samplesize", process_samplesize)
    workflow.add_node("ethics", process_ethics)
    workflow.add_node("feasibility", process_feasibility)
    workflow.add_node("report", process_report)
    
    workflow.set_entry_point("intake")
    workflow.add_edge("intake", "literature")
    workflow.add_edge("literature", "design")
    workflow.add_edge("design", "eligibility")
    workflow.add_edge("eligibility", "endpoints")
    workflow.add_edge("endpoints", "samplesize")
    workflow.add_edge("samplesize", "ethics")
    workflow.add_edge("ethics", "feasibility")
    workflow.add_edge("feasibility", "report")
    workflow.add_edge("report", END)
    
    return workflow.compile()
