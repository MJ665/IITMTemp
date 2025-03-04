# # import json
# # from http.server import BaseHTTPRequestHandler
# # import urllib.parse

# # # Marks data (replace this with your JSON file content)
# # marks_data = [{"name":"X","marks":10},{"name":"Y","marks":20},{"name":"2Zx","marks":52},{"name":"SZV","marks":35},{"name":"v","marks":16},{"name":"TmRHn0a1FF","marks":88},{"name":"8YJR","marks":52},{"name":"gTxYR","marks":13},{"name":"t2joiU","marks":6},{"name":"2C7S00","marks":48},{"name":"GyecPT","marks":47},{"name":"6Xh7NjV4","marks":77},{"name":"eVn","marks":97},{"name":"2m426rc","marks":60},{"name":"DVatxo","marks":79},{"name":"sOR3s","marks":83},{"name":"GQxMS","marks":7},{"name":"LPCrvp","marks":90},{"name":"KX2","marks":69},{"name":"OIzh","marks":59},{"name":"5JJ0be","marks":78},{"name":"a","marks":49},{"name":"zpTHQAFX","marks":35},{"name":"nyrXb23mG","marks":97},{"name":"l","marks":16},{"name":"Wi","marks":81},{"name":"l1fDEe46","marks":60},{"name":"Mjn","marks":69},{"name":"BNfXNpIEZ","marks":56},{"name":"Zno9","marks":52},{"name":"GhIwC","marks":62},{"name":"ZN","marks":5},{"name":"pkwLjtcn","marks":16},{"name":"fUkitvMd","marks":71},{"name":"8Okd5oH","marks":82},{"name":"XqU","marks":16},{"name":"6","marks":70},{"name":"Bnmrqb","marks":55},{"name":"ll0I","marks":16},{"name":"nYLpxsSh","marks":84},{"name":"yr2","marks":41},{"name":"SC","marks":11},{"name":"w3p","marks":96},{"name":"WsUevm5V","marks":31},{"name":"18y8zSanht","marks":61},{"name":"BZA","marks":50},{"name":"Poq","marks":63},{"name":"G6ezFKjUJj","marks":48},{"name":"7","marks":63},{"name":"sFVzld0EyP","marks":49},{"name":"g0EcoMf","marks":36},{"name":"eJxM","marks":9},{"name":"FXmjayG4","marks":8},{"name":"eCkNvLr","marks":11},{"name":"T","marks":42},{"name":"FLGl3ZYNYZ","marks":18},{"name":"PLX4","marks":6},{"name":"O9h","marks":59},{"name":"VhHtRVaS3p","marks":4},{"name":"X1rF9u","marks":66},{"name":"EAW1eSy","marks":22},{"name":"J","marks":10},{"name":"oFEyLf","marks":84},{"name":"Ht7","marks":41},{"name":"eZCzIhul","marks":11},{"name":"wcNpN3Nop","marks":81},{"name":"4BypQ61b","marks":58},{"name":"vWJv","marks":86},{"name":"K3UcfAdhpn","marks":10},{"name":"EpD","marks":27},{"name":"y1Hj","marks":11},{"name":"wF","marks":89},{"name":"Ul2W3Q","marks":88},{"name":"dmi8R","marks":62},{"name":"BpSwQ","marks":68},{"name":"jInBS","marks":93},{"name":"Wb","marks":11},{"name":"Dj","marks":66},{"name":"bbdTJkJJF","marks":63},{"name":"WduVtl1o","marks":20},{"name":"mzFn79WVwN","marks":6},{"name":"u","marks":91},{"name":"WtpWLuHoL9","marks":26},{"name":"JCUQsch2","marks":81},{"name":"FGP","marks":48},{"name":"n3cnGFwCz","marks":57},{"name":"OEACb5vTH","marks":63},{"name":"z","marks":99},{"name":"Iwim4iTSy","marks":77},{"name":"4PFiMjI","marks":87},{"name":"eaLvOGBirc","marks":6},{"name":"BAMWVluESI","marks":38},{"name":"jSXLjt","marks":46},{"name":"1CUm3PsLk","marks":98},{"name":"fivgQK0F","marks":34},{"name":"hPx","marks":44},{"name":"8T","marks":80},{"name":"B5Yc","marks":51},{"name":"3Fy8","marks":23},{"name":"i7lT1","marks":24},{"name":"M8OA3mF","marks":34},{"name":"VqczVDvT","marks":43}]



# # # Convert the list of dictionaries to a name-to-marks dictionary for easy lookup
# # marks_dict = {entry["name"]: entry["marks"] for entry in marks_data}

# # class handler(BaseHTTPRequestHandler):
# #     def do_GET(self):
# #         # Parse query parameters
# #         query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
# #         names = query.get('name', [])

# #         # Get the marks for the requested names
# #         marks = [marks_dict.get(name, None) for name in names]

# #         # Filter out any None values for names not found in the data
# #         valid_marks = [mark for mark in marks if mark is not None]

# #         # Send the response
# #         self.send_response(200)
# #         self.send_header('Content-type', 'application/json')
# #         self.end_headers()
# #         self.wfile.write(json.dumps({"marks": valid_marks}).encode('utf-8'))
# #         return





# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# import json
# import os

# # Load JSON data
# json_file = os.path.join(os.path.dirname(__file__), "./q-vercel-python.json")
# with open(json_file, "r") as file:
#     students = json.load(file)

# # Create FastAPI app
# app = FastAPI()

# # Enable CORS for all origins
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Endpoint to fetch marks by name
# @app.get("/api")
# def get_marks(name: list[str] = Query(default=[])):
#     if not name:  
#         # If no name is provided, return full student data
#         return {"students": students}
    
#     # Find marks for given names
#     marks = [student["marks"] for student in students if student["name"] in name]
#     return {"marks": marks}







from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

# Load JSON data
json_file = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(json_file, "r") as file:
    students = json.load(file)

# Convert list to dictionary for fast lookups
students_dict = {student["name"]: student["marks"] for student in students}

# Create FastAPI app
app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

# API route should be "/api/"
@app.get("/api/")
def get_marks(name: list[str] = Query(default=[])):
    if not name:  
        return {"students": students}
    
    # Fetch marks **in the order of the request**
    marks = [students_dict.get(n, None) for n in name]
    return {"marks": marks}
