from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["api"],
)

@router.get("/")
def test():
    return {"message": "Hello Api Area"}