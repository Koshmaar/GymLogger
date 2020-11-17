from typing import List, Tuple, Optional

# todo put to conf file
AVERAGE_REPETITION_COUNT=6


class ExerciseDefinition:
    """
    Stores one exercise definition, ie.
        name_pl: Martwy ciąg
        name_eng: Deadlift
        alternative_names: MC, martwy, deadlift
    """
    def __init__(self, name_pl: str, name_eng: str, alternative_names: list):
        self.name_pl = name_pl
        self.name_eng = name_eng
        self.alternative_names = alternative_names

    # todo I don't like this func
    def compare_by_name(self, exercise_definition):
        return self.name_pl == exercise_definition.name_pl

    def compare_by_alternatives(self, name: str) -> bool:
        for alter in self.alternative_names:
            if alter.lower() == name:
                return True
        return False

    def __str__(self):
        return self.name_pl


# todo change name to SingleSet
class Set:
    """
    Stores exercise Set, ie.
        weight: 40
        repetitions: 10
        comment: almost fainted
    If comments is not empty, then weight and repetitions aren't stored.
    If repetitions equals -1, there was only one set.
    """
    def __init__(self, weight: int, reps: int, comment: str):
        self.weight = weight
        self.repetitions = reps
        self.comment = comment

    def estimate_total_work(self) -> int:
        if self.is_comment_only():
            return 0
        if self.repetitions < 0:
            return self.weight * AVERAGE_REPETITION_COUNT
        else:
            return self.weight * self.repetitions

    def get_max_weight(self) -> int:
        if self.is_comment_only():
            return 0
        return self.weight

    def get_reps_for_max(self) -> int:
        """
        Returns amount of repetitions that would be used for exercise with max load
        """
        if self.is_comment_only():
            return 0
        if self.repetitions < 0:
            return 1
        else:
            return self.repetitions

    def __str__(self):
        if self.is_comment_only():
            return self.comment
        if self.repetitions < 0:
            return str(self.weight)
        else:
            return "{}/{}".format(self.weight, self.repetitions)

    def is_comment_only(self) -> bool:
        return len(self.comment) > 0


class Exercise:
    """
    Stores list of exercise Sets
    """
    def __init__(self, definition: ExerciseDefinition):
        self.definition = definition
        self.sets: List[Set] = []

    def estimate_total_work(self) -> int:
        ret = 0
        for s in self.sets:
            ret += s.estimate_total_work()
        return ret

    def compare_by_name(self, ext_definition: ExerciseDefinition) -> bool:
        return self.definition.compare_by_name(ext_definition)

    def get_max_weight_reps(self) -> Tuple[int, int]:
        max_weight = 0
        max_reps = 0
        for s in self.sets:
            new_weight = s.get_max_weight()
            if new_weight > max_weight:
                max_weight = new_weight
                max_reps = s.get_reps_for_max()
        return max_weight, max_reps

    def str_set_list(self) -> str:
        return "[" + ", ".join(str(s) for s in self.sets) + "]"

    def __str__(self):
        ret = "* Exercise: " + str(self.definition) + "\n"
        for s in self.sets:
            ret += str(s) + "\n"
        return ret


class Training:
    """
    Stores training data. Date and comment can be None.
    Exercises is list of Exercise
    """
    def __init__(self, date: str, comment: str, exercises: List[Exercise]):
        self.date = date
        self.comment = comment
        self.exercises = exercises

    def get_max_for_exercise(self, ed: ExerciseDefinition) -> Tuple[Optional[Exercise], int, int]:
        """
        Searches all stored exercises that match ed,
        for their max. Returns it.
        Assumes there's only one exercise type in list.
        """
        for e in self.exercises:
            if e.compare_by_name(ed):
                max_weight, max_reps = e.get_max_weight_reps()
                return e, max_weight, max_reps
        return None, 0, 0

    def print(self):
        print("[gym training]")
        print("  date: " + self.date)
        print("  comment: " + self.comment)
        for e in self.exercises:
            print("  " + str(e))


