def generate_roadmap_text(
    current_stage: str,
    selected_path: str,
    selected_career: str,
    career_info: dict
) -> str:
    roadmap = f"Career Roadmap:\n1. Stage: {current_stage}\n"
    roadmap += f"2. Path: {selected_path.replace('_', ' ')}\n"
    roadmap += f"3. Career: {selected_career}\n\nDetails:\n"
    roadmap += f"- Skills: {', '.join(career_info.get('skills', []))}\n"
    roadmap += f"- Entrance Exams: {', '.join(career_info.get('entrance', []))}\n"
    roadmap += f"- Salary: {career_info.get('salary_range', 'N/A')}\n"
    roadmap += f"- Growth: {career_info.get('growth', 'N/A')}\n"
    if career_info.get('resources'):
        roadmap += "- Resources:\n"
        for r in career_info['resources']:
            roadmap += f"    • {r}\n"
    return roadmap
