# Convert CSV to parquet file

This small tool is used to convert a CSV file to parquet files. By default chunks of 100 000 rows is used to split into different parquet files.


## Usage
```
docker run -it --rm \
  -v $PATH_TO_DATA:/data \
  markthebault/csv-to-parquet \
  --csv /data/titanic.csv \
  --parquet /data/export-parquet/data
```
you can specify how much rows should be processed at once with the argument `--chunksize=5000000`

## Build the image

`make build`

## test with titanic.csv

`make test`


## Generate a huge csv
In the data folder there is a python script that will generate hug CSV (by default 2.2GB, 10 million rows), if you want to change those parameters, you need to edit the file an replace
Usage:
```
$ pip install faker
$ python data/generate-csv.py --file /tmp/small.csv --records 100 --duplicates 1
$ python data/generate-csv.py --file /tmp/big.csv --records 1000 --duplicates 10000
```