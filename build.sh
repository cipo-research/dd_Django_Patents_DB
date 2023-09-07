#!/usr/bin/env bash
# exit on error
#set -o errexit

ls ../
source ../Scripts/activate
python manage.py migrate