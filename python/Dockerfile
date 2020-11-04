FROM python:3.8

RUN apt update && \
    apt install -y build-essential libsnappy-dev

WORKDIR /app

#install requirements
COPY requirements.txt /app
RUN pip install -r requirements.txt

#copy the rest of files
COPY . /app

ENTRYPOINT ["python", "csv-to-parquet.py"]