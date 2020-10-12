
"""
Design a data structure that can, efficiently with respect to time used,
store and check If the total of any three successively added elements is equal to a given total.
For example, MovingTotal creates an empty container with no existing totals.oppend([1, 2, 3]) appends elements [1, 2, 3],
which means that there is only one existing total (1+2+3= 6).
append(4) appends element 4 and creates an additional total from [2, 3, 4]. There would now be two totals (1+2+3=6 and 2+3+4= 9).
At this point contains(6) and contains(9) should return True, while contains(7) should return False.

"""


class MovingTotal:
    list1 = []
    list2 = []


    def append(self, numbers):
        for i in numbers:
            if len(self.list1) >= 2:
                self.calculate_sum_of_last_3_elements(i)
            else:
                self.list1.append(i)
        # print(self.list1)

    def calculate_sum_of_last_3_elements(self,n):
        self.list1.append(n)
        l = len(self.list1)
        s  = self.list1[-1] + self.list1[-2] + self.list1[-3]
        self.list2.append(s)


    def contains(self, total):
        if total in self.list2:
            return True
        return False

if __name__ == '__main__':
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))

    movingtotal.append([4])
    print(movingtotal.contains(9))
    print(movingtotal.contains(7))
    movingtotal.append([5])
    print(movingtotal.contains(12))
    print(movingtotal.contains(6))

    movingtotal1=MovingTotal()
