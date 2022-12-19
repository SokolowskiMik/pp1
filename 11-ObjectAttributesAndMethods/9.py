import random

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def create_array(number, lenght):
        arr = []
        for i in range(int(lenght)):
            arr.append(int(number))
        print(arr)

    @staticmethod
    def random_value(lenght, m, n):
        arr = []
        for i in range(lenght):
            arr.append(random.randint(m,n))

    @staticmethod
    def num_of_el(array,m,n):
        ile = dict
        for i in array:
            if i in range(-1, 2, 1):
                i = str(i)
                if i in ile:
                    ile[i] = ile.get(i, 0) + 1 
        print(ile)


my_array = [4,1,8,6,2]
Arrays.print_in_col(my_array)
Arrays.create_array(1, 10)
Arrays.random_value(10, 1, 2)

a1 = [1,-1,1,-1,2,2,3,3,-3,-3]

Arrays.num_of_el(a1, -1, 1)