#!/bin/bash

N_SIZES=$(./get_bsize.py)

qsub job-bsize.pbs -t 1-$N_SIZES%5
