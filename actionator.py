import json

# Global Variables
stats = {}

def addAction(json_string: str) -> str:
    try:
        activity = json.loads(json_string)
    except json.decoder.JSONDecodeError:
        return "ERROR: invalid JSON"

    if "action" in activity and "time" in activity:
        if activity["action"] in stats:
            prev_stat = stats[activity["action"]]
            # Calculate the travelling mean
            new_avg = (prev_stat["avg"] * prev_stat["count"] + activity["time"]) / (prev_stat["count"] + 1)

            stats[activity["action"]]["avg"] = new_avg
            stats[activity["action"]]["count"] += 1
        else:
            stats[activity["action"]] = {"avg": float(activity["time"]), "count": 1}
    else:
        return "ERROR: missing required key"

def getStats() -> str:
    summary = [{"action": action, "avg": stat["avg"]} for action, stat in stats.items()]
    return json.dumps(summary)

def _reset_state():
    '''
    Primarily used for unit testing to ensure a clean state between tests
    '''
    global stats
    stats = {}
