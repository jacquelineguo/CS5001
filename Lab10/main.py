'''
Xuan Guo, Zihan Wang, Qiong Peng
CS5001, Fall 2020
Lab 10
'''
from Actor import Actor
from Channel import Channel
from Show import Show

def shows_starring(actor, avaliable_channels):
    starring_list = []
    for ch in avaliable_channels:
        starring_list += ch.get_shows_by_actor(actor)
    return starring_list

def all_shows_by_day(day, avaliable_channels):
    all_shows = set()
    for ch in avaliable_channels:
        all_shows |= ch.schedule[day]
    return all_shows

# print('actor1 = Actor("Actor", "1"​)'.encode('ascii', 'ignore'))
# print('actor2 = Actor(​"Actor"​, ​"2"​)'.encode('ascii', 'ignore'))
# print('actor3 = Actor(​"Actor"​, ​"3"​)'.encode('ascii', 'ignore'))
# print('show1 = Show(​"Monday Show"​, [actor1, actor2])'.encode('ascii', 'ignore'))
# print('show2 = Show(​"Tuesday Show"​, [actor1, actor2, actor3]) show3 = Show(​"Friday Show"​, [actor2, actor3]) channel1 = Channel(​"DEF"​, ​42​, [show1])'.encode('ascii', 'ignore'))
# print('channel2 = Channel(​"XYZ"​, ​31​, [show2, show3])'.encode('ascii', 'ignore'))

actor1 = Actor("Actor", "1")
actor2 = Actor("Actor", "2")
actor3 = Actor("Actor", "3")
show1 = Show("Monday Show", [actor1, actor2])
show2 = Show("Tuesday Show", [actor1, actor2, actor3])
show3 = Show("Friday Show", [actor2, actor3]) 
channel1 = Channel("DEF", 42, [show1])
channel2 = Channel("XYZ", 31, [show2, show3])
channel = [channel1, channel2]

# for x in (actor3.show_set):
#     print(x.title)

# PART 1
print("----------PART1-------------")
l = shows_starring(actor3, channel)
for x in l:
    print(x.title)


# PART2-1
print("----------PART2-1-------------")
for x in show3.channel_set:
    print(x.name)

# PART2-3
print("----------PART2-3-------------")
day = "mon"
print("default schedule")
for day in ["mon", "tue", "wed", 'thur', "fri", "sat", "sun"]:
    print(day)
    for x in all_shows_by_day(day, channel):
        print("---", x.title)
        
print("\nafter some reschedule")
channel2.reschedule_show("tue", show2)
channel2.reschedule_show("fri", show3)
channel1.reschedule_show("mon", show1)
for day in ["mon", "tue", "wed", 'thur', "fri", "sat", "sun"]:
    print(day)
    for x in all_shows_by_day(day, channel):
        print("---", x.title)