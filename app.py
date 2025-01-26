# # Graded Assignment 2

# from fastapi import FastAPI, HTTPException, Request
# from typing import List, Dict, Union
# import time
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Simulate a database
# items: List[Dict[str, Union[int, float, str]]] = []

# @app.get("/")
# async def root():
#     return {"message": "Hello!"}

# @app.get("/items")
# async def get_items():
#     return items

# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     item = next((i for i in items if i["id"] == item_id), None)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item

# @app.post("/items")
# async def create_item(item: Dict[str, Union[str, float]]):  # Corrected type hinting
#     new_item = {"id": len(items) + 1, **item}
#     items.append(new_item)
#     return new_item

# @app.middleware("http")
# async def log_process_time(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )








from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json  # For custom formatting

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"],  # Allow all headers
)

# Global variable to hold student data
students = []

# Load data from the CSV file
def load_data(filename: str):
    global students
    try:
        with open(filename, mode="r") as file:
            csv_reader = csv.DictReader(file)
            # Convert CSV rows to a list of dictionaries
            students = [{"studentId": int(row["studentId"]), "class": row["class"]} for row in csv_reader]
    except Exception as e:
        print(f"Error loading data from {filename}: {e}")
        students = []

# Load the CSV file into memory
load_data("./q-fastapiGA2.csv")  # Update with the correct file path

@app.get("/api")
async def get_students(class_filter: Optional[List[str]] = Query(None)):
    """
    Endpoint to retrieve student data.
    - If no query parameter is provided, return all students.
    - If class query parameters are provided, filter students by class.
    """
    if not students:
        raise HTTPException(status_code=500, detail="Student data not loaded.")
    
    if class_filter:
        # Filter students by the provided class query parameter(s)
        filtered_students = [student for student in students if student["class"] in class_filter]
    else:
        filtered_students = students

    # Format response with pretty indentation using jsonable_encoder
    response_content = jsonable_encoder({"students": filtered_students})
    
    # Convert the response to a JSON string with pretty indentation
    json_response = json.dumps(response_content, indent=4)
    
    return JSONResponse(content=json_response)
