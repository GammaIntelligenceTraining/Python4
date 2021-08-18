user_id = input('Please enter ID code: ')
user_choice = input('Please choose\n1. Get data\n2. Validate\n3. Exit')
if user_choice == '1':
    # Check id owners gender
    if int(user_id[0]) % 2 == 0:
        gender = 'Female'
    else:
        gender = 'Male'

    # Check id owners birth centure
    if user_id[0] == '1' or user_id[0] == '2':
        birth_cent = '18'
    elif user_id[0] == '3' or user_id[0] == '4':
        birth_cent = '19'
    elif user_id[0] == '5' or user_id[0] == '6':
        birth_cent = '20'

    # Birth date variables
    by = user_id[1:3]
    bm = user_id[3:5]
    bd = user_id[5:7]
    birth_region = user_id[7:10]
    chk_number = user_id[10]

    # Check birth region
    if int(birth_region) in range(1, 11):
        region = 'Kuressaare haigla'
    elif int(birth_region) in range(11, 20):
        region = 'Tartu Ülikooli Naistekliinik'
    elif int(birth_region) in range(21, 151):
        region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif int(birth_region) in range(151, 161):
        region = 'Keila haigla'
    elif int(birth_region) in range(161, 221):
        region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif int(birth_region) in range(221, 271):
        region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif int(birth_region) in range(271, 371):
        region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif int(birth_region) in range(371, 421):
        region = 'Narva haigla'
    elif int(birth_region) in range(421, 471):
        region = 'Pärnu haigla'
    elif int(birth_region) in range(471, 491):
        region = 'Haapsalu haigla'
    elif int(birth_region) in range(491, 521):
        region = 'Järvamaa haigla (Paide)'
    elif int(birth_region) in range(521, 571):
        region = 'Rakvere haigla, Tapa haigla'
    elif int(birth_region) in range(571, 601):
        region = 'Valga haigla'
    elif int(birth_region) in range(601, 651):
        region = 'Viljandi haigla'
    elif int(birth_region) in range(651, 701):
        region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
    else:
        region = 'Unknown'

    # Print results
    print(f'Your id code is {user_id}')
    print(f'You are {gender}')
    print(f'Your date of birth is {bd}.{bm}.{birth_cent}{by}')
    print(f'You were born in {region}')
    print(f'Your check number is {chk_number}')

elif user_choice == '2':
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    chk_result = 0
    cnt_index = 0
    for num in chk1:
        chk_result += int(user_id[cnt_index]) * chk1[cnt_index]
        cnt_index += 1
    if chk_result % 11 == 10 or chk_result % 11 == 0:
        chk_result = 0
        cnt_index = 0
        for num in chk2:
            chk_result += int(user_id[cnt_index]) * chk2[cnt_index]
            cnt_index += 1
        if chk_result % 11 == int(user_id[10]):
            print('Code is valid. Used second range')
        else:
            print('Code is not valid. Used second range')
    elif chk_result % 11 == int(user_id[10]):
        print('Code is valid. Used first range')
    else:
        print('Code is not valid. Used first range')
elif user_choice == '3':
    pass
else:
    print('Choice is out of range')