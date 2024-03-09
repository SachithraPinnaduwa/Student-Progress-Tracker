from user import User


class Student(User):
    def __init__(self, user_id, pass_credits, defer_credits, fail_credits):
        super().__init__(user_id)
        self.pass_credits = pass_credits
        self.defer_credits = defer_credits
        self.fail_credits = fail_credits
        self.outcome = self.determine_outcome()

    def determine_outcome(self):
        total_credits = self.pass_credits + self.defer_credits + self.fail_credits
        if total_credits != 120:
            return 'Total credits incorrect'
        elif self.pass_credits == 120:
            return 'Progress'
        elif self.pass_credits == 100:
            return 'Progress (module trailer)'
        elif self.fail_credits <= 60:
            return 'Module retriever'
        else:
            return 'Exclude'

    def display_outcome(self):
        print(f"{self.user_id}: {self.outcome} - {self.pass_credits}, {self.defer_credits}, {self.fail_credits}")
