# 装饰器的高级使用：校验用户权限（读、写、执行、删除）
user_permission = 11

DELETE_PERMISSION = 8
READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXECCUTE_PERMISSION =1

def check_permission(m, n):
    def handle_action(fn):
        def do_action():
            if m & n != 0:
                fn()
            else:
                print("权限不足")
        return do_action
    return handle_action

@check_permission(user_permission, READ_PERMISSION)
def read():
    print("正在读取内容……")

@check_permission(user_permission, WRITE_PERMISSION)
def write():
    print("正在写入内容……")

@check_permission(user_permission, EXECCUTE_PERMISSION)
def execute():
    print("正在执行……")

@check_permission(user_permission, DELETE_PERMISSION)
def delete():
    print("正在删除内容……")

read()
write()
execute()
delete()