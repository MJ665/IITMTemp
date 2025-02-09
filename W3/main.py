from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from pydantic import BaseModel
import numpy as np
import httpx  # Changed from openai import OpenAI
import os
from dotenv import load_dotenv

print("Loading .env file...")
load_dotenv() # Load the API key from .env

print("Creating FastAPI app...")
app = FastAPI()

# Enable CORS
print("Adding CORS middleware...")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

print("Defining SimilarityRequest model...")
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

print("Defining SimilarityResponse model...")
class SimilarityResponse(BaseModel):
    matches: List[str]

#API KEY (Replace with your API Key)
print("Getting OPENAI_API_KEY from environment...")
OPENAI_API_KEY = os.getenv("aiproxy") #DO NOT HARDCODE

print("Checking if OPENAI_API_KEY is set...")
if not OPENAI_API_KEY:
    raise Exception("OPENAI_API_KEY environment variable not set. Please set it before running the application.")


# Load API key from environment variable


async def get_embedding(text: str):
    """
    Generates an embedding for the given text using OpenAI's text-embedding-3-small model.
    """
    print(f"Getting embedding for text: {text[:20]}...") # Only print the first 20 characters
    try:
        print("Creating headers...")
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        print("Creating data...")
        data = {
            "input": text,
            "model": "text-embedding-3-small"
        }
        print("Creating httpx AsyncClient...")
        async with httpx.AsyncClient() as client: #Asynchronous HTTP client
            print("Posting request to OpenAI API...")
            response = await client.post(
                "https://aiproxy.sanand.workers.dev/openai/v1/embeddings",
                headers=headers,
                json=data
            )
            print("Checking response status code...")
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            print("Parsing response JSON...")
            return response.json()['data'][0]['embedding']


    except httpx.HTTPStatusError as e: #Catch HTTP Status errors
        print(f"HTTP error generating embedding: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=f"Failed to generate embedding: {e}")
    except Exception as e: # Catch any other exceptions
        print(f"Error generating embedding: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate embedding: {e}")


def cosine_similarity(a, b):
    """
    Calculates the cosine similarity between two vectors.
    """
    print("Calculating cosine similarity...")
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


@app.post("/similarity", response_model=SimilarityResponse)
async def calculate_similarity(request: SimilarityRequest):
    """
    Calculates the cosine similarity between the query and each document,
    and returns the top 3 most similar documents.
    """
    print("Starting calculate_similarity function...")
    docs = request.docs
    query = request.query

    try:
        # Generate embeddings for the documents and the query
        print("Getting query embedding...")
        query_embedding = await get_embedding(query)
        print("Getting doc embeddings...")
        doc_embeddings = [await get_embedding(doc) for doc in docs]

        # Calculate cosine similarities
        print("Calculating cosine similarities...")
        similarities = [cosine_similarity(query_embedding, doc_embedding) for doc_embedding in doc_embeddings]

        # Rank documents by similarity
        print("Ranking documents...")
        ranked_docs = sorted(zip(docs, similarities), key=lambda x: x[1], reverse=True)

        # Get the top 3 most similar documents
        print("Getting top 3 docs...")
        top_3_docs = [doc for doc, _ in ranked_docs[:3]]

        print("Returning SimilarityResponse...")
        return SimilarityResponse(matches=top_3_docs)

    except Exception as e:
        print(f"Exception in calculate_similarity: {e}")
        raise HTTPException(status_code=500, detail=str(e))

#API URL endpoint
print("Defining API URL endpoint...")
api_url = "http://127.0.0.1:8080/similarity"

print(f"The API URL endpoint is: {api_url}")