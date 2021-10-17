import os

from generator.main import set_aws_credentials, generate
from generator.targets import Targets

ACCESS_KEY = ""
ACCESS_SECRET = ""
BUCKET_NAME = ""


def test_s3():
    replacement_definition = {
        "name": "Hello World"
    }
    s3_key = "sample.html"
    # set credential can be called once. These stuff are remembered if used as a package
    set_aws_credentials(ACCESS_KEY, ACCESS_SECRET, BUCKET_NAME)
    value = generate(replacement_definition, s3_key, Targets.Amazon)

    assert type(value) == bytes
    # uncomment is you want a sample file
    # location = os.path.realpath(
    #     os.path.join(os.getcwd(), os.path.dirname(__file__)))
    # with open(os.path.join(location, "test.pdf"), 'wb') as b:
    #     b.write(value)


def test_object_instance():
    replacement_definition = {
        "name": "Hello World"
    }
    s3_key = "sample.html"

    set_aws_credentials(ACCESS_KEY, ACCESS_SECRET, BUCKET_NAME)
    value = generate(replacement_definition, s3_key, Targets.Amazon)
    value2 = generate(replacement_definition, s3_key, Targets.Amazon)
    assert value == value2

