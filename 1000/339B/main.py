n_houses, n_task = map(int, input().split())
tasks = [int(task) for task in input().split()]
houses_count = tasks[0] - 1

for current_task, last_task in zip(tasks[1:], tasks):
    if current_task < last_task:
        houses_count += n_houses - last_task
        houses_count += current_task
    elif current_task > last_task:
        houses_count += current_task - last_task

print(houses_count)
   