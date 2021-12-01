from app import blueprint

from app.main import App

app = App.create_app(App)
app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
	app.run()
