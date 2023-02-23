// build.sh
#!/usr/bin/env bash
# exit on error
set -o errexit

sudo apt-get update
sudo apt-get install python3
python3 --version


python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt 

python3 manage.py migrate
