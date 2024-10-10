IMAGE = django-api-example:latest
BUILDER = podman

.PHONY: container
container:
	$(BUILDER) build . -t $(IMAGE)
