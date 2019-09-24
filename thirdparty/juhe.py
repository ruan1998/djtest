import json
import requests

def movie(moviename):
    key = '6c03f71a8d18d6a277d47cba0d7c2eb6'
    api = 'http://v.juhe.cn/movie/index'
    params = 'title=%s&smode=0&key=%s&' % (moviename, key)
    url = api + '?' + params
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    result = json_data.get('result')
    response = []
    for mov in result:
        movie = {}
        movie['rating'] = mov.get('rating')
        movie['genres'] = mov.get('genres')
        movie['title'] = mov.get('title')
        movie['actors'] = mov.get('actors')
        movie['simple_plot'] = mov.get('plot_simple')
        movie['year'] = movie.get('year')
        response.append(movie)
    return response
