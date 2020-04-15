include env.make

create-pip-env:
	pipenv install --python=python3

setup:
	sudo python3 -m pip install pyqt5==5.14
	sudo apt-get install pyqt5-dev-tools
	sudo apt-get install qttools5-dev-tools
	sudo -H pip install -U pipenv

activate-env: create-pip-env
	pipenv shell

run-app: create-pip-env
	pipenv run python src/sskmAnalyser.py
