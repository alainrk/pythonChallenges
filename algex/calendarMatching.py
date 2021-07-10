def calendarMatching(cal1, bounds1, cal2, bounds2, duration):
	cal1 = calToMins(cal1)
	cal2 = calToMins(cal2)
	bounds1 = list(map(lambda t: toMins(t), bounds1))
	bounds2 = list(map(lambda t: toMins(t), bounds2))

	busy = merge(cal1, cal2, bounds1, bounds2)

	res = []

	for i in range(len(busy) - 1):
		# re-establish correcteness of this end, if the start was changed previously
		busy[i][1] = max(busy[i])
		# change the start of the next to align with the end of this one
		busy[i+1][0] = max(busy[i][1], busy[i+1][0])
		# add the slot if possible
		if busy[i + 1][0] - busy[i][1] >= duration:
			res.append([busy[i][1], busy[i+1][0]])

	res = calToTime(res)
	return res

def merge(cal1, cal2, bounds1, bounds2):
	busy = [] # merge busy slots
	maxstart = max(bounds1[0], bounds2[0])
	minend = min(bounds1[1], bounds2[1])
	busy.append([0, maxstart])

	c1, c2 = 0, 0
	while c1 < len(cal1) and c2 < len(cal2):
		s1, e1 = cal1[c1]
		s2, e2 = cal2[c2]
		case = situation(cal1[c1], cal2[c2])

		if case == "after":
			busy.append([s2, e2])
			c2 += 1
		if case == "beforematch":
			busy.append([s1, e2])
			c1 += 1
		if case == "aftermatch":
			busy.append([s2, e1])
			c2 += 1
		if case == "before":
			busy.append([s1, e1])
			c1 += 1
		if case == "contained":
			busy.append([s2, e2])
			c1 += 1
		if case == "containing":
			busy.append([s1, e1])
			c2 += 1

	busy.extend(cal1[c1:])
	busy.extend(cal1[c2:])
	busy.append([minend, 60 * 24])

	for i in range(len(busy) - 1):
		busy[i + 1][0] = max(busy[i][1], busy[i + 1][0])

	return busy

def situation(slot1, slot2):
	s1, e1 = slot1
	s2, e2 = slot2

#		 [  ]
#	[  ]
	if s1 >= e2:
		return "after"

#		 [      ]
#	        [     ]
	if s1 <= s2 <= e1 <= e2:
		return "beforematch"

#		       [    ]
#	        [     ]
	if s2 <= s1 <= e2 <= e1:
		return "aftermatch"

#		 [  ]
#	           [  ]
	if e1 <= s2:
		return "before"

#		 [  ]
#	[           ]
	if s1 >= s2 and e1 <= e2:
		return "contained"

#		 [      ]
#	       [  ]
	if s1 <= s2 and e1 >= e2:
		return "containing"
	else:
		raise "invalid case or not handled"

def calToTime(cal):
	return list(map(lambda slot: [toTime(slot[0]), toTime(slot[1])], cal))

def calToMins(cal):
	return list(map(lambda slot: [toMins(slot[0]), toMins(slot[1])], cal))

def toMins(time):
	h, m = time.split(':')
	mins = int(h) * 60 + int(m)
	return mins

def toTime(mins):
	h, m = str(mins // 60), mins % 60
	m = str(m) if m else '00'
	return f'{h}:{m}'