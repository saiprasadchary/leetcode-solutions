from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_len=len(beginWord)
        que=deque()
        que.append((beginWord, 1))
        wordList=set(wordList)

        while que:
            q, level=que.popleft()
            if q == endWord:
                return level
            for ind in range(word_len):
                temp=""
                for ch in range(97, 123):
                    temp=q[:ind]+chr(ch)+q[ind+1:]
                    if temp in wordList:
                        wordList.remove(temp)
                        que.append((temp, level+1))

        return 0



        




# from collections import deque, defaultdict

# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         if endWord not in wordList:
#             return 0
        
#         # All words are of the same length.
#         L = len(beginWord)
        
#         # Dictionary to hold combination of words that can be reached from any given word.
#         # By replacing one letter at a time.
#         all_combo_dict = defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 # Key is the generic word
#                 # Value is a list of words which have the same intermediate generic word.
#                 all_combo_dict[word[:i] + '_' + word[i+1:]].append(word)
        
#         # Queue for BFS
#         queue = deque([(beginWord, 1)])
#         # Visited to make sure we don't repeat processing same word.
#         visited = {beginWord}
#         while queue:
#             current_word, level = queue.popleft()    
#             for i in range(L):
#                 # Intermediate words for current word
#                 intermediate_word = current_word[:i] + '_' + current_word[i+1:]
                
#                 # Next states are all the words which share the same intermediate state.
#                 for word in all_combo_dict[intermediate_word]:
#                     # If at any point if we find what we are looking for
#                     # i.e., the end word - we can return with the answer.
#                     if word == endWord:
#                         return level + 1
#                     # Otherwise, add it to the BFS Queue. Also mark it visited
#                     if word not in visited:
#                         visited.add(word)
#                         queue.append((word, level + 1))
#                 all_combo_dict[intermediate_word] = []  # Empty after processing
#         return 0