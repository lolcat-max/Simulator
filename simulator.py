import numpy as np
from itertools import combinations

class SemanticSpatiotemporalSimulator:
    def __init__(self, alpha=1.0, delta=5.0):
        self.alpha = alpha  # Temporal distance weight
        self.delta = delta  # Spatiotemporal proximity threshold
        self.keywords = {}

    def add_keyword_occurrences(self, keyword, coords_times):
        """
        Add occurrences for a keyword.
        coords_times is a list of tuples (x, y, z, time)
        """
        self.keywords[keyword] = coords_times

    def spatiotemporal_distance(self, a, b):
        """
        Calculate combined spatiotemporal distance between two points (x,y,z,t)
        """
        spatial_dist = np.linalg.norm(np.array(a[:3]) - np.array(b[:3]))
        temporal_dist = abs(a[3] - b[3])
        return spatial_dist + self.alpha * temporal_dist

    def is_impossible_combination(self, keyword1, keyword2):
        """
        Check if any pair of occurrences from keyword1 and keyword2 have
        spatiotemporal distance >= threshold delta, indicating impossibility.
        Returns True if impossible, False otherwise.
        """
        if keyword1 not in self.keywords or keyword2 not in self.keywords:
            return False
        set1 = self.keywords[keyword1]
        set2 = self.keywords[keyword2]
        for c1 in set1:
            for c2 in set2:
                dist = self.spatiotemporal_distance(c1, c2)
                if dist >= self.delta:
                    return True
        return False

    def infer_all_possibilities(self):
        """
        Analyze all unique keyword pairs.
        Returns:
          possible: list of pairs with all distances < delta (possible together)
          impossible: list of pairs with any distance >= delta (impossible combination)
        """
        possible = []
        impossible = []
        for k1, k2 in combinations(self.keywords.keys(), 2):
            if self.is_impossible_combination(k1, k2):
                impossible.append((k1, k2))
            else:
                possible.append((k1, k2))
        return possible, impossible

def input_coords():
    coords = []
    print("Enter occurrences as x,y,z,t (comma-separated). Type 'done' when finished.")
    while True:
        line = input("Occurrence: ").strip()
        if line.lower() == 'done':
            break
        try:
            x, y, z, t = map(float, line.split(','))
            coords.append((x, y, z, t))
        except:
            print("Invalid input. Please enter as x,y,z,t or 'done'.")
    return coords

if __name__ == "__main__":
    print("Spatiotemporal Mutual Exclusivity Simulator")
    alpha = float(input("Set alpha (temporal weight, default 1.0): ") or 1.0)
    delta = float(input("Set delta (distance threshold, default 5.0): ") or 5.0)
    sim = SemanticSpatiotemporalSimulator(alpha=alpha, delta=delta)

    while True:
        kw = input("Enter keyword (or 'done' to finish): ").strip()
        if kw.lower() == 'done':
            break
        occurrences = input_coords()
        sim.add_keyword_occurrences(kw, occurrences)
        print(f"Added {len(occurrences)} occurrences for '{kw}'.\n")

    print("\nAnalyzing keyword pair possibilities...\n")
    possible_pairs, impossible_pairs = sim.infer_all_possibilities()

    print("Possible keyword pairs (all distances less than delta):")
    if possible_pairs:
        for k1, k2 in possible_pairs:
            print(f" - {k1} & {k2}")
    else:
        print(" None")

    print("\nImpossible keyword pairs (any distance greater than or equal to delta):")
    if impossible_pairs:
        for k1, k2 in impossible_pairs:
            print(f" - {k1} <--> {k2}")
    else:
        print(" None")
