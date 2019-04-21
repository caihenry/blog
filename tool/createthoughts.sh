#!/bin/bash
#shellpath=`dirname $0`
now_str=`date "+%Y%m%d%H%M%S"` 
newfile=$now_str'.txt'
echo $now_str > $newfile
vim $newfile
