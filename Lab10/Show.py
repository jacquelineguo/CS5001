class Show:
    def __init__(self, title, actor_list):
        self.title = title
        self.actor_list = actor_list
        self.channel_set = set()
        for actor in actor_list:
            actor.show_set.add(self)
        
    def cast_contains(self, a1):
        for a2 in self.actor_list:
            if (a1.fname == a2.fname and a1.lname == a2.lname):
                return True
        return False

