# docker image for mgmt-framework

DOCKER_MGMT_FRAMEWORK_STEM = docker-sonic-mgmt-framework
DOCKER_MGMT_FRAMEWORK = $(DOCKER_MGMT_FRAMEWORK_STEM).gz
DOCKER_MGMT_FRAMEWORK_DBG = $(DOCKER_MGMT_FRAMEWORK_STEM)-$(DBG_IMAGE_MARK).gz

$(DOCKER_MGMT_FRAMEWORK)_PATH = $(DOCKERS_PATH)/$(DOCKER_MGMT_FRAMEWORK_STEM)

$(DOCKER_MGMT_FRAMEWORK)_DEPENDS += $(REDIS_TOOLS) $(SONIC_MGMT_FRAMEWORK) $(SONIC_LIBNSS_HAM)
$(DOCKER_MGMT_FRAMEWORK)_DBG_DEPENDS = $($(DOCKER_CONFIG_ENGINE_STRETCH)_DBG_DEPENDS)

SONIC_DOCKER_IMAGES += $(DOCKER_MGMT_FRAMEWORK)
$(DOCKER_MGMT_FRAMEWORK)_LOAD_DOCKERS += $(DOCKER_CONFIG_ENGINE_STRETCH)
#$(DOCKER_MGMT_FRAMEWORK)_DBG_IMAGE_PACKAGES = $($(DOCKER_CONFIG_ENGINE_STRETCH)_DBG_IMAGE_PACKAGES)

SONIC_INSTALL_DOCKER_IMAGES += $(DOCKER_MGMT_FRAMEWORK)
SONIC_STRETCH_DOCKERS += $(DOCKER_MGMT_FRAMEWORK)

$(DOCKER_MGMT_FRAMEWORK)_CONTAINER_NAME = mgmt-framework
SONIC_DOCKER_DBG_IMAGES += $(DOCKER_MGMT_FRAMEWORK_DBG)
SONIC_INSTALL_DOCKER_DBG_IMAGES += $(DOCKER_MGMT_FRAMEWORK_DBG)
SONIC_STRETCH_DBG_DOCKERS += $(DOCKER_MGMT_FRAMEWORK_DBG)
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += --net=host --privileged -t
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += -v /etc/sonic:/etc/sonic:ro
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += -v /var/run/docker.sock:/var/run/docker.sock
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += -v /usr/bin/docker:/usr/bin/docker:ro
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += -v /home:/home:ro
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += -v /host/cli-ca:/host/cli-ca:rw
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += -v /etc:/host_etc:ro
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += -v /var/run/dbus:/var/run/dbus:rw
$(DOCKER_MGMT_FRAMEWORK)_RUN_OPT += --mount type=bind,source="/var/platform/",target="/mnt/platform/"

$(DOCKER_MGMT_FRAMEWORK)_BASE_IMAGE_FILES += sonic-cli:/usr/bin/sonic-cli

