# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# import re

# app = FastAPI()

# # Allow all origins for CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

# # Pre-defined functions (for simulation)
# def get_ticket_status(ticket_id: int):
#     return {"status": f"Ticket {ticket_id} is being processed."}

# def schedule_meeting(date: str, time: str, meeting_room: str):
#     return {"message": f"Meeting scheduled for {date} at {time} in {meeting_room}."}

# def get_expense_balance(employee_id: int):
#     return {"balance": f"Employee {employee_id} has an expense balance of $1000."}

# def calculate_performance_bonus(employee_id: int, current_year: int):
#     return {"bonus": f"Employee {employee_id} will receive a bonus for {current_year}."}

# def report_office_issue(issue_code: int, department: str):
#     return {"report": f"Issue {issue_code} reported to {department} department."}

# # Function to extract parameters from query and map to a function call
# def parse_query(query: str):
#     # Define regex patterns for each type of query
#     ticket_pattern = r"status of ticket (\d+)"
#     meeting_pattern = r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)"
#     expense_pattern = r"expense balance for employee (\d+)"
#     bonus_pattern = r"performance bonus for employee (\d+) for (\d{4})"
#     issue_pattern = r"office issue (\d+) for the (\w+) department"

#     # Check for ticket status query
#     match_ticket = re.search(ticket_pattern, query)
#     if match_ticket:
#         return {"name": "get_ticket_status", "arguments": {"ticket_id": int(match_ticket.group(1))}}

#     # Check for meeting schedule query
#     match_meeting = re.search(meeting_pattern, query)
#     if match_meeting:
#         return {"name": "schedule_meeting", "arguments": {
#             "date": match_meeting.group(1),
#             "time": match_meeting.group(2),
#             "meeting_room": match_meeting.group(3)
#         }}

#     # Check for expense balance query
#     match_expense = re.search(expense_pattern, query)
#     if match_expense:
#         return {"name": "get_expense_balance", "arguments": {"employee_id": int(match_expense.group(1))}}

#     # Check for performance bonus query
#     match_bonus = re.search(bonus_pattern, query)
#     if match_bonus:
#         return {"name": "calculate_performance_bonus", "arguments": {
#             "employee_id": int(match_bonus.group(1)),
#             "current_year": int(match_bonus.group(2))
#         }}

#     # Check for office issue report query
#     match_issue = re.search(issue_pattern, query)
#     if match_issue:
#         return {"name": "report_office_issue", "arguments": {
#             "issue_code": int(match_issue.group(1)),
#             "department": match_issue.group(2)
#         }}

#     # If no match, return an error
#     return {"error": "Unable to parse the query."}

# @app.get("/execute")
# async def execute_query(q: str):
#     result = parse_query(q)
#     return JSONResponse(content=result)





# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# import re
# import json

# app = FastAPI()

# # Allow all origins for CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Function to extract parameters from query and map to a function call
# def parse_query(query: str):
#     # Define regex patterns for each type of query
#     patterns = [
#         (r"status of ticket (\d+)", "get_ticket_status", ["ticket_id"]),
#         (r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)", "schedule_meeting", ["date", "time", "meeting_room"]),
#         (r"expense balance for employee (\d+)", "get_expense_balance", ["employee_id"]),
#         (r"performance bonus for employee (\d+) for (\d{4})", "calculate_performance_bonus", ["employee_id", "current_year"]),
#         (r"office issue (\d+) for the (\w+) department", "report_office_issue", ["issue_code", "department"])
#     ]
    
#     for pattern, func_name, param_names in patterns:
#         match = re.search(pattern, query, re.IGNORECASE)
#         if match:
#             params = {param_names[i]: int(match.group(i+1)) if param_names[i].isdigit() else match.group(i+1) for i in range(len(param_names))}
#             return {"name": func_name, "arguments": json.dumps(params, sort_keys=False)}
    
#     return {"error": "Unable to parse the query."}

# @app.get("/execute")
# async def execute_query(q: str = None):
#     if not q:
#         return JSONResponse(content={"message": "No query provided."})
    
#     queries = q.split(";")  # Handle multiple queries
#     results = [parse_query(query.strip()) for query in queries]
    
#     return JSONResponse(content={"results": results})






# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# import re
# import json

# app = FastAPI()

# # Allow all origins for CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Define available functions
# AVAILABLE_FUNCTIONS = [
#     {"name": "get_ticket_status", "arguments": "{\"ticket_id\": 83742}"},
#     {"name": "schedule_meeting", "arguments": "{\"date\": \"2024-02-10\", \"time\": \"14:00\", \"meeting_room\": \"Room A\"}"},
#     {"name": "get_expense_balance", "arguments": "{\"employee_id\": 12345}"},
#     {"name": "calculate_performance_bonus", "arguments": "{\"employee_id\": 56789, \"current_year\": 2024}"},
#     {"name": "report_office_issue", "arguments": "{\"issue_code\": 9012, \"department\": \"IT\"}"}
# ]

