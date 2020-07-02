from flask import g, url_for
from flask_appbuilder import IndexView, expose
from werkzeug.utils import redirect


class HomeView(IndexView):
    index_template = 'all.html'

    @expose('/')
    def index(self):
        user = g.user

        if user.is_anonymous:
            return redirect(url_for('AuthDBView.login'))
        else:
            if user.first_name == 'Pasquale':
                return redirect(url_for('HomePage.admin'))
            else:
                return redirect(url_for('HomePage.user'))
