# 1094. 拼车
# 中等
# 车上最初有 capacity 个空座位。
# 车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
# 给定整数 capacity 和一个数组 trips ,  
# trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，
# 接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。

def carPooling(trips, capacity):
    max_distance = 1001
    diff = [0] * max_distance

    for numPassengers, from_, to in trips:
        diff[from_] += numPassengers
        diff[to] -= numPassengers
    current_passengers = 0
    for i in range(max_distance):
        current_passengers += diff[i]
        if current_passengers>capacity:
            return False
    return True

trips = [[2,1,5],[3,3,7]]
capacity = 4
print(carPooling(trips,capacity))