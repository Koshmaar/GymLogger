from typing import List, Tuple
import yaml
from gym.definitions import ExerciseDefinition, Training
from gym.parsers import TrainingParser


def load_yaml(filename: str):
    with open(filename, 'r', encoding='utf8') as file:
        try:
            parsed = yaml.load(file, Loader=yaml.FullLoader)
            return parsed, False
        except yaml.YAMLError as exc:
            print(exc)
            return None, True


def load_exercise_definitions(filename: str) -> Tuple[List[ExerciseDefinition], bool]:
    parsed, err = load_yaml(filename)
    if err:
        return [], True

    definitions_sections = parsed['Exercises definitions']
    ret_defs = []

    for d in definitions_sections:
        for name,alternative_names in d.items():
            name_pl = ""
            name_eng = ""
            if name.find("/") != -1:
                names = name.split("/")
                name_eng = names[0]
                name_pl = names[1]
            else:
                name_pl = name
            ed = ExerciseDefinition(name_pl, name_eng, alternative_names)
            ret_defs.append(ed)
    return ret_defs, False


def load_trainings_file(
        filename: str,
        exercise_definitions: List[ExerciseDefinition]) -> Tuple[List[Training], bool]:
    parsed, err = load_yaml(filename)
    if err:
        return [], True

    _trainings_list = []
    trainings_sections = parsed['Trainings']
    parser = TrainingParser(exercise_definitions)

    for ts in trainings_sections:
        training = parser.parse_training(ts)
        _trainings_list.append(training)

    return _trainings_list, False

