# docker image for teamd agent

DOCKER_TEAMD_STEM = docker-teamd
DOCKER_TEAMD = $(DOCKER_TEAMD_STEM).gz
DOCKER_TEAMD_DBG = $(DOCKER_TEAMD_STEM)-$(DBG_IMAGE_MARK).gz

$(DOCKER_TEAMD)_PATH = $(DOCKERS_PATH)/$(DOCKER_TEAMD_STEM)

$(DOCKER_TEAMD)_DEPENDS += $(SWSS) $(LIBTEAMDCT) $(LIBTEAM_UTILS) $(REDIS_TOOLS)
$(DOCKER_TEAMD)_DBG_DEPENDS = $($(DOCKER_CONFIG_ENGINE_STRETCH)_DBG_DEPENDS)
$(DOCKER_TEAMD)_DBG_DEPENDS += $(SWSS_DBG) $(LIBSWSSCOMMON_DBG)
$(DOCKER_TEAMD)_DBG_IMAGE_PACKAGES = $($(DOCKER_CONFIG_ENGINE_STRETCH)_DBG_IMAGE_PACKAGES)

$(DOCKER_TEAMD)_LOAD_DOCKERS += $(DOCKER_CONFIG_ENGINE_STRETCH)

SONIC_DOCKER_IMAGES += $(DOCKER_TEAMD)
SONIC_INSTALL_DOCKER_IMAGES += $(DOCKER_TEAMD)
SONIC_STRETCH_DOCKERS += $(DOCKER_TEAMD)

SONIC_DOCKER_DBG_IMAGES += $(DOCKER_TEAMD_DBG)
SONIC_INSTALL_DOCKER_DBG_IMAGES += $(DOCKER_TEAMD_DBG)
SONIC_STRETCH_DBG_DOCKERS += $(DOCKER_TEAMD_DBG)

$(DOCKER_TEAMD)_CONTAINER_NAME = teamd
$(DOCKER_TEAMD)_RUN_OPT += --net=host --privileged -t
$(DOCKER_TEAMD)_RUN_OPT += -v /etc/sonic:/etc/sonic:ro
$(DOCKER_TEAMD)_RUN_OPT += -v /host/warmboot:/var/warmboot
$(DOCKER_TEAMD)_RUN_OPT += -v /tmp:/tmp/portchannelstat:rw

$(DOCKER_TEAMD)_BASE_IMAGE_FILES += teamdctl:/usr/bin/teamdctl
