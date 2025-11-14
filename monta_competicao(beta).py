import requests

#PROTOTYPE FOR 14/11/2025 UFMGs IC SUBJECT FINAL PROJECT PRESENTATION

# Hardcoded for testing
competitors = ["matheussgr"]

problemset_url = f"https://codeforces.com/api/problemset.problems?"
problemset_res = requests.get(problemset_url).json()

# Retrieves global problemset
problemset = []
for problem in problemset_res["result"]["problems"]:

    rating = problem.get("rating")
    if rating is None:
        continue
    
    contestId = problem.get("contestId")
    index = problem.get("index")
    name = problem.get("name")

    problemset.append((contestId, index, name, rating))

# Retrieves problems already solved by competitors
solved_problems = set()
for competitor in competitors:
    competitor_status_url = (
        f"https://codeforces.com/api/user.status?handle={competitor}"
    )
    competitor_status_res = requests.get(competitor_status_url).json()

    for submission in competitor_status_res["result"]:
        if submission["verdict"] == "OK":
            solved_problems.add(
                (submission["problem"]["contestId"], submission["problem"]["index"])
            )

# Determinates the available problems for the challenge
valid_problems = []
for contest_id, index, name, rating in problemset:

    if (contest_id, index) not in solved_problems:
        valid_problems.append((contest_id, index, name, rating))
    else:
        print(
            f"REMOVED: Contest: {contest_id}\nIndex: {index}\nName: {name}\nRating: {rating}\n"
        )

#Order by rating
valid_problems.sort(key=lambda p: p[3])

# Display the available problems
print("\n<< Problemas disponíveis (20 primeiros)>>\n")

for contest_id, index, name, rating in valid_problems[:20]:
    print(f"Contest: {contest_id}\nIndex: {index}\nName: {name}\nRating: {rating}\n")
