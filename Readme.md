# PyPDF

Create PDF files from using html templates stored on disk or s3 (more source to come) and have parts of the templates replaced using [mustache](mustache.github.io)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install XXX.

```bash
pip install XXX-NOT-YET-THERE
```

## Usage

```python
from generator.main import set_aws_credentials, generate
from generator.targets import Targets


replacement_definition = {
        "name": "Hello World"
}

s3_key = "sample.html"

# set credential can be called once. These credentials are remembered.
set_aws_credentials(ACCESS_KEY, ACCESS_SECRET, BUCKET_NAME)
value = generate(replacement_definition, s3_key, Targets.Amazon)
# value contains pdf content
```

## Contributing
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)