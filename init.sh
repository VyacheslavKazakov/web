#!/usr/bin/bash

sudo rm /etc/nginx/sites-enabled/test.conf
sudo rm /etc/gunicorn.d/test
sudo rm /etc/gunicorn.d/gunicorn-django.conf
sudo rm /etc/nginx/sites-enabled/default

sudo apt-get install python3-venv

if [ -d /home/box/venv]; then
  mkdir /home/box/venv
fi

python3 -m venv /home/box/venv
source /home/box/venv/bin/activate

pip3 install -r requirements.txt

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/gunicorn-django.conf
sudo /etc/init.d/gunicorn restart test
sudo /etc/init.d/gunicorn restart gunicorn-django.conf
sudo /etc/init.d/mysql start
