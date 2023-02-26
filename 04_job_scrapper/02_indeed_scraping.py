from extractors.indeed import extract_indeed_jobs

keyword = input("What do you want to search for?")
jobs = extract_indeed_jobs(keyword)

for job in jobs:
    print(job)