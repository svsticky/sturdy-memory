from fastapi import FastAPI
from pyfiglet import figlet_format as ascii_print
from database import lifespan2
from config import tags_metadata
from routes.general import router as general_router
from auth.routes import router as auth_router

# Create FastAPI application with metadata and lifespan management
app = FastAPI(
    title="Stocky backend",
    description="The backend service for Stocky, providing APIs for Sticky.",
    version="1.0.0",
    openapi_tags=tags_metadata,
    lifespan=lifespan2
)

# Print a styled ASCII banner for the app startup
print(ascii_print("Stocky backend"))

# Include routers for authentication and general routes
app.include_router(auth_router)
app.include_router(general_router)
