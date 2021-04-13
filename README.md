# python-experiments

Where I test things about python...

## building the package

This command builds and installs the package to a custom directory for AWS Lambda

```shell
docker run -v "$PWD":/var/task "lambci/lambda:build-python3.7" /bin/sh -c "pip install . -t python/lib/python3.7/site-packages/; exit"
```

## dataThings.py

### testing

```shell
# start a pyenv shell
pipenv shell
# enable develop mode
# this creates some symbolic links to load 
# files on the sys.path
python setup.py develop
# run test
python -m pytest tests/test_dataThings.py
```

