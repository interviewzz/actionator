import json

def addAction(json_string: str) -> str:
    try:
        action = json.loads(json_string)
    except json.decoder.JSONDecodeError:
        return "ERROR: invalid JSON"

    if "action" in action and "time" in action:
        pass
    else:
        return "ERROR: missing required key"

def getStats():
    pass
