from Instruction import Instruction

class ALU:
    def __init__(self):
        self.Instruction0  = Instruction(lambda a, b: a + b  , 'ADD')
        self.Instruction1  = Instruction(lambda a, b: a - b  , 'SUB')
        self.Instruction2  = Instruction(lambda a, b: a ** b , 'POW')
        self.Instruction3  = Instruction(lambda a, b: a / b  , 'DIV')
        self.Instruction4  = Instruction(lambda a, b: a * b  , 'MUL')
        self.Instruction5  = Instruction(lambda a, b: a and b, 'AND')
        self.Instruction6  = Instruction(lambda a, b: a or b , 'OR' )
        self.Instruction7  = Instruction(lambda a, b: a ^ b  , 'XOR')
        self.Instruction8  = Instruction(lambda a:    not a  , 'NOT')
        self.Instruction9  = Instruction(lambda a, b: a % b  , 'MOD') 
        self.Instruction10 = Instruction(lambda a, b: a << b , 'SHL')
        self.Instruction11 = Instruction(lambda a, b: a >> b , 'SHR')
        self.Instruction12 = Instruction(lambda a:   -a      , 'NEG')
        self.Instruction13 = Instruction(lambda a, b: a > b  , 'CGT')
        self.Instruction14 = Instruction(lambda a, b: a < b  , 'CLT')
        self.Instruction15 = Instruction(lambda a, b: a == b , 'CEQ')

    def __getitem__(self, x): # Using [] as a way to pass in operands
        x = filter(lambda _: _.isdigit(), str(x))
        instructions = []
        for i in x:
            instructions += [eval(f"self.Instruction{i}")]
        return instructions


alu = ALU()

print(alu[1][0].description + '[3, 2] =', alu[1][0][3, 2])

for instruction in alu[0, 3, 2]:
    print(instruction.description + '[4, 4] =', instruction[4, 4])