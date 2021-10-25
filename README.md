# spambuster
![spam filter](./logo.png)

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

# Usage(TESTING)
First setup the project
Then

```sh
make test
```
### Content of test(OUTPUT = 0.40 % Chance of being a spam)
```vi
Subject: flat screens
hello ,
please call or contact regarding the other flat screens requested .
trisha tlapek - eb 3132 b
michael sergeev - eb 3132 a
also the sun blocker that was taken away from eb 3131 a .
trisha should two monitors also michael .
thanks
kevin moore
```
### Content of test 2(OUTPUT = 99.99 % Chance of being a spam)
```vi
Subject: let ' s stop the mlm insanity !
still believe you can earn $ 100 , 000 fast in mlm ? get real !
get emm , a brand new system that replaces mlm with something that works !
start earning 1 , 000 ' s now ! up to $ 10 , 000 per week doing simple online tasks .
free info - breakfree @ luxmail . com - type " send emm info " in the subject box .
this message is sent in compliance of the proposed bill section 301 . per section 301 , paragraph ( a ) ( 2 ) ( c ) of s . 1618 . further transmission to you by the sender of this e - mail may be stopped at no cost to you by sending a reply to : " email address " with the word remove in the subject line .
```

# Usage(General)
Setup the project, then use cl interface
```sh
./app -i <INPUT PATH TO THE TEXT FILE>
```
# Serve REST API
in the root of the project, first activate the vertual environment
```sh
source env/bin/activate
```
then either use
```sh
make api
```
or
```
./serv
 ```
