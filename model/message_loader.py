import json

def load_default_messages():
    with open("messages.json", "r", encoding="utf-8") as f:
        return json.load(f)
