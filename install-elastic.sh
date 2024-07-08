# install elasticsearch, kibana in cent-os

# https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html#install-rpm

# Add GPG Key
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

# Download and install the RPM manually
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.14.2-x86_64.rpm

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.14.2-x86_64.rpm.sha512

sha512sum -c elasticsearch-8.14.2-x86_64.rpm.sha512

sudo rpm --install elasticsearch-8.14.2-x86_64.rpm

sudo systemctl daemon-reload

sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch

sudo systemctl status elasticsearch

# configuring cluster
vim /etc/elasticsearch/elasticsearch.yml
