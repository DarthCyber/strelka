#/bin/sh

#testing

mkdir /opt/strelka/socket/
touch /etc/docker/daemon.json
echo '{"dns":["10.10.10.8":"8.8.8.8"]}' > /etc/docker/daemon.json
