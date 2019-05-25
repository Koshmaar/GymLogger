import yaml
import definitions
import utils

def load_yaml(filename):
    with open(filename, 'r', encoding='utf8') as file:
        try:
            parsed = yaml.load(file, Loader=yaml.FullLoader)
            return parsed,False
        except yaml.YAMLError as exc:
            print(exc)
            return None,True

# --------

def load_exercise_definitions(filename):

    parsed,err = load_yaml(filename)
    if err != False:
        return

    definitions_sections = parsed['Exercises definitions']
    ret_defs = []

    for d in definitions_sections:
        # print(d)
        for name,alternative_names in d.items():
            # print(name)
            # print(alternative_names)
            # print()
            name_pl = ""
            name_eng = ""
            if name.find("/") != -1:
                names = name.split("/")
                name_eng = names[0]
                name_pl = names[1]
            else:
                name_pl = name
            ret_defs.append(definitions.ExerciseDefinition(name_pl, name_eng, alternative_names))
    return ret_defs

# --------

def load_trainings_file(filename, exercise_definitions):
    parsed, err = load_yaml(filename)
    if err != False:
        return

    _trainings_list = []
    trainings_sections = parsed['Trainings']

    for t in trainings_sections:
        print("--------")
        training = parse_training(t, exercise_definitions)
        _trainings_list.append(training)

    return _trainings_list

# --------

def parse_training(t, exercise_definitions):
    comm = ""
    if t.get('comment') is not None:
        comm = t['comment']

    training = definitions.Training(t['date'], comm)

    for e in t.get('exercises'):
        exercise = parse_exercise(e, exercise_definitions)
        training.add_exercise(exercise)

    return training

# --------

def parse_exercise(e, exercise_definitions):
    exercise_name = ""
    sets = None

    if type(e) == type(""):
        exercise_name = str(e)
        print("  - " + exercise_name)

    elif type(e) == type({}):
        for e_name, e_sets in e.items():
            exercise_name = e_name
            print("  - " + e_name)
            for rep in e_sets:
                print("   " + str(rep))
            sets = e_sets
        # print("   dict")
    else:
        print("error unknown type")
        print(type(e))

    exercise_def = utils.get_exercise_def_by_name(exercise_definitions, exercise_name)

    exercise = definitions.Exercise(exercise_def)
    if sets is not None:
        for s in sets:
            # print("  * " + str(s))
            one_set = parse_Set_object(s)
            exercise.sets.append(one_set)

    return exercise


# --------

def parse_Set_object(s):
    weight = -1
    reps = -1
    comment = ""

    if type(s) == type(1):
        weight = s
    elif s.find("/") != -1:
        parts = s.split("/")
        weight = int(parts[0])
        reps = int(parts[1])
    elif type(s) == type(""):
        comment = s
    return definitions.Set(weight, reps, comment)

