# udacity_intro_to_hadoop_and_mapreduce
This repo has set of Map reduce jobs that I wrote for the assignments of this MOOC

## Important Commands for Cloudera VM

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.13.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input myinput -output myoutput

cat purchases_test | ./mapper.py | sort | ./reducer.py
