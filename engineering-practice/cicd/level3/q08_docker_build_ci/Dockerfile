FROM python:3.11-slim
WORKDIR /app
COPY sample_app/requirements.txt .
RUN pip install -r requirements.txt
COPY sample_app/ .
CMD ["pytest"]
