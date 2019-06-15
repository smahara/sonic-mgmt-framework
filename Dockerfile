FROM python:3.6.7-slim-jessie

## Remove retired jessie-updates repo
RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list

## Make apt-get non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# install necessary components
RUN apt-get update && apt-get install --yes gcc supervisor rsyslog sed

ARG docker_container_name
RUN [ -f /etc/rsyslog.conf ] && sed -ri "s/%syslogtag%/$docker_container_name#%syslogtag%/;" /etc/rsyslog.conf

RUN mkdir -p /usr/sonic-mgmt/rest_server /usr/sonic-mgmt/rest_server/ui /var/log/supervisor
COPY build/rest_server/dist/main /usr/sonic-mgmt/rest_server
COPY build/rest_server/dist/ui /usr/sonic-mgmt/rest_server/ui
COPY ["start.sh", "/usr/bin/"]
COPY ["supervisord.conf", "/etc/supervisor/conf.d/"]

RUN mkdir -p /usr/sonic-mgmt/CLI
COPY src/CLI/clish_start /usr/sonic-mgmt/CLI
ADD  src/CLI/target /usr/sonic-mgmt/CLI/target
COPY src/CLI/target/.libs /usr/local/lib
COPY swagger_client  /usr/sonic-mgmt/swagger_client
COPY swagger_server  /usr/sonic-mgmt/swagger_server

ENV PYTHONPATH /usr/sonic-mgmt

#install sonic specific python packages 
RUN mkdir -p /tmp/python-wheels 
COPY python-wheels/swsssdk-2.0.1-py3-none-any.whl /tmp/python-wheels 
RUN pip3 install /tmp/python-wheels/swsssdk-2.0.1-py3-none-any.whl 

#install dependent python packages 
COPY requirements.txt /tmp 
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

## Clean up packages which are not needed anymore
RUN apt-get remove --yes gcc && apt-get clean --yes && apt-get autoclean --yes && apt-get autoremove --yes
#RUN rm -rf /tmp/ *&& rm -rf /var/lib/apt/lists/*

# Export port 80 for http ie REST
EXPOSE 8080

CMD ["/usr/bin/supervisord"]
