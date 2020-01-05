class Counter:
    def __init__(self):
        self.mention_count = 0

    def mentions(self):
        return self.mention_count

    def mention_incr(self):
        self.mention_count += 1
        return self.mention_count

    def reset_counter(self):
        self.mention_count = 0
        return self.mention_count