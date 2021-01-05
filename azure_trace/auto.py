import os
import signal
import time
from multiprocessing import Process
import subprocess

actions = [ "image", "map_reduce", "couchdb_test"]
# actions = ["video", "network", "linpack", "disk", "float_operation", "k-means", "markdown2html", "matmul", "image", "map_reduce", "couchdb_test"]
# iteration = {'video': [7], "float_operation":[8], "k-means": [8], "matmul": [8], "markdown2html":[8], 'image':[8], "map_reduce": [8],  "network": [8],  "linpack":[8], "disk":[8], "couchdb_test":[8]}
# iteration = {"video":[7], "map_reduce":[9], "couchdb_test":[9]}
for action in actions:
    for i in range(10, 11):
        dir = 'results/' + action + '/' + str(i)
        os.system('cp ' + dir + '/action_config.yaml ' + '../intraaction_controller/action_config.yaml')
        os.system('python3 ../interaction_controller/test_inter/init.py')
        inter = subprocess.Popen(['python3', '../interaction_controller/inter_controller.py'])
        time.sleep(360)
        intra = subprocess.Popen(['sudo', '/home/openwhisk/anaconda3/bin/python3', '/home/openwhisk/gls/intraaction_controller/proxy.py', str(5001)])
        time.sleep(30)
        os.system('python3 run.py ' + dir + '/set.json')
        time.sleep(30)
        os.system('sudo kill -9 ' + str(inter.pid))
        os.system('./kill.sh ' + str(intra.pid))
        os.system('python3 get_results.py ' + dir)
        time.sleep(30)
        '''
        dir = 'results/' + action + '/' + str(i)
        os.system('cp ' + dir + '/action_config.yaml ' + '../intraaction_controller/action_config.yaml')
        os.system('python3 ../interaction_controller/test_inter/init.py')
        inter = subprocess.Popen(['python3', '../interaction_controller/inter_controller.py'])
        # time.sleep(300)
        intra = subprocess.Popen(['sudo', '/home/openwhisk/anaconda3/bin/python3', '/home/openwhisk/gls/intraaction_controller/proxy.py', str(5001)])
        time.sleep(30)
        os.system('python3 run.py ' + dir + '/set.json')
        time.sleep(30)
        os.system('sudo kill -9 ' + str(inter.pid))
        os.system('./kill.sh ' + str(intra.pid))
        os.system('mkdir ' + dir + '_')
        os.system('python3 get_results.py ' + dir + '_')
        time.sleep(30)
        '''