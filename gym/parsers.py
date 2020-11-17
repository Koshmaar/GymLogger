from typing import Any

from gym.definitions import Training, Exercise, Set
from gym.utils import get_exercise_def_by_name


class TrainingParser:

    def __init__(self, exercise_definitions):
        self.exercise_definitions = exercise_definitions

    def parse_training(self, tr: dict) -> Training:
        """
        Parses training section (from yaml)
        """
        training = Training(
            date=tr.get('date') or "",
            comment=tr.get('comment') or "",
            exercises=[self.parse_exercise(e) for e in tr.get('exercises')],
        )
        return training

    def parse_exercise(self, e: Any):
        exercise_name = ""
        sets = None

        if isinstance(e, str):
            exercise_name = str(e)
            print("  - " + exercise_name)

        elif isinstance(e, dict):
            for e_name, e_sets in e.items():
                exercise_name = e_name
                sets = e_sets
        else:
            # for now alarm about it but don't stop parsing
            # we need to be lenient about possible values here
            print("error unknown type")
            print(type(e))
            return None

        exercise_def = get_exercise_def_by_name(self.exercise_definitions, exercise_name)
        if exercise_def is None:
            return None

        exercise = Exercise(exercise_def)
        if sets is not None:
            for s in sets:
                one_set = self.parse_set_object(s)
                exercise.sets.append(one_set)
        return exercise

    def parse_set_object(self, s) -> Set:
        weight = -1
        reps = -1
        comment = ""

        if isinstance(s, int):
            weight = s
        elif s.find("/") != -1:
            parts = s.split("/")
            weight = int(parts[0])
            reps = int(parts[1])
        elif isinstance(s, str):
            comment = s
        return Set(weight, reps, comment)

