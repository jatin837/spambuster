# spambuster
a spam detector 


# Download data
```sh
bash data.sh
```

# Setup the Project
```sh
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```
## Temp
```console

click win prize																						y
click meeting setup meeting																n
prize free prize																					y
click prize free																					y

free setup meeting free																		?

===============================================================================
P(S) = 3/4
P(NS) = 1/4
===============================================================================

/=========================================\
|How to represente this in data structure?|
\=========================================/

=============
click		=> 0
free		=> 1
meeting => 2
prize   => 3
setup		=> 4
win			=> 5
=============

data = [
	[
		[0, 1], 
		[5, 1], 
		[3, 1]
	],

	[
		[0, 1],
		[2, 2],
		[4, 1]
	],

	[
		[3, 2],
		[1, 1]
	], 

	[
		[1, 2],
		[2, 1],
		[4, 1]
	]
]
```

