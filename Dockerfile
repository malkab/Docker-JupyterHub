FROM ubuntu:latest

LABEL maintainer="Juan Pedro Perez"
LABEL email="jp.perez.alcantara@gmail.com"

# Base packages for JupyterHub
RUN apt-get update

RUN apt-get install -y python3 npm nodejs-legacy python3-pip libgeos-dev graphviz

RUN npm install -g configurable-http-proxy

RUN pip3 install jupyterhub

RUN pip3 install --upgrade notebook

EXPOSE 8000

# Additional packages
RUN pip3 install numpy pandas matplotlib geopandas seaborn ipywidgets tqdm folium sklearn pydotplus

# Add notebooks
ADD Assets/notebooks /Notebooks

# Add users
ADD Assets/JupyterHub-Setup.sh /setup.sh
RUN /setup.sh

# Add configuration
ADD Assets/jupyterhub_config.py /jupyterhub_config.py

# Add SSL keys
ADD Assets/SSL-Certificate /SSL-Certificate

ENTRYPOINT ["jupyterhub", "-f", "/jupyterhub_config.py"]
