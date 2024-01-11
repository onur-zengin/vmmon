#!/usr/bin/env python3

import os
import sys
import json
import boto3
from botocore.exceptions import ClientError


def put_secret(secret_name, region_name):

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        ...


def main(args):

    # Make an API call to AWS Secrets Manager using the command-line arguments (usage: ./putSecrets.py [secret_name] [region_name] [domain_name])
    secret      = put_secret(args[1], args[2])

    # If domain_name is provided, then update the Nginx configuration with it;
    if len(sys.argv) > 3:

        write_domain = "sed -i 's/DOMAIN.NAME/%s/g' ../configs/nginx/nginx.conf" % (args[3])

        try:    
            os.system(write_domain)
        except:
            print("Unknown error (3). Falling back to non-secure HTTP URL.")
            os.system(fallback)
            sys.exit(3)
    
    else:
        
        print("TLS certificate successfully uploaded.")


if __name__ == '__main__':
    main(sys.argv)
