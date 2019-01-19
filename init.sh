#!/usr/bin/bash

sudo /etc/init.d/gunicorn stop test
sudo /etc/init.d/gunicorn stop gunicorn-django.conf

sudo rm /etc/nginx/sites-enabled/test.conf
sudo rm /etc/gunicorn.d/test
sudo rm /etc/gunicorn.d/gunicorn-django.conf
sudo rm /etc/nginx/sites-enabled/default

sudo pip3 uninstall gunicorn
sudo pip3 uninstall django
sudo pip3 install -r requirements.txt

sudo vi /usr/sbin/gunicorn-debian
sudo vi /usr/bin/gunicorn
sudo vi /usr/bin/gunicorn_django
sudo vi /usr/bin/gunicorn_paster

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/gunicorn-django.conf
sudo /etc/init.d/gunicorn restart test
sudo /etc/init.d/gunicorn restart gunicorn-django.conf
sudo /etc/init.d/mysql start
