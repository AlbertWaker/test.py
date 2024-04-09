def insert(ls):#添加学生
    num=input("请输入学号:")
    name=input("请输入姓名:")
    sex=input("请输入性别:")
    subject=input("请输入专业:")
    native=input("请输入籍贯:")
    info={"学号":num,"姓名":name,"性别":sex,"专业":subject,"籍贯":native}
    ls.append(info)
def find(ls):#查询学生
    while True:
        print("1.按学号查询    2.按姓名查询")
        choose = input("请输入数字1-2:")
        if choose == '1':
            number=input("请输入学号:")
            for info in ls:
                if info["学号"]==number:
                    print("学号:",info["学号"], "姓名:", info["姓名"], "性别:", info["性别"], "专业:", info["专业"], "籍贯:", info["籍贯"])
                    return
            else:
                print("未找到该学生信息")
                break
        elif choose == '2':
            name=input("请输入姓名:")
            for info in ls:
                if info["姓名"]==name:
                    print("学号:",info["学号"], "姓名:", info["姓名"], "性别:", info["性别"], "专业:", info["专业"], "籍贯:", info["籍贯"])
                    return
            else:
                print("未找到该学生信息")
                break
        else:
            print("输入错误，请重新输入")
def modify(ls):#修改记录
    #input("修改记录，尚在建设")
    name=input("请输入要修改的学生姓名:")
    for info in ls:
        if info["姓名"]==name:
            while True:
                print("学号:", info["学号"], "姓名:", info["姓名"], "性别:", info["性别"], "专业:", info["专业"],"籍贯:", info["籍贯"])
                object = input("请输入要修改的对象(完成修改请输入退出):")
                if object in ["学号", "姓名", "性别", "专业", "籍贯"]:
                    revise=input("请修改:")
                    info[object] = revise
                    print("修改成功")
                elif object == "退出":
                    return
                else:
                    print("输入错误，请重新输入")
        else:
            print("修改失败，查无此人")
def delete(ls):#删除记录
    name=input("请输入要删除的学生的姓名:")
    for info in ls:
        if info["姓名"]==name:
            ls.remove(info)
            print("删除成功")
            return
    else:
        print("删除失败，查无此人")
        return
def star(ls):#人数统计
    while True:
        print("1.按专业统计  2.按籍贯统计  3.按性别统计")
        number = input("请输入数字1-3:")
        if number == '1':
            subject = input("请输入专业名称：")
            count = 0
            for info in ls:
                if info["专业"] == subject:
                    count += 1
            print(f"{subject}专业的学生人数为：{count}")
            return
        elif number == '2':
            native = input("请输入籍贯名称：")
            count = 0
            for info in ls:
                if info["籍贯"] == native:
                    count += 1
            print(f"{native}籍的学生人数为：{count}")
            return
        elif number == '3':
            sex = input("请输入性别（男/女）：")
            count = 0
            for info in ls:
                if info["性别"] == sex:
                    count += 1
            print(f"{sex}生的人数为：{count}")
            return
        else:
            print("输入错误，请重新输入")
def menu():#菜单
    print("**********************")
    print("      学生管理系统      ")
    print("**********************")
    print()
    print("1.添加学生    2.查询学生")
    print("3.修改记录    4.删除记录")
    print("5.人数统计    0.退出")
def main():#主函数
    ls=[]#学生列表初始化
    while True:
        menu()#菜单
        choice=input("请输入数字0-5:")#选择
        if choice=='1':
            insert(ls)#添加学生
        elif choice=='2':
            find(ls)#查询学生
        elif choice == '3':
            modify(ls)#修改记录
        elif choice == '4':
            delete(ls)#删除记录
        elif choice == '5':
            star(ls)#人数统计
        elif choice == '0':
            break#退出
        else:#非法输入
            print("输入错误，请重新输入")
    print("谢谢访问!")
main()#主函数


