#!/usr/bin/env python

import os
import shutil
import sys

# append project directory to path so predict.py can be imported
sys.path.append('.')

os.system("mkdir models_cache")
os.system("cd models_cache")

os.system("git clone --branch fp16 https://huggingface.co/runwayml/stable-diffusion-v1-5")
os.system("cd stable-diffusion-v1-5")
os.system("apt-get install git-lfs")
os.system("git lfs install")
os.system("git lfs pull")
print("Now you should replace the vocab file in models_cache/stable-duffusion-v1-5/tokenizer")