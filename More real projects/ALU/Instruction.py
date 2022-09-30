class Instruction:
    def __init__(self, instruction, description):
        self.instruction = instruction
        self.description = description

    def __repr__(self):
        return self.description

    def __getitem__(self, x):

        x = map(int, filter(lambda _: _.isdigit(), str(x)))

        return self.instruction(*x)