def operate_help(data):
    print("Help placeholder")
    return False

def operate_update(data):
    data["updated"] = True
    return True

commands = {  
    "help": operate_help,
    "update": operate_update,
}
