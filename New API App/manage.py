from app import blueprint

from app.main import create_app

app = create_app()
app.app_context().push()

app.register_blueprint(blueprint)

if __name__ == '__main__':
	app.run()
