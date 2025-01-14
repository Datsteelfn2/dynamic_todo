do_list=[]


def add():
    task=input("What task do you want to add:> ")
    due=input("When is that task due:> ")
    priority=input("What is the priority:> ")
    row=[task,due,priority]
    do_list.append(row)

def remove():
    remove_what=input('Name the task you want to remove:> ')
    for row in do_list:
        if remove_what.strip().lower()==row[0].strip().lower():
            do_list.remove(row)
        else:
            print("name doesnt exist")
def view():
    view_choice=input("Do you want to view all todos or  based on priority:> ")
    if view_choice.strip().lower()[0]=='a':
        if not do_list:
            print("List is empty")
        for row in do_list:
            for item in row:
                print(f"{item:^10}",end=' | ')
            print()# turns each row into a new line

    if view_choice.strip().lower()[0]=='p':
        priority_choice=input("Which priority?> ")
        if priority_choice.strip().lower()[0]=='h':
            for row in do_list:
                for item in row:
                    if row[2].strip().lower()[0]=='h':
                        print(f"{item:^10}", end=' | ')
                print()
        elif priority_choice.strip().lower()[0]=='m':
            for row in do_list:
                for item in row:
                    if row[2].strip().lower()[0]=='m':
                        print(f"{item:^10}", end=' | ')
                print() 
        elif priority_choice.strip().lower()[0]=='l':
            for row in do_list:
                for item in row:
                    if row[2].strip().lower()[0]=='l':
                        print(f"{item:^10}", end=' | ')
                print()  


while True:
    choice=input("Do you want to add,remove,view or edit:> ")
    if choice.strip().lower()[0]=='a':
        add()
    elif choice.strip().lower()[0]=='r':
        remove()
    elif choice.strip().lower()[0]=='v':
        view()
    exit=input('do you want to exit:> ')
    if exit.strip()=='y':
        break