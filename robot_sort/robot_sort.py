class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        '''
        bubble sort due to the robots light being like swap = true
        def bubble_sort(arr):
            swap = True
            while swap is True:
                swap = False
                for i in range(0, len(arr)-1):
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swap = True
            return arr
        print(bubble_sort(testArray))
        '''
        def swap_moveright():
            self.swap_item()
            self.move_right()
        def swap_turnlight():
            self.swap_item()
            self.set_light_on()

        self.set_light_on()
        ''' while swap is true'''
        while self.light_is_on():
            '''swap = false'''
            self.set_light_off()
            '''if I can move once to the right'''
            while self.can_move_right():
                '''on first pass replace none with 1st item'''
                '''on second pass replace none with 2nd item'''
                swap_moveright()
                # self.swap_item()
                ''' then move to the right'''
                # self.move_right()
                ''' 1st compare item 0 to item 1'''
                ''' 2nd compare item 1 to item 2'''
                ''' third pass compare item 2 to item 3'''
                ''' first pass compare_item isn't 1'''
                ''' second pass compare_item isn't 1'''
                ''' third pass compare_item is 1'''
                if self.compare_item() == 1:
                    ''' if item is bigger swap items'''
                    swap_turnlight()
                    # self.swap_item()
                    ''' turn light back on because a swap occured'''
                    # self.set_light_on()
                '''first pass we just move back to the left and put the 15 back down'''
                '''second pass we just move back to the left and put the 41 back down'''
                '''move back to the left where you started'''
                self.move_left()
                '''first pass put the item from index 0 back and take none'''
                '''second pass put the item from index 1 back and take none''' 
                ''' robot now has none in his hand again'''
                swap_moveright()
                # self.swap_item()
                ''' on first pass robot puts back down the 15 and picks up the None'''
                '''move back in front of where the compared swap occured'''
                # self.move_right()
            while self.can_move_left():
                self.move_left()


'''HOW TO OPTIMIZE THIS ROBOT'''
'''DO I NEED TO TWEAK THIS BUBBLE-esque SORT OR USE ANOTHER SORTING METHOD'''

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)