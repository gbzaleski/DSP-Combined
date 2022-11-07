 
cat NC_010437.faa | grep ">" | wc -l
cat NC_002306.faa | grep ">" | wc -l

cat NC_002306.faa | grep "spike" > out1.txt
cat NC_010437.faa | grep "spike" > out2.txt

diff out1.txt out2.txt
