import os

from generator.pdf_generator import PDFGenerator
from generator.targets import Targets


def generate(data: dict, key: str, target: Targets) -> bytes:
    # one object used in lifetime
    instance = PDFGenerator()
    return instance.generate(data, key, target)


def set_aws_credentials(aws_access_key: str, aws_secret_key: str, aws_bucket: str):
    """
    pass credentials to instance.
    :param aws_access_key: AWS access key
    :param aws_secret_key: AWS secret key
    :param aws_bucket: AWS bucket name
    """

    # same instance using singleton
    PDFGenerator(aws_access_key=aws_access_key,
                 aws_secret_key=aws_secret_key,
                 aws_bucket=aws_bucket)

