FROM python:3.8

RUN apt update && \
    apt install -y build-essential libsnappy-dev

WORKDIR /app

#install requirements
COPY requirements.txt /app
RUN pip install --no-cache-dir --ignore-installed -r requirements.txt

#copy the script
COPY csv-to-parquet.py /app

ENTRYPOINT ["python", "csv-to-parquet.py"]