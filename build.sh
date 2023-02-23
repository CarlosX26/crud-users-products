// build.sh
#!/usr/bin/env bash
# exit on error
set -o errexit

python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt 

python3 manage.py migrate
