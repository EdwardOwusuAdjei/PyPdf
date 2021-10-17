from io import BytesIO

import chevron
from xhtml2pdf import pisa

from generator.singleton import Singleton
from generator.targets import Targets
from generator.template_types.awss3_template_finder import AWSS3Template
from generator.template_types.ondisk_template_finder import OnDiskTemplate


class PDFGenerator(metaclass=Singleton):

    def __init__(self, aws_access_key=None, aws_secret_key=None, aws_bucket=None):
        """
        pass required values if using target
        :param aws_access_key: AWS access key
        :param aws_secret_key: AWS secret key
        :param aws_bucket: AWS bucket name
        """
        self.bucket = aws_bucket
        self.secret_key = aws_secret_key
        self.access_key = aws_access_key

    def generate(self, data: dict, key: str, target: Targets) -> bytes:
        template = ""
        if target == Targets.OnDisk:
            on_disk = OnDiskTemplate()
            template = on_disk.get_template_file(key)
        elif target == Targets.Amazon:
            if self.__validate(target):
                template_s3 = AWSS3Template(self.access_key, self.secret_key, self.bucket)
                template = template_s3.get_template_file(key)
            else:
                raise Exception("all values in AWS config not passed.")

        argument = {
            'template': template,
            'data': data
        }
        replaced_str = chevron.render(**argument)
        result = BytesIO()
        pisa.CreatePDF(
            replaced_str,
            dest=result)
        return result.getvalue()

    def __validate(self, target: Targets):
        if target == Targets.Amazon:
            return self.bucket and self.secret_key and self.secret_key
