#!/usr/bin/env python3

inventory = {
    "group": {
        "hosts": ["master4.example.com", "master5.example.com"],
        "vars": {
            "deployment_type": "openshift-enterprise",
            "ansible_ssh_user": "openshift",
            "ansible_become": "true"
        }
    },
    "_meta": {
        "hostvars": {
            "master4.example.com": {
                "openshift_hostname": "master4.example.com"
            },
            "master5.example.com": {
                "openshift_hostname": "master5.example.com"
            }
        }
    }
}

print inventory
