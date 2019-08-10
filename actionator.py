import json
from threading import Lock

stats = {}
lock = Lock()


def addAction(json_string: str) -> str:
    """
    Accepts a serialized json string containing an action and time
    ex. {"action":"jump", "time":100}

    The action is used to compute a running average time of all actions stored
    in the stats global dictionary. This method will be called concurrently so
    ensure that any reads/writes of the global stats variable utilize the global
    lock.

    This function will return an informative error message as a string otherwise
    it will return None.
    """
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
    """
    Returns a serialized json array of the average time of each action that has
    been added to the global stats object via addAction.

    This method will be called concurrently so make sure to utilize the global lock
    """
    global stats, lock
    with lock:
        summary = [{"action": action, "avg": round(stat["avg"], 2)}
                    for action, stat in stats.items()]
    return json.dumps(summary)


def _reset_state():
    """
    Primarily used for unit testing to ensure a clean state between tests
    """
    global stats
    stats = {}
