import os
import sys
import io
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process

# Force UTF-8 encoding for Windows terminal safety
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def run_war_room(topic):
    load_dotenv()
    
    # Extract your 3 separate keys
    k1 = os.getenv("GEMINI_KEY_1")
    k2 = os.getenv("GEMINI_KEY_2")
    k3 = os.getenv("GEMINI_KEY_3")

    # Satisfy the library's internal check by setting a global key temporarily
    if k1:
        os.environ["GOOGLE_API_KEY"] = k1

    # CONFIGURE FOR GEMINI 2.5 FLASH
    # Spreading the load across 3 keys to prevent the 429 error
    llm_perf = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=k1)
    llm_safe = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=k2)
    llm_arch = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=k3)

    # Agent 1: Performance Specialist
    performance_agent = Agent(
        role='Performance Specialist',
        goal=f'Optimize {topic} for speed using Gemini 2.5 capabilities.',
        backstory='Expert in low-latency systems and high-tier model optimizations.',
        llm=llm_perf,
        verbose=False
    )

    # Agent 2: Security Analyst
    security_agent = Agent(
        role='Security Lead',
        goal=f'Conduct risk assessment for {topic}.',
        backstory='Expert in cybersecurity and technical debt.',
        llm=llm_safe,
        verbose=False
    )

    # Agent 3: Architecture Lead
    architecture_agent = Agent(
        role='Architecture Lead',
        goal=f'Design the structural blueprint for {topic}.',
        backstory='Expert in scalable system design.',
        llm=llm_arch,
        verbose=False
    )

    # Tasks
    t1 = Task(description=f'3 speed fixes for {topic}', agent=performance_agent, expected_output='List')
    t2 = Task(description=f'2 security risks for {topic}', agent=security_agent, expected_output='Summary')
    t3 = Task(description=f'Folder structure for {topic}', agent=architecture_agent, expected_output='Blueprint')

    # Orchestration
    crew = Crew(
        agents=[performance_agent, security_agent, architecture_agent],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        max_rpm=1, # Conservative to stay within quota during demo
        verbose=False
    )

    return crew.kickoff()