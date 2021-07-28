import mysql.connector
import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database='test_db'
)
cursor = conn.cursor()

# # Commented, because used once, to create db.
# cursor.execute('CREATE SCHEMA test_db')

# # Commented, because used once, to create table
# cursor.execute('''
# CREATE TABLE `test_db`.`people` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `name` VARCHAR(255) NOT NULL,
#   `surname` VARCHAR(255) NOT NULL,
#   `date_of_birth` DATE NOT NULL,
#   `email` VARCHAR(255) NOT NULL,
#   `phone` VARCHAR(255) NOT NULL,
#   PRIMARY KEY (`id`));
#   ''')


def main():
    user_choice = input('Please choose:\n'
                        '1. Add to DB\n'
                        '2. Read from DB\n'
                        '3. Exit\n'
                        '--> ')
    if user_choice == '1':
        add_to_db()
    elif user_choice == '2':
        read_from_db()
    elif user_choice == '3':
        exit()
    else:
        print('Choice out of range!')
        main()


def add_to_db():
    print('Hello, please follow steps to enter your data to database')
    user_name, user_surname = input('Please enter your name and surname, split with space: ').split()
    user_dob = input('Please enter your date of birth, use (YYYY-MM-DD) format: ')
    user_email = input('Please enter your email: ')
    user_phone = input('Please enter your phone: ')
    cursor.execute(f'INSERT INTO people (`name`, `surname`, `date_of_birth`, `email`, `phone`) VALUES ("{user_name}",'
                   f' "{user_surname}", "{user_dob}","{user_email}", "{user_phone}");')
    conn.commit()
    main()


def read_from_db():
    cursor.execute('SELECT * FROM people')
    result = cursor.fetchall()
    for row in result:
        print(f'Hello {row[1]} {row[2]}. You were born on {row[3]}. We can contact you with {row[4]} or {row[5]}')
        print(type(row[3]))
    main()


main()