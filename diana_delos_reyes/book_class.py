class Booklist():
	def __init__(self):
		self.books = []
	def add(self, title, author):
		book = {}
		book['title']= title
		book['author']= author
		self.books.append(book)
	def count_books(self):
		return len (self.books)
	def remove_title(self, title):
		for book in self.books:
			if book in self.books:
				if(book['title']) == title:
					self.books.remove(book)
	def display_titles(self):
		sort_books = sorted(self.books, key=lambda item: item['title'])
		for book in sort_books:
			print(book['title'])
		# 	new_book_list = sorted(book['title'])
		# 	return new_book_list
		# 	print(new_book_list)
