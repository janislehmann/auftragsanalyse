from fastapi import APIRouter
from models.models import Employee, WorkMonth
from config.database import coll_employees, coll_work_month, coll_orders
from schema.schemas import list_employee_serial, individual_employee_serial, list_work_month_serial, individual_work_month_serial
from bson import ObjectId

router = APIRouter()

# Mitarbeiter
@router.get("/employees")
async def read_all_employees()  -> list[Employee]:
    employees = list_employee_serial(coll_employees.find())
    return employees

@router.get("/employees/{id}")
async def read_employee(id: str) -> Employee:
    employee = individual_employee_serial(coll_employees.find_one({"_id": ObjectId(id)}))
    print(employee)
    return employee

@router.post("/employees")
async def create_employee(employee: Employee):
    coll_employees.insert_one(dict(employee))

@router.put("/employees/{id}")
async def update_employee(id: str, employee: Employee):
    coll_employees.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(employee)})

@router.delete("/employees/{id}")
async def delete_employee(id: str):
    coll_employees.find_one_and_delete({"_id": ObjectId(id)})


# Work months
@router.get("/work_months")
async def read_all_work_months() -> list[WorkMonth]:
    work_months = list_work_month_serial(coll_work_month.find())
    return work_months

@router.get("/work_months/{month}")
async def read_work_month(month: str) -> WorkMonth:
    data_month = individual_work_month_serial(coll_work_month.find_one({"working_month": month}))
    return data_month



# Orders