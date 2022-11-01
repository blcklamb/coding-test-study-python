# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
left, times = map(int, input().split())
payList = []
for _ in range(times):
	type, money = input().split()
	while len(payList) != 0 and left-payList[0]>=0:
		left -= payList.pop(0)
	if type == 'deposit':
		left += int(money)
	elif type == 'pay':
		if left >= int(money):
			left -= int(money)
	else:
		if left < int(money):
			payList.append(int(money))
		elif len(payList) != 0:
			payList.append(int(money))
		else:
			left -= int(money)
	
while len(payList) != 0 and left-payList[0]>=0:
	left -= payList.pop(0)

print(left)