#!/bin/sh

apt update && apt upgrade && \
apt install sudo && \
sudo apt-get update && apt-get install -y software-properties-common && \
sudo add-apt-repository -y ppa:ethereum/ethereum && \
sudo apt-get update && apt-get install -y solc