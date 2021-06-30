#/bin/sh

#testing

apt-get update
apt install git
apt install net-tools
apt install docker.io
apt install docker-compose
apt install docker.io
apt install python
apt install -y python3-pip
apt install golang


mkdir /opt/strelka/socket/
chmod a+rwx /opt/strelka/socket/
touch /etc/docker/daemon.json
echo '{"dns":["10.10.10.8":"8.8.8.8"]}' > /etc/docker/daemon.json
docker pull clamav/clamav:unstable
