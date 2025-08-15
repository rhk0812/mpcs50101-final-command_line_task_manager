import argparse
import pickle

class Task:
    """Representation of a task
  Attributes:
              - created - date  (python built-in modules)
              - completed - date (time-stamp)
              - name - string
              - unique id - number (time hash, keep track of #) uuid python package
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
    """
    def __init__(self,name, priority):
     self.name = name
     self.priority = priority
     self.unique_id = #
     self.created = #
     self.completed = None
     self.due_date = None
    
class Tasks:
    """A list of `Task` objects."""
    #first time, if pickle file exists, create / if not open it up
    #load pickle, save it back to disk 

    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 
        # your code here

    def pickle_tasks(self):
        """Picle your task list to a file"""
        # your code here
        #last thing that happens before program closes

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        pass

    def report(self):
        pass

    def done(self):
        pass

    def query(self):
        pass

    def add(self):
        pass
    
    #add, list, report, done, delete,etc

def main():
    parser = argparse.ArgumentParser(description = "Update your ToDo List")
    parser.add_argument('--add', type=str, required = False, help = 'a taks string to add your list')
    parser.add_argument('--priority', type=int, required =False, default =1, help = "priority of task; default value is 1")
    parser.add_argument('--due', type = str, required=False, help="due date in dd/MM/YYY format")
    parser.add_argument('--query', type=str, required=False, nargs ="+", help="task details")
    parser.add_argument('--list', action = 'store_true', required = False, help="list all the tasks that have not been completed.")
    
    #parse the argument
    args = parser.parse_args()

    #Create instance of Tasks
    task_list = Tasks()

    #Read out arguments (note the types)
    if args.add:
        print(f"We need to add {args.add} to our todo list with a priority of {args.priority}")
        task_list.add(args.add, args.priority)

    elif args.report:
        print('Print out the report')

    #Create instance of Tasks


    for t in task_list.tasks():
        print("These are all the tasks in my Tasks() object")

    #to do something with the data based on the user commands
    task_list.pickle_tasks()
    exit

if __name__ == "__main__":
    main()
