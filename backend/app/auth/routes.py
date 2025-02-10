from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
import httpx
from auth.dependencies import isBoard
from config import OIDC_DISCOVERY_URL, OIDC_CLIENT_ID, OIDC_CLIENT_SECRET, OIDC_REDIRECT_URI

router = APIRouter()

async def get_oidc_config():
    """
    Fetches the OIDC discovery document and returns the necessary endpoints.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(OIDC_DISCOVERY_URL)

    if response.status_code != 200:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to retrieve OIDC configuration")

    return response.json()


@router.get("/login")
async def login():
    """
    Redirects the user to the OIDC authorization endpoint for login.
    """
    config = await get_oidc_config()
    authorization_url = config.get("authorization_endpoint")
    if not authorization_url:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Authorization endpoint not found in discovery document")

    authorization_url = (
        f"{authorization_url}?response_type=code&client_id={OIDC_CLIENT_ID}"
        f"&redirect_uri={OIDC_REDIRECT_URI}&scope=openid%20profile%20email"
    )
    return RedirectResponse(authorization_url)


@router.get("/callback")
async def callback(code: str):
    """
    Handles the OIDC callback after user login.
    """
    config = await get_oidc_config()

    token_url = config.get("token_endpoint")
    if not token_url:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Token endpoint not found in discovery document")

    # Exchange authorization code for access token
    async with httpx.AsyncClient() as client:
        response = await client.post(
            token_url,
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
    userinfo_url = config.get("userinfo_endpoint")
    if not userinfo_url:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Userinfo endpoint not found in discovery document")

    async with httpx.AsyncClient() as client:
        user_response = await client.get(userinfo_url, headers={"Authorization": f"Bearer {access_token}"})

    if not isBoard(user_response):
        return RedirectResponse(url="/login")

    # Set access token in a secure HTTP-only cookie and redirect to the welcome page
    response = RedirectResponse(url="/welcome")
    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True)
    return response
