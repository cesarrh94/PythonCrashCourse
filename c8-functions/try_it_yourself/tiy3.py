# city names:
def city_country(city, country):
    response = f'{city.title()}, {country.title()}'
    return response

print(city_country('guadalajara', 'mexico'))
print(city_country('los angeles', 'usa'))
print(city_country('tokyo', 'japan'))


# album:
def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'album': album_title}
    return album

print(make_album('guns n roses', 'appetite for destruction'))
print(make_album('metallica', 'black album'))
print(make_album('red hot chilli peppers', 'by the way'))