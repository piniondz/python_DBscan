from point import Point


class DBscan:
    def __init__(self, dataset, min_points, epsilon):
        self.neighbors: list[Point] = []
        self.database: list[Point] = []
        self.dataset = dataset
        self.min_points: int = min_points
        self.epsilon: float = epsilon
        self.cluster_counter: int = 0
        self.point_conversion()

    def label_change(self, dataset: list[Point]):
        for point in dataset:
            if point.label == -1:
                point.set_label(self.cluster_counter)
            if point.label is None:
                point.set_label(self.cluster_counter)
                self.range_query(point)
                if self.density_check():
                    dataset.extend(self.neighbors)

    def density_check(self):
        if len(self.neighbors)+1 < self.min_points:
            return False
        else:
            return True

    def range_query(self, point1):
        self.neighbors.clear()
        for point2 in self.database:
            if point1.distance(point2) <= self.epsilon:
                self.neighbors.append(point2)
        self.neighbors.remove(point1)

    def dbscan(self):
        for point in self.database:
            if point.label is None:
                self.range_query(point)
                if self.density_check():
                    point.set_label(self.cluster_counter)
                    dataset = self.neighbors.copy()
                    self.label_change(dataset)
                    self.cluster_counter += 1
                else:
                    point.set_label(-1)
        return self.werid_dataset_assembly()

    def point_conversion(self):
        for coordx, coordy in self.dataset:
            self.database.append(Point(coordx, coordy))

    def werid_dataset_assembly(self):
        dataset = []
        points = []
        labels = []
        for point in self.database:
            points.append([point.x, point.y])
            labels.append(point.label)
        dataset.append(points)
        dataset.append(labels)
        return dataset
