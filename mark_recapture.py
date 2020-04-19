from copy import deepcopy
from statistics import mean
from pprint import pprint
import random


class MarkRecapture:
    def __init__(self):
        self.beans = [0 if i < 80 else 1 for i in range(100)]
        self.reps = 10
        self.sets = 15

    def experiment(self):
        #grab ten animals
        #wm = mark
        #nm = no mark
        beans_2 = deepcopy(self.beans)
        captured = []
        while len(captured) < self.reps:
            idx = random.randint(0, len(self.beans)-1)
            captured.append(beans_2[idx])
        return captured.count(0), captured.count(1)

    def repetitions(self):
        final = [self.experiment() for i in range(self.sets)]
        return final

    def get_averages(self):
        final_catch = self.repetitions()
        nm_avg = mean([f[0] for f in final_catch])
        wm_avg = mean([f[1] for f in final_catch])
        d = {"a_trials": final_catch, "nm_avg": nm_avg, "wm_avg": wm_avg}
        return d

    def calculate_population_size(self):
        """(M * (WM +NM)) /WM"""
        exp = self.get_averages()
        pprint(exp)
        pop_size = (20 * (exp["wm_avg"] + exp["nm_avg"]))/exp["wm_avg"]
        return pop_size


if __name__ == '__main__':
    mk = MarkRecapture()
    l = mk.calculate_population_size()
    pprint(l)



