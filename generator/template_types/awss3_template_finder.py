import boto3
from botocore.exceptions import ClientError
import logging

from cachetools import cached, TTLCache

from generator.singleton import Singleton
from generator.template import Template


class AWSS3Template(Template, metaclass=Singleton):

    def __init__(self, access_key: str, secret_key: str, bucket: str):
        """
        Init class which takes from s3
        :param access_key: AWS Access Key
        :param secret_key: AWS Secret Key
        :param bucket: Bucket Name
        """
        self.client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
        self.bucket = bucket

    @cached(cache=TTLCache(maxsize=10, ttl=100))
    def get_template_file(self, path: str) -> str:
        """
        Get template file from AWS S3 bucket
        :param path: S3 key path
        :return: str
        """


        try:
            meta_data = self.client.head_object(Bucket=self.bucket, Key=path)
            if meta_data["ContentType"] != 'text/html':
                raise Exception(f"Type template is not html found in bucket with key {path}")
        except ClientError:
            message = f"Specified key,{path} does not exist in {self.bucket}"
            logging.error(message)
            raise Exception(message)
            pass
        pass
        obj = self.client.get_object(Bucket=self.bucket, Key=path)
        template = obj['Body'].read().decode('utf-8')
        return template
