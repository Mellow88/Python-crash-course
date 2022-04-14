"""HW_8"""


def display_message(message):
    """Виведення коментаря про нову інформацію"""
    print(message)

display_message('stop')

def favorite_book(book):
    """Виведення коментаря про улюблену книгу"""
    print(f"One of my favorite books is {book.title()}")

favorite_book('Alice in Wonderland')

def make_shirt(size='s', logo=''):
    """make a shirts"""
    print(f"We made shirt size: {size}, with logo: {logo}")

make_shirt('m', 'python')
make_shirt(logo='c++')

city_list = []
city_list.append({'city': 'lviv', 'country': 'ukraine'})
city_list.append({'city': 'kyiv', 'country': 'ukraine'})
city_list.append({'city': 'chikago', 'country': 'usa'})


def city_counry(city_name, counry_name):
    """Return format name"""
    f_city_name = f"{city_name}, {counry_name}"
    return f_city_name.title()

for value in city_list:
    city = value['city']
    counry = value['country']
    print(city_counry(city, counry))

def make_album(singer, album_name, songs_count=None):
    """Build album"""
    album = {}
    album['singer'] = singer.title()
    album['album_name'] = album_name.title()
    if songs_count:
        album['songs_count'] = songs_count
    return album

for value in range(0,3):
    album_ = make_album('Jimmy', 'World', 24)
    print(album_)
