import json
from threading import Lock

stats = {}
lock = Lock()


def addAction(json_string: str) -> str:
    global stats, lock
    try:
        activity = json.loads(json_string)
    except json.decoder.JSONDecodeError:
        return "ERROR: invalid JSON"

    if "action" in activity and "time" in activity:
        action = activity["action"]
        with lock:
            if action in stats:
                prev_stat = stats[action]
                stats[action]['avg'] = (prev_stat['avg'] * prev_stat['count']
                                        + activity['time']) / (prev_stat['count'] + 1)
                stats[action]["count"] = prev_stat["count"] + 1
            else:
                stats[action] = {"avg": float(activity["time"]), "count": 1}
    else:
        return "ERROR: missing required key"


def getStats() -> str:
    global stats, lock
    with lock:
        summary = [{"action": action, "avg": round(stat["avg"], 2)}
                    for action, stat in stats.items()]
    return json.dumps(summary)


def _reset_state():
    '''
    Primarily used for unit testing to ensure a clean state between tests
    '''
    global stats
    stats = {}
