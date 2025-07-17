from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from utils import get_db_connection, get_schema_info, generate_sql, execute_sql

app = FastAPI()

class PromptInput(BaseModel):
    question: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now (restrict in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

@app.post("/query")
def query_data(data: PromptInput):
    try:
        # conn = get_db_connection()
        # cursor = conn.cursor()

        # schema_info = get_schema_info(cursor)
        # sql = generate_sql(data.question, schema_info)
        # print("Generated SQL:", sql)

        # results = execute_sql(, cursor)
        return {"success": True, "query": "select", "results":data}
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    
 
