FROM node:21
WORKDIR /usr/blockchain
RUN apt upgrade && apt update && apt install -y software-properties-common python3 python3-pip python3-launchpadlib nano && rm -rf /var/lib/apt/lists/*
RUN npm install --save ethers
RUN pip3 install web3 py-solc-x python-dotenv --break-system-packages
RUN pip3 install django-cors-headers --break-system-packages
COPY config/requirements.txt .
RUN pip3 install -r requirements.txt --break-system-packages
#RUN add-apt-repository ppa:ethereum/ethereum -y && apt update
COPY solx.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/solx.sh
# RUN apt-get update && apt-get install -y software-properties-common
# RUN add-apt-repository -y ppa:ethereum/ethereum
# RUN apt-get update 
# RUN apt-get install -y solc
WORKDIR /
RUN django-admin startproject blockchainTestProject
WORKDIR /blockchainTestProject
RUN python3 manage.py startapp blockchainTestApp
COPY configBlockchainTestProject/settings.py ./blockchainTestProject
COPY configBlockchainTestProject/urls.py ./blockchainTestProject
COPY configBlockchainTestApp/__init__.py ./blockchainTestProject
COPY configBlockchainTestApp/.env ./blockchainTestProject
COPY configBlockchainTestApp/admin.py ./blockchainTestApp
COPY configBlockchainTestApp/models.py ./blockchainTestApp
COPY configBlockchainTestApp/urls.py ./blockchainTestApp
COPY configBlockchainTestApp/views.py ./blockchainTestApp
COPY configBlockchainTestApp/trans.sol ./blockchainTestApp
COPY configBlockchainTestApp/compile_sepo.py ./blockchainTestApp
COPY configBlockchainTestApp/deploy_sepo.py ./blockchainTestApp
COPY config/manage.py .
COPY config/.env .
COPY config/entrypoint.sh .
CMD ./entrypoint.sh