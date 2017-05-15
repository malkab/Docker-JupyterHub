#!/bin/bash

# Runs JupyterHub

docker run -d -v `pwd`:/src -p 8000:8000 --name test_jupyterhub malkab/jupyterhub:latest
