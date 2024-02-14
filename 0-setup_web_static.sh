#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<h1>Abimbola Ronald</h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart