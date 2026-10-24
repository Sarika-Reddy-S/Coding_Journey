class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        def to_date(date):
            month, day = map(int, date.split("-"))
            return month * 100 + day
        Astart = to_date(arriveAlice)
        Aend = to_date(leaveAlice)
        Bstart = to_date(arriveBob)
        Bend = to_date(leaveBob)
        start = max(Astart, Bstart)
        end = min(Aend, Bend)

        if start <= end:
            days = (end // 100 - start // 100) * 0  
            from datetime import date
            start_date = date(2025, start // 100, start % 100)
            end_date = date(2025, end // 100, end % 100)
            return ((end_date - start_date).days + 1)
        else:
            return 0
        