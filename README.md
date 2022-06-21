# Custom nbconvert Template
**nbconvert templates** can automate **styling** and **consistency** in your company's exported jupyter notebooks. To create your own, you can clone this package. If you'd like some instructions, you can follow my 10 minute [step-by-step guide]().

## 📦 Packaging
In my experience, nbconvert templates are most useful if **packaged**. This allows every team to access them 24/7. Clone this repository to get a ready-to-use template. Then modify it to fit your needs.

## ♻️ Workflow
This is the workflow I use at my company:

1. Store the package as a private GitHub repo.
2. Install it [using pip](https://docs.readthedocs.io/en/stable/guides/private-python-packages.html).
3. Convert notebook using the `--template` argument!