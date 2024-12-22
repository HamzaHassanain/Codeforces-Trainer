import requests
from Task import Task
from connection import load_tasks_table, delete_db, create_db, insert


solved = set()
not_solved = set()
loaded = False
file_name = "db.cft"


def write_handle(handle):
    global file_name
    # append the handle to the end of the file_name
    with open(file_name, "a") as file:
        file.write(handle + "\n")


def read_handle():
    global file_name
    # read the handle from the end of the file_name
    with open(file_name, "r") as file:
        lines = file.readlines()
        return lines[-1].strip()


def tasks_tuple_to_tasks(tasks_tuple):
    # id, name, link, state, contestId, index

    tasks = []

    for task in tasks_tuple:
        tasks.append(Task(task[1], task[2], task[3]))
        tasks[-1].contestId = task[4]
        tasks[-1].index = task[5]

    for task in tasks:
        print(task.name, task.link, task.state)

    return tasks


def load_tasks(file=file_name):
    tasks = []
    try:
        with open(file, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                name = lines[i].strip()
                if i+1 >= len(lines):
                    break
                link = lines[i+1].strip()
                state = lines[i+2].strip()
                contestId = int(lines[i+3].strip())
                index = lines[i+4].strip()
                tasks.append(Task(name, link, state))
                tasks[-1].contestId = contestId
                tasks[-1].index = index
        tasks_tuple = load_tasks_table()

        # print(tasks_tuple_to_tasks(tasks_tuple))
        return tasks_tuple_to_tasks(tasks_tuple)
    except Exception as e:
        print(e)
        return []


def write_tasks(tasks):
    global file_name

    delete_db()
    create_db()

    for task in tasks:
        insert(task.name, task.link, task.state, task.contestId, task.index)

    # write to db file

    with open(file_name, "w") as file:
        for task in tasks:
            file.write(f"{task.name}\n{task.link}\n{task.state}\n{
                       task.contestId}\n{task.index}\n")


def make_task(problem, state):
    link = f"https://codeforces.com/problemset/problem/{
        problem['contestId']}/{problem['index']}"
    # print(state)
    tsk = Task(problem["name"], link, state)
    # print(tsk.state)
    tsk.contestId = problem["contestId"]
    tsk.index = problem["index"]

    return tsk


def get_status(contestId, index, my_handle, doRefresh=False):
    global solved, not_solved, loaded

    if doRefresh:
        loaded = False
        not_solved.clear()
        solved.clear()
    try:
        if not loaded:
            response2 = requests.get(
                f"https://codeforces.com/api/user.status?handle={my_handle}&from=1&count=1000")

            if response2.status_code == 200:
                result2 = response2.json()
                if "status" in result2 and result2["status"] == "OK":
                    submissions = result2["result"]
                    for submission in submissions:
                        if submission["verdict"] == "OK":
                            solved.add(
                                (submission["problem"]["contestId"], submission["problem"]["index"]))
                        else:
                            not_solved.add(
                                (submission["problem"]["contestId"], submission["problem"]["index"]))

                loaded = True

        if (contestId, index) in solved:
            return "AC"
        elif (contestId, index) in not_solved:
            return "WA"
        else:
            return "NA"

    except Exception as e:
        print(e)
        return "NA"


def fetch_random_unsolved_problmes_of_rate(problmes_count, rating_from, rating_to, my_handle):

    def is_valid(problem):
        return "contestId" in problem and "index" in problem and "rating" in problem and "type" in problem and problem["type"] == "PROGRAMMING"

    # print(response)
    try:
        url = f"https://codeforces.com/api/problemset.problems"
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            if "status" in result and result["status"] == "OK":
                problems = result["result"]["problems"]
                # print(problems)
                answer = []

                for problem in problems:
                    status = get_status(
                        problem["contestId"], problem["index"], my_handle)

                    if is_valid(problem) and status != "AC" and rating_from <= int(problem["rating"]) <= rating_to:
                        answer.append(make_task(problem, status))
                        if len(answer) == problmes_count:
                            break

                return answer
            else:
                raise Exception("Error: Status is not OK")
        else:
            raise Exception("Response status is not 200")

    except Exception as e:
        print(e)
        return []


# fetch_random_unsolved_problmes_of_rate(5, 3000, 3300, "Hamza_Hassanain")
