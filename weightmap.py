import json


class WeightMap:
    def __init__(self, width, height):
        self.weights = []
        self.width = width
        self.height = height
        self.generations = 0
        for _ in range(width):
            self.weights.append([0] * height)

    def get_weight(self, x, y):
        return self.weights[x][y] / self.generations

    def train(self, other_map):
        for x in range(self.width):
            for y in range(self.height):
                self.weights[x][y] += other_map.get_weight(x, y)
        self.generations += 1

    def get_confidence(self, other_map):
        confidence = 0
        for x in range(self.width):
            for y in range(self.height):
                confidence += self.get_weight(x, y) * \
                    other_map.get_weight(x, y)

        return confidence

    def to_json(self):
        out_dict = {
            'width': self.width,
            'height': self.height,
            'generations': self.generations,
            'weights': self.weights
        }
        return json.dumps(out_dict, indent=4)

    @classmethod
    def from_pg_surface(self, surface):
        out = self(surface.get_width(), surface.get_height())
        out.generations = 1
        for x in range(out.width):
            for y in range(out.height):
                color = surface.get_at((x, y))
                weight = (color[0] + color[1] + color[2]) / 3.0
                out.weights[x][y] = (weight / 255.0) * 2.0 - 1.0

        return out

    @classmethod
    def from_json(self, in_json):
        in_dict = json.loads(in_json)
        out = self(in_dict['width'], in_dict['height'])
        out.generations = in_dict['generations']
        out.weights = in_dict['weights']
        return out
