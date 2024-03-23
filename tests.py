#Нужно исправить: здесь и далее: при наличии методов работы с атрибутом у тестируемой программы, необходимо использовать их,
#нам важно знать что не только атрибут изменился но и метод работы с ним работает, так и тестов будет меньше и атомарность не пострадает

# был такой комментарий в прошлой проверке

# books_genre (и другие атриботы в assert - результат вывода метода add_new_book(). Простой вызов метода add_new_book() выводит None. Я понимаю, что проверка избыточна, и метод add_new_book() проверяется дальше. Но задание сделать провреку для всех методов.
import pytest
from main import BooksCollector
class TestBooksCollector:

    def test_add_new_book_add_too_long_name_not_added(self):
        collect = BooksCollector()
        collect.add_new_book('Гордость и предубеждение и зомби  всякая чепухахахаххахаххахахаххахахахаххахахаххахахахахххахахаххахахахахах')
        assert len(collect.get_books_genre()) == 0

    def test_set_book_genre_added_book_with_genre(self, book_dict):
        book_with_genre = BooksCollector()
        book_with_genre.add_new_book(book_dict["name"])
        book_with_genre.set_book_genre(book_dict["name"], book_dict["genre"])
        assert book_with_genre.get_books_genre() == {book_dict["name"]: book_dict["genre"]}

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', None]
        ]
    )
    def test_set_book_genre_added_book_no_genre(self, name, genre):
        book_no_genre = BooksCollector()
        book_no_genre.add_new_book(name)
        book_no_genre.set_book_genre(name, genre)
        assert book_no_genre.get_books_genre() == {name: ''}

    def test_get_book_genre_added_book_with_genre(self, book_dict):
        book_withgenre = BooksCollector()
        book_withgenre.add_new_book(book_dict["name"])
        book_withgenre.set_book_genre(book_dict["name"], book_dict["genre"])
        assert book_withgenre.get_book_genre(book_dict["name"]) == book_dict["genre"]

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', '']
        ]
    )
    def test_get_book_genre_added_book_no_genre(self, name, genre):
        book_nogenre = BooksCollector()
        book_nogenre.add_new_book(name)
        book_nogenre.set_book_genre(name, genre)
        assert book_nogenre.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_added_book_with_genre(self, book_dict):
        book_with_spgenre = BooksCollector()
        book_with_spgenre.add_new_book(book_dict["name"])
        book_with_spgenre.set_book_genre(book_dict["name"], book_dict["genre"])
        assert book_with_spgenre.get_books_with_specific_genre(book_dict["genre"]) == [book_dict["name"]]

    def test_get_books_genre_add_two_books(self):
        add_books = BooksCollector()
        add_books.add_new_book('Гордость и предубеждение и зомби')
        add_books.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(add_books.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Комедии']
        ]
    )
    def test_get_books_for_children_genre_not_in_genre_age_rating_added(self, name, genre):
        children_books = BooksCollector()
        children_books.add_new_book(name)
        children_books.set_book_genre(name, genre)
        assert children_books.get_books_for_children() == [name]

    def test_get_books_for_children_genre_not_in_genre_age_rating_not_added(self, book_dict):
        not_children_books = BooksCollector()
        not_children_books.add_new_book(book_dict["name"])
        not_children_books.set_book_genre(book_dict["name"], book_dict["genre"])
        assert not_children_books.get_books_for_children() != [book_dict["name"]]

    def test_add_book_in_favorites_added_book(self, book_dict):
        favorite_book = BooksCollector()
        favorite_book.add_new_book(book_dict["name"])
        favorite_book.set_book_genre(book_dict["name"], book_dict["genre"])
        favorite_book.add_book_in_favorites(book_dict["name"])
        assert favorite_book.get_list_of_favorites_books() == [book_dict["name"]]

    def test_delete_book_from_favorites_deleted_book(self, book_dict):
        del_favorite_book = BooksCollector()
        del_favorite_book.add_new_book(book_dict["name"])
        del_favorite_book.set_book_genre(book_dict["name"], book_dict["genre"])
        del_favorite_book.add_book_in_favorites(book_dict["name"])
        del_favorite_book.delete_book_from_favorites(book_dict["name"])
        assert len(del_favorite_book.get_list_of_favorites_books()) == 0

    def test_get_book_from_favorites_get_book(self, book_dict):
        list_favorite_book = BooksCollector()
        list_favorite_book.add_new_book(book_dict["name"])
        list_favorite_book.set_book_genre(book_dict["name"], book_dict["genre"])
        list_favorite_book.add_book_in_favorites(book_dict["name"])
        assert list_favorite_book.get_list_of_favorites_books() == [book_dict["name"]]

    def test_get_list_of_favorites_books_add_book_in_favorite_book_added(self, book_dict):
        list_favorite_book = BooksCollector()
        list_favorite_book.add_new_book(book_dict["name"])
        list_favorite_book.set_book_genre(book_dict["name"], book_dict["genre"])
        list_favorite_book.add_book_in_favorites(book_dict["name"])
        assert list_favorite_book.get_list_of_favorites_books() == [book_dict["name"]]