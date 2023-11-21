FROM python:3.12.0-alpine3.18
COPY mi_app mi_app/ 
WORKDIR /mi_app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]