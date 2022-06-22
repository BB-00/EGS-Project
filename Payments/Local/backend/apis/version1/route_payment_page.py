from fastapi import APIRouter, HTTPException, status
from fastapi import Request
from fastapi.templating import Jinja2Templates
import requests

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.post("/")
async def payment(request: Request):
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

	params = {"token":token}

	response = requests.get("http://127.0.0.1:9020/validate", params=params)

	if response.json() != username:
		raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="payments: login no longer valid!"
        )

	return templates.TemplateResponse("general_pages/payments.html",{"request":request, "_amount":amount, "_methodID":0, "_username":username})