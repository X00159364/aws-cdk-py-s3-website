#!/usr/bin/env python3

from aws_cdk import core

from cdk_s3_website.cdk_s3_website_stack import CdkS3WebsiteStack


app = core.App()
CdkS3WebsiteStack(app, "cdk-py-s3-website")

app.synth()
