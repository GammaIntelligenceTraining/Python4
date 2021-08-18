import pandas as pd
import time

'''
Написать программу, которая по выбору пользователя делает следующее:
1. Выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')
2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов
3. Выводит таблицу со странами (столбец 'Country'). Группирует и выводит в порядке убывания
4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке убывания
'''
pd.set_option('display.max_rows', 70000)


def user_menu():
    stack_overflow_survey = pd.read_csv('data_files//survey_results_public.csv')
    user_choice = input('Please choose:\n'
                        '1. Hobby/Pro\n'
                        '2. Age\n'
                        '3. Countries\n'
                        '4. Currency\n'
                        '0. Exit\n'
                        '--> ')
    if user_choice == '1':
        hobbyist_pro(stack_overflow_survey)
    elif user_choice == '2':
        user_age(stack_overflow_survey)
    elif user_choice == '3':
        countries(stack_overflow_survey)
    elif user_choice == '4':
        currency(stack_overflow_survey)
    elif user_choice == '0':
        print('Good Bye!')
        time.sleep(2)
        exit()


def hobbyist_pro(df):
    print(df['Hobbyist'].value_counts())
    time.sleep(2)
    user_menu()


def user_age(df):
    print(f"Respondents minimum age is {df['Age'].min()}")
    print(f"Respondents maximum age is {df['Age'].max()}")
    print(f"Respondents mean age is {df['Age'].mean()}")
    time.sleep(2)
    user_menu()


def countries(df):
    sorted_values = df[['Country', 'Respondent']]
    print(sorted_values.groupby('Country').count().sort_values('Respondent', ascending=False))
    time.sleep(2)
    user_menu()


def currency(df):
    print(df['CurrencyDesc'].value_counts())
    time.sleep(2)
    user_menu()


user_menu()