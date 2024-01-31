#from todoApp.app import create_app
#from todoApp.auth_app.models import User
def migrate():
    from todoApp.api.app import create_app, db
    from flask_migrate import upgrade, migrate, init, stamp
    from todoApp.auth_app.models import User

    app = create_app()
    app.app_context().push()

    db.create_all()

    init()
    stamp()
    migrate()
    upgrade()

migrate()
'''
def create_tables():
    app = create_app()
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
   i create_tables()
   '''
