"""
PinLearn LMS
Application Extensions

All Flask extensions are initialized here.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()

mail = Mail()

csrf = CSRFProtect()

cache = Cache()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200/day", "50/hour"]
)