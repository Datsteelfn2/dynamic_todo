do_list=[]



def add():
    task=input("What task do you want to add:> ")
    due=input("When is that task due:> ")
    priority=input("What is the priority:> ")
    row=[task,due,priority]
    do_list.append(row)
def remove():
    pass
def view():
    for row in do_list:
        for item in row:
            print(f"{item:^10}",end=' | ')
        print()

while True:
    choice=input("Do you want to add,remove,view or edit:> ")
    if choice.strip().lower()[0]=='a':
        add()
    elif choice.strip().lower()[0]=='r':
        remove()
    elif choice.strip().lower()[0]=='v':
        view()