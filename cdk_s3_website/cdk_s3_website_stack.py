from aws_cdk import core
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_s3_deployment

class CdkS3WebsiteStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        bucket = _s3.Bucket(self, id + "_s3-bucket",
            bucket_name= ('cdk-py-s3-static-website'),
            website_index_document= 'index.html',
            website_error_document= 'error.html',
            public_read_access= True,
            removal_policy= core.RemovalPolicy.DESTROY)  

        aws_s3_deployment.BucketDeployment(self, "DeployWebsite",
            sources=[aws_s3_deployment.Source.asset("./www")],
            destination_bucket=bucket,
            destination_key_prefix="web/static"
        )
