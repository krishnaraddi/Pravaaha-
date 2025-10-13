from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI
from agents.triage_agent import classify_ticket
from agents.technician_assistant import generate_resolution_suggestion
from agents.time_tracker import log_time
from agents.efficiency_analyzer import update_dashboard

llm = OpenAI(temperature=0)

tools = [
    Tool(name="ClassifyTicket", func=classify_ticket, description="Classify and route ticket"),
    Tool(name="SuggestResolution", func=generate_resolution_suggestion, description="Suggest fix steps"),
    Tool(name="LogTime", func=log_time, description="Log technician time"),
    Tool(name="UpdateDashboard", func=update_dashboard, description="Update KPI dashboard"),
]

agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")
