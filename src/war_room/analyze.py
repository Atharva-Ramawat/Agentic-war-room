import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process

# 1. Load the environment variables
load_dotenv()

# 2. Explicitly define the Gemini 2.5 Flash model
# This prevents CrewAI from looking for an OPENAI_API_KEY
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Use the stable name for the 2.x series
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

def analyze(topic):
    # 3. Assign the LLM to every Agent
    performance_optimizer = Agent(
        role='Performance Specialist',
        goal=f'Optimize {topic} for speed',
        backstory='Expert in low-latency systems.',
        llm=llm, # CRITICAL: You must pass the llm here
        allow_delegation=False
    )

    security_analyst = Agent(
        role='Security Analyst',
        goal=f'Secure {topic}',
        backstory='Expert in cybersecurity and stability.',
        llm=llm, # CRITICAL: You must pass the llm here
        allow_delegation=False
    )

    # 4. Define Tasks as before
    task1 = Task(description=f'Analyze {topic} speed.', agent=performance_optimizer, expected_output='3 points')
    task2 = Task(description=f'Analyze {topic} safety.', agent=security_analyst, expected_output='3 points')



        # In src/war_room/analyze.py
# Update these in src/war_room/analyze.py
    crew = Crew(
    agents=[performance_optimizer, security_analyst],
    tasks=[task1, task2],
    process=Process.sequential,
    max_rpm=1,  # Lowered to 1 to be extremely safe
    verbose=False # <--- CHANGE THIS TO FALSE
)

    return crew.kickoff()

