#!/bin/bash

ansible-playbook -i ./inventory/host_file.ini -u ubuntu --key-file=./.ssh/MRC-group52.pem deploy_frontend.yaml