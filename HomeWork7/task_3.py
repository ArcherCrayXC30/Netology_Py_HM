from libs.employee import Employee


class Designer(Employee):
    def __init__(self, name, seniority, grants=2):
        super().__init__(name, seniority + grants * 2)
        self.grants = grants

    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1

        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()


designer = Designer('Петров', 0, 2)

for i in range(22):
    designer.check_if_it_is_time_for_upgrade()
