import random
from pprint import pprint

class EstimatePopulation:
    def __init__(self):
        self.grid = [[2, 3, 2, 2, 1, 3, 3, 3, 2, 2],
                     [3, 2, 3, 2, 3, 3, 3, 2, 3, 2],
                     [1, 2, 2, 3, 3, 1, 3, 2, 2, 3],
                     [4, 2, 3, 2, 2, 4, 1, 2, 3, 2],
                     [2, 3, 3, 3, 3, 2, 2, 1, 2, 3],
                     [3, 3, 1, 3, 3, 2, 2, 2, 3, 2],
                     [3, 4, 4, 3, 3, 1, 3, 3, 2, 2],
                     [2, 3, 2, 2, 2, 4, 2, 3, 2, 3],
                     [3, 3, 2, 3, 2, 1, 4, 1, 2, 3],
                     [1, 0, 0, 2, 1, 0, 1, 0, 1, 1]]

    def conduct_experiment(self, iterations, plots):
        while len(plots) < iterations:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if (row, col) not in plots:
                plots[(row, col)] = self.grid[row][col]

        return plots

    def get_results(self, plots):
        total = 0
        for key, value in plots.items():
            total += value
            results = {"total": total, "average": total/len(plots)}
        return results

    def get_total(self):
        total = 0
        for i in range(10):
            for j in range(10):
                total += self.grid[i][j]

        return {"total": total, "average": total/100}


    def main(self):
        # do first 5
        first_5 = self.conduct_experiment(5, {})
        results_1 = self.get_results(first_5)
        print("Results for first 5")
        pprint(first_5)
        pprint(results_1)

        # do 20
        final = self.conduct_experiment(20, first_5)
        results_2 = self.get_results(final)
        print("Results for final 20")
        pprint(final)
        pprint(results_2)

        pprint("Total:")
        pprint(self.get_total())


if __name__ == '__main__':
    e = EstimatePopulation()
    e.main()
