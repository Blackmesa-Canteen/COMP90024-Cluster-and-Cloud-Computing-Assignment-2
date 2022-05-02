#!/bin/bash

ansible-playbook -i ./inventory/host_ip_file.ini -u ubuntu --key-file=./.ssh/MRC-group52.pem prepare-instance.yaml