students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

vote_counter = {}

vote_counter['이영희'] = 0
vote_counter['김철수'] = 0
vote_counter['조민지'] = 0

for name in students:

    vote_counter[name] += 1

    print(vote_counter)
