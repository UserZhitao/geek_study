# coding:utf-8
import copy
def start_game():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("""
        1. **Create hero**
        2. **Show hero info**
        3. **Update hero info**
        4. **Delete the hero**
        5. **Exit**
        6. **Show all hero info**
        """)
def create_hero(hero_list,hero_name_list):
    print('You will create a new hero')
    while True:
        name = input('Please input the hero name: \n')
        if name in hero_name_list:
            print('Sorry, the hero name has existed, please input again')
            continue
        hp = input('Please input the hero Hit Points: \n')
        attack_power = input('Please input the hero attack power: \n')
        hero_info = {'Name': name, 'HP': hp, 'Power': attack_power}
        print('Create Success!!!')
        hero_name_list.append(name)
        hero_list.append(hero_info)
        break

def get_hero_from_list(hero_list,search_name):
    for i in hero_list:
        if i.get('Name') == search_name:
            return i
    return {}

def get_index_for_hero_name(hero_name_list,search_name):
    for j in range(len(hero_name_list)):
        if hero_name_list[j] == search_name:
            return j
    print('No hero name is %s'.format(search_name))
    return len(hero_name_list)
def search_hero():
    search_name = input('Please enter the name of the hero you want to view: \n')
    search_flag = False
    i = get_hero_from_list(hero_list,search_name)
    if len(i):
        print(
            'Hero Name: ' + i.get('Name') + '\n' + 'Hero hp: ' + i.get('HP') + '\n' + 'Hero Attack Power: ' + i.get(
                'Power') + '\n')
    else:
        print(f'No hero name is {search_name}')
    # for i in hero_list:
    #     if i.get('Name') == search_name:
    #         print(
    #             'Hero Name: ' + i.get('Name') + '\n' + 'Hero hp: ' + i.get('HP') + '\n' + 'Hero Attack Power: ' + i.get(
    #                 'Power') + '\n')
    #         search_flag = True
    #         break
    # if search_flag:
    #     pass
    # else:
    #     print(f'No hero name is {search_name}')

def update_hero_info(hero_list,hero_name_list):
    search_name = input('Please enter the name of the hero you want to update: \n')
    search_flag = False
    i = get_hero_from_list(hero_list, search_name)
    if len(i):
        j = get_index_for_hero_name(hero_name_list,search_name)
        new_hero_name_list = copy.deepcopy(hero_name_list)
        new_hero_name_list.pop(j)
        while True:
            new_name = input('Please input the hero new name: \n')
            if new_name in new_hero_name_list:
                print('Sorry, the hero name has existed, please input again')
                continue
            i['Name'] = new_name
            break
        i['HP'] = input('Please input the hero new Hit Points: \n')
        i['Power'] = input('Please input the hero new attack power: \n')
        hero_name_list[j] = new_name
        print('Update Success!!!')
    else:
        print(f'No hero name is {search_name}')
    # for i in hero_list:
    #     if i.get('Name') == search_name:
    #         while True:
    #             new_name = input('Please input the hero new name: \n')
    #             if new_name in hero_name_list:
    #                 print('Sorry, the hero name has existed, please input again')
    #                 continue
    #             i['Name'] = new_name
    #             break
    #         i['HP'] = input('Please input the hero new Hit Points: \n')
    #         i['Power'] = input('Please input the hero new attack power: \n')
    #         for j in range(len(hero_name_list)):
    #             if hero_name_list[j] == search_name:
    #                 hero_name_list[j] = new_name
    #                 break
    #         search_flag = True
    #         break
    # if search_flag:
    #     print('Update Success!!!')
    #     # pass
    # else:
    #     print(f'No hero name is {search_name}')

def delete_hero(hero_list,hero_name_list):
    search_name = input('Please enter the name of the hero you want to delete: \n')
    search_flag = False
    i = get_hero_from_list(hero_list, search_name)
    if len(i):
        hero_list.remove(i)
        for i in hero_name_list:
            if i == search_name:
                hero_name_list.remove(i)
                break

        print('Delete Success!!!')
    else:
        print(f'No hero name is {search_name}')
    # for i in hero_list:
    #     if i.get('Name') == search_name:
    #         hero_list.remove(i)
    #         search_flag = True
    #         break
    # for i in hero_name_list:
    #     if i == search_name:
    #         hero_name_list.remove(i)
    #         break
    # if search_flag:
    #     print('Delete Success!!!')
    #     # pass
    # else:
    #     print(f'No hero name is {search_name}')
#多个数据，使用List
#每个影响有多个属性， key-value， 使用Dict

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game()
    hero_list = []
    hero_name_list = []
    while True:
        res = input('Please select the operation you want to execute: \n')
        if res == '1':
            create_hero(hero_list,hero_name_list)
            # print('You will create a new hero')
            # while True:
            #     name = input('Please input the hero name: \n')
            #     if name in hero_name_list:
            #         print('Sorry, the hero name has existed, please input again')
            #         continue
            #     hp = input('Please input the hero Hit Points: \n')
            #     attack_power = input('Please input the hero attack power: \n')
            #     hero_info = {'Name': name, 'HP': hp, 'Power': attack_power}
            #     print('Create Success!!!')
            #     hero_name_list.append(name)
            #     hero_list.append(hero_info)
            #     break
            # continue
        elif res == '2':
            search_hero()
            # search_name = input('Please enter the name of the hero you want to view: \n')
            # search_flag = False
            # for i  in hero_list:
            #     if i.get('Name') == search_name:
            #         print('Hero Name: ' + i.get('Name')+'\n' + 'Hero hp: ' + i.get('HP')+'\n'+ 'Hero Attack Power: ' + i.get('Power') + '\n')
            #         search_flag = True
            #         break
            # if search_flag:
            #     pass
            # else:
            #     print(f'No hero name is {search_name}')
        elif res == '3':
            update_hero_info(hero_list,hero_name_list)
            # search_name = input('Please enter the name of the hero you want to update: \n')
            # search_flag = False
            # for i  in hero_list:
            #     if i.get('Name') == search_name:
            #         while True:
            #             new_name = input('Please input the hero new name: \n')
            #             if new_name in hero_name_list:
            #                 print('Sorry, the hero name has existed, please input again')
            #                 continue
            #             i['Name'] = new_name
            #             break
            #         i['HP'] = input('Please input the hero new Hit Points: \n')
            #         i['Power'] = input('Please input the hero new attack power: \n')
            #         for j in range(len(hero_name_list)):
            #             if hero_name_list[j] == search_name:
            #                 hero_name_list[j] = new_name
            #                 break
            #         search_flag = True
            #         break
            # if search_flag:
            #     print('Update Success!!!')
            #     # pass
            # else:
            #     print(f'No hero name is {search_name}')
        elif res == '4':
            delete_hero(hero_list,hero_name_list)
            # search_name = input('Please enter the name of the hero you want to delete: \n')
            # search_flag = False
            # for i  in hero_list:
            #     if i.get('Name') == search_name:
            #         hero_list.remove(i)
            #         search_flag = True
            #         break
            # for i in hero_name_list:
            #     if i == search_name:
            #         hero_name_list.remove(i)
            #         break
            # if search_flag:
            #     print('Delete Success!!!')
            #     # pass
            # else:
            #     print(f'No hero name is {search_name}')
        elif res == '5':
            print('Exit Success')
            break
        elif res == '6':
            print(hero_list)
            print(hero_name_list)
        else:
            print('Input is invalid, please enter again')

