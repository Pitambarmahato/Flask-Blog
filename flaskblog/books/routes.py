from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required

books = Blueprint('books', __name__)

@books.route('/books')
def book():
	return render_template('books.html')