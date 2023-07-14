import copy


class RotateArray:
    def rotateBruteForce(self, arr, nor):
        # time = O(n2) and space = O(n)
        for rot in range(0, nor):
            first_elem = arr[0]
            for index in range(len(arr) - 1, -1, -1):
                next_index = 0 if index + 1 >= len(arr) else index + 1
                if next_index == 1:
                    arr[next_index] = first_elem
                else:
                    arr[next_index] = arr[index]

        return arr

    def rotateExtraArray(self, arr, nor):
        # time and space = O(n)
        rotated_array = [0]*len(arr)
        for index in range(len(arr)-1,-1,-1):
            next_index = (index + nor) % len(arr)
            rotated_array[next_index] = arr[index]

        return rotated_array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    print(f"Array before rotation {array}")
    ra = RotateArray()
    ret_array = ra.rotateExtraArray(array, 2)
    print(f"Array after rotation {ret_array}")
