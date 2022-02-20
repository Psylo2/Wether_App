from flask import Flask
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)


from presentation.controllers import city_blueprint

from infrastructure.adapters import repository

from application.core import Factory, AppConfigurations
from application.handlers import CityHandler


app = Flask(__name__,
            static_folder='presentation/gui/static',
            template_folder='presentation/gui/templates')

AppConfigurations(app=app)

repository.init_app(app=app)

factory = Factory()
city_handler = CityHandler(factory=factory)
city_blueprint.handler = city_handler


app.register_blueprint(blueprint=city_blueprint)


@app.before_first_request
def create_tables():
    repository.create_all(app=app)


if __name__ == '__main__':
    app.run(debug=False)
