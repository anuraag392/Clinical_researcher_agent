import streamlit as st
import os
from dotenv import load_dotenv
from graph import create_graph
from state import TrialState

load_dotenv()

st.set_page_config(
    page_title="Autonomous Clinical Trial Designer",
    layout="wide"
)

st.title("Autonomous Clinical Trial Designer")
st.markdown("Design comprehensive clinical trials using AI-powered workflow automation")

if not os.getenv("GOOGLE_API_KEY"):
    st.error("GOOGLE_API_KEY not found. Please add it to your .env file.")
    st.stop()

with st.sidebar:
    st.header("About")
    st.info("""
    This application uses LangGraph to orchestrate multiple AI agents that collaboratively design clinical trials.
    
    **Workflow:**
    1. Intake
    2. Literature Review
    3. Trial Design
    4. Eligibility Criteria
    5. Endpoints
    6. Sample Size
    7. Ethics
    8. Feasibility
    9. Final Report
    """)

query = st.text_area(
    "Enter your clinical trial request:",
    placeholder="Example: Design a phase 3 trial for evaluating a new diabetes drug targeting HbA1c reduction in type 2 diabetes patients",
    height=150
)

if st.button("Generate Trial Design", type="primary", use_container_width=True):
    if not query.strip():
        st.warning("Please enter a clinical trial request.")
    else:
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
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        agents = [
            "Intake Analysis",
            "Literature Review",
            "Trial Design",
            "Eligibility Criteria",
            "Endpoints Definition",
            "Sample Size Calculation",
            "Ethics Considerations",
            "Feasibility Assessment",
            "Final Report Generation"
        ]
        
        with st.spinner("Processing your request..."):
            graph = create_graph()
            
            for i, agent in enumerate(agents):
                progress = (i + 1) / len(agents)
                progress_bar.progress(progress)
                status_text.text(f"⚙️ {agent}...")
            
            final_state = graph.invoke(initial_state)
            
            progress_bar.progress(1.0)
            status_text.text("✅ Complete!")
        
        st.success("Clinical trial design generated successfully!")
        
        st.markdown("---")
        st.markdown("## 📋 Clinical Trial Design Report")
        
        st.markdown(final_state["final_report"])
        
        with st.expander("🔍 View Detailed Agent Outputs"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Background")
                st.write(final_state["background"])
                
                st.subheader("Literature Summary")
                st.write(final_state["literature_summary"])
                
                st.subheader("Trial Design")
                st.write(final_state["trial_design"])
                
                st.subheader("Eligibility Criteria")
                st.write(final_state["eligibility_criteria"])
            
            with col2:
                st.subheader("Endpoints")
                st.write(final_state["trial_endpoints"])
                
                st.subheader("Sample Size")
                st.write(final_state["sample_size"])
                
                st.subheader("Ethics Considerations")
                st.write(final_state["ethics_considerations"])
                
                st.subheader("Feasibility Assessment")
                st.write(final_state["feasibility_assessment"])

st.markdown("---")
st.markdown("*Copyrighted by Anuraag Das*")
