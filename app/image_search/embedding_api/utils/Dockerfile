# FROM python:3.10

# RUN mkdir /workspace
# COPY . /workspace/

# WORKDIR /workspace
# RUN apt-get update && apt-get install -y git
# RUN pip install -r requirements.txt
# RUN mkdir -p ~/miniconda3 &&\
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh &&\
# bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 &&\
# rm -rf ~/miniconda3/miniconda.sh &&\
# ~/miniconda3/bin/conda init bash &&\
# ~/miniconda3/bin/conda init zsh
# RUN conda install pytorch torchvision torchaudio cpuonly -c pytorch


# ENV HOME=/workspace

# CMD [ "python" , "main.py" ]


FROM continuumio/miniconda3:latest

WORKDIR /workspace

# Copy the environment.yml file
COPY environment.yml .

# Install git and build essentials
RUN apt-get update && apt-get install -y git build-essential

# Create a new conda environment from the environment.yml file
RUN conda env create -f environment.yml

# Activate the conda environment
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

RUN conda install pytorch torchvision torchaudio cpuonly -c pytorch
# Copy the rest of your application
COPY . .

# Set the default command to run your application
CMD ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "main.py"]