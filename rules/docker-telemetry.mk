# docker image for telemetry agent

DOCKER_TELEMETRY_STEM = docker-sonic-telemetry
DOCKER_TELEMETRY = $(DOCKER_TELEMETRY_STEM).gz
#DOCKER_TELEMETRY_DBG = $(DOCKER_TELEMETRY_STEM)-$(DBG_IMAGE_MARK).gz

$(DOCKER_TELEMETRY)_PATH = $(DOCKERS_PATH)/$(DOCKER_TELEMETRY_STEM)

$(DOCKER_TELEMETRY)_DEPENDS += $(REDIS_TOOLS) $(SONIC_TELEMETRY) $(SONIC_LIBNSS_HAM)
#$(DOCKER_TELEMETRY)_DBG_DEPENDS = $($(DOCKER_CONFIG_ENGINE_STRETCH)_DBG_DEPENDS)

$(DOCKER_TELEMETRY)_LOAD_DOCKERS += $(DOCKER_CONFIG_ENGINE_STRETCH)
#$(DOCKER_TELEMETRY)_DBG_IMAGE_PACKAGES = $($(DOCKER_CONFIG_ENGINE_STRETCH)_DBG_IMAGE_PACKAGES)

SONIC_DOCKER_IMAGES += $(DOCKER_TELEMETRY)
ifeq ($(ENABLE_SYSTEM_TELEMETRY), y)
SONIC_INSTALL_DOCKER_IMAGES += $(DOCKER_TELEMETRY)
SONIC_STRETCH_DOCKERS += $(DOCKER_TELEMETRY)
endif

#SONIC_DOCKER_DBG_IMAGES += $(DOCKER_TELEMETRY_DBG)
ifeq ($(ENABLE_SYSTEM_TELEMETRY), y)
SONIC_INSTALL_DOCKER_DBG_IMAGES += $(DOCKER_TELEMETRY_DBG)
#SONIC_STRETCH_DBG_DOCKERS += $(DOCKER_TELEMETRY_DBG)
endif

$(DOCKER_TELEMETRY)_CONTAINER_NAME = telemetry
$(DOCKER_TELEMETRY)_RUN_OPT += --net=host --privileged -t
$(DOCKER_TELEMETRY)_RUN_OPT += -v /etc/sonic:/etc/sonic:ro
$(DOCKER_TELEMETRY)_RUN_OPT += -v /var/run/dbus:/var/run/dbus:rw
$(DOCKER_TELEMETRY)_RUN_OPT += -v /var/run/docker.sock:/var/run/docker.sock
$(DOCKER_TELEMETRY)_RUN_OPT += -v /usr/bin/docker:/usr/bin/docker:ro
$(DOCKER_TELEMETRY)_RUN_OPT += --mount type=bind,source="/var/platform/",target="/mnt/platform/"
