    def test_stretch_times(self):
        robot = SortingRobot(self.small_list)
        robot.sort()
        self.assertLess(robot._time, 110)

        robot = SortingRobot(self.medium_list)
        robot.sort()
        print(robot._time)
        self.assertLess(robot._time, 1948)

        robot = SortingRobot(self.large_list)
        robot.sort()
        print(robot._time)
        self.assertLess(robot._time, 27513)

        robot = SortingRobot(self.large_varied_list)
        robot.sort()
        print(robot._time)
        self.assertLess(robot._time, 28308)