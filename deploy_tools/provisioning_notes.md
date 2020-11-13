Provisioning new site
======================

## Required packages:

* nginx
* python3
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo apt update
    sudo apt install nginx git python3 python3-venv
    
## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.geekpj.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.geekpj.com

## Folder structure:

Assume we have a user account at /home/username

    /home/username
    |___ sites
        |___ DOMAIN1
        |   |___ .env
        |   |___ db.sqlite3
        |   |___ manage.py etc
        |   |___ static
        |   |___ virtualenv
        |___ DOMAIN2
            |___ .env
            |___ db.sqlite3
            |___ etc