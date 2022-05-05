#!/bin/bash

. ./unimelb-COMP90024-2022-grp-52-openrc.sh; ansible-playbook -i ./inventory/host_file.ini -u ubuntu --key-file=./.ssh/MRC-group52.pem --ask-become-pass ansible_bootstrap.yaml