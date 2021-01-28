SERVICE_NAME=locust-hello-world

build:
	docker build -t ${SERVICE_NAME} .

run:
	docker run --rm -ti --name=${SERVICE_NAME} -p 8089:8089 -e HOST=https://www.pelando.com.br ${SERVICE_NAME}