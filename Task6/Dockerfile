FROM python:3.12

WORKDIR /messenger

COPY ./requirements.txt /messenger/requirements.txt
COPY ./.env /messenger/.env
RUN pip install -r requirements.txt

COPY ./rest_api /messenger/rest_api
COPY ./api_gateway.py /messenger/api_gateway.py

CMD ["uvicorn", "api_gateway:app", "--host", "0.0.0.0", "--port", "8001"]


# COPY ./api_gateway.py /app/api_gateway.py

# CMD ["uvicorn", "api_gateway:app", "--host", "0.0.0.0", "--port", "8001"]
