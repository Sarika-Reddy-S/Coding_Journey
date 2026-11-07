class Solution(object):
    def trafficSignal(self, timer):
        if timer==0:
            return "Green"
        elif timer==30:
            return "Orange"
        elif timer<=90 and timer>=30:
            return "Red"
        else:
            return "Invalid" 
        