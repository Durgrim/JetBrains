from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta, date

# Creating sqlite database engine with sqlalchemy
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

#  It allows us to create classes that include directives
#  to describe the actual database table they will be mapped to.
Base = declarative_base()

# Definition of the database table 'Table'
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

# Creation of the table in the database (sql commands)
Base.metadata.create_all(engine)

# Manages persistence operations for ORM-mapped objects
Session = sessionmaker(bind=engine)
session = Session()

# ***************************
# Definition of the functions
# ***************************

def show_all_task():
# Prints out all the tasks
    rows = session.query(Table).all()
    if len(rows) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows)):
            print(str(i+1) + '. ' + str(rows[i]) + " " + rows.deadline.strftime("%d %b"))


def show_week_task():
# Prints out all the tasks for one week (starting today)
    now = datetime.now()
    # now += timedelta(days=-now.weekday())  Remove comment to force the start of the week on current Monday
    for i in range(7):
        print()
        print(now.strftime("%A %d %b"))
        rows = session.query(Table).filter(Table.deadline == now.date()).all()
        now += timedelta(days=+1)
        if len(rows) == 0:
            print("Nothing to do!\n")
        else:
            for i in range(len(rows)):
                print(str(i+1) + '. ' + str(rows[i]))
    print()


def show_today_task():
# Prints out today's tasks
    today = datetime.today().strftime("%d %b")
    rows = session.query(Table).filter(Table.deadline == today).all()
    print("Today " + today + ":")
    if len(rows) == 0:
        print("Nothing to do!\n")
    else:
        for i in range(len(rows)):
            print(str(i+1) + '. ' + str(rows[i]))
        print()


def add_task():
# Database task addition
    task = input("\nEnter task\n")
    deadline = [int(n) for n in input("\nEnter deadline\n").split("-")]
    new_row = Table(task= task, deadline= date(deadline[0], deadline[1], deadline[2]))
    session.add(new_row)
    session.commit()
    print("The task has been added!")
    return print()


def show_miss():
# Print missed tasks (ordered by deadline)
    now = datetime.now()
    rows = session.query(Table).filter(Table.deadline < now.date()).order_by(Table.deadline).all()
    print("\nMissed tasks:")
    if len(rows) == 0:
        print("Nothing is missed!\n")
    else:
        for i in range(len(rows)):
            print(rows[i].deadline)
            print(str(i+1) + '. ' + str(rows[i]) + " " + rows[i].deadline.strftime("%d %b"))
    print()


def delete_task():
# Delete tasks. Print all tasks (ordered by deadline)
    rows = session.query(Table).order_by(Table.deadline).all()
    if len(rows) == 0:
        print("Nothing to delete")
    else:
        print("\nChose the number of the task you want to delete:")
        for i in range(len(rows)):
            print(str(i+1) + '. ' + str(rows[i]) + " " + rows[i].deadline.strftime("%d %b"))
        n = int(input())
        session.delete(rows[n - 1])
        session.commit()
    print("The task has been deleted!\n")


def todolist():
# Main menu definition
    while True:
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")
        user = int(input())
        if user == 1:
            show_today_task()
        elif user == 2:
            show_week_task()
        elif user == 3:
            show_all_task()
        elif user == 4:
            show_miss()
        elif user == 5:
            add_task()
        elif user == 6:
            delete_task()
        elif user == 0:
            print("\nBye!\n")
            break

# ************************
# Execution of the program
# ************************

todolist()
