#!/usr/bin/env bash

for file1 in test_main.py
do
  echo "[test] $file1"
  python tests/$file1
done
