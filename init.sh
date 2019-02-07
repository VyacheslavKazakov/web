#!/usr/bin/bash

sudo rm /etc/nginx/sites-enabled/test.conf
sudo rm /etc/gunicorn.d/test
sudo rm /etc/gunicorn.d/gunicorn-django.conf
sudo rm /etc/nginx/sites-enabled/default

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/gunicorn-django.conf
sudo /etc/init.d/gunicorn restart test
sudo /etc/init.d/gunicorn restart gunicorn-django.conf
sudo /etc/init.d/mysql start

###
sudo mysql -uroot -e "CREATE DATABASE IF NOT EXISTS stepik DEFAULT CHARACTER SET = utf8"
sudo mysql -uroot -e "CREATE USER djanga@localhost auth_option: { IDENTIFIED BY 'dj_pass' }"
sudo mysql -uroot -e "GRANT ALL ON stepik.* TO djanga@localhost"
