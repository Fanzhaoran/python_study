def read_input():
    incompatible_num, container_num = map(int, input().strip().split(" "))
    incompatibility = list()
    containers = list()

    incompatible_num_temp = incompatible_num
    while incompatible_num_temp:
        __info = input().strip().split(" ")
        incompatibility.append(__info)
        incompatible_num_temp -= 1

    container_num_temp = container_num
    while container_num_temp:
        __info = input().strip().split(" ")
        containers.append(__info[1:])
        container_num_temp -= 1

    return incompatible_num, container_num, incompatibility, containers


def func():
    incompatible_num, container_num, incompatibility, containers = read_input()

    incompatibility_dict = {}

    for incompatibility_item in incompatibility:
        if not incompatibility_dict.get(incompatibility_item[0]):
            incompatibility_dict[incompatibility_item[0]] = []
        incompatibility_dict[incompatibility_item[0]].append(incompatibility_item[1])

    for container in containers:
        result = True
        for item in container:
            if not result:
                break

            if incompatibility_dict.get(item):
                for incompatibility_item in incompatibility_dict[item]:
                    if incompatibility_item in container:
                        result = False
                        break
        if result:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    func()
