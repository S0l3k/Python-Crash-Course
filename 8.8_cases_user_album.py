def make_album(executor, name_album, number_of_song='None'):
    f_album = {'executor': executor, 'name_album': name_album}
    if number_of_song:
        f_album['number_of_song'] = number_of_song
    return f_album

while True:
    print(f"\nEnter some information about artist.")
    print(f"If you want to leave, enter the 'quit'")

    executor = input("\nEnter the name artist: ")
    if executor == 'quit':
        break

    name_album = input("Enter the name album: ")
    if name_album == 'quit':
        break

    number_of_song = input("Enter the number of song(if you know): ")
    if number_of_song == 'quit':
        break

formatted_information_about_artist = make_album(executor, name_album,
                                                number_of_song)
print(f"\nThis what is done", formatted_information_about_artist, "!")
#first_album = make_album('OG Buda', 'FREE RIO', number_of_song=21)
#second_album = make_album('Dora', 'MISS', number_of_song=13)
#thirt_album = make_album('Maks Korzh', 'Her guilt')
#print(first_album)
#print(second_album)