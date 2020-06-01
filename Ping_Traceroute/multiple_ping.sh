#!/usr/bin/env bash
for i in www.nsa.gov de.yahoo.com www.google.de
do
ping -p $i
done

