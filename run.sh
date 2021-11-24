#!/usr/bin/env bash


start=1631188800
num_queries=10
script=$1

echo "-- running ${num_queries} queries in parallel ${script} ---"

for i in $(seq 1 $num_queries)
do

    if [[ $script = "t" ]]
    then
      time python python/query-traffic.py $start &
    elif [[ $script = 'p' ]]
    then
      time python python/query-pyopensky.py $start &
    else
      echo "Wrong arg...exiting"
      exit
    fi

   start=$(( start + 1800))
done


