# version of stable internships modified by ChatGPT 4.5 to be easier for a human
# to remember
def stable_matching(intern_prefs, team_prefs):
    free_interns = list(range(len(intern_prefs)))
    intern_next_choice = [0] * len(intern_prefs)
    teams_current = {}

    # Create rankings for teams
    team_rankings = [
        {intern: rank for rank, intern in enumerate(team)}
        for team in team_prefs
    ]

    while free_interns:
        intern = free_interns.pop()
        intern_choice = intern_prefs[intern][intern_next_choice[intern]]
        intern_next_choice[intern] += 1

        if intern_choice not in teams_current:
            teams_current[intern_choice] = intern
        else:
            current_intern = teams_current[intern_choice]
            # Check if the new intern is preferred over the current one
            if team_rankings[intern_choice][intern] < team_rankings[intern_choice][current_intern]:
                teams_current[intern_choice] = intern
                free_interns.append(current_intern)
            else:
                free_interns.append(intern)

    return [(intern, team) for team, intern in teams_current.items()]
