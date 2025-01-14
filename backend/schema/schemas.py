def individual_work_month_serial(work_month) -> dict:
    return {
        "id": str(work_month["_id"]),
        "working_month": work_month["working_month"],
        "employee_id": str(work_month["emoloyee_id"]),
        "team": work_month["team"],
        "vacation_days": work_month["vacation_days"],
        "sick_days": work_month["sick_days"],
        "calendar_work_days": work_month["calendar_work_days"],
        "holidays": work_month["holidays"],
        "target_working_time_in_days": work_month["target_working_time_in_days"],
        "actual_working_time_in_days": work_month["actual_working_time_in_days"],
        "target_utilization_in_hours": work_month["target_utilization_in_hours"],
        "target_utilization_in_hours_per_day": work_month["target_utilization_in_hours_per_day"],
        "actual_working_time_in_hours": work_month["actual_working_time_in_hours"],
    }


def list_work_month_serial(work_months):
    return [individual_work_month_serial(work_month) for work_month in work_months]

def individual_employee_serial(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "first_name": employee["first_name"],
        "last_name": employee["last_name"],
        "position": employee["position"],
        "target_utilization": employee["target_utilization"]
    }

def list_employee_serial(employees) -> list:
    return [individual_employee_serial(employee) for employee in employees]