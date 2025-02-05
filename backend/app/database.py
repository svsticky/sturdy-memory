import asyncpg
from fastapi import FastAPI
from config import POSTGRES_DSN
from contextlib import asynccontextmanager

db_pool = None  # Global variable to hold the asyncpg connection pool


@asynccontextmanager
async def lifespan2(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application.

    This context manager is called during the startup and shutdown of the FastAPI app.
    It initializes the database connection pool during startup and ensures it is properly closed during shutdown.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None
    """
    print("Starting lifespan...")
    try:
        await startup()  # Initialize the DB pool
    except Exception as e:
        print(f"Error creating db pool: {e}")
        raise  # Re-raise the exception to prevent the app from starting
    yield
    await shutdown()  # Close the DB pool when the app shuts down


async def startup():
    """
    Initializes the asyncpg connection pool.

    This function is called during the startup of the FastAPI application.
    It creates a connection pool to the PostgreSQL database using the DSN from the configuration.

    Raises:
        Exception: If the connection to the database fails.
    """
    global db_pool
    print("Connecting to", POSTGRES_DSN)
    db_pool = await asyncpg.create_pool(dsn=POSTGRES_DSN)
    print("Database connection pool created.")


async def shutdown():
    """
    Closes the asyncpg connection pool.

    This function is called during the shutdown of the FastAPI application.
    It closes the database connection pool if it has been initialized.
    """
    global db_pool
    if db_pool:
        await db_pool.close()
        print("Database connection pool closed.")
    else:
        print("No database pool to close.")


def get_db_pool():
    """
    Returns the asyncpg connection pool.

    This function is used to get the current database connection pool.
    If the pool has not been initialized, it raises a RuntimeError.

    Returns:
        asyncpg.pool.Pool: The asyncpg connection pool.

    Raises:
        RuntimeError: If the database connection pool is not initialized.
    """
    if db_pool is None:
        raise RuntimeError("Database connection pool is not initialized.")
    return db_pool
