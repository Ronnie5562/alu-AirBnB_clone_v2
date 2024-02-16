#!/usr/bin/env bash

new_error_page="include /etc/nginx/sites-enabled/*;\n\tserver{\n\t\t}"
sudo sed -i "include /etc/nginx/sites-enabled/*;|$new_error_page|" /etc/nginx/sites-enabled/default

sudo service nginx restart