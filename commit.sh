#!/bin/bash
for i in {1..144}
do
	git add .
	git commit -m 'Updated daily algorithm week 6 mon'
	git push
	sleep 300
done
