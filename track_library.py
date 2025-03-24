from library_item import LibraryItem
import os
'''
with open("_library.csv") as f:
    contents = f.readlines()
'''
library = {}
library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)
library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5)
library["03"] = LibraryItem("Highway to Hell ", "AC/DC", 2)
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1)
library["05"] = LibraryItem("Someone Like You", "Adele", 3)
library["06"] = LibraryItem("Beat It","Micheal Jackson",5)


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return


if __name__ == "__main__":
    csv_path = "_library.csv"

    if not os.path.exists(csv_path):
        print(f"File does not exist.")
    else:
        print(f"File exists.")

    with open("_library.csv") as f:
        contents = f.readlines()
        contents.pop(0)
        for i in range(len(contents)):
            contents[i] = contents[i].strip().split(',')
        print(contents)
        for name,artist,rating in contents:
            print(f'{name}\n{artist}\n{int(rating)}')
            #item = LibraryItem()

    '''for key in library:
        print(library[key].info())'''