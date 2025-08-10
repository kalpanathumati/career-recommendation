def generate_roadmap_text(current_stage, selected_path, selected_career, career_info):
    """
    Generates a textual career roadmap summary.

    Args:
        current_stage (str): e.g., '10th'
        selected_path (str): e.g., 'Intermediate_BiPC'
        selected_career (str): e.g., 'MBBS'
        career_info (dict): Data from career_db.json for that career

    Returns:
        str: A formatted career roadmap
    """
    roadmap = f"📌 Career Roadmap:\n\n"
    roadmap += f"1️⃣ Current Academic Stage: {current_stage}\n"
    roadmap += f"2️⃣ Selected Education Path: {selected_path.replace('_', ' ')}\n"
    roadmap += f"3️⃣ Target Career: {selected_career}\n\n"

    roadmap += "🔍 Career Details:\n"
    roadmap += f"- Required Skills: {', '.join(career_info.get('skills', []))}\n"
    roadmap += f"- Entrance Exams: {', '.join(career_info.get('entrance', []))}\n"
    roadmap += f"- Salary Range: {career_info.get('salary_range', 'N/A')}\n"
    roadmap += f"- Job Outlook: {career_info.get('growth', 'N/A')}\n"

    resources = career_info.get("resources", [])
    if resources:
        roadmap += "- Learning Resources:\n"
        for url in resources:
            roadmap += f"  • {url}\n"

    roadmap += "\n✨ Good luck on your career path!"
    return roadmap
