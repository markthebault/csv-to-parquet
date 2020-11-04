IMAGE_NAME=markthebault/csv-to-parquet
IMAGE_TAG=latest

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

push:
	docker push $(IMAGE_NAME):$(IMAGE_TAG)

test:
	docker run -it --rm -v $(PWD)/data:/data csv --csv /data/titanic.csv --parquet /data/export-parquet/data