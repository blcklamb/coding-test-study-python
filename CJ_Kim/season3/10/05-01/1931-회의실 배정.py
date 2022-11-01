import sys, operator
input = sys.stdin.readline

meetingNum = int(input())
meetingList = []
for _ in range(meetingNum):
    start, end = map(int, input().split())
    meetingList.append((start, end))

'''
조건문 처리 예시
0 1 2 3 4 5 6
  |-----|
1)  |--|

2)  |---|
    |-------|

3)      |---|
          |-|    
'''
# 시작시간대로 정렬한 뒤, 같은 시작시간일 경우, 끝시간대로 정렬하기
meetingList = sorted(meetingList, key=operator.itemgetter(0, 1))

confirmedMeeting = []

for thisMeeting in meetingList:
    if not confirmedMeeting:
        confirmedMeeting.append(thisMeeting)
        continue
    prevStart, prevEnd = confirmedMeeting[-1]
    currStart, currEnd = thisMeeting
    if currStart < prevEnd:
        # 1)
        if currEnd < prevEnd:
            confirmedMeeting.pop()
            confirmedMeeting.append(thisMeeting)
        # 2)
    else:
        # 3)
        confirmedMeeting.append(thisMeeting)

print(len(confirmedMeeting))