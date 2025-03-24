from library_item import LibraryItem

test_item_1 = LibraryItem("Beat It", "Micheal Jackson", 5)
test_item_2 = LibraryItem("06 Quen Lam","Ngot",4)
test_item_3 = LibraryItem("02 Mo Lam Ma","Ngot",3)
test_item_4 = LibraryItem("Devourer of Gods","DM DOKURO",4)

def test_name():
    assert test_item_1.name == "Beat It"
    assert test_item_2.name == "06 Quen Lam"
    assert test_item_3.name == "02 Mo Lam Ma"
    assert test_item_4.name == "Devourer of Gods"

def test_artist():
    assert test_item_1.artist == "Micheal Jackson"
    assert test_item_2.artist == "Ngot"
    assert test_item_3.artist == "Ngot"
    assert test_item_4.artist == "DM DOKURO"

def test_rating():
    assert test_item_1.rating == 5
    assert test_item_2.rating == 4
    assert test_item_3.rating == 3
    assert test_item_4.rating == 4

def test_info():
    assert test_item_1.info() == "Beat It - Micheal Jackson *****"
    assert test_item_2.info() == "06 Quen Lam - Ngot ****"
    assert test_item_3.info() == "02 Mo Lam Ma - Ngot ***"
    assert test_item_4.info() == "Devourer of Gods - DM DOKURO ****"

def test_star():
    assert test_item_1.stars() == "*****"
    assert test_item_2.stars() == "****"
    assert test_item_3.stars() == "***"
    assert test_item_4.stars() == "****"

def test_play_count():
    assert test_item_1.play_count == 0
    assert test_item_2.play_count == 0
    assert test_item_3.play_count == 0
    assert test_item_4.play_count == 0

if __name__ == "__main__":
    test_name()
    test_artist()
    test_rating()
    test_play_count()
    test_star()
    test_info()