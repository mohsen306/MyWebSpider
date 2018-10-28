from utlilites.url_utilities import load_urls_from_files


def test_load_file():
    test_urls = load_urls_from_files("input.txt")
    assert (len(test_urls) > 1)
