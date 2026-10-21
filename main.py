"""Voice AI Agent - Initial Backend Foundation.

FastAPI application providing health checks, welcome endpoint, and interactive documentation.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from lead_service import load_leads

# Initialize FastAPI application with informative metadata
app = FastAPI(
    title="Voice AI Agent API",
    description="Initial backend foundation for the Voice AI Agent.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["General"])
async def root():
    """Welcome endpoint providing basic API information and documentation link."""
    return {
        "message": "Welcome to Voice AI Agent API!",
        "status": "online",
        "version": "0.1.0",
        "docs": "/docs",
    }


@app.get("/health", tags=["General"])
async def health_check():
    """Health status endpoint to verify service availability."""
    return {
        "status": "healthy",
        "service": "voice-ai-agent-backend",
    }


<<<<<<< HEAD
@app.get("/leads")
def get_leads():
    df = load_leads()

    return {
        "total_leads": len(df),
        "columns": df.columns.tolist(),
        "sample": df.head(3).fillna("").to_dict(
            orient="records"
        )
    }

=======
>>>>>>> d05cfc96009fd403728863d9fda21685cf73fcf1
if __name__ == "__main__":
    import uvicorn

    # Run the development server when executed directly
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
