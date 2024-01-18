FROM python:3.10-slim
LABEL authors="Clement"

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
