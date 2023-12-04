import requests
from bs4 import BeautifulSoup

def get_jordan_stats(season):
    url = f'https://www.espn.com/nba/player/stats/_/id/1035/michael-jordan/year/{season}'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        points = soup.find('span', {'data-stat': 'pts'}).text
        assists = soup.find('span', {'data-stat': 'ast'}).text
        rebounds = soup.find('span', {'data-stat': 'reb'}).text

        
        return {
            'season': season,
            'points': points,
            'assists': assists,
            'rebounds': rebounds,
 
        }
    else:
        return None

season_stats = get_jordan_stats(1995)
print(season_stats)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    season = request.form.get('season')
    jordan_stats = get_jordan_stats(season)
    
    return render_template('results.html', jordan_stats=jordan_stats)

if __name__ == '__main__':
    app.run(debug=True)


