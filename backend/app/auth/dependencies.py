from fastapi import Request, HTTPException
import httpx

async def require_valid_token(request: Request):
    """
    This function checks if the incoming request has a valid access token in the cookies.
    If no access token is found, it raises an HTTP 401 Unauthorized exception.
    
    Args:
        request (Request): The FastAPI request object containing the cookies.

    Returns:
        str: The access token if found.

    Raises:
        HTTPException: If the access token is not present, an Unauthorized error is raised.
    """
    access_token = request.cookies.get("access_token")
    if not access_token:
        raise HTTPException(status_code=401, detail="Unauthorized. Please log in.")
    return access_token


def isBoard(response: httpx.Response):
    """
    This function checks if the response contains a valid admin board indicator by parsing the JSON response.
    It looks for the 'is_admin' key and checks if its value is 'True'. This should be the case for board members, who are the only people allowed to view and use Stocky.

    Args:
        response (httpx.Response): The HTTP response object to inspect.

    Returns:
        bool: True if the 'is_admin' field in the response JSON is 'True', False otherwise.
    """
    json = response.json()
    print(json)
    return json.get("is_admin") == "True"
