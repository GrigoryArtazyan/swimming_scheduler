import json
from pathlib import Path

def load_workout_qa(json_path="data/swim_workout_prompts.json"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [f"Q: {item['prompt']}\nA: {item['response']}" for item in data]
