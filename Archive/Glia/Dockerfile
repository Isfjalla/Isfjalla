FROM python:3.9

WORKDIR /app

COPY ./src /app/src
COPY ./requirements.txt /app/requirements.txt
COPY ./README.txt /app/README.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]