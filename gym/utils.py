from typing import List, Optional, Tuple
from gym.definitions import ExerciseDefinition, Training, Exercise


def find_max_for_exercise(
        trainings: List[Training],
        ed: ExerciseDefinition) -> Tuple[int, int, Optional[Exercise], Optional[Training]]:

    curr_max_weight = -1
    curr_max_reps = -1
    curr_max_exercise = None
    curr_max_training = None

    for t in trainings:
        exercise, max_weight, max_reps = t.get_max_for_exercise(ed)
        if max_weight > curr_max_weight:
            curr_max_weight = max_weight
            curr_max_reps = max_reps
            curr_max_training = t
            curr_max_exercise = exercise

    return curr_max_weight, curr_max_reps, curr_max_exercise, curr_max_training


def get_exercise_def_by_name(
        exercises: List[ExerciseDefinition],
        exercise_name: str) -> Optional[ExerciseDefinition]:

    exercise_name = exercise_name.lower()

    for d in exercises:
        if d.compare_by_alternatives(exercise_name):
            return d

    return None
