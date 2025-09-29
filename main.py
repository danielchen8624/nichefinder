from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS so the React app (localhost:3000) can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://loca"
    "lhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary dummy endpoint (we'll wire Google Trends + GPT later)
@app.get("/api/trends")
def get_trends():
    return [
        {"title": "AI Study Tools", "score": 8.7, "summary": "Rising demand among students for AI-enhanced study apps", "category": "saas"},
        {"title": "Cold Plunge Tubs", "score": 7.9, "summary": "Wellness & recovery trend intensifying on TikTok", "category": "ecom"},
        {"title": "Smart Mirror Fitness", "score": 8.3, "summary": "At-home workouts + computer vision coaching buzz", "category": "ecom"},
    ]
