FROM python:3.7


ADD code /app
ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
    && useradd -ms /bin/bash admin


USER admin
WORKDIR /app

EXPOSE 5000
CMD ["python", "main.py"]

