f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in word_set:
    word_set.add(word.lower())


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# make graph
# treverse it BFS
# Parse result and return

def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            # loop though string_word and change each letter to letter and check
            # if it's a word in the provided list
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors


def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v= path[-1]
        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)


print(find_word_ladder('boat', 'hail'))