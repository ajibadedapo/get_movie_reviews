import sys, time,  requests
from bs4 import BeautifulSoup


def get_review():
    start_time = time.clock()
    film_type = input('Is this a movie series ? (Yes/No)')
    if film_type.strip() == 'yes':
        filename = input('Enter a SERIES name: ')
        fileseason = input('Enter a movie season (e.g 03 for season 3): ')
        website = "https://www.rottentomatoes.com/tv/"+str(filename.replace(' ', '_'))+"/s"+str(fileseason)+"/reviews/?type=top_critics"
    else:
        filename = input('Enter a movie name: ')
        website = "https://www.rottentomatoes.com/m/" + str(filename.replace(' ', '_')) + "/reviews/?type=top_critics"
    reviewlink = website.strip()
    print(reviewlink)
    res = requests.get(reviewlink)
    if res.status_code == 404:
        print('MOVIE NOT FOUND, CHECK SPELLING !')
        sys.exit()
    result = res.content
    soup = BeautifulSoup(result)
    review = soup.findAll("div", {"class": "the_review"})
    i = 0
    print(str(filename) + ' reviews')
    print('.......................................')
    for texts in review:
        i += 1
        print(str(i) + str(') ') + texts.string)
    print('Program running time :' + str(time.clock() - start_time))
    sys.exit()
get_review()
