all: build deploy test

build: build_image push_image

build_image:
	docker build --tag hydria/cmpapi:latest --tag hydria/cmpapi:1.0 --no-cache .
build_and_push_image_all_platforms:
	docker buildx build --platform linux/amd64,linux/arm64,linux/arm --push --tag hydria/cmpapi:latest --tag hydria/cmpapi:1.0 --no-cache .
deploy:
	kubectl apply -f ./k8s
push_image:
	docker image push --all-tags hydria/cmpapi
test:
	pytest ./test.py
