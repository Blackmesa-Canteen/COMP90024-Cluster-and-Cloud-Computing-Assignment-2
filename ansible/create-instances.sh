#!/bin/bash

. ./unimelb-COMP90024-2022-grp-52-openrc.sh; ansible-playbook -i ./inventory/host_file.ini --ask-become-pass create-instances.yaml