# csv_to_parquet.py

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import argparse


parser = argparse.ArgumentParser(description='Convert a CSV file to a parquet files')

parser.add_argument('--csv',  type=str, help='source data, path of the csv file')
parser.add_argument('--parquet', type=str, help='destination data, path of the parquet file without extention')
parser.add_argument('--separator', type=str, help='CSV separator, devault ","', nargs='?',default=",")
parser.add_argument('--chunksize', type=str, help='Amount of rows read at once', nargs='?',default=100000)
args = parser.parse_args()

csv_file = args.csv
parquet_file = args.parquet
chunksize = args.chunksize
csv_stream = pd.read_csv(csv_file, sep=args.separator, chunksize=chunksize, low_memory=False)

for i, chunk in enumerate(csv_stream):
    out_file_name = "{}_{}.parquet".format(parquet_file, i)
    print("Writing: {}".format(out_file_name) )

    # Guess the schema of the CSV file from the first chunk
    parquet_schema = pa.Table.from_pandas(df=chunk).schema
    # Open a Parquet file for writing
    parquet_writer = pq.ParquetWriter(out_file_name, parquet_schema, compression='snappy')
    # Write CSV chunk to the parquet file
    table = pa.Table.from_pandas(chunk, schema=parquet_schema)
    parquet_writer.write_table(table)

    parquet_writer.close()