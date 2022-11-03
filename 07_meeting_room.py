class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        meeting_rooms = 0 # number of meeting rooms
        meeting_end_time = [] # Sorted List of started meetings end time
        for meeting in intervals:
            meeting_end_time.sort() # sort the list
            start_time = meeting[0]
            end_time = meeting[1]

            # first meeting
            if meeting_rooms == 0:
                meeting_rooms += 1 # 1
                meeting_end_time.append(end_time) # [30]
            else:
                if start_time >= meeting_end_time[0]:
                    # re-use a meeting room
                    meeting_end_time.pop(0)
                    meeting_end_time.append(end_time)
                else:
                    # need a new room
                    meeting_rooms += 1
                    meeting_end_time.append(end_time)
        return meeting_rooms


obj = Solution()
interval = [[7,10],[2,4]]
output = obj.minMeetingRooms(intervals=interval)
print(output)
