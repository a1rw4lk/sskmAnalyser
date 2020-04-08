include env.make

create-pip-env:
	pipenv install

setup:
	sudo -H pip install -U pipenv

activate-env: create-pip-env
	pipenv shell

run-app: create-pip-env
	pipenv run python src/sskmAnalyser.py
