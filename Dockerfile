FROM ubuntu:20.04

# Install python3.
RUN apt-get update -qqy \
    && apt-get install -qqy python3 python3-pip \
    && apt-get clean

# Check python3 version and install tensorflow.
RUN python3 --version && pip3 install tensorflow tensorflow_datasets

# Add test code.
ADD mnist-test.py /mnist-test.py