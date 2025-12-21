# main.py
import sys
from dotenv import load_dotenv 
load_dotenv()   

from src.war_room.crew import WarRoomCrew
             

def run():
    print("## WELCOME TO THE AGENTIC WAR ROOM ##")
    print("-------------------------------------")
    headline = input("Enter a News Headline to simulate: ")
    
    inputs = {
        'headline': headline
    }
    
    # Kickoff the debate!
    WarRoomCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()