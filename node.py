class Node(object):

    def __init__(self, dest, distant):
        self.dest = dest
        self.distant = distant

    def __str__(self):
        return "dest: " + self.dest + ", distant: " + str(self.distant)
