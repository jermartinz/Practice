def get_formatted_name (first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


#8.6
def city_country(city, country):
    name = f"{city}, {country}"
    return name.title()

chile = city_country('santiago', 'chile')
print(chile)

#8.7
def make_album(artist, album_name, songs=None):
    album = {
        'artist': artist,
        'album_n': album_name,
    }
    if songs:
        album['songs'] = songs
    return album

midnight = make_album('The Midnight', 'Orion')
print(midnight)
midnight = make_album('The Midnight', 'Orion', 14)
print(midnight)

#8.8 
def make_album():
    album = {}
    while True:
        print("\nPlease give me info of the album")
        album['album_name'] = input("Album name: ")
        album['artist'] = input("Artist name: ")
        print(album)
        exit_p = input("Do you want print more albums? ('enter 'no' to quit) ")
        if exit_p == 'no':
            break
    

make_album()





