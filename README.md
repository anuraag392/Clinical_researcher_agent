# Autonomous Clinical Trial Designer

> AI-powered workflow automation for comprehensive clinical trial design using Google's Gemini and LangGraph

## Overview

The Autonomous Clinical Trial Designer is an intelligent application that streamlines the complex process of designing clinical trials. By leveraging the power of Google's Gemini AI and LangGraph workflow orchestration, this tool automatically handles multiple critical aspects of trial design—from initial intake and literature review to ethics considerations and feasibility assessments.

Whether you're a researcher, clinician, or pharmaceutical professional, this application transforms a weeks-long manual process into an automated workflow that delivers comprehensive, structured trial designs in minutes.

## 🚀 Live Demo

Try the application now: **[Clinical Researcher Agent](https://clinical-researcher-agent.streamlit.app/)**

## Key Features

- **Multi-Agent Orchestration**: Nine specialized AI agents work sequentially to handle different aspects of trial design
- **Literature-Informed Design**: Automatic synthesis of relevant research to inform trial parameters
- **Statistical Rigor**: Automated sample size calculations and endpoint definitions
- **Ethics & Compliance**: Built-in ethical considerations and regulatory guidance
- **Feasibility Assessment**: Real-world implementation analysis
- **Dual Interface**: Both command-line and web-based Streamlit interface
- **Structured Reports**: Generate comprehensive, well-formatted clinical trial design documents

## How It Works

The application uses a sequential workflow powered by LangGraph, where each agent builds upon the work of the previous one:

1.  **Intake Agent** - Analyzes your request and extracts key requirements
2.  **Literature Agent** - Reviews relevant research and summarizes findings
3.  **Design Agent** - Proposes the overall trial design structure
4.  **Eligibility Agent** - Defines inclusion and exclusion criteria
5.  **Endpoints Agent** - Specifies primary and secondary endpoints
6.  **Sample Size Agent** - Calculates required participant numbers with statistical justification
7.  **Ethics Agent** - Addresses ethical considerations and regulatory requirements
8.  **Feasibility Agent** - Assesses practical implementation challenges
9.  **Report Agent** - Compiles everything into a comprehensive final document

## Try These Examples

Here are some test questions you can try with the application to see its capabilities:

### Cardiology
```
Design a phase 3 trial for evaluating a new beta-blocker in patients with heart failure with reduced ejection fraction
```

### Oncology
```
Create a clinical trial design for a novel immunotherapy targeting PD-L1 in advanced non-small cell lung cancer patients
```

### Neurology
```
Design a study to assess the efficacy of a new monoclonal antibody for preventing migraine attacks in chronic migraine patients
```

### Endocrinology
```
Develop a trial protocol for a once-weekly GLP-1 receptor agonist for weight management in obese adults without diabetes
```

### Infectious Diseases
```
Design a phase 2 trial for a new antiviral drug targeting resistant strains of influenza in hospitalized patients
```

### Rheumatology
```
Create a trial design for evaluating a JAK inhibitor in patients with moderate to severe rheumatoid arthritis who failed methotrexate
```

### Psychiatry
```
Design a clinical trial for a novel antidepressant with rapid onset of action in treatment-resistant major depressive disorder
```

### Medical Devices
```
Develop a trial protocol for a new continuous glucose monitoring device in pediatric type 1 diabetes patients
```

### Rare Diseases
```
Design a study to evaluate gene therapy for Duchenne muscular dystrophy in boys aged 4-7 years
```

### Preventive Medicine
```
Create a trial design for assessing a new vaccine candidate for preventing Lyme disease in endemic areas
```

## Project Architecture

```
autonomous_clinical_trial_designer/
├── app.py                    # Streamlit web interface
├── main.py                   # Command-line interface
├── graph.py                  # LangGraph workflow definition
├── state.py                  # TypedDict state schema
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .env                      # API keys (not in git)
├── .env.example              # Template for .env
├── .gitignore                # Git exclusions
├── .streamlit/
│   └── config.toml           # Streamlit configuration
└── agents/                   # Individual agent functions
    ├── intake.py             # Request analysis
    ├── literature.py         # Literature review
    ├── design.py             # Trial design
    ├── eligibility.py        # Inclusion/exclusion criteria
    ├── endpoints.py          # Primary/secondary endpoints
    ├── samplesize.py         # Statistical calculations
    ├── ethics.py             # Ethical considerations
    ├── feasibility.py        # Implementation assessment
    └── report.py             # Final report generation
```

## Technical Stack

-   **LangChain**: LLM application framework
-   **LangGraph**: Workflow orchestration and state management
-   **Google Gemini**: Large language model for text generation
-   **Streamlit**: Web interface framework
-   **Python 3.8+**: Core programming language

## Example Use Cases

1.  **Pharmaceutical Research**: Design trials for new drug candidates
2.  **Medical Device Testing**: Structure studies for device efficacy and safety
3.  **Academic Research**: Create trial protocols for investigator-initiated studies
4.  **Regulatory Submissions**: Generate structured trial designs for regulatory review
5.  **Feasibility Studies**: Quickly evaluate multiple trial design options

## Limitations & Considerations

-   AI-generated designs should be reviewed by qualified clinical research professionals
-   The tool provides a structured framework but does not replace expert medical judgment
-   Regulatory requirements vary by country and therapeutic area—consult local guidelines
-   API costs apply based on Gemini usage (see Google's pricing)

## Contributing

This is a personal project by Anuraag Das. If you'd like to suggest improvements or report issues, feel free to reach out.

## License

Copyright © 2025 Anuraag Das. All rights reserved.

## Support

For questions, issues, or feedback, please contact the developer.

---

**Built by Anuraag Das**
