from pydantic import BaseModel, Field

class Employee(BaseModel):
    _oid: str
    first_name: str
    last_name: str
    position: str
    target_utilization: float


class WorkMonth(BaseModel):
    _oid: str
    working_month: str
    employee_id: str
    team: str
    vacation_days: float
    sick_days: float
    calendar_work_days: int
    holidays: int
    target_working_time_in_days: float
    actual_working_time_in_days: float
    target_utilization_in_hours: float
    target_utilization_in_hours_per_day: float
    actual_working_time_in_hours: int