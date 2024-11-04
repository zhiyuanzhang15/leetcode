# 1109. 航班预订统计
# 中等
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 
# 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
# 请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
def corpFlightBookings(bookings, n):
    answer = [0] * n
    for firsti, lasti, seatsi in bookings:
        answer[firsti-1] += seatsi
        if lasti < n :
            answer[lasti] -= seatsi
    for i in range(1,n):
        answer[i] += answer[i-1]
    return answer

bookings = [[1,2,10],[2,3,20],[2,5,25]] 
n = 5
print(corpFlightBookings(bookings,n))