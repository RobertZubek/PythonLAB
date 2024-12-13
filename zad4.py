from collections import deque, defaultdict


class AhoCorasick:
    def __init__(self):
        self.trie = {}  
        self.fail = {} 
        self.output = defaultdict(list) 
        self.state_count = 0 

    def build_trie(self, patterns):
        self.trie = {0: {}} 
        self.state_count = 1

        for pattern in patterns:
            current_state = 0
            for char in pattern:
                if char not in self.trie[current_state]:
                    self.trie[current_state][char] = self.state_count
                    self.trie[self.state_count] = {}
                    self.state_count += 1
                current_state = self.trie[current_state][char]
            self.output[current_state].append(pattern)

    def build_automaton(self):
        self.fail = {0: 0}  
        queue = deque()

        for char, next_state in self.trie[0].items():
            self.fail[next_state] = 0
            queue.append(next_state)

        while queue:
            current_state = queue.popleft()

            for char, next_state in self.trie[current_state].items():
                fail_state = self.fail[current_state]
                while fail_state != 0 and char not in self.trie[fail_state]:
                    fail_state = self.fail[fail_state]

                self.fail[next_state] = self.trie[fail_state].get(char, 0)

                self.output[next_state].extend(self.output[self.fail[next_state]])

                queue.append(next_state)

    def search(self, text):
        matches = []
        current_state = 0

        for i, char in enumerate(text):
            while current_state != 0 and char not in self.trie[current_state]:
                current_state = self.fail[current_state]

            current_state = self.trie[current_state].get(char, 0)

            for pattern in self.output[current_state]:
                matches.append((i - len(pattern) + 1, pattern))

        return matches


if __name__ == "__main__":
    patterns = ["he", "she", "his", "hers"]
    text = "ahishers"

    ac = AhoCorasick()
    ac.build_trie(patterns)
    ac.build_automaton()
    matches = ac.search(text)

    print("Znalezione wzorce:")
    for index, pattern in matches:
        print(f"Wzorzec '{pattern}' znaleziony na pozycji {index}.")
