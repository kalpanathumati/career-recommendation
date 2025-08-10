def generate_flowchart(current_stage, selected_path, careers_dict):
    """
    Generates a Graphviz flowchart of the career path.

    Args:
        current_stage (str): e.g., '10th'
        selected_path (str): e.g., 'Intermediate_BiPC'
        careers_dict (dict): Dictionary of career options from career_db.json

    Returns:
        str: Graphviz DOT code for visualization
    """
    dot = "digraph CareerPath {\n"
    dot += "  rankdir=LR;\n"
    dot += '  node [shape=box, style="filled", fillcolor="#AED6F1"];\n'

    # Start node (Current stage)
    dot += f'  "{current_stage}" [shape=oval, fillcolor="#85C1E9"];\n'

    # Education path node
    path_label = selected_path.replace('_', ' ')
    dot += f'  "{path_label}" [shape=box, fillcolor="#D6EAF8"];\n'
    dot += f'  "{current_stage}" -> "{path_label}";\n'

    # Careers
    for career in careers_dict.keys():
        dot += f'  "{career}" [shape=box, fillcolor="#ABEBC6"];\n'
        dot += f'  "{path_label}" -> "{career}";\n'

    dot += "}"
    return dot
