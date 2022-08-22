[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# netbox-initializers

This repository contains `yaml` and `csv` files used to import various object types into [NetBox](https://github.com/netbox-community/netbox)

## Building the csv files from the yaml sources

The csv files are built from git hooks but this may be useful for local generation

1. It is recommended that you setup your own ["virtual environment"](https://docs.python.org/3/library/venv.html)
2. Install requirements:
    ```
    pip install -r requirements.txt
    ```
2. Execute the build process
    ```
    venv~> ./build_csv_files.py
    ```

## Pre-commit

Run `pre-commit install` to install pre-commit into your git hooks. pre-commit will now run on every commit.

If you want to manually run all pre-commit hooks on a repository, run `pre-commit run --all-files`. To run individual hooks use pre-commit run <hook_id>.

The first time pre-commit runs on a file it will automatically download, install, and run the hook. Note that running a hook for the first time may be slow. For example: If the machine does not have a specific python package installed, pre-commit will download and install it.
