def add_task(task_list, task):
    task_list.append(task)
    return task_list

def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
    else:
        print(f"'{task}' finnes ikke i listen.")
    return task_list
