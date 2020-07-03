from flask import render_template, g, url_for, request
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, has_access, IndexView
from werkzeug.utils import redirect
from flask_babel import _
from googletrans import Translator

from . import appbuilder, db, app

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

"""
https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd
"""
trans = Translator()


class HomePage(BaseView):
    route_base = "/home"

    @expose('/admin/')
    @has_access
    def admin(self):
        self.update_redirect()
        if not g.get('lang_code', None):
            g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
        return self.render_template('index.html', lang=g.lang_code, HOME=trans.translate('Home', dest=g.lang_code).text,
                                    FUNZIONI=trans.translate('Functions',
                                                             dest=g.lang_code).text,
                                    GESTIONE=trans.translate('Management',
                                                             dest=g.lang_code).text,
                                    CONFIG=trans.translate('Configuration',
                                                           dest=g.lang_code).text,
                                    FILEM=trans.translate('File Manager',
                                                          dest=g.lang_code).text)

    @expose('/user/')
    def user(self):
        self.update_redirect()
        if not g.get('lang_code', None):
            g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
        return self.render_template('all.html', title=_('Home'), FUNZ=trans.translate('Functions',
                                                             dest=g.lang_code).text, GEST=trans.translate('Managment',
                                                             dest=g.lang_code).text)


class Menu(BaseView):
    default_view = 'home'

    @expose('/')
    @has_access
    def home(self):
        self.update_redirect()
        if not g.get('lang_code', None):
            g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
        return self.render_template('index.html', lang=g.lang_code, HOME=trans.translate('Home', dest=g.lang_code).text,
                                    FUNZIONI=trans.translate('Functions',
                                                             dest=g.lang_code).text,
                                    GESTIONE=trans.translate('Management',
                                                             dest=g.lang_code).text,
                                    CONFIG=trans.translate('Configurations',
                                                           dest=g.lang_code).text,
                                    FILEM=trans.translate('File Manager',
                                                          dest=g.lang_code).text)

    @expose('/funzioni/')
    def funzioni(self):
        return self.render_template('pagine.html', Title=_('Funzioni'), Heading=_('Funzioni'))

    @expose('/gestione/')
    @has_access
    def gestione(self):
        self.update_redirect()
        return self.render_template('pagine.html', Title=_('Gestione'), Heading=_('Gestione'))

    @expose('/configurazione/')
    @has_access
    def configurazione(self):
        self.update_redirect()
        return self.render_template('pagine.html', Title=_('Configurazione'), Heading=_('Configurazione'))

    @expose('/filemanager/')
    @has_access
    def filemanager(self):
        self.update_redirect()
        return self.render_template('pagine.html', Title=_('Filemanager'), Heading=_('Filemanager'))


appbuilder.add_view_no_menu(HomePage())
appbuilder.add_view(Menu, "Home", category='Menu')
appbuilder.add_link(_("Funzioni"), href='/menu/funzioni/', category='Menu')
appbuilder.add_link(_("Gestione"), href='/menu/gestione/', category='Menu')
appbuilder.add_link(_("Configurazione"), href='/menu/configurazione/', category='Menu')
appbuilder.add_link(_("File Manager"), href='/menu/filemanager/', category='Menu')


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
