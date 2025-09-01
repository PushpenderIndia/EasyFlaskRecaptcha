<h1 align="center">EasyFlaskRecaptcha</h1>

<h2 align="center">EasyFlaskRecaptcha is a python Module which makes Google Recaptcha Integration in flask application easy</h2>

<p align="center">
<a href="https://pypi.org/project/easyflaskrecaptcha/"><img alt="pypi" src="https://img.shields.io/pypi/v/easyflaskrecaptcha.svg"></a>
<a href="https://pepy.tech/project/easyflaskrecaptcha?versions=1*&versions=2*&versions=3*"><img alt="Downloads" src="https://pepy.tech/badge/easyflaskrecaptcha"></a>
<a href="https://pepy.tech/project/easyflaskrecaptcha?versions=1*&versions=2*&versions=3*"><img alt="Downloads" src="https://pepy.tech/badge/easyflaskrecaptcha/month"></a>
<a href="https://github.com/PushpenderIndia/EasyFlaskRecaptcha/commits/main"><img alt="GitHub lastest commit" src="https://img.shields.io/github/last-commit/PushpenderIndia/EasyFlaskRecaptcha?color=blue&style=flat-square"></a>
</p>

--------------------------------------------------------------------------

## Installation

```
pip install EasyFlaskRecaptcha
```

### Implementation
```
from flask import Flask
from EasyFlaskRecaptcha import ReCaptcha

app = Flask(__name__)
recaptcha = ReCaptcha(app)

app.config.update(dict(
    GOOGLE_RECAPTCHA_ENABLED=True,
    GOOGLE_RECAPTCHA_SITE_KEY="6Lf74pUpXXXXXXXXXXXXXXXi012KXXXX7KB-31XXXH",
    GOOGLE_RECAPTCHA_SECRET_KEY="6LXXXXXXXXXXAFX-ZAXXXXXGSd-y5g0o-JZXXXXB"
))
recaptcha.init_app(app)
```
    
## Flask Template Usage Example (Frontend)
```
Description: Use {{ recaptcha }} Tag inside form tag
```

```
<form method="post" action="/submit">
    ...
    {{ recaptcha }}

    [submit]
</form>
```

## Flask Backend Route Example
```
@route("/submit", methods=["POST"])
def submit():
    if recaptcha.verify():
        print("SUCCESS") 
            
    else:
        print("FAILED")
```

## Default Settings
```
GOOGLE_RECAPTCHA_ENABLED = True
GOOGLE_RECAPTCHA_THEME = "light"
GOOGLE_RECAPTCHA_TYPE = "image"
GOOGLE_RECAPTCHA_SIZE = "normal"
GOOGLE_RECAPTCHA_LANGUAGE = "en"
GOOGLE_RECAPTCHA_TABINDEX = 0
```

## More Settings

```
GOOGLE_RECAPTCHA_ENABLED = True
GOOGLE_RECAPTCHA_SITE_KEY = ""
GOOGLE_RECAPTCHA_SECRET_KEY = ""
GOOGLE_RECAPTCHA_THEME = "light"
GOOGLE_RECAPTCHA_TYPE = "image"
GOOGLE_RECAPTCHA_SIZE = "normal"
GOOGLE_RECAPTCHA_LANGUAGE = "en"
GOOGLE_RECAPTCHA_TABINDEX = 10
```

Apply these settings like this:
```
from flask import Flask
from EasyFlaskRecaptcha import ReCaptcha

app = Flask(__name__)
recaptcha = ReCaptcha(app)

app.config.update(dict(
    GOOGLE_RECAPTCHA_ENABLED=True,
    GOOGLE_RECAPTCHA_SITE_KEY="6Lf74pUpXXXXXXXXXXXXXXXi012KXXXX7KB-31XXXH",
    GOOGLE_RECAPTCHA_SECRET_KEY="6LXXXXXXXXXXAFX-ZAXXXXXGSd-y5g0o-JZXXXXB",
    GOOGLE_RECAPTCHA_THEME = "light",
    GOOGLE_RECAPTCHA_TYPE = "image",
    GOOGLE_RECAPTCHA_SIZE = "normal",
    GOOGLE_RECAPTCHA_LANGUAGE = "en",
    GOOGLE_RECAPTCHA_RTABINDEX = 10,
))
recaptcha.init_app(app)
```

- Figure out your desired language code (such as for english, language code is en) from this link: [Google Recaptcha Language Codes](https://developers.google.com/recaptcha/docs/language)
- Set this parameter: `GOOGLE_RECAPTCHA_LANGUAGE = "en"`

## Link:

* [Google Recaptcha Language Codes](https://developers.google.com/recaptcha/docs/language)
* [Documentation](https://github.com/PushpenderIndia/EasyFlaskRecaptcha)
* [PyPI](https://pypi.org/project/EasyFlaskRecaptcha/)

## License

This project is licensed under the MIT License (see the `LICENSE` file for details).
