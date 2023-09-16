FROM python:3.8
RUN mkdir -p /app
WORKDIR /app
COPY ./ /app/
EXPOSE 8000
RUN pip install -r requirements.txt
CMD python3 -m uvicorn days_off.asgi:application