#!/bin/bash
# Démarrer Nginx
service nginx start

# Démarrer Gunicorn
gunicorn door_django.wsgi:application --bind 0.0.0.0:8000