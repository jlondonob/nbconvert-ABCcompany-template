# Custom nbconvert Template
Improve the **styling** and **consistency** of your exported jupyter notebooks using nbconvert templates. Clone this repository to get a ready-to-use packaged template. You can find customization instructions in my 10 minute [step-by-step guide]().

## 📦 Packaging
Packaged templates are the most powerful. They are available for every person in your organization on a 24/7 basis. Clone this repository to get a ready-to-use packaged template. Then modify it to fit your needs.

## ♻️ Workflow with a packaged template
This is the workflow I use:

1. Store the package as a private GitHub repo.
2. Install it [using pip](https://docs.readthedocs.io/en/stable/guides/private-python-packages.html).
3. Start converting your notebooks using the `--template` argument.

```bash
# Install the template
pip install git+https://github.com/jlondonob/nbconvert-ABCcompany-template

# Convert notebook.ipynb
jupyter nbconvert --to html --template=ABCcompany notebook.ipynb
```