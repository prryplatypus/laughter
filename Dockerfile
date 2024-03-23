
FROM python:3.11
ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app
RUN pip install -e "."
