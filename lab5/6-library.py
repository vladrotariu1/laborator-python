class LibraryItem:
    def __init__(self, title, author_or_director, item_id):
        self.title = title
        self.author_or_director = author_or_director
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Item ID: {self.item_id}\nTitle: {self.title}\nAuthor/Director: {self.author_or_director}\nChecked Out: {'Yes' if self.checked_out else 'No'}")

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} checked out successfully.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} returned successfully.")
        else:
            print(f"{self.title} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Type: Book\nNumber of Pages: {self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Type: DVD\nDuration: {self.duration} minutes")


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number):
        super().__init__(title, publisher, item_id)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Type: Magazine\nIssue Number: {self.issue_number}")


def main():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "B001", 180)
    book.display_info()
    book.check_out()

    dvd = DVD("Inception", "Christopher Nolan", "D001", 148)
    dvd.display_info()
    dvd.return_item()

    magazine = Magazine("National Geographic", "National Geographic Society", "M001", 123)
    magazine.display_info()
    magazine.check_out()


if __name__ == "__main__":
    main()
