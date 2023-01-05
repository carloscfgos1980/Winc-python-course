# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
film_names = ['Star Wars',  'Jaws', 'Close Encounters of the Third Kind', 'Superman', 'E.T. the Extra-Terrestrial', 'Home Alone films', 'the Indiana Jones films',
              'Jurassic Park I', 'Jurassic Park II', "Schindler's List", 'Saving Private Ryan', 'Catch Me If You Can', 'Seven Years In Tibet', 'Harry Potter I', 'Harry Potter II', 'Harry Potter III']
golden_globe_rewarded_films = [
    'Jaws', 'Star Wars: Episode IV – A New Hope', 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']


def all_lower(my_list):
    return [x.lower() for x in my_list]


def alphabetical_order(film):
    return sorted(film)


print('John Williams films in alpabetial order',
      alphabetical_order(film_names))


def won_golden_globe(film):
    if film.lower() in all_lower(golden_globe_rewarded_films):
        print(f'{film} won a golden globe')
        return True
    else:
        print(f"{film} didn't get a Golden glove prize")
        return False


print('Checking won golden globe', won_golden_globe('Harry Potter'))

print('Checking won golden globe', won_golden_globe('Jaws'))
print('Checking won golden globe', won_golden_globe('jaws'))

toto_albums = 'Toto', 'Hydra', 'The Seventh One', 'Falling in Between'

mixed_albums = ['The John Towner Touch', 'World on a String', 'Toto', 'Hydra',
                'The Johnny Williams Orchestra Plays Sounds from Screen Spectaculars', 'Rhythm in Motion', 'The Five Sacred Trees', 'The Seventh One', 'The Hollywood Sound', 'Treesong', 'The Spielberg/Williams Collaboration Part III', 'Falling in Between']


def remove_toto_albums(list, extra_items):
    my_list = []
    for cd in list:
        if cd not in extra_items:
            my_list.append(cd)
    return my_list


print('checking removing', remove_toto_albums(mixed_albums, toto_albums))
