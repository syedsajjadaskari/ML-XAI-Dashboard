echo [$(date)]: "START"
echo [$(date)]: "creating env with python 3.12 version"
virtualenv venv --python=python3.11
echo [$(date)] "Activationg the dev envirnmnets"
. venv/bin/activate
echo [$(date)]: "installing the  dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"