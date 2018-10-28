# auther mohsen niknezhad
import os
import argparse
from utlilites import url_utilities
from  utlilites import database_utilities

def main(database: str, url_list_file: str):
    big_word_list = []
    print("we are going work with" + database)
    print("we are going scan" + url_list_file)
    urls = url_utilities.load_urls_from_files(url_list_file)
    for url in urls:
        print("reading "+ url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)
        #print(big_word_list)
    # DataBase Code
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "words.db")
    database_utilities.create_database(database_path=path)
    database_utilities.save_words_to_database(database_path=path,words_list=big_word_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="Sqlite File name")
    parser.add_argument("-i", "--input", help="File contianing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
