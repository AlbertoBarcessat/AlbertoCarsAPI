# create a virtual environment
python -m venv .venv

# run api
python main.py

# run tests
cd tests
python -m unittest

# get swagger
http://127.0.0.1:5000/swagger.json

# get swagger ui
http://127.0.0.1:5000/swagger-ui/

# try api
http://127.0.0.1:5000/cars