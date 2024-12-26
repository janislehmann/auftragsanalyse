
def individual_serial(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "surname": employee["surname"],
        "team": employee["team"],
        "position": employee["position"]

    }

def list_serial(employees) -> list:
    return [individual_serial(employee) for employee in employees]