from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_design(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Design a clinical trial following ICH E6 GCP and SPIRIT guidelines. Specify:
        
        **Trial Type & Phase**: RCT/Observational/Single-arm | Phase I/II/III/IV with justification
        **Study Design**: Parallel/Crossover/Factorial design with rationale
        **Randomization**: Method (block/stratified/adaptive), allocation concealment
        **Blinding**: Open-label/Single/Double/Triple-blind with masking procedures  
        **Treatment Arms**: Detailed description of each arm with dosing regimens
        **Study Duration**: Screening, treatment, follow-up periods with visit schedule
        **Intervention Details**: Drug formulation, administration route, dose escalation if applicable
        **Rescue Medications**: Permitted concomitant therapies
        **Discontinuation Criteria**: Individual and trial-level stopping rules
        
        Provide scientific rationale for each design element based on literature review."""),
        ("user", "Background: {background}\nLiterature: {literature}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "background": state["background"],
        "literature": state["literature_summary"]
    })
    
    state["trial_design"] = response.content
    time.sleep(0.5)
    return state

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_eligibility(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Define comprehensive eligibility criteria following CONSORT standards:
        
        **Inclusion Criteria**:
        - Demographic requirements (age, sex, race/ethnicity if applicable)
        - Disease-specific criteria (diagnosis, staging, biomarkers)
        - Prior treatment requirements or restrictions
        - Baseline performance status (ECOG/Karnofsky)
        - Organ function requirements (lab parameters with specific ranges)
        - Contraception requirements for WOCBP/men
        
        **Exclusion Criteria**:
        - Concurrent medical conditions that may interfere
        - Prior/concurrent medications (washout periods)
        - Laboratory abnormalities (with specific cutoffs)
        - Pregnancy/breastfeeding
        - Known hypersensitivity
        - Legal/administrative issues
        
        For each criterion, provide scientific rationale and operational definitions. Ensure criteria are measurable, objective, and protect participant safety while maximizing generalizability."""),
        ("user", "Trial design: {design}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"design": state["trial_design"]})
    
    state["eligibility_criteria"] = response.content
    time.sleep(0.5)
    return state

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_endpoints(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Define trial endpoints following CONSORT and FDA guidance:
        
        **Primary Endpoint**: 
        - Precise definition with measurement scale/units
        - Measurement method and instruments (validated scales if applicable)
        - Timepoint(s) for assessment (specific weeks/months)
        - Clinical relevance and regulatory acceptability
        - Sensitivity to detect treatment effect
        
        **Secondary Endpoints** (ranked by importance):
        - Each with definition, measurement, timepoint
        - Include patient-reported outcomes (PROs) if applicable
        - Health economics endpoints (QALYs, healthcare utilization)
        - Biomarker/pharmacokinetic endpoints if relevant
        
        **Exploratory Endpoints**:
        - Hypothesis-generating analyses
        - Subgroup analyses (pre-specified)
        
        **Safety Endpoints**:
        - Adverse events (CTCAE grading)
        - Laboratory monitoring schedule
        - Vital signs, ECG, imaging as appropriate
        
        Specify data collection forms, central adjudication if needed, and missing data handling."""),
        ("user", "Trial design: {design}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"design": state["trial_design"]})
    
    state["trial_endpoints"] = response.content
    time.sleep(0.5)
    return state

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_ethics(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Address ethical and regulatory considerations following ICH E6 GCP and Declaration of Helsinki:
        
        **Informed Consent**:
        - ICF development process (reading level, language translation)
        - Key elements to be disclosed (risks, benefits, alternatives)
        - Process for obtaining and documenting consent
        - Assent procedures for minors/legally incapable persons
        - Re-consent triggers if protocol amended
        
        **Risk-Benefit Assessment**:
        - Known and anticipated risks (physical, psychological, social)
        - Potential benefits to subjects and society
        - Risk mitigation strategies
        - Data Safety Monitoring Board (DSMB) charter if applicable
        
        **Vulnerable Populations**:
        - Special protections for children, pregnant women, prisoners, etc.
        - Additional safeguards and justification for inclusion
        
        **Data Protection & Privacy**:
        - Personal data handling per GDPR/HIPAA
        - Data anonymization and security measures
        - Subject privacy protections
        - Data retention and destruction plan
        
        **Regulatory Approvals**:
        - IRB/EC approval requirements
        - Regulatory authority notifications (FDA IND, EudraCT, etc.)
        - Clinical trial registration (ClinicalTrials.gov)
        
        **Subject Rights**:
        - Right to withdraw without penalty
        - Access to trial results
        - Compensation for trial-related injury
        
        Provide comprehensive ethical justification for all aspects of the trial."""),
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

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_feasibility(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Assess operational feasibility with detailed planning:
        
        **Recruitment Feasibility**:
        - Patient population prevalence and accessibility
        - Screening-to-enrollment ratio estimate
        - Recruitment timeline (month-by-month enrollment projection)
        - Site selection criteria and geographic distribution
        - Investigator experience requirements
        - Recruitment strategies (physician referral, advertising, patient registries)
        
        **Site Requirements**:
        - Number and type of sites needed (academic medical centers, community hospitals)
        - Specialized equipment/facilities required
        - Staff requirements (sub-investigators, coordinators, pharmacists)
        - Site start-up timeline
        
        **Timeline (GANTT-style)**:
        - Protocol development and regulatory approval: X months
        - Site initiation: X months  
        - Patient recruitment: X months
        - Treatment period: X months
        - Follow-up: X months
        - Data analysis and reporting: X months
        - Total study duration: X months/years
        
        **Budget Considerations**:
        - Per-patient costs (procedures, lab tests, imaging)
        - Site overhead (IRB fees, pharmacy, monitoring)
        - Central costs (CRO, data management, biostatistics)
        - Regulatory costs (IND maintenance, safety reporting)
        - Estimated total budget range
        
        **Potential Barriers**:
        - Scientific/technical challenges
        - Regulatory hurdles
        - Competitive trials
        - Supply chain considerations
        
        **Mitigation Strategies**:
        - For each identified barrier, propose specific mitigation approach
        
        Provide realistic assessment with contingency planning."""),
        ("user", "Sample size: {sample_size}\nDesign: {design}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "sample_size": state["sample_size"],
        "design": state["trial_design"]
    })
    
    state["feasibility_assessment"] = response.content
    time.sleep(0.5)
    return state

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_intake(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Extract and structure the clinical problem using the PICO framework:
        P (Population): Target patient population with specific characteristics
        I (Intervention): Proposed treatment/intervention being studied
        C (Comparison): Control or comparator treatment
        O (Outcome): Expected outcomes and benefits
        
        Provide comprehensive background context including disease epidemiology, current treatment landscape, and unmet medical needs."""),
        ("user", "{query}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]})
    
    state["background"] = response.content
    time.sleep(0.5)
    return state

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_literature(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Conduct a systematic literature review focusing on:
        1. Prior clinical trials addressing similar hypotheses (Phase I-IV)
        2. Meta-analyses and systematic reviews of existing evidence
        3. Evidence gaps and unmet medical needs
        4. Safety and efficacy data from comparable interventions
        5. Real-world evidence and post-marketing surveillance data
        
        Cite quality of evidence (high/moderate/low) and provide evidence-based recommendations for trial design."""),
        ("user", "Background: {background}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"background": state["background"]})
    
    state["literature_summary"] = response.content
    time.sleep(0.5)
    return state

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_report(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Generate a comprehensive clinical trial protocol following ICH E6 GCP and SPIRIT 2013 guidelines. Structure as:
        
        # CLINICAL TRIAL PROTOCOL
        
        ## 1. PROTOCOL SUMMARY
        - Protocol title
        - Protocol number and version
        - Study phase
        - Brief synopsis (150-200 words)
        
        ## 2. BACKGROUND AND RATIONALE
        - Disease background and epidemiology
        - Current treatment landscape
        - Unmet medical need
        - Rationale for proposed intervention
        - Evidence from literature review
        - Risk-benefit assessment
        
        ## 3. STUDY OBJECTIVES
        
        ### 3.1 Primary Objective
        - Single, clear primary objective
        
        ### 3.2 Secondary Objectives  
        - Ranked list of secondary objectives
        
        ### 3.3 Exploratory Objectives
        - Hypothesis-generating objectives
        
        ## 4. STUDY DESIGN
        
        ### 4.1 Overall Design
        - Study type and phase with scientific justification
        - Schematic diagram description
        
        ### 4.2 Randomization and Blinding
        - Randomization method and ratio
        - Stratification factors
        - Blinding procedures
        - Unblinding procedures (emergency/planned)
        
        ### 4.3 Study Duration and Visits
        - Screening period
        - Treatment period
        - Follow-up period
        - Visit schedule with study day/week
        
        ### 4.4 Treatment Arms
        - Detailed description of each arm
        - Dosing regimen and administration
        - Permitted concomitant medications
        - Prohibited medications
        
        ## 5. STUDY POPULATION
        
        ### 5.1 Inclusion Criteria
        - Numbered list with rationale
        
        ### 5.2 Exclusion Criteria
        - Numbered list with rationale
        
        ### 5.3 Subject Withdrawal Criteria
        - Individual withdrawal criteria
        - Trial stopping rules
        
        ## 6. STUDY ENDPOINTS
        
        ### 6.1 Primary Endpoint
        - Definition, measurement method, timepoint
        - Clinical relevance
        
        ### 6.2 Secondary Endpoints
        - Each endpoint with definition, measurement, timepoint
        
        ### 6.3 Safety Endpoints
        - Adverse event monitoring
        - Laboratory/vital signs monitoring schedule
        
        ## 7. STATISTICAL CONSIDERATIONS
        
        ### 7.1 Sample Size Calculation
        - Statistical test
        - Effect size with justification
        - Power, alpha level
        - Dropout assumption
        - Final sample size per arm and total
        
        ### 7.2 Statistical Analyses
        - Primary analysis method
        - Secondary analyses
        - Handling of missing data
        - Interim analyses (if applicable)
        - Subgroup analyses (pre-specified)
        
        ## 8. ETHICS AND REGULATORY
        
        ### 8.1 Ethical Conduct
        - GCP compliance statement
        - Declaration of Helsinki compliance
        
        ### 8.2 Informed Consent
        - Consent process
        - Key elements to be disclosed
        
        ### 8.3 Regulatory Approvals
        - IRB/EC requirements
        - Regulatory notifications
        - Trial registration
        
        ### 8.4 Data Protection
        - Subject confidentiality measures
        - Data handling per GDPR/HIPAA
        
        ### 8.5 Safety Monitoring
        - Adverse event reporting
        - DSMB oversight (if applicable)
        
        ## 9. STUDY CONDUCT AND FEASIBILITY
        
        ### 9.1 Site Selection
        - Number and type of sites
        - Site requirements
        
        ### 9.2 Recruitment Strategy
        - Patient identification methods
        - Screening approach
        - Enrollment timeline
        
        ### 9.3 Study Timeline
        - Protocol finalization: Month X
        - Regulatory approvals: Month Y
        - Site initiation: Month Z
        - First patient enrolled: Month A
        - Last patient enrolled: Month B
        - Last patient complete: Month C
        - Final analysis: Month D
        - Total duration: X months/years
        
        ### 9.4 Budget Overview
        - Estimated per-patient costs
        - Total budget range
        
        ### 9.5 Risk Assessment and Mitigation
        - Identified feasibility risks
        - Mitigation strategies
        
        ## 10. STUDY LIMITATIONS
        - Acknowledged limitations of study design
        - Generalizability considerations
        - Potential confounding factors
        
        ## 11. REFERENCES
        - Key literature supporting the protocol
        
        ---
        
        Format the protocol in clean, professional markdown with clear section numbering. Use tables where appropriate for visit schedules or endpoint definitions. Ensure all sections flow logically and are comprehensive yet concise."""),
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

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import time


def process_samplesize(state):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Calculate sample size with comprehensive statistical justification:
        
        **Primary Analysis**:
        - Statistical test to be used (t-test, log-rank, chi-square, etc.)
        - Effect size: Specify minimum clinically important difference (MCID)
          * Absolute or relative difference
          * Justification based on literature or clinical significance
        - Variability estimate: Standard deviation, event rate, hazard ratio
        - Type I error (alpha): typically 0.05 (one-sided/two-sided)
        - Power (1-beta): typically 80% or 90%
        - Sample size calculation formula and result
        
        **Adjustments**:
        - Dropout/attrition rate (with justification from literature)
        - Interim analyses (alpha spending function if applicable)
        - Multiplicity adjustments for multiple comparisons
        - Stratification factors if applicable
        
        **Subgroup Analyses**:
        - Pre-specified subgroups and required sample sizes
        - Interaction tests planned
        
        **Recruitment**:
        - Per-site enrollment capacity
        - Number of sites required
        - Screening failure rate estimate
        - Total subjects to be screened
        
        Provide the final target sample size per arm and total, with clear rationale for all assumptions."""),
        ("user", "Endpoints: {endpoints}\nDesign: {design}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "endpoints": state["trial_endpoints"],
        "design": state["trial_design"]
    })
    
    state["sample_size"] = response.content
    time.sleep(0.5)
    return state

