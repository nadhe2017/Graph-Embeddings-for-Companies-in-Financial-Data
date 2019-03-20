#!/bin/sh
cd code
source activate tf27
source ~/.bashrc
# python test.py
python train.py
python auc.py
