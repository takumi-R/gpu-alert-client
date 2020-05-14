#!/usr/bin/env python3
import os
from slackclient import SlackClient
import subprocess
import json
import re
import requests
url_gpu = os.environ.get("URL_GPU")
gpu_id = os.environ.get("GPU_ID")
statusFinding = subprocess.Popen(
                    ['nvidia-smi', '--query-gpu=memory.used,memory.total,', '--format=csv'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
currentStatus = statusFinding.stdout.read().decode()
currentStatus = re.split(',|\n', currentStatus)
gpu_mem = []
gpu_mem_free = []

for i in range(1,len(currentStatus) // 2):
               gpu_mem.append(int(currentStatus[2 * i ].split(' ')[0]))
               gpu_mem_free.append(int(currentStatus[2 * i + 1].split(' ')[1]))

statusFinding = subprocess.Popen(
                    ['hostname'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
host_name = statusFinding.stdout.read().decode()

str_json = {'gpu_id':gpu_id, 'gpu_size': gpu_mem, 'gpu_mem': gpu_mem_free,'name':host_name}
r = requests.post(url_gpu, json=str_json)

