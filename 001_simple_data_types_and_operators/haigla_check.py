user_code = ''
while(len(user_code) != 11):
    try:
        user_code = input('Please enter your ID: ')
        if len(user_code) != 11:
            raise UserWarning
        # int(user_code)
        print(user_code)
    except:
        print('Error')
user_choice = 0
while(user_choice != 3):

# user_code = input('Please enter your ID')
    user_choice = input('Please choose\n'
                        '1. ID data\n'
                        '2. Validate\n'
                        '3. Exit')
    if user_choice == '1':
        maakond = int(user_code[8:10])
        if maakond >= 0 and maakond <= 10:
            birth_place = 'Kuressaare haigla'
        elif maakond >= 11 and maakond <= 19:
            birth_place = 'Tartu Ülikooli Naistekliinik'
        elif maakond >= 21 and maakond <= 150:
            birth_place = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
        elif maakond >= 151 and maakond <= 161:
            birth_place = 'Keila haigla'
        elif maakond >= 161 and maakond <= 220:
            birth_place = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
        elif maakond >= 221 and maakond <= 270:
            birth_place = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
        elif maakond >= 271 and maakond <= 370:
            birth_place = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla)'
        elif maakond >= 371 and maakond <= 420:
            birth_place = 'Narva haigla'
        elif maakond >= 421 and maakond <= 470:
            birth_place = 'Pärnu haigla'
        elif maakond >= 471 and maakond <= 490:
            birth_place = 'Haapsalu haigla'
        elif maakond >= 491 and maakond <= 520:
            birth_place = 'Järvamaa haigla (Paide)'
        elif maakond >= 521 and maakond <= 570:
            birth_place = 'Rakvere haigla, Tapa haigla'
        elif maakond >= 571 and maakond <= 600:
            birth_place = 'Valga haigla'
        elif maakond >= 601 and maakond <= 650:
            birth_place = 'Viljandi haigla'
        elif maakond >= 651 and maakond <= 700:
            birth_place = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
        else:
            birth_place = 'Impossible'



        if int(user_code[0]) % 2 == 0:
            gender = 'Female'
        else :
            gender = 'Male'


        if user_code[0] == '1' or user_code[0] == '2':
            birth_cent = '18'
        elif user_code[0] == '3' or user_code[0] == '4':
            birth_cent = '19'
        elif user_code[0] == '5' or user_code[0] == '6':
            birth_cent = '20'
        print('Century: '+birth_cent)
        print('Sex: '+gender)
        print('Birth Place: '+birth_place)
        print('Birthday: '+user_code[5:7] + '.' + user_code[3:5] + '.' + birth_cent + user_code[1:3])






    elif user_choice == '2':
        user_code_validity = int(user_code[0]) * 1 + int(user_code[1]) * 2 + int(user_code[2]) * 3 + int(user_code[3]) * 4 + \
                              int(user_code[4]) * 5 + int(user_code[5]) * 6 + int(user_code[6]) * 7 + int(user_code[7]) * 8 + \
                              int(user_code[8]) * 9 + int(user_code[9]) * 1

        user_code_validity_mod = user_code_validity % 11

        # print(type(user_code[-1]), type(user_code_validity_mod)) ---- check your classes ±!!
        if user_code_validity_mod >= 10:
            user_code_validity = int(user_code[0]) * 3 + int(user_code[1]) * 4 + int(user_code[2]) * 5 + int(
                user_code[3]) * 6 + \
                                 int(user_code[4]) * 7 + int(user_code[5]) * 8 + int(user_code[6]) * 9 + int(
                user_code[7]) * 1 + \
                                 int(user_code[8]) * 2 + int(user_code[9]) * 3

            user_code_validity_mod = user_code_validity % 11


        if str(user_code_validity_mod) != user_code[-1]:
            print('code invalid')
        else:
            print('code valid')






    elif user_choice == '3':
        break







