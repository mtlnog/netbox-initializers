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