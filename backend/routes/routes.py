from fastapi import APIRouter
from models.employee import Employee
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()

@router.get("/employees")
async def get_all_employees():
    employees = list_serial(collection_name.find())
    return employees

@router.get("/employees/{id}")
async def get_employee(id: str):
    employee = individual_serial(collection_name.find_one({"_id": ObjectId(id)}))
    return employee

@router.post("/employees")
async def post_employee(employee: Employee):
    collection_name.insert_one(dict(employee))

@router.put("/employees/{id}")
async def put_employee(id: str, employee: Employee):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(employee)})

@router.delete("/employees/{id}")
async def delete_employee(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})