class Config:
	SECRET_KEY = 'ad1c409a05615a548657b90ae138d677'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 465
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')