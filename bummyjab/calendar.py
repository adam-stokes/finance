from datetime import date, timedelta
from bummyjab.budget import Budget
import os.path as path
from os import makedirs
import yaml


class Calendar:

    def __init__(self, storage_dir):
        self.current_day = date.today().day
        self.current_month = date.today().month
        self.current_year = date.today().year
        self.storage_dir = storage_dir

    def create_budget_files(self):
        """ Creates budget files for current_day + year

        """
        def save(day):
            _save_path = path.join(self.storage_dir, str(day.year),
                                   str(day.month),
                                   str(day.day), 'budget.yaml')
            if not path.exists(_save_path):
                if not path.exists(path.dirname(_save_path)):
                    makedirs(path.dirname(_save_path))
                with open(_save_path, 'w') as f:
                    yaml_out = dict(timestamp=day)
                    f.write(yaml.safe_dump(yaml_out, default_flow_style=False))

        d1 = date.today()
        d2 = date(self.current_year + 1, self.current_month, self.current_day)
        delta = d2 - d1
        for i in range(delta.days + 1):
            save(d1 + timedelta(days=i))

    def load_today(self):
        """ loads today's budget
        """
        today_budget_file = path.join(self.storage_dir,
                                      str(self.current_year),
                                      str(self.current_month),
                                      str(self.current_day),
                                      'budget.yaml')
        if path.exists(today_budget_file):
            return Budget(today_budget_file)
        else:
            raise Exception('Couldnt load budget for {}'.format(date.today()))
