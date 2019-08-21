TARGET := pddf_fan_driver_module

#$(info  ===========$(M)=========)

obj-m := $(TARGET).o 

$(TARGET)-objs := pddf_fan_api.o pddf_fan_driver.o
#GCOV_PROFILE := y

ccflags-y := -I$(M)/modules/include
