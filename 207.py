# 207. 课程表
# 中等
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
# 在选修某些课程之前需要一些先修课程。 
# 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，
# 表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

from collections import deque, defaultdict

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    processed_courses = 0
    while queue:
        course = queue.popleft()
        processed_courses += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return processed_courses == numCourses

# 示例使用
numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))  # 输出: True