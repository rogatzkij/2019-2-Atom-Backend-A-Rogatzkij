#!/bin/bash

echo "Make links"
ln -s ./nginx/hw3.conf /etc/nginx/sites-available/hw3.com
rm -rf /var/www/hw3.com
cp -r ./nginx/hw3 /var/www/hw3.com

sudo ln -s /etc/nginx/sites-available/hw3.com /etc/nginx/sites-enabled/

echo "Restart nginx"
nginx -s reload

echo "Run gunicorn"
source ./hw3/bin/activate
cd ./sarvar
gunicorn --workers 4 main:cur_time

echo "All works done"