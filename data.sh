wget -O enron1.tar.gz http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron1.tar.gz

mkdir -p dat/
tar -xvf enron1.tar.gz -C dat/

rm enron1.tar.gz
