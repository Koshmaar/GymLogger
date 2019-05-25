
def find_max_for_exercise(trainings, exercise_def):
    curr_max_weight = -1
    curr_max_reps = -1
    curr_max_exercise = None
    curr_max_training = None
    for t in trainings:
        result = t.get_max_for_exercise(exercise_def)
        if result is None:
            continue
        (exercise, results) = result
        if curr_max_weight < results[0]:
            curr_max_weight = results[0]
            curr_max_reps = results[1]
            # print("new max:" + str(curr_max_weight) )
            curr_max_training = t
            curr_max_exercise = exercise

    return curr_max_weight, curr_max_reps, curr_max_exercise, curr_max_training

# --------

def get_exercise_def_by_name(exercise_definitions, exercise_name):
    exercise_name = exercise_name.lower()
    # print("Matching by " + exercise_name )
    for d in exercise_definitions:
        # print("- " + d.name )
        for alter in d.alternative_names:
            if alter.lower() == exercise_name:
                print("Matched {} to {}".format(exercise_name, d.name_pl))
                return d

    print("Didn't match {}".format(exercise_name))
    return None
