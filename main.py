import sys
import os
from dotenv import load_dotenv
from graph import create_graph
from state import TrialState

load_dotenv()


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py '<clinical trial query>'")
        sys.exit(1)
    
    query = sys.argv[1]
    
    initial_state: TrialState = {
        "query": query,
        "background": None,
        "literature_summary": None,
        "trial_design": None,
        "eligibility_criteria": None,
        "trial_endpoints": None,
        "sample_size": None,
        "ethics_considerations": None,
        "feasibility_assessment": None,
        "final_report": None
    }
    
    graph = create_graph()
    final_state = graph.invoke(initial_state)
    
    print("\n" + "="*80)
    print("CLINICAL TRIAL DESIGN REPORT")
    print("="*80 + "\n")
    print(final_state["final_report"])


if __name__ == "__main__":
    main()
