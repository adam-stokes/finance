import yaml


class Budget:

    """ Processes deductions current day """

    def __init__(self, budget_file):
        self.budget_file = budget_file
        with open(self.budget_file) as f:
            data = f.read().strip()
            self._budget = yaml.load(data)

    def save(self):
        """ updates today's budget """
        with open(self.budget_file, 'w') as f:
            f.write(yaml.safe_dump(self._budget, default_flow_style=False))

    def daily_spend(self):
        """ returns daily spend amount """
        if 'deductions' not in self._budget:
            return self._budget['daily_spend']
        else:
            # Add up dedications to reflect daily_spend
            _deduction_amount = 0
            for d, a in self._budget['deductions']:
                _deduction_amount += a
            return self._budget['daily_spend'] - _deduction_amount

    def monthly_spend(self):
        return self._budget['monthly_spend']

    def add_deduction(self, key, amount):
        """ Adds a deduction from daily spend """
        if 'deductions' not in self._budget:
            self._budget = dict(deductions=[(key, amount)])
        else:
            self._budget['deductions'].append((key, amount))

    def remove_deduction(self, key):
        self._budget['deductions'] = [(k, a) for k, a
                                      in self._budget['deducations']
                                      if k != key]

    def increase_daily_spend(self, amount):
        """ Increases daily spend for rest of current month """
        pass

    def increase_monthly_spend(self, amount):
        """ Increases monthly spend for rest of current month """
        pass
