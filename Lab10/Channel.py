import collections
DATE = ["mon", "tue", "wed", 'thur', "fri", "sat", "sun"]

class Channel:
    def __init__(self, name, number, show_list):
        self.name = name
        self.number = number
        self.show_list = show_list
        for show in show_list:
            show.channel_set.add(self)

        self.sched = Schedule(self.show_list)
        self.schedule = self.sched.schedule_dic


    def get_shows_by_actor(self, actor):
        shows_found = []
        for show in self.show_list:
            if show.cast_contains(actor):
                shows_found.append(show)
        return shows_found

    def reschedule_show(self, day, show):
        self.schedule = self.sched.reschedule(day, show)



class Schedule:
    def __init__(self, show_list):
        self.schedule_dic = collections.defaultdict(set)
        self.show2day = {}
        self.init_assign(show_list)
    
    def init_assign(self, show_list):
        for i in range(len(show_list)):
            self.schedule_dic[DATE[i % 7]].add(show_list[i])
            self.show2day[show_list[i]] = DATE[i % 7]

    def reschedule(self, day, show):
        self.schedule_dic[self.show2day[show]].remove(show)
        self.schedule_dic[day].add(show)
        self.show2day[show] = day
        return self.schedule_dic

