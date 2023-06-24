from datetime import datetime, timedelta

# -----------------------------------------functions----------------------------------------------------
books = {}
members = {}

# creating member
def create_member():
    name = input('Enter member name: ')
    last_name = input('Enter member last name: ')
    birth_date = input('Enter member birth date: ')
    address = input('Enter member address: ')
    registration_date = input('Enter a date (with this form 1390/02/12) : ')
    member_id = int(input("enter your library code"))
    while True :
        if member_id in members.keys():
            prin("its exsist")
        else:

            national_code = input('Enter member national code: ')
            while True:
                for i,j in members.items():
                    if j["natioanal_code"] == national_code :
                        print("repetitious")
                    else:
                        members[member_id] = {'name': name, 'last_name': last_name, 'national_code': national_code,
                                'birth_date': birth_date, 'address': address, 'registration_date': registration_date}
                            print(f'Member with id {member_id} has been created successfully.')
                break
        break
# editing member
def edit_member(member_id):
    if member_id in members:
        member = members[member_id]
        member['name'] = input('Enter new member name (press enter to keep it unchanged): ') or member['name']
        member['last_name'] = input('Enter new member last name (press enter to keep it unchanged): ') or member['last_name']
        member['national_code'] = input('Enter new member national code (press enter to keep it unchanged): ') or member['national_code']
        member['birth_date'] = input('Enter new member birth date (press enter to keep it unchanged): ') or member['birth_date']
        member['address'] = input('Enter new member address (press enter to keep it unchanged): ') or member['address']
        print(f'Member with id {member_id} has been updated successfully.')
    else:
        print(f'Member with id {member_id} not found.')

# deleteing member
def delete_member(member_id):
    if member_id in members:
        del members[member_id]
        print(f'Member with id {member_id} has been deleted successfully.')
    else:
        print(f'Member with id {member_id} not found.')

# adding books
def create_book():
    name = input('Enter book name: ')
    author = input('Enter book author: ')
    year = input('Enter book publication year: ')
    category = input('Enter book category: ')
    book_id = len(books) + 1
    books[book_id] = {'name': name, 'author': author, 'year': year, 'category': category, 'is_borrowed': False}
    print(f'Book with id {book_id} has been created successfully.')

#editing books
def edit_book(book_id):
    if book_id in books:
        book = books[book_id]
        book['name'] = input('Enter new book name (press enter to keep it unchanged): ') or book['name']
        book['author'] = input('Enter new book author (press enter to keep it unchanged): ') or book['author']
        book['year'] = input('Enter new book publication year (press enter to keep it unchanged): ') or book['year']
        book['category'] = input('Enter new book category (press enter to keep it unchanged): ') or book['category']
        print(f'Book with id {book_id} has been updated successfully.')
    else:
        print(f'Book with id {book_id} not found.')

# deleting books
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        print(f'Book with id {book_id} has been deleted successfully.')
    else:
        print(f'Book with id {book_id} not found.')

# borrowing the book
def borrow_book(member_id, book_id):
    if member_id in members:
        member = members[member_id]
        if book_id in books:
            book = books[book_id]
            if book['is_borrowed'] == True:
                print(f'Book with id {book_id} has already been borrowed.')
            else:
                borrow_date = datetime.now().strftime('%Y-%m-%d') # تاریخ امانت دادن کتاب
                return_date = (datetime.now() +timedelta(days=14)).strftime('%Y-%m-%d')  
                book['is_borrowed'] = True
                member.setdefault('borrowed_books', {})
                member['borrowed_books'][book_id] = {'borrow_date': borrow_date, 'return_date': return_date}
                print(f'Book with id {book_id} has been borrowed successfully by member with id {member_id}.')
        else:
            print(f'Book with id {book_id} not found.')
    else:
        print(f'Member with id {member_id} not found.')

# returning the book
def return_book():
    if member_id in members:
        member = members[member_id]
        if book_id in member.get('borrowed_books', {}):
            book = books[book_id]
            book['is_borrowed'] = False
            del member['borrowed_books'][book_id]
            print(f'Book with id {book_id} has been returned successfully by member with id {member_id}.')
        else:
            print(f'Member with id {member_id} has not borrowed book with id {book_id}.')
    else:
        print(f'Member with id {member_id} not found.')
# displaying member
def display_members():
        for member_id, member_info in members.items():
            print(f'ID: {member_id} - Name: {member_info["name"]} {member_info["last_name"]}')

# displaying boks
def display_books():
    for book_id, book_info in books.items():
        print(f'ID: {book_id} - Name: {book_info["name"]} - Author: {book_info["author"]}')


#--------------------------------------------------------------main------------------------------------------------------------------------
print('Welcome to the library management system.')
while True:
    print('Please select one of the following options:')
    print('1. Create a new member')
    print('2. Edit an existing member')
    print('3. Delete an existing member')
    print('4. Create a new book')
    print('5. Edit an existing book')
    print('6. Delete an existing book')
    print('7. Borrow a book')
    print('8. Return a book')
    print('9. Display all members')
    print('10. Display all books')
    print('11. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        create_member()
    elif choice == '2':
        member_id = int(input('Enter member id: '))
        edit_member(member_id)
    elif choice == '3':
        member_id = int(input('Enter member id: '))
        delete_member(member_id)
    elif choice == '4':
        create_book()
    elif choice == '5':
        book_id = int(input('Enter book id: '))
        edit_book(book_id)
    elif choice == '6':
        book_id = int(input('Enter book id: '))
        delete_book(book_id)
    elif choice == '7':
        member_id = int(input('Enter member id: '))
        book_id = int(input('Enter book id: '))
        borrow_book(member_id, book_id)
    elif choice == '8':
        member_id = int(input('Enter member id: '))
        book_id = int(input('Enter book id: '))
        return_book(member_id, book_id)
    elif choice == '9':
        display_members()
    elif choice == '10':
        display_books()
    elif choice == '11':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please enter a valid choice.')
