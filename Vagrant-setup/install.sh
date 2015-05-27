#!/bin/bash

# Script to set up a Django project on Vagrant.

# Installation settings

PROJECT_NAME=$1

DB_NAME=$PROJECT_NAME
VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME
PROVISIONING_FLAG_DIR=/home/vagrant/provisioning/$PROJECT_NAME

PGSQL_VERSION=9.3

# Need to fix locale so that Postgres creates databases in UTF-8
cp -p $PROJECT_DIR/Vagrant-setup/conf/etc-bash.bashrc /etc/bash.bashrc

mkdir -p $PROVISIONING_FLAG_DIR

if [ ! -f $PROVISIONING_FLAG_DIR/provisioned_locales ]; then
    locale-gen en_GB.UTF-8
    dpkg-reconfigure locales

    export LANGUAGE=en_GB.UTF-8
    export LANG=en_GB.UTF-8
    export LC_ALL=en_GB.UTF-8

    date > "$PROVISIONING_FLAG_DIR/provisioned_locales"
fi

# Install essential packages from Apt
apt-get update -y
# Python dev packages
apt-get install -y build-essential python python-dev
# python-setuptools being installed manually
if ! command -v easy_install; then
    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
fi
# Dependencies for image processing with Pillow (drop-in replacement for PIL)
# supporting: jpeg, tiff, png, freetype, littlecms
# (pip install pillow to get pillow itself, it is not in requirements.txt)
apt-get install -y libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev
# Git (we'd rather avoid people keeping credentials for git commits in the repo, but sometimes we need it for pip requirements that aren't in PyPI)
apt-get install -y git

# Install project dependencies for audio transcoding (mpeg, aac)
apt-get install -y lame faad

# Setup Redis
apt-get install -y redis-server

# Setup RabbitMQ
apt-get install -y rabbitmq-server

# Enable RabbitMQ management plugin
rabbitmq-plugins enable rabbitmq_management

# Setup RabbitMQ
rabbitmqctl add_user $PROJECT_NAME $PROJECT_NAME
rabbitmqctl add_vhost $PROJECT_NAME
rabbitmqctl set_permissions -p $PROJECT_NAME $PROJECT_NAME ".*" ".*" ".*"

service rabbitmq-server restart


# Postgresql
if ! command -v psql; then
    sudo apt-get -y install python-software-properties
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    
    sudo sh -c "echo \"deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -c | awk '{print $2}'`-pgdg main\" >> /etc/apt/sources.list.d/postgresql.list"
    sudo apt-get update
    
    apt-get install -y postgresql-$PGSQL_VERSION libpq-dev
fi

cp $PROJECT_DIR/Vagrant-setup/conf/pg_hba.conf /etc/postgresql/$PGSQL_VERSION/main/
/etc/init.d/postgresql reload

# virtualenv global setup
if ! command -v pip; then
    easy_install -U pip
fi
if [[ ! -f /usr/local/bin/virtualenv ]]; then
    pip install virtualenv virtualenvwrapper stevedore virtualenv-clone
fi

# bash environment global setup
cp -p $PROJECT_DIR/Vagrant-setup/conf/bashrc /home/vagrant/.bashrc


# postgresql setup for project

sudo su - postgres -c "psql -c \"CREATE USER $PROJECT_NAME WITH PASSWORD '$PROJECT_NAME';\""
createdb -Upostgres -O $PROJECT_NAME $DB_NAME

# virtualenv setup for project
sudo su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project"

sudo su - vagrant -c "$VIRTUALENV_DIR/bin/pip install -r $PROJECT_DIR/requirements.txt"

echo "workon $VIRTUALENV_NAME" >> /home/vagrant/.bashrc

# Set execute permissions on manage.py, as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py
chmod a+x $PROJECT_DIR/worker.sh


sudo su - vagrant -c "$VIRTUALENV_DIR/bin/python $PROJECT_DIR/manage.py migrate"
# sudo su - vagrant -c "$VIRTUALENV_DIR/bin/python $PROJECT_DIR/manage.py projectsetup"
