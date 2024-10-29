from . import utils as ms
from threading import Thread

# def group_add_list(lake_name,user_name):
#     for i in user_name:
#         ms.group_add_member(lake_name,i)

def as_group_add_list(lake_name,user_name):
    Thread(target=ms.group_add_member, args=(lake_name,user_name,)).start()

def group_remove_list(lake_name,user_name):
    for i in user_name:
        ms.group_remove_member(lake_name,i)

def as_group_remove_list(lake_name,user_name):
    Thread(target=group_remove_list, args=(lake_name,user_name,)).start()