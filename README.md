# Pagurus

## Introduction

Pagurus is a container management system for serverless computing. It targets on reusing idle containers to help other functions alleviate the system-level cold startups. In Pagurus, contaienrs that created by it owner function is call Executor Container. Once the executor containers are identified as idle (e.g., not serving queries for 5 minutes), Pagurus will replace it with a Zygote Container. The Zygote Container is created from an image that installs the shared packages of all the to-be-helped functions. Once the to-be-helped function would experience the cold startup, Pagurus will fork a zygote container for it and avoid the time-consuming container creation, software environment setup, and dependencies preparation. The forked container in Pagurus is called Helper container.


## Getting Started

We provide a quick setup script to deploy Pagurus in your machine. To deploy Pagurus and prepare the related software dependicies:
```
git clone https://github.com/lzjzx1122/Pagurus.git
./install.sh
```
Then you can get start Pagurus by the following command:
```
xxxxxxx
```
Now Pagurus is successfully started and ready for serving function queries. You can send a query for test by the following command:
```
curl -X http://0.0.0.0:5000/listen -d {"action":"float_operation", "params": {'param': 1000000}}
```
and returns:
```
xxxxxxxxxxxxxxxxxxxx
```
All the invoked functions and results are logged in the CouchDB Server, and you can get the invocation results and traces by:
```
curl -X xxxxx
``` 

## Applications and Functions

We already provide several function benchmarks in Pagurus, such as FunctionBench, FaaSProfiler, simple version of aws-example-applications, and Azure trace mapping.

Each function should be define with a entry point with ```"def main(param):" ```. The packages needed for the function should also assigned in a **requirements.txt** along with the **main.py** or **.zip** file. These assigned packages and versions are maintained [here](https://github.com/lzjzx1122/Pagurus/blob/master/interaction_controller/build_file/aws_packages.json) in the json format like: 
```
"cer_lambda": {
        "requests": "2.25.1",
        "xlsxwriter": "1.4.0",
        "pandas": "0.24.2",
        "numpy": "1.16.6"
    },
```
Besides the functions, Pagurus also support the invocation of an application. The application contains several functions and follow a sequence or parallel logic to construt a complex business. 
It should be noticed that the functions and applications must be created and defined before being invoked in Pagurus. 

## Detailed Concepts and Related Components

![Pagurus](https://github.com/lzjzx1122/Pagurus/tree/master/pagurus_h.pdf "The Pagurus structure")

Pagurus contains three main components as shown in the figure: intra-function container manager, inter-function container scheduler, and sharing-aware function balancer. Serverless functions are running in Docker containers. The communication between them are thruogh REST APIs.

* [Proxy in Docker Container](https://github.com/lzjzx1122/Pagurus/tree/master/container)
* Inter-Function Container Scheduler
* [Intra-Function Container Manager](https://github.com/lzjzx1122/Pagurus/tree/master/intraaction_controller)
* [Sharing-aware Function Balancer](https://github.com/lzjzx1122/Pagurus/tree/master/load_balancer)
* CouchDB Server

Besides these components of Pagurrus, we also provide two additional prewarm-based policy in Pagurus: OpenWhisk-based Prewarm and SOCK-based Prewarm. You can find their prewarm manager [here](https://github.com/lzjzx1122/Pagurus/tree/master/intraaction_controller/prewarm_manger.py).

