class TrieNode():
    def __init__(self,val = None,children ={},isEnd=False) -> None:
        self.val = val
        self.children = children
        self.isEnd = isEnd
class Trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        current = self.root
        for x in word:
            if x not in current.children:
                current.children[x] = TrieNode(x,{})
            current = current.children[x]
        current.isEnd = True
    
    def search(self,word):
        current = self.root
        for x in word:
            if x not in current.children:
                return False
            current = current.children[x]
        return current.isEnd
    
    def autocomplete(self,word,maxDepth=9999):
        curr = self.root
        for x in word:
            if x not in curr.children:
                print("unknown word")
                return []
            curr = curr.children[x]
        results = []
        queue = [[curr,list(word),0]]
        while queue:
            currentNode,genWord,d = queue.pop()
            if currentNode.isEnd:
                results.append("".join(genWord))
            if currentNode.children and (d+1) <= maxDepth:
                for x in currentNode.children:
                    queue.append([currentNode.children[x],genWord+[currentNode.children[x].val],d+1])
        return results
    

if __name__ == "__main__":
    suggest = Trie()
    suggest.insert("Pulp Fiction")
    suggest.insert("God Father")
    suggest.insert("The Great Gatsby")
    suggest.insert("God Father 2")
    suggest.insert("Terminator")
    print(suggest.autocomplete("The"))
    print(suggest.autocomplete("T"))
    print(suggest.autocomplete("Go"))