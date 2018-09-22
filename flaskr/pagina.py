import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from flaskr.db import get_db
import json, requests
from tmdbv3api import TMDb, TV, Movie,Season

bp = Blueprint('pagina', __name__)
apikey="e00b72174e4ae097af808f34a8f220fc"


@bp.route('/')
def index():
    discover = 'https://api.themoviedb.org/3/discover/movie'
    '''
        Allowed Values: , popularity.asc, popularity.desc, release_date.asc, release_date.desc, revenue.asc, revenue.desc, primary_release_date.asc, primary_release_date.desc, original_title.asc, original_title.desc, vote_average.asc, vote_average.desc, vote_count.asc, vote_count.desc
        default: popularity.desc
    '''
    parameters = dict(
        api_key=apikey,
        language='es-ES'
        # sort_by='release_date.desc'
    )
    resp = requests.get(url=discover, params=parameters)
    data = json.loads(resp.text)

    # print(data['page'])
    # print(data['total_results'])
    # print(data['total_pages'])

    return render_template('pagina/index.html', posts=data['results'])



@bp.route('/buscar', methods=('GET', 'POST'))
def buscar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        error = None

        if not titulo:
            error = 'El Titulo es requerido.'

        if error is not None:
            flash(error)
            return redirect(url_for('pagina.index'))
        else:
            tmdb= TMDb()
            # tmdb.api_key="e00b72174e4ae097af808f34a8f220fc"
            tmdb.api_key=apikey
            tmdb.language='es-ES'

            if tipo == "peliculas":
                entidad = Movie()
            elif tipo == "series":
                entidad = Season()
            elif tipo == "tv":
                entidad = TV()

            show=entidad.search(titulo)
    return render_template('pagina/buscar.html', posts=show)




def get_detalles(id, check_author=True):
    post = ""

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    # if check_author and post['author_id'] != g.user['id']:
    #     abort(403)

    return post



@bp.route('/<int:id>/detalles', methods=('GET', 'POST'))
def detalles(id):
    if request.method == 'POST':
        tipo = request.get['tipo']
        print(tipo)
        post = get_detalles(id)
    
    return render_template('pagina/detalles.html', post=post)