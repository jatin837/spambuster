test: test/*
	./app -i test/test.txt
	./app -i test/test2.txt
	./app -i test/test3.txt

api: serv
	./serv
