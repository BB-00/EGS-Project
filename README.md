# EGS-Project

Run locally:
 - launch Authentication API: uvicorn main:app --reload --host 127.0.0.1 --port 9020
 - launch Payments API: uvicorn main:app --reload --host 127.0.0.1 --port 9021
 - launch WebApp: python3 run.py