
class State:
    def __init__(self, name, output):
        self.name = name
        self.output = output
        self.switches = {}

    def add_switch(self, symbol, wanted_state):
        self.switches[symbol] = wanted_state

    def next_state(self, symbol):
        return self.switches.get(symbol, None)


class Moore:
    def __init__(self, initial_state):
        self.state = initial_state

    def process_symbol(self, symbol):
        next_state = self.state.next_state(symbol)
        if next_state:
            self.state = next_state
        else:
            print(f"There is no way for symbol: {symbol}")

    def get_output(self):
        return self.state.output


state1 = State("S1", "a")
state2 = State("S2", "b")
state3 = State("S3", "c")

state1.add_switch(0, state2)
state1.add_switch(1, state3)

state2.add_switch(0, state1)
state2.add_switch(1, state3)

state3.add_switch(0, state1)
state3.add_switch(1, state2)

state_machine = Moore(state2)

symbol_list = [1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]

print(f"initial state: {state_machine.state.name}")

for symbol in symbol_list:
    print(f"symbol: {symbol}")
    state_machine.process_symbol(symbol)
    print(f"new state: {state_machine.state.name}")
    print(f"output: {state_machine.get_output()}")
