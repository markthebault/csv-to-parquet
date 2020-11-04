import csv
from faker import Faker
import datetime
import argparse

def datagenerate(file_name, replication, records, headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open(file_name, 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name
            
            row =   {
                    "Email Id" : userId,
                    "Prefix" : fake.prefix(),
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    "Phone Number" : fake1.phone_number(),
                    "Additional Email Id": fake.email(),
                    "Address" : fake.address(),
                    "Zip Code" : fake.zipcode(),
                    "City" : fake.city(),
                    "State" : fake.state(),
                    "Country" : fake.country(),
                    "Year":fake.year(),
                    "Time": fake.time(),
                    "Link": fake.url(),
                    "Text": fake.word(),
                    }
            for i in range(0, replication):
                writer.writerow(row)
    
if __name__ == '__main__':

    #arguments
    parser = argparse.ArgumentParser(description='Convert a CSV file to a parquet files')
    parser.add_argument('--records', type=int, help='Number of unique records that will be created (default: 1000)', nargs='?',default=1000)
    parser.add_argument('--duplicates', type=int, help='Duplicate the record "n" times, this is to faster the generation process', nargs='?',default=10000)
    parser.add_argument('--file', type=str, help='File name and path that will be produced', nargs='?')
    args = parser.parse_args()

    records = args.records
    replication = args.duplicates
    filepath = args.file

    headers = ["Email Id", "Prefix", "Name", "Birth Date", "Phone Number", "Additional Email Id",
               "Address", "Zip Code", "City","State", "Country", "Year", "Time", "Link", "Text"]
    datagenerate(filepath, replication, records, headers)
    print("{}: CSV generation complete!".format(filepath) )