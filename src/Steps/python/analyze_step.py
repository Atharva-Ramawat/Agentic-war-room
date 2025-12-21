import sys
import os
import io

# Setup Paths so it finds the war_room folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

# Force UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.war_room.crew import run_war_room

config = {
    "name": "AnalyzeStep",
    "type": "event",
    "subscribes": ["analyze-request"],
    "emits": ["analyze-result"],
    "flows": ["ai-war-room-flow"]
}

def handler(event, context):
    # Marker for sidebar
    open("I_AM_WORKING.txt", "w").write("Python handler active!")

    data = event.get("data", {})
    text = data.get("text", "No headline provided")
    request_id = data.get("requestId", "unknown")
    
    # Run the crew logic with Gemini 2.5 Flash
    result = run_war_room(text)
    
    # Save the output file
    with open("HACKATHON_FINAL_OUTPUT.txt", "w", encoding="utf-8") as f:
        f.write(f"--- AI WAR ROOM REPORT (GEMINI 2.5 FLASH) ---\n")
        f.write(f"Request ID: {request_id}\n")
        f.write(f"Topic: {text}\n")
        f.write("-" * 30 + "\n")
        f.write(str(result))
    
    return {
        "topic": "analyze-result",
        "data": {
            "requestId": request_id,
            "result": str(result)
        }
    }