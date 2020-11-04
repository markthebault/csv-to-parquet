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
