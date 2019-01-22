"""
Candy data reader
We want to find some results of the candy sales data

"""

import os
import csv


my_dir = os.path.dirname(os.path.realpath(__file__))
items_filename = 'items.csv'
transactions_filename = 'transactions.csv'

dict_items = {}
dict_transactions = {}
chock = []
vanil = []
cher = []
ketch = []
dict_chock = {'Elon':[],'Frozone':[],'Emilia':[]}
dict_vanil = {'Elon':[],'Frozone':[],'Emilia':[]}
dict_cher = {'Elon':[],'Frozone':[],'Emilia':[]}
dict_ketch = {'Elon':[],'Frozone':[],'Emilia':[]}

with open(my_dir + '/' + items_filename, 'r') as items, open(my_dir + '/' + transactions_filename, 'r') as transactions:
    items_csv_file = csv.reader(items)
    transactions_csv_file = csv.reader(transactions)
    next(items_csv_file)
    next(transactions_csv_file)

    for row_items in items_csv_file:
        key_items = int(row_items[0])
        value_name = row_items[1]
        value_flavor = row_items[2]
        value_items = [value_name, value_flavor]
        dict_items[key_items]= value_items

        for row_transactions in transactions_csv_file:
            key_transactions = int(row_transactions[0])
            value_customer = row_transactions[1]
            value_item_id = int(row_transactions[2])
            value_quantity = int(row_transactions[3])
            value_transactions = [value_customer, value_item_id, value_quantity]
            dict_transactions[key_transactions]=value_transactions
    # print(dict_items)
    # print(dict_transactions)

    for index in range(10):
        flavor = dict_transactions[index+1][1]
        if flavor==0:
            for num in range(dict_transactions[index+1][2]):
                chock.append(0)
        elif flavor==1:
            for num in range(dict_transactions[index+1][2]):
                vanil.append(0)
        elif flavor==2:
            for num in range(dict_transactions[index+1][2]):
                cher.append(0)
        elif flavor==3:
            for num in range(dict_transactions[index+1][2]):
                ketch.append(0)
    # print(chock, vanil, cher, ketch)
    print('{0} Chocolate, {1} Vanilla, {2} Cherry, and {3} Ketchup  were bought'.format(len(chock),len(vanil),len(cher),len(ketch)))


    for index2 in range(10):
        if dict_transactions[index2+1][1] == 0:
            for index3 in range(dict_transactions[index2+1][2]):
                dict_chock[dict_transactions[index2+1][0]].append(0)
        elif dict_transactions[index2+1][1] == 1:
            for index3 in range(dict_transactions[index2+1][2]):
                dict_vanil[dict_transactions[index2+1][0]].append(0)
        elif dict_transactions[index2+1][1] == 2:
            for index3 in range(dict_transactions[index2+1][2]):
                dict_cher[dict_transactions[index2+1][0]].append(0)
        elif dict_transactions[index2+1][1] == 3:
            for index3 in range(dict_transactions[index2+1][2]):
                dict_ketch[dict_transactions[index2+1][0]].append(0)


    keys_chock = list(dict_chock.keys())
    if len(dict_chock[keys_chock[0]]) > len(dict_chock[keys_chock[1]]):
        if len(dict_chock[keys_chock[0]]) > len(dict_chock[keys_chock[2]]):
            print('Elon bought most of Chocolate Chockula')
        else:
            print('Emilia bought most of Chocolate Chockula')
    else:
        if len(dict_chock[keys_chock[1]]) > len(dict_chock[keys_chock[2]]):
            print('Frozone bought most of Chocolate Chockula')
        else:
            print('Emilia bought most of Chocolate Chockula')

    keys_vanil = list(dict_vanil.keys())
    if len(dict_vanil[keys_vanil[0]]) > len(dict_vanil[keys_vanil[1]]):
        if len(dict_vanil[keys_vanil[0]]) > len(dict_vanil[keys_vanil[2]]):
            print('Elon bought most of Vanilla Crema')
        else:
            print('Emilia bought most of Vanilla Crema')
    else:
        if len(dict_vanil[keys_vanil[1]]) > len(dict_vanil[keys_vanil[2]]):
            print('Frozone bought most of Vanilla Crema')
        else:
            print('Emilia bought most of Vanilla Crema')

    keys_cher = list(dict_cher.keys())
    if len(dict_cher[keys_cher[0]]) > len(dict_cher[keys_cher[1]]):
        if len(dict_cher[keys_cher[0]]) > len(dict_cher[keys_cher[2]]):
            print('Elon bought most of Cherry Bing')
        else:
            print('Emilia bought most of Cherry Bing')
    else:
        if len(dict_cher[keys_cher[1]]) > len(dict_cher[keys_cher[2]]):
            print('Frozone bought most of Cherry Bing')
        else:
            print('Emilia bought most of Cherry Bing')

    keys_ketch = list(dict_ketch.keys())
    if len(dict_ketch[keys_ketch[0]]) > len(dict_ketch[keys_ketch[1]]):
        if len(dict_ketch[keys_ketch[0]]) > len(dict_ketch[keys_ketch[2]]):
            print('Elon bought most of Ketchup Tommy')
        else:
            print('Emilia bought most of Ketchup Tommy')
    else:
        if len(dict_ketch[keys_ketch[1]]) > len(dict_ketch[keys_ketch[2]]):
            print('Frozone bought most of Ketchup Tommy')
        else:
            print('Emilia bought most of Ketchup Tommy')
