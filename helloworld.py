name = raw_input("what's your name?")
sum = 100+100
print ('hello %s' %name)
print ('sum=%d' %sum)
i = 0
total = 0
while i < 100 :
    i +=1
    if i%2 == 0 :
        continue
    else:
        total +=i
print ('1+3+5+7....+99=%d' %total)
