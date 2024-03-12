from setuptools import setup

# python setup.py bdist_wheel sdist
# twine upload dist/*

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='EasyFlaskRecaptcha',
    version='1.0.2',
    url='https://github.com/pushpenderindia/EasyFlaskRecaptcha',
    license='MIT License',
    author='Pushpender Singh',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='pushpendersingh@protonmail.com',
    keywords=['flaskrecaptcha', 'flask', 'recaptcha', "google", 'python'],
    description=u'Easy Integration of Google Recaptcha in Flask',
    install_requires=['requests', 'MarkupSafe'],
    )