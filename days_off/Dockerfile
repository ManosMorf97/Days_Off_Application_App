FROM python:3.8
RUN mkdir -p /app
WORKDIR /app
COPY ./ /app/
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
RUN pip install -r requirements.txt
CMD python3 manage.py runserver 0.0.0.0:8000