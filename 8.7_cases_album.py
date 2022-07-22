def make_album(executor, name_album, number_of_song='None'):
    f_album = {'executor': executor, 'name_album': name_album}
    if number_of_song:
        f_album['number_of_song'] = number_of_song
    return f_album

first_album = make_album('OG Buda', 'FREE RIO', number_of_song=21)
second_album = make_album('Dora', 'MISS', number_of_song=13)
thirt_album = make_album('Maks Korzh', 'Her guilt')
print(first_album)
print(second_album)
print(thirt_album)