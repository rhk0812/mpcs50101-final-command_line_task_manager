import argparse
import pickle
import datetime

class Task:
    """Representation of a task
    Attributes:
              - name - string
              - priority - int value of 1, 2, or 3; 1 is default, and 3 being highest
              - unique id - number (time hash, keep track of #) uuid python package
              - created - date  (python built-in modules)
              - completed - date (time-stamp)
              - due date - date, this is optional
    """
    #initializing task object
    def __init__(self,name,priority):
     self.name = name
     self.priority = priority
     self.unique_id = 0
     self.created = datetime.datetime.now().strftime("%a %b %d %X %Z %Y")
     self.completed = False
     self.due_date = None
    
class Tasks:
    """A list of `Task` objects."""

    def __init__(self):
        """Read pickled tasks file into a list"""
        # when the program is run first time, check if pickle file exists, 
        # if there is no pickle file, we create one.
        try:
            with open('.todo.pickle','rb') as f:
                self.tasks = pickle.load(f)
        except:
            #if there is no existing pickle file, we initialize the list
            self.tasks = []

    def pickle_tasks(self):
        """Picle your task list to a file"""
        #last thing that happens before program closes
        with open('.todo.pickle', 'wb') as f:
            pickle.dump(self.task, f)

  
    def list(self):
        pass

    def report(self):
        #display a list of not completed tasks sorted by due date. If same date, sort by decreasing priority
        pass

    def done(self):
        #marking it as complete
        pass

    def query(self):
        pass

    def add(self):
        #add a new task
        pass
    
    def delete(self):
        #delte the task with the unique identifier
        pass
    

def main():
    #parsing the arguments passed by the user
    """
    ex) --add "Walk Dog" --due 4/17/2018 --priority 1
        --add "Study for finals" --due 3/20/2018 --priority 3
        --list
        --query eggs
        --done 1
        --delete 3
        --report
    """
    parser = argparse.ArgumentParser(description = "Update your ToDo List")
    parser.add_argument('--add', type=str, required = False, help = 'a taks string to add your list')
    parser.add_argument('--priority', type=int, required =False, default =1, help = "priority of task; default value is 1")
    parser.add_argument('--due', type = str, required=False, help="due date in dd/MM/YYY format")
    parser.add_argument('--query', type=str, required=False, nargs ="+", help="task details")
    parser.add_argument('--list', action = 'store_true', required = False, help="list all the tasks that have not been completed.")
    parser.add_argument('--report', action = 'store_true', required = False, help="list all the tasks both completed and incompleted.")
    
    #parse the argument
    args = parser.parse_args()

    #Create instance of Tasks
    task_list = Tasks()


    #Read out arguments (note the types) + manipulate tasks

    if args.add:
        #task_list.add(args.add, args.priority)
        current_task=Task(args.add,args.priority)
        if args.due:
            try:
                #return datetime corresponding to date_string, parsed according to format MM/dd/YYY
                valid_date = datetime.strptime(args.due, "%m/%d/%Y")
                current_task.due_date = valid_date

            except ValueError:
                print("Please enter a date with format MM/dd/YYYY.")
            
        #print(current_task.name, current_task.priority, current_task.created, current_task.due_date)

    elif args.report:
        print('Print out the report')


#    for t in task_list.tasks():
 #       print("These are all the tasks in my Tasks() object")

    #to do something with the data based on the user commands
  #  task_list.pickle_tasks()
    exit

if __name__ == "__main__":
    main()
