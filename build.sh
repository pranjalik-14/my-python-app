#!/bin/bash
rm deployment.zip
. .venv/bin/acivate
pip freeze > requirements.txt
pyton manage.py collectstatic --noinput
zip -r deployment.zip . -x "*.git*" "*.venv*"