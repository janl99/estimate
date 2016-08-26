#!/usr/bin/env python
# -*- coding:utf8 -*-
import os, sys
from flask_script import Manager, Server,Shell
from flask_migrate import Migrate,MigrateCommand
from estimate import app,db

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db)

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = 5000)
)

manager.add_command("run", Server(
    use_debugger = True,
    use_reloader = True,
    host = '192.168.2.100',
    port = 8000)
)



if __name__ == "__main__":
    manager.run()
