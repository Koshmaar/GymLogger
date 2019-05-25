import definitions
import utils
from loader import *

# --------


def find_max_for(exercise_name):
    print("\n>>>> {} max: ". format(exercise_name))
    squats = utils.get_exercise_def_by_name(exercise_definitions, exercise_name)

    squat_max = utils.find_max_for_exercise(trainings_list, squats)
    if squat_max is not None:
        max_weight, max_reps, max_exercise, max_training = squat_max
        print("Max for {} is {}, it was done with {} reps ".format(str(squats), max_weight, max_reps))
        print(" Done on training at {}".format(max_training.date) )
        print(" Whole exercise looked like that: {}".format(max_exercise.get_set_list_as_str()))

# ----------------------------


if __name__ == "__main__":
    exercise_definitions = load_exercise_definitions("treningi.yaml")
    # debug
    for d in exercise_definitions:
        print("- " + d.name_pl )
        for alter in d.alternative_names:
            print("   " + alter)

    print("\n********\n")

    trainings_list = load_trainings_file("treningi.yaml", exercise_definitions)

    print("\n>>>> Trainings: ")
    for t in trainings_list:
        t.print()

    find_max_for("Przysiady")

