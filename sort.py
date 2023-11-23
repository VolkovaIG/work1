class sort():
    def __init__(self, lst1):
        self.lst1 = lst1

    def __str__(self):
        return self.any

    def _istype_(selfself,val):
        return isinstance((val, list) | (val, dict))

    def sort_vibor(any):
        for i in range(len(any)):
            first_ind = i
            for j in range(i + 1, len(any)):
                if any[j] < any[first_ind]:
                    first_ind = j
            any[i], any[first_ind] = any[first_ind], any[i]    # Меняем местами
        return any

lst = [20, 1, 8, 10, 15, 2, 0]
sort(lst.sort())
print(lst)
