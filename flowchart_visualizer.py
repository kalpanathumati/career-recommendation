def generate_flowchart(current_stage, selected_path, careers_dict):
    """
    Generates a Graphviz DOT graph string visualizing career paths.

    Args:
        current_stage (str): e.g., '10th'
        selected_path (str): e.g., 'Intermediate_BiPC'
        careers_dict (dict): career options with metadata

    Returns:
        str: Graphviz DOT format string
    """
    dot = "digraph CareerPath {\n"
    dot += "  rankdir=LR;\n"
    dot += '  node [shape=box, style="filled", fillcolor="#AED6F1"];\n'

    # Current stage node
    dot += f'  "{current_stage}" [shape=oval, fillcolor="#85C1E9"];\n'

    # Selected education path node
    display_path = selected_path.replace('_', ' ')
    dot += f'  "{display_path}" [shape=box, fillcolor="#D6EAF8"];\n'

    # Edge from current stage to selected path
    dot += f'  "{current_stage}" -> "{display_path}";\n'

    # Add career nodes and edges
    for career in careers_dict.keys():
        dot += f'  "{career}" [shape=box, fillcolor="#ABEBC6"];\n'
        dot += f'  "{display_path}" -> "{career}";\n'

    dot += "}"
    return dot
