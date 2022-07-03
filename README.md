# Custom nbconvert template
Improve **styling** and **consistency** in your exported jupyter notebooks. Clone this repository to get a ready-to-use packaged template. You can learn to cusomize it in my 10 minute [step-by-step guide]().

![template_example](https://user-images.githubusercontent.com/43001823/177047693-483eae3c-cc84-4e0f-89ec-40701ffacab3.png)

## 📦 Packaging
Packaged templates are the most powerful. They are available for every person in your organization on a 24/7 basis. Clone this repository to get a ready-to-use packaged template, then modify it to fit your needs.

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
