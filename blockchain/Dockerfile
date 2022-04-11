FROM node:16.14.2

RUN mkdir -p /usr/src/blockchain
WORKDIR /usr/src/blockchain

COPY . /usr/src/blockchain

RUN npm install -g truffle
RUN npm install -g ganache

# Script to upload the contract
RUN chmod a+x update_contract.sh

ENTRYPOINT [ "ganache", "--db=/app/ganache_data", "--networkId", "'5777'", "--hostname", "'0.0.0.0'", "--port", "'7545'", "--mnemonic", "grape solution air laundry garage body erupt thought ritual renew ginger tackle" ]