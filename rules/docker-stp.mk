# Docker image for STP

DOCKER_STP = docker-stp.gz
$(DOCKER_STP)_PATH = $(DOCKERS_PATH)/docker-stp
$(DOCKER_STP)_DEPENDS += $(STP) $(SWSS)

$(DOCKER_STP)_LOAD_DOCKERS = $(DOCKER_CONFIG_ENGINE)

SONIC_DOCKER_IMAGES += $(DOCKER_STP)

SONIC_INSTALL_DOCKER_IMAGES += $(DOCKER_STP)


$(DOCKER_STP)_CONTAINER_NAME = stp
$(DOCKER_STP)_RUN_OPT += --net=host --privileged -t
$(DOCKER_STP)_RUN_OPT += -v /etc/sonic:/etc/sonic:ro
$(DOCKER_STP)_RUN_OPT += -v /host/warmboot:/var/warmboot
