FROM python:3.12

WORKDIR /messenger

COPY ./requirements.txt /messenger/requirements.txt
COPY ./.env /messenger/.env
RUN pip install -r requirements.txt

COPY ./rest_api /messenger/rest_api

ENTRYPOINT ["uvicorn", "rest_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--env-file", ".env"]
