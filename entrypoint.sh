#!/bin/sh -l

echo "Hello, world"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT
