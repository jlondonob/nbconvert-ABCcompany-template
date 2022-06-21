# A custom nbconvert template
This is an example of how to package an nbconvert template. Use this repo to create your own pip-installable template.

## Structure of the package
Te package is structured as follows:
```
├── README.md
├── pyproject.toml
├── setup.cfg
├── setup.py
└── share
    └── jupyter
        └── nbconvert
            └── templates
                └── ACBcompany
                    ├── conf.json
                    ├── logo.svg
                    ├── index.html.j2
                    └── static
                        └── index.css
```

## Installation
To install this template create a vitrual environment and then pip install it from GitHub.
```bash
pip install git+https://github.com/jlondonob nbconvert-ABCcompany-template
```

## Usage
Add the `--template==ABCcompany` option to your export commond.

```bash
jupyter nbconvert mynotebook.ipynb --to html --template=ACBcompany
```
