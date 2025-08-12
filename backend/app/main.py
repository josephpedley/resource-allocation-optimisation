from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Resource Allocation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://ui.localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "poooop"}