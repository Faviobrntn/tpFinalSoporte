import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'E-mail is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'El usuario {} ya se encuentra registrado.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password, email) VALUES (?, ?, ?)',
                (username, generate_password_hash(password), email)
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')



@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Usuario incorrecto'
        elif not check_password_hash(user['password'], password):
            error = 'Contraseña incorrecta.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')



@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()



@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.route('/mis-favoritos')
@login_required
def favoritos():
    db = get_db()
    favoritos = db.execute(
        'SELECT * FROM favoritos f WHERE f.user_id = ?', (g.user['id'], )
    ).fetchall()
    return render_template('auth/favoritos.html', favoritos=favoritos)



@bp.route('/<int:id>/eliminar-favorito', methods=('POST',))
@login_required
def quitarFavorito(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM favoritos WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('auth.favoritos'))