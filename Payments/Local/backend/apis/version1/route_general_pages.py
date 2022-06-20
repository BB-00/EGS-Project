from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.post("/")
async def home(request: Request):
	
	body = await request.json()
	user = body['amount']
	print(user)
	return templates.TemplateResponse("general_pages/homepage.html",{"request":request})

