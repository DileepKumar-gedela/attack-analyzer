from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router
from app.db import engine
from app.routes.auth_routes import router as auth_router
from app.models import Base
app = FastAPI(title="Cyber Attack Analyzer")
Base.metadata.create_all(bind=engine)
# ----- CORS CONFIG -----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev mode (we restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------

app.include_router(upload_router)
app.include_router(auth_router)

@app.get("/")
def health():
    return {"status": "Backend running"}
