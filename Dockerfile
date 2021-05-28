FROM python:3.7


ADD code /app


USER admin
WORKDIR /app

EXPOSE 5000
CMD ["python", "main.py"]

