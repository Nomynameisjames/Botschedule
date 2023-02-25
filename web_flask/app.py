import os
from web_flask import create_app, db
from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, db)

@app.route('/test')
def make_shell_context():
    return dict(db=db)
