import requests
from Task import Task

solved = set()
not_solved = set()
loaded = False
file_name = "db.cft"


def make_task(problem, state):
    link = f"https://codeforces.com/problemset/problem/{
        problem['contestId']}/{problem['index']}"
    # print(state)
    tsk = Task(problem["name"], link, state)
    # print(tsk.state)
    tsk.contestId = problem["contestId"]
    tsk.index = problem["index"]

    return tsk


def write_tasks(tasks):
    global file_name

    with open(file_name, "w") as file:
        for task in tasks:
            file.write(f"{task.name}\n{task.link}\n{task.state}\n{
                       task.contestId}\n{task.index}\n")


def get_status(contestId, index, my_handle):
    global solved, not_solved, loaded
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
