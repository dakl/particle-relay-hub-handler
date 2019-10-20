FROM python:3.7.4-alpine3.10

RUN pip install flask requests

WORKDIR /code
COPY . /code

CMD ["python", "run.py"]