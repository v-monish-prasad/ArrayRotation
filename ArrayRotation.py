def reverseArray(array):
    if not array:
        return "Empty Array."

    i = 0
    j = len(array) - 1

    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    return array


def rotateArray(array, B):
    if not array:
        return "Empty Array."

    length = len(array)
    if B > length:
        B %= length

    array = reverseArray(array)

    array = reverseArray(array[:B]) + reverseArray(array[B:])
    return array


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    B = int(input())
    print(rotateArray(array, B))
