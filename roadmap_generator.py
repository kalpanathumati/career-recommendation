def generate_roadmap_text(current_stage, selected_path, selected_career, career_info):
    """
    Generates a textual career roadmap summary.

    Args:
        current_stage (str): User's current academic level (e.g., '10th').
        selected_path (str): Selected educational path (e.g., 'Intermediate_BiPC').
        selected_career (str): Selected career option (e.g., 'MBBS').
        career_info (dict): Career details including skills, entrance exams, salary, growth, resources.

    Returns:
        str: A formatted roadmap summary.
    """

    roadmap = f"📌 Career Roadmap:\n\n"
    roadmap += f"1️⃣ Current Academic Stage: {current_stage}\n"
    roadmap += f"2️⃣ Selected Education Path: {selected_path.replace('_', ' ')}\n"
    roadmap += f"3️⃣ Career Option: {selected_career}\n\n"

    roadmap += "🔍 Career Details:\n"
    roadmap += f"- Required Skills: {', '.join(career_info.get('skills', []))}\n"
    roadmap += f"- Entrance Exams: {', '.join(career_info.get('entrance', []))}\n"
    roadmap += f"- Expected Salary Range: {career_info.get('salary_range', 'N/A')}\n"
    roadmap += f"- Job Growth Outlook: {career_info.get('growth', 'N/A')}\n"
    roadmap += f"- Learning Resources:\n"

    for link in career_info.get('resources', []):
        roadmap += f"  • {link}\n"

    roadmap += "\nBest of luck with your career journey! 🚀"

    return roadmap
