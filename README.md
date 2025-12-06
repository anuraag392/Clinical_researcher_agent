# Autonomous Clinical Trial Designer

LangChain + LangGraph project for designing clinical trials using Gemini AI.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure API key:
   - Copy `.env.example` to `.env`
   - Add your Gemini API key to `.env`:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

## Usage

### Command Line Interface

```bash
python main.py "Design a trial for evaluating a new diabetes drug"
```

### Web Interface (Streamlit)

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add `GOOGLE_API_KEY` to Streamlit secrets
5. Deploy!

### Local Deployment

```bash
streamlit run app.py --server.port 8501
```

## Workflow

intake → literature → design → eligibility → endpoints → sample size → ethics → feasibility → report → END

## Project Structure

```
autonomous_clinical_trial_designer/
├── app.py               
├── main.py              
├── graph.py             
├── state.py             
├── requirements.txt     
├── README.md            
├── .env                 
├── .env.example         
├── .gitignore           
├── .streamlit/
│   └── config.toml      
└── agents/
    ├── intake.py        
    ├── literature.py    
    ├── design.py        
    ├── eligibility.py   
    ├── endpoints.py     
    ├── samplesize.py    
    ├── ethics.py        
    ├── feasibility.py   
    └── report.py        
```
