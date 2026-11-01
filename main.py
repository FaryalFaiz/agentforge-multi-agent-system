from agents.profile_agent import analyze_profile

profile = {
    "opportunity_types": ["internship", "research"],
    "countries": ["Ireland", "Germany", "Qatar", "India"],
    "cities": ["Delhi"],
    "remote": True,
    "onsite": True
}

result = analyze_profile(profile)

print(result)
