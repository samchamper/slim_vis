#  Virtual environment
INVENV = . env/bin/activate ;

install: env

env:
	python3 -m venv env
	$(INVENV) pip3 install -r requirements.txt

run:	env
	($(INVENV) python3 slim_vis.py) ||  true

clean:
	rm -f *.pyc */*.pyc
	rm -rf __pycache__ */__pycache__

veryclean:
	make clean
	rm -rf env


