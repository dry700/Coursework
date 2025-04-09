from library_item import LibraryItem

test_items = []
test_items.append({"name":"Beat It", "artist":"Micheal Jackson", "rating":5})
test_items.append({"name":"06 Quen Lam","artist":"Ngot","rating":4})
test_items.append({"name":"02 Mo Lam Ma","artist":"Ngot","rating":3})
test_items.append({"name":"Devourer of Gods","artist":"DM DOKURO","rating":4})

def test_init():
    for item in test_items:
        testing_item = LibraryItem(item["name"],item["artist"],item["rating"])
        assert testing_item.name == item["name"]
        assert testing_item.artist == item["artist"]
        assert testing_item.rating == item["rating"]
        assert testing_item.play_count ==0

def test_info():
    for item in test_items:
        testing_item = LibraryItem(item["name"],item["artist"],item["rating"])
        assert testing_item.info() == f"{item["name"]} - {item["artist"]} {testing_item.stars()}"

def test_stars():
    for item in test_items:
        testing_item = LibraryItem(item["name"],item["artist"],item["rating"])
        expected_star = ''
        for i in range(item['rating']):
            expected_star += '*'
        assert testing_item.stars() == expected_star

if __name__ == "__main__":
    test_init()
    test_info()
    test_stars()