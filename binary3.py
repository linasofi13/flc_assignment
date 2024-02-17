from automata.fa.dfa import DFA

# DFA which matches all binary strings that are a multiple of three in binary
my_dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q1', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q0'}
)

try:
    while True:
        string = input("Enter your string:")
        if my_dfa.accepts_input(string):
            print(f"The DFA accepts the string '{string}'")
        elif string == "e":
            print(f"The DFA accepts the string '{string}'")
        else:
            print(f"The DFA rejects the string '{string}'")

except KeyboardInterrupt:
    print('')