# # Function to extract parameters from query and map to a function call
# def parse_query(query: str):
#     patterns = [
#         (r"status of ticket (\d+)", "get_ticket_status", ["ticket_id"]),
#         (r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)", "schedule_meeting", ["date", "time", "meeting_room"]),
#         (r"expense balance for employee (\d+)", "get_expense_balance", ["employee_id"]),
#         (r"performance bonus for employee (\d+) for (\d{4})", "calculate_performance_bonus", ["employee_id", "current_year"]),
#         (r"office issue (\d+) for the (\w+) department", "report_office_issue", ["issue_code", "department"])
#     ]

#     for pattern, func_name, param_names in patterns:
#         match = re.search(pattern, query, re.IGNORECASE)
#         if match:
#             params = {param_names[i]: match.group(i + 1) for i in range(len(param_names))}
#             return {"name": func_name, "arguments": json.dumps(params, sort_keys=False)}

#     return {"error": "Unable to parse the query."}

# @app.get("/execute")
# async def execute_query(q: str = None):
#     if not q:
#         # Return all available functions when no query is provided
#         return JSONResponse(content={"results": AVAILABLE_FUNCTIONS})

#     queries = q.split(";")  # Handle multiple queries
#     results = [parse_query(query.strip()) for query in queries]
#     return JSONResponse(content={"results": results})







from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Pre-defined functions (simulated)
def get_ticket_status(ticket_id: int):
    """Gets the status of a ticket."""
    return {"ticket_id": ticket_id}

def schedule_meeting(date: str, time: str, meeting_room: str):
    """Schedules a meeting."""
    return {"date": date, "time": time, "meeting_room": meeting_room}

def get_expense_balance(employee_id: int):
    """Gets the expense balance for an employee."""
    return {"employee_id": employee_id}

def calculate_performance_bonus(employee_id: int, current_year: int):
    """Calculates the performance bonus for an employee."""
    return {"employee_id": employee_id, "current_year": current_year}

def report_office_issue(issue_code: int, department: str):
    """Reports an office issue."""
    return {"issue_code": issue_code, "department": department}

@app.get("/execute")
async def execute_query(q: str):
    """
    Analyzes the query and routes it to the appropriate function.
    Returns a JSON response with the function name and arguments.
    """

    try:
        if "What is the status of ticket" in q:
            match = re.search(r"ticket (\d+)", q, re.IGNORECASE)
            if match:
                ticket_id = int(match.group(1))
                return {"name": "get_ticket_status", "arguments": f'{{"ticket_id": {ticket_id}}}'}
            else:
                raise HTTPException(status_code=400, detail="Invalid ticket query.")

        elif "Schedule a meeting on" in q:
            match = re.search(r"on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in Room (\w+)", q, re.IGNORECASE)
            if match:
                date = match.group(1)
                time = match.group(2)
                meeting_room = match.group(3)
                return {"name": "schedule_meeting", "arguments": f'{{"date": "{date}", "time": "{time}", "meeting_room": "{meeting_room}"}}'}
            else:
                raise HTTPException(status_code=400, detail="Invalid meeting schedule query.")

        elif "Show my expense balance for employee" in q:
            match = re.search(r"employee (\d+)", q, re.IGNORECASE)
            if match:
                employee_id = int(match.group(1))
                return {"name": "get_expense_balance", "arguments": f'{{"employee_id": {employee_id}}}'}
            else:
                raise HTTPException(status_code=400, detail="Invalid expense balance query.")

        elif "performance bonus" in q.lower(): # Modified regex to find performance bonus
            match = re.search(r"employee (\d+) performance bonus (\d{4})", q, re.IGNORECASE)
            if match:
                employee_id = int(match.group(1))
                current_year = int(match.group(2))
                return {"name": "calculate_performance_bonus", "arguments": f'{{"employee_id": {employee_id}, "current_year": {current_year}}}'}
            else:
                raise HTTPException(status_code=400, detail="Invalid performance bonus query.")

        elif "Report office issue" in q:
            match = re.search(r"issue (\d+) for the (\w+) department", q, re.IGNORECASE)
            if match:
                issue_code = int(match.group(1))
                department = match.group(2)
                return {"name": "report_office_issue", "arguments": f'{{"issue_code": {issue_code}, "department": "{department}"}}'}
            else:
                raise HTTPException(status_code=400, detail="Invalid office issue query.")

        else:
            raise HTTPException(status_code=400, detail="Invalid query.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# The API URL endpoint
api_url = "http://127.0.0.1:8000/execute"

print(f"The API URL endpoint is: {api_url}")
