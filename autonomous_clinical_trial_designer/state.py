from typing import TypedDict, Optional


class TrialState(TypedDict):
    query: str
    background: Optional[str]
    literature_summary: Optional[str]
    trial_design: Optional[str]
    eligibility_criteria: Optional[str]
    trial_endpoints: Optional[str]
    sample_size: Optional[str]
    ethics_considerations: Optional[str]
    feasibility_assessment: Optional[str]
    final_report: Optional[str]
