from fastapi import FastAPI

app = FastAPI(title="Aura ML")

@app.get("/")
def root():
    return {
        "status": "Aura ML backend running",
        "phase": "Phase 0 - Foundation"
    }
