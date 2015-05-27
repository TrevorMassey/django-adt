#!/bin/sh
!#/bin/bash

PROJECT_NAME=sptelephony

VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

su - vagrant -c "$VIRTUALENV_DIR/bin/python $PROJECT_DIR/manage.py syncdb --all --noinput"
su - vagrant -c "$VIRTUALENV_DIR/bin/python $PROJECT_DIR/manage.py migrate --fake"

su - vagrant -c "$VIRTUALENV_DIR/bin/python $PROJECT_DIR/manage.py init_defaults"
su - vagrant -c "$VIRTUALENV_DIR/bin/python $PROJECT_DIR/manage.py setupproject"