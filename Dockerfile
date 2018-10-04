FROM python:3.6-slim
WORKDIR /app
COPY ../../requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY ../.. /app
CMD ["python", "tweets_delete.py"]