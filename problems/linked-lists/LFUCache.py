# https://leetcode.com/problems/lfu-cache/
# 460. LFU Cache

class FreqNode: 
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.next = next    
        self.prev = prev
        self.head = KeyNode()
        self.tail = KeyNode()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.count = 0

class KeyNode: 
    def __init__(self, val=None, prev=None, next=None, freqNode = None):
        self.val = val
        self.prev = prev
        self.next = next    
        self.freqNode = freqNode
        
def removeKeyNode(keyNode): 
    prev = keyNode.prev
    next = keyNode.next
    prev.next = next
    next.prev = prev
    keyNode.prev = None
    keyNode.next = None
    keyNode.freqNode.count -= 1
    return 

def insertKeyNode(keyNode, freqNode):
    keyNode.freqNode = freqNode
    nextAfterKeyNode = freqNode.head.next
    freqNode.keyNode
    keyNode.next = nextAfterKeyNode
    keyNode.prev = freqNode.head
    freqNode.count += 1
    return 

# don't forget to remove from the lookup
def removeFreqNode(freqNode): 
    prev = freqNode.prev
    next = freqNode.next
    prev.next = next
    next.prev = prev
    freqNode.prev = None
    freqNode.next = None
    return 

def insertFreqNode(freqNodeBeforeNew): 
    newNext = freqNodeBeforeNew.next
    newFreqNode = FreqNode(freqNodeBeforeNew.val + 1, freqNodeBeforeNew, newNext)
    newNext.prev = newFreqNode
    freqNodeBeforeNew.next = newFreqNode
    return 

# assumes count > 0
def evictLFU(freqNodeHead): 
    targetFreqNode = freqNodeHead.next
    targetKeyNode = targetFreqNode.tail.prev
    removeKeyNode(targetKeyNode)
    if targetFreqNode.count == 0: 
        removeFreqNode(targetFreqNode)
    return 


class LFUCache:

    def __init__(self, capacity: int):
        # self.freqNodes = {}
        self.keyNodes = {}
        self.freqNodeHead = FreqNode(0, None,None)
        self.count = 0
        self.countLimit = capacity    

    # (1) get the key, (2) increment frequency
    # to do (2): 
    # - remove keynode; keep track of prior val
    # - if freqNode + 1  doesn't exist, create it
    # - insert keynode into val + 1
    # - if old freqNode is empty, remove
    # - update value 
    def get(self, key: int) -> int:
        if key not in self.keyNodes: return -1 
        node = self.keyNodes[key]
        removeKeyNode(node)
        priorFreqNode = node.freqNode
        if not priorFreqNode.next or priorFreqNode.next.val != priorFreqNode.val + 1: 
            insertFreqNode(priorFreqNode, self.freqNodes)
        insertKeyNode(node, priorFreqNode.next)
        if priorFreqNode.count == 0: 
            removeFreqNode(priorFreqNode)                
        return key


    # update curCap, cap
    def put(self, key: int, value: int) -> None:
        # insert into the 1 spot
        if key not in self.keyNodes: 
            if self.cap == self.curCap: 
                evictLFU(self.freqNodeHead)
                self.curCap -= 1
            newKeyNode = KeyNode(value, None, None, None) # 
            self.keyNodes[value] = newKeyNode
            if not self.freqNodeHead.next or self.freqNodeHead.next.val != 1: 
                insertFreqNode(self.freqNodeHead)
            insertKeyNode(newKeyNode, self.freqNodeHead.next)        
            newKeyNode.freqNode = self.freqNodeHead.next
            self.curCap += 1                        
        else: 
        # update
                    
            # evict 
            #  UPDATE THIS LATER

        
        # do insertion

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)