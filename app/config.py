class Configuration:
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:1111@localhost/database1'
    SECRET_KEY='SECRET_KEY'

    ### flask security ###
    SECURITY_PASSWORD_SALT='$2b$12$ctTq5EgEL6MyWooqQGwCe..cGsgCpyXVN08QartxThUNRJRD/PIai]'
    SECURITY_PASSWORD_HASH='bcrypt'