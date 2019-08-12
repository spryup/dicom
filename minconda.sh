#!/usr/bin/env bash

#wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh

#bash Miniconda2-latest-Linux-x86_64.sh # take care of the installation directory

#-q standard -W 5000
#-q shared_memory -W 10000
#-q long -W 20000

#cd
#conda remove mkl mkl-service -y
#conda install nomkl -y
conda install pip numpy scipy scikit-learn matplotlib pandas -y

conda install cython nltk pymongo pandas opencv
pip install lda jupyter pydicom Pillow docx2txt plotly google-cloud-vision google-cloud google-cloud-storage google-cloud-datastore
#conda install -c conda-forge google-cloud-sdk google-api-python-client
pip install git+https://github.com/hlin117/mdlp-discretization

#conda install mkl -y
#pip install --upgrade pip


