from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
import requests

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.post("/")
async def home(request: Request):
	body = await request.body()
	body = body.decode("utf-8")

	body_list=body.split('&')
	body_list.pop(0)
	# print(body)

	token = body_list[0].split('=')[1]
	amount = body_list[1].split('=')[1]
	username = body_list[2].split('=')[1]
	# print(token)
	# print(amount)
	# print(username)

	response = requests.get("http://127.0.0.1:9020/validate", params=token)

	if response is not username:
		return "merda"

	return templates.TemplateResponse("general_pages/homepage.html",{"request":request})