from automathon import DFA
from graphviz import Digraph, Source
from IPython.display import display

# Define states and input symbols (from the recommendation system)
#states = {"A", "AV", "C", "D", "F", "FC", "H", "M", "R", "S", "T", "DO", "AN", "MI", "HI", "G", "CR", "B", "E", "W"}
#input_symbols = {"a", "av", "c", "d", "f", "fc", "h", "m", "r", "s", "t", "do", "an", "mi", "hi", "g", "cr", "b", "e", "w"}

states = {"A", "AV", "C", "D"}
input_symbols = {"a", "av", "c", "d"}

# Initialize genre affinity scores
genre_affinity = {genre: 1 for genre in states}

# Define the complex transition function
def transition_function(current_state, input_symbol, history):
    genre_affinity[input_symbol.upper()] += 1
    next_state = max(genre_affinity, key=genre_affinity.get)
    return next_state

# Initialize DFA parameters
initial_state = "A"
accept_states = states  # All states are accepting

# Create the DFA object
dfa = DFA(states, input_symbols, transition_function, initial_state, accept_states)

# Visualize the DFA
dot = Digraph()

# Add nodes to the graph
for state in states:
    dot.node(state)  # No need to differentiate final states as all are accepting

# Add edges to the graph
for state in states:
    for symbol in input_symbols:
        next_state = transition_function(state, symbol, [])  # Empty history for visualization
        dot.edge(state, next_state, label=symbol)

# Display the graph directly in the notebook
display(Source(dot.source))

# Generate PNG image
dot.format = 'png'  # Set the output format to PNG
dot.render('dfa_visualization', view=False)  # Render and save the image

print("PNG image generated as 'dfa_visualization.png'")
