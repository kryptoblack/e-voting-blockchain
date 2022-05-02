FROM node:16.14.2

RUN mkdir -p /app
WORKDIR /app

COPY . /app

# Install Packages
RUN yarn install

# Script to upload the contract
RUN chmod a+x update_contract.sh
