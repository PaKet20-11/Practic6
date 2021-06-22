import bottle
from bottle import route
from bottle import run
from bottle import request

@route(/albums)ц
def alb():
    artist = request.query.artist
    gener = request.query.gener
    album = request.query.album


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
