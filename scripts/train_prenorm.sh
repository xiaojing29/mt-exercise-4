#!/bin/bash

scripts=$(dirname "$0")
base=$(cd "$scripts"/.. && pwd)

models=$base/models
configs=$base/configs

mkdir -p $models

num_threads=7

SECONDS=0

logs=$base/logs

model_name=deen_transformer_prenorm

mkdir -p $logs

mkdir -p $logs/$model_name

OMP_NUM_THREADS=$num_threads python -m joeynmt train $configs/$model_name.yaml > $logs/$model_name/out 2> $logs/$model_name/err

echo "time taken:"
echo "$SECONDS seconds"
