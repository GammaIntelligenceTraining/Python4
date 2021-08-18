'''
Написать программу, которая по выбору пользователя делает следующее:
1. Выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')
2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов
3. Выводит таблицу со странами (столбец 'Country'). Группирует и выводит в порядке убывания
4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке убывания
'''


import pandas as pd
import time
pd.set_option('display.max_rows', 999999)


# Function to control users choices
def user_menu():
    survey_data_frame = pd.read_csv('data_files//survey_results_public.csv')
    user_choice = input('Please choose:\n'
                        '1. Hobby/Pro\n'
                        '2. Age\n'
                        '3. Countries\n'
                        '4. Currency\n'
                        '0. Exit\n'
                        '-->')
    if user_choice == '1':
        hobby_pro(survey_data_frame)
    elif user_choice == '2':
        dev_age(survey_data_frame)
    elif user_choice == '3':
        countries(survey_data_frame)
    elif user_choice == '4':
        currency(survey_data_frame)
    elif user_choice == '0':
        print('\n')
        print('Good bye!')
        time.sleep(2)
        exit()
    else:
        print('\n')
        print('Choice is out of range!')
        time.sleep(2)
        user_menu()


# Function to group by Hobbyist column and show count
def hobby_pro(df):
    sorted_df = df[['Hobbyist', 'Respondent']]
    print(sorted_df.groupby('Hobbyist').count())
    time.sleep(2)
    print('\n')
    user_menu()


# Function to show min, max and mean age
def dev_age(df):
    print(f"Maximum age is {df['Age'].max()}")
    print(f"Minimum age is {df['Age'].min()}")
    print(f"Mean age is {df['Age'].mean()}")
    time.sleep(2)
    print('\n')
    user_menu()


# Function to group by Country column and show count
def countries(df):
    sorted_df = df[['Country', 'Respondent']]
    print(sorted_df.groupby('Country').count().sort_values('Respondent', ascending=False))
    time.sleep(2)
    print('\n')
    user_menu()


# Function to group by CurrencyDesc column and show count
def currency(df):
    sorted_df = df[['CurrencyDesc', 'Respondent']]
    print(sorted_df.groupby('CurrencyDesc').count().sort_values('Respondent', ascending=False))
    time.sleep(2)
    print('\n')
    user_menu()


user_menu()
