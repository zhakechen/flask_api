from application import db, create_app
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager



def main():
    app = create_app('settings')

    # 迁移用
    migrate = Migrate(app, db)
    # 传输命令行参数用
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    manager.run()


if __name__ == '__main__':
    main()