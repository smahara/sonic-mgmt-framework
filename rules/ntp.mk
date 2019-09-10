# ntp package

NTP_VERSION = 4.2.8p10+dfsg
export NTP_VERSION

NTP = ntp_$(NTP_VERSION)-3+deb9u4_amd64.deb
$(NTP)_SRC_PATH = $(SRC_PATH)/ntp
SONIC_MAKE_DEBS += $(NTP)
SONIC_STRETCH_DEBS += $(NTP)

export NTP
