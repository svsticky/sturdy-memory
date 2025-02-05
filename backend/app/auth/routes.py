from fastapi import APIRouter, HTTPException, status, Depends, Request
from fastapi.responses import RedirectResponse
import httpx
from auth.dependencies import isBoard
from config import (
    OIDC_AUTHORIZATION_URL, OIDC_TOKEN_URL, OIDC_USERINFO_URL, 
    OIDC_CLIENT_ID, OIDC_CLIENT_SECRET, OIDC_REDIRECT_URI
)

router = APIRouter(tags=["auth"])

@router.get("/login")
async def login():
    """
    Redirects the user to the OIDC authorization endpoint for login.

    Returns:
        RedirectResponse: Redirects to the OIDC authorization URL.
    """
    authorization_url = (
        f"{OIDC_AUTHORIZATION_URL}?response_type=code&client_id={OIDC_CLIENT_ID}"
        f"&redirect_uri={OIDC_REDIRECT_URI}&scope=openid%20profile%20email"
    )
    return RedirectResponse(authorization_url)


@router.get("/callback")
async def callback(code: str):
    """
    Handles the OIDC callback after user login.

    It exchanges the authorization code for an access token, retrieves user info, 
    and sets a secure cookie with the token if the user is valid.

    Args:
        code (str): Authorization code received from OIDC provider.

    Returns:
        RedirectResponse: Redirects to '/welcome' on success, or '/login' if unauthorized.
    
    Raises:
        HTTPException: If token retrieval or access token extraction fails.
    """
    # Exchange authorization code for access token
    async with httpx.AsyncClient() as client:
        response = await client.post(
            OIDC_TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": OIDC_REDIRECT_URI,
                "client_id": OIDC_CLIENT_ID,
                "client_secret": OIDC_CLIENT_SECRET,
            },
        )

    if response.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to retrieve token")

    access_token = response.json().get("access_token")
    if not access_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Access token not found")

    # Retrieve user information using the access token
    async with httpx.AsyncClient() as client:
        user_response = await client.get(OIDC_USERINFO_URL, headers={"Authorization": f"Bearer {access_token}"})

    if not isBoard(user_response):
        # Redirect back to login if user is not authorized
        return RedirectResponse(url="/login")
        #TODO: make sure this does not become infinite loop

    # Set access token in a secure HTTP-only cookie and redirect to the welcome page
    response = RedirectResponse(url="/welcome")
    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True)
    return response
