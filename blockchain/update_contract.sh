#!/bin/bash

# Compile contracts
truffle console --network development

# Run migrations
migrate

exit