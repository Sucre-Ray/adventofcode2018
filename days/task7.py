from AOCDay import AOCDay


class Day7(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 7
        self.input_data = self.load_input(self.day)

    @staticmethod
    def extract_edges(data):
        edges = [
            (line.split()[1],
             line.split()[7],
             Day7.eval_price(line.split()[7]))
            for line in data]
        return edges

    @staticmethod
    def is_available_vertex(edges, done_steps, vertex):
        prerequisites = [edge[0] for edge in edges if edge[1] == vertex]
        return all(i in done_steps for i in prerequisites)

    @staticmethod
    def add_starting_edges(edges):
        available_sp = {edge[0] for edge in edges} - {edge[1] for edge in edges}
        return {(None, i, Day7.eval_price(i)) for i in available_sp}

    @staticmethod
    def choose_vertex_by_cost(pending_edges):
        return min(pending_edges, key=lambda x: x[2])

    def get_available_edges(self, edges, done_steps):
        return {edge
                for edge in edges
                if self.is_available_vertex(edges, done_steps, edge[1]) and edge[1] not in done_steps}

    def update_available_edges(self, edges, done_steps, edges_in_work):
        steps_in_work = [i[1] for i in edges_in_work]
        return {edge
                for edge in edges
                if self.is_available_vertex(edges, done_steps, edge[1])
                and (edge[1] not in done_steps)
                and (edge[1] not in steps_in_work)}

    @staticmethod
    def remove_redundant_edges(pending_edges, edge):
        return set(filter(lambda x: x[1] != edge[1], pending_edges))

    @staticmethod
    def eval_price(vertex):
        # vertices from A=1 to Z=26
        OFFSET = 64
        return ord(vertex) - OFFSET

    @staticmethod
    def do_work(workers):
        return {key: value - 1 for key, value in workers.items()}

    @staticmethod
    def get_finished(workers):
        return [key for key, value in workers.items() if value == 0]

    def main1(self):
        edges = self.extract_edges(self.input_data)
        pending_edges = self.add_starting_edges(edges)
        done_steps = []
        while pending_edges:
            next_step = self.choose_vertex_by_cost(pending_edges)
            done_steps.append(next_step[1])
            pending_edges = self.remove_redundant_edges(pending_edges, next_step)
            pending_edges.update(self.get_available_edges(edges, done_steps))
        return ''.join(done_steps)

    def main2(self):
        time = 0
        max_workers = 5
        time_offset = 60
        workers = dict()
        edges = self.extract_edges(self.input_data)
        pending_edges = self.add_starting_edges(edges)
        done_steps = []
        while pending_edges or workers:
            # some work need to be done or pending
            while len(workers) < max_workers and (pending_edges - workers.keys()):
                # add more workers
                next_step = self.choose_vertex_by_cost(pending_edges)
                pending_edges = self.remove_redundant_edges(pending_edges, next_step)
                workers[next_step] = next_step[2] + time_offset
            while not self.get_finished(workers):
                # do exact work
                workers = self.do_work(workers)
                time += 1
            for edge in self.get_finished(workers):
                # remove workers, add done steps, add new available points
                done_steps.append(edge[1])
                del workers[edge]
                pending_edges.update(self.update_available_edges(edges, done_steps, workers.keys()))
        return time