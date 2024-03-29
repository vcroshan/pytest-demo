#!/bin/bash

for i in `ls -d */`; do
	lobfldrs+=(${i#/})
done

for fldr in ${lobfldrs[@]}; do
	for i in `ls -d ${fldr}tests/*`; do
		testfldr+=(${i#/})
	done
done
echo ${testfldr[@]}

for i in ${testfldr[@]}; do
	echo "executing test cases from folder ${i}"
	$HOME/bin/python3 -m pytest --cov-report xml $i
done
