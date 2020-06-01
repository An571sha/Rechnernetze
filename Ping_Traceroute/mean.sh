#!/usr/bin/env bash
for ((i = 100 ; i <= 1400 ; i = i + 100)); do
    ping -l ${i} -n 10 www.google.in  | findstr Average >> result_mean.txt
done