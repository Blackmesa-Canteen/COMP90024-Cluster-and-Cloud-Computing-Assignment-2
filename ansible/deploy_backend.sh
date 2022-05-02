#!/bin/bash

ansible-playbook -i ./inventory/host_ip_file.ini -u ubuntu --key-file=./.ssh/MRC-group52.pem deploy_backend.yaml