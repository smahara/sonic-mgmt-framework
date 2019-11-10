# Docker image for UDLD

DOCKER_UDLD_STEM = docker-udld
DOCKER_UDLD = $(DOCKER_UDLD_STEM).gz
DOCKER_UDLD_DBG = $(DOCKER_UDLD_STEM)-$(DBG_IMAGE_MARK).gz

$(DOCKER_UDLD)_PATH = $(DOCKERS_PATH)/$(DOCKER_UDLD_STEM)

$(DOCKER_UDLD)_DEPENDS += $(UDLD) $(SWSS)
$(DOCKER_UDLD)_DBG_DEPENDS = $($(DOCKER_CONFIG_ENGINE_STRETCH)_DBG_DEPENDS)
$(DOCKER_UDLD)_DBG_DEPENDS += $(UDLD) $(SWSS)
$(DOCKER_UDLD)_DBG_IMAGE_PACKAGES = $($(DOCKER_CONFIG_ENGINE_STRETCH)_DBG_IMAGE_PACKAGES)

SONIC_DOCKER_IMAGES += $(DOCKER_UDLD)
SONIC_STRETCH_DOCKERS += $(DOCKER_UDLD)
SONIC_INSTALL_DOCKER_IMAGES += $(DOCKER_UDLD)

SONIC_DOCKER_DBG_IMAGES += $(DOCKER_UDLD_DBG)
SONIC_STRETCH_DBG_DOCKERS += $(DOCKER_UDLD_DBG)
SONIC_INSTALL_DOCKER_DBG_IMAGES += $(DOCKER_UDLD_DBG)

$(DOCKER_UDLD)_LOAD_DOCKERS = $(DOCKER_CONFIG_ENGINE_STRETCH)

$(DOCKER_UDLD)_CONTAINER_NAME = udld
$(DOCKER_UDLD)_RUN_OPT += --net=host --privileged -t
$(DOCKER_UDLD)_RUN_OPT += -v /etc/sonic:/etc/sonic:ro
$(DOCKER_UDLD)_RUN_OPT += -v /host/warmboot:/var/warmboot

$(DOCKER_UDLD)_BASE_IMAGE_FILES += udldctl:/usr/bin/udldctl
