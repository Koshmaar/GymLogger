from gym import load_exercise_definitions, get_exercise_def_by_name,\
    find_max_for_exercise, load_trainings_file


def find_max_for(exercise_name):
    print(f"\n>>>> {exercise_name} max: ")
    squats = get_exercise_def_by_name(exercise_definitions, exercise_name)

    squat_max = find_max_for_exercise(trainings_list, squats)
    if squat_max is not None:
        max_weight, max_reps, max_exercise, max_training = squat_max
        print(f"Max for {squats} is {max_weight}, it was done with {max_reps} reps ")
        print(f" Done on training at {max_training.date}")
        print(f" Whole exercise looked like that: {max_exercise.str_set_list()}")


if __name__ == "__main__":
    exercise_definitions, err = load_exercise_definitions("exercises.yaml")
    if err:
        print("Error loading 'exercises.yaml'")
        exit(1)

    for d in exercise_definitions:
        print("- " + d.name_pl )
        for alter in d.alternative_names:
            print("   " + alter)

    print("\n********\n")

    trainings_list, err = load_trainings_file("training.yaml", exercise_definitions)
    if err:
        print("Error loading 'training.yaml'")
        exit(1)

    print("\n>>>> Trainings: ")
    for t in trainings_list:
        t.print()

    find_max_for("Przysiady")

