from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from database import get_db_pool
from auth.dependencies import require_valid_token

router = APIRouter(tags=["general"])

@router.get("/welcome")
async def welcome(access_token: str = Depends(require_valid_token)):
    """
    Protected endpoint that returns a welcome message.

    Args:
        access_token (str): Validated access token from the dependency.

    Returns:
        dict: A message indicating access to the protected page.
    """
    return {"message": "Welcome to the protected page!"}


@router.get("/getTables")
async def get_tables(access_token: str = Depends(require_valid_token)):
    """
    Fetches the list of table names from the public schema of the PostgreSQL database.

    Args:
        access_token (str): Validated access token from the dependency.

    Returns:
        JSONResponse: A JSON response containing the list of table names, 
        or an error message if the database connection pool is not initialized.
    """
    db_pool = get_db_pool()
    if db_pool is None:
        return JSONResponse(status_code=500, content={"error": "Database connection pool not initialized yet."})

    # Query the database for table names
    async with db_pool.acquire() as connection:
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        rows = await connection.fetch(query)
        tables = [row["table_name"] for row in rows]
        return JSONResponse(content={"tables": tables})
