// build.sh
#!/usr/bin/env bash
# exit on error
set -o errexit

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt 

py manage.py migrate
