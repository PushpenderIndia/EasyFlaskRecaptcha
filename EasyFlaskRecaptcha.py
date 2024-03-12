from markupsafe import Markup
import requests

class default(object):
    ENABLED = True
    THEME = "light"
    TYPE = "image"
    SIZE = "normal"
    LANGUAGE = "en"
    TABINDEX = 0

class ReCaptcha(object):
    VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
    site_key = None
    secret_key = None
    enabled = False

    def __init__(self, app=None, site_key=None, secret_key=None, enabled=True, **kwargs):
        if site_key:
            self.site_key = site_key
            self.secret_key = secret_key
            self.enabled = enabled
            self.theme = kwargs.get('theme', default.THEME)
            self.type = kwargs.get('type', default.TYPE)
            self.size = kwargs.get('size', default.SIZE)
            self.language = kwargs.get('language', default.LANGUAGE)
            self.tabindex = kwargs.get('tabindex', default.TABINDEX)

        elif app:
            self.init_app(app=app)

    def init_app(self, app=None):
        self.__init__(site_key=app.config.get("GOOGLE_RECAPTCHA_SITE_KEY"),
                      secret_key=app.config.get("GOOGLE_RECAPTCHA_SECRET_KEY"),
                      enabled=app.config.get("GOOGLE_RECAPTCHA_ENABLED", default.ENABLED),
                      theme=app.config.get("GOOGLE_RECAPTCHA_THEME", default.THEME),
                      type=app.config.get("GOOGLE_RECAPTCHA_TYPE", default.TYPE),
                      size=app.config.get("GOOGLE_RECAPTCHA_SIZE", default.SIZE),
                      language=app.config.get("GOOGLE_RECAPTCHA_LANGUAGE", default.LANGUAGE),
                      tabindex=app.config.get("GOOGLE_RECAPTCHA_TABINDEX", default.TABINDEX))

        @app.context_processor
        def get_code():
            return dict(recaptcha=Markup(self.get_code()))

    def get_code(self):
        return "" if not self.enabled else ("""<script src='//www.google.com/recaptcha/api.js?hl={LANGUAGE}'></script>
                                                <div class="g-recaptcha" data-sitekey="{SITE_KEY}" data-theme="{THEME}" data-type="{TYPE}" data-size="{SIZE}"\
                                                data-tabindex="{TABINDEX}"></div>
                                                """.format(SITE_KEY=self.site_key, THEME=self.theme, TYPE=self.type, SIZE=self.size, LANGUAGE=self.language, TABINDEX=self.tabindex))

    def verify(self, response=None, remote_ip=None):
        if self.enabled:
            data = {
                "secret": self.secret_key,
                "response": response or requests.form.get('g-recaptcha-response'),
                "remoteip": remote_ip or requests.environ.get('REMOTE_ADDR')
            }
            r = requests.get(self.VERIFY_URL, params=data)
            return r.json()["success"] if r.status_code == 200 else False
        return True
