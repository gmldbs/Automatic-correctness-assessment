projects = ['Chart', 'Cli', 'Closure', 'Codec', 'Collections', 'Compress', 'Csv', 'Gson', 'JacksonCore','JacksonDatabind','JacksonXml', 'Jsoup', 'JxPath', 'Lang', 'Math', 'Mockito', 'Time']
numbers_of_bugs = [26,39,174,18,4,47,16,18,26,112,6,93,22,64,106,38,26]
deprecated_bugs = [[],[6],[63,93],[],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],[],[],[],[],[],[],[],[],[2],[],[],[21]]

active_bugs = []
for kind in range(len(numbers_of_bugs)):
    cnt = 0
    num = 0
    act = []
    while True:
        num+=1
        if num in deprecated_bugs[kind]: continue
        cnt+=1
        act.append(num)
        if cnt == numbers_of_bugs[kind]: break
    active_bugs.append(act)

for kind in range(len(projects)):
    for each_bug in active_bugs[kind]:
        print('{} {}'.format(projects[kind],each_bug))
