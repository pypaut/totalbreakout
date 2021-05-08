OBJS = \
	   src/main.py \
	   src/Player.py \
	   src/Ball.py \
	   src/Block.py
BIN = src/main.py


all:
	python3 src/main.py

lint:
	black -l 79 ${OBJS}
	flake8 .
