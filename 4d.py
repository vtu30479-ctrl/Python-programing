def pain_balloons(s):
    amber=s.count('a')
    brass=s.count('b')
    pain_balloons=min(amber,brass)
    return pain_balloons
for i in range(int(input())):
    s=input().strip()
    print(pain_balloons(s))
