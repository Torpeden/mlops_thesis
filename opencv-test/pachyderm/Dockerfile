FROM ubuntu:20.04

# Install python3.
RUN apt-get update -qqy \
    && apt-get install -qqy python3 python3-pip \
    && apt-get clean

# Check python3 version and install opencv and matplotlib.
RUN python3 --version && pip3 install opencv-python-headless matplotlib

# Add test code.
ADD opencv-test.py /opencv-test.py