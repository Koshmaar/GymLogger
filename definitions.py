
class ExerciseDefinition:
    def __init__(self, name_pl, name_eng, alternative_names):
        self.name_pl = name_pl
        self.name_eng = name_eng
        self.alternative_names = alternative_names
        pass

    def is_equal_by_def(self, exercise_definition):
        return self.name_pl == exercise_definition.name_pl

    def __str__(self):
        return self.name_pl

# --------

AVERAGE_REPETITION_COUNT=6

class Set:
    def __init__(self, weight, reps, comment):
        self.weight = weight
        self.repetitions = reps
        self.comment = comment
        print("  new set: " + str(self) )

    def estimate_total_work(self):
        if len(self.comment) > 0:
            return 0
        if self.repetitions < 0:
            return self.weight * AVERAGE_REPETITION_COUNT
        else:
            return self.weight * self.repetitions

    def get_max_weight(self):
        if len(self.comment) > 0:
            return 0
        return self.weight

    def get_reps_for_max(self):
        if len(self.comment) > 0:
            return 0
        if self.repetitions < 0:
            return 1
        else:
            return self.repetitions

    def __str__(self):
        if len(self.comment) > 0:
            return self.comment
        if self.repetitions < 0:
            return str(self.weight)
        else:
            return "{}/{}".format(self.weight, self.repetitions)

# --------

class Exercise:
    def __init__(self, exercise_definition):
        self.exercise_definition = exercise_definition
        if self.exercise_definition is None:
            print("!!!!!!!!! Warn, NONE")
        self.sets = [] # contains Set
        pass

    def __str__(self):
        ret = "* Exercise: " + str(self.exercise_definition) + "\n"
        for s in self.sets:
            ret += str(s) + "\n"
        return ret

    def get_set_list_as_str(self):
        return "[" + ", ".join(str(s) for s in self.sets) + "]"

    def estimate_total_work(self):
        ret = 0
        for s in self.sets:
            ret += s.estimate_total_work()
        return ret

    def is_equal_by_def(self, exercise_definition):
        if self.exercise_definition is not None:
            return self.exercise_definition.is_equal_by_def(exercise_definition)
        else:
            return False

    def get_max_weight(self):
        max_weight = 0
        max_reps = 0
        for s in self.sets:
            new_weight = s.get_max_weight()
            if new_weight > max_weight:
                max_weight = new_weight
                max_reps = s.get_reps_for_max()
        return (max_weight, max_reps)


# ----------------------------

class Training:
    def __init__(self, date, comment):
        self.date = date
        self.comment = comment
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def print(self):
        print("[gym training]")
        print("  date: " + self.date)
        print("  comment: " + self.comment)
        for e in self.exercises:
            print("  " + str(e))

    def get_max_for_exercise(self, exercise_definition):
        for e in self.exercises:
            if e.is_equal_by_def(exercise_definition):
                weight_reps = e.get_max_weight()
                return (e, weight_reps)
        return None


