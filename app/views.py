from flask import render_template, g, url_for
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, has_access, IndexView
from werkzeug.utils import redirect

from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


class HomePage(BaseView):
    route_base = "/home"

    @expose('/admin/')
    def admin(self):
        return self.render_template('index.html')

    @expose('/user/')
    def user(self):
        return self.render_template('all.html')


class Menu(BaseView):
    default_view = 'home'

    @expose('/')
    @has_access
    def home(self):
        self.update_redirect()
        return self.render_template('index.html', Title='Ciao')

    @expose('/funzioni/')
    def funzioni(self):
        return self.render_template('pagine.html', Title='Funzioni', Heading='Funzioni')

    @expose('/gestione/')
    @has_access
    def gestione(self):
        self.update_redirect()
        return self.render_template('pagine.html', Title='Gestione', Heading='Gestione')

    @expose('/configurazione/')
    @has_access
    def configurazione(self):
        self.update_redirect()
        return self.render_template('pagine.html', Title='Configurazione', Heading='Configurazione')

    @expose('/filemanager/')
    @has_access
    def filemanager(self):
        self.update_redirect()
        return self.render_template('pagine.html', Title='Filemanager', Heading='Filemanager')


appbuilder.add_view_no_menu(HomePage())
appbuilder.add_view(Menu, "Home", category='Menu')
appbuilder.add_link("Funzioni", href='/menu/funzioni/', category='Menu')
appbuilder.add_link("Gestione", href='/menu/gestione/', category='Menu')
appbuilder.add_link("Configurazione", href='/menu/configurazione/', category='Menu')
appbuilder.add_link("File Manager", href='/menu/filemanager/', category='Menu')


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
