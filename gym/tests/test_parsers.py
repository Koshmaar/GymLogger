from gym.loader import load_exercise_definitions, load_trainings_file


def test_load_exercise_definitions():
    exercise_definitions, err = load_exercise_definitions("simple_trainings.yaml")
    assert err is False

    ed = exercise_definitions[0]
    assert ed.name_pl == "Przysiady"
    assert ed.name_eng == "Squats"
    assert all(elem in ed.alternative_names for elem in ["przysiady", "przysiad", "przysiady waskie"])

    ed = exercise_definitions[1]
    assert ed.name_pl == "Żuraw"
    assert ed.name_eng == "Cranes"
    assert all(elem in ed.alternative_names for elem in ["zurawie", "żurawie", "żuraw", "zuraw"])


def test_load_training():
    exercise_definitions, err = load_exercise_definitions("simple_trainings.yaml")
    assert err is False

    trainings_list, err = load_trainings_file("simple_trainings.yaml", exercise_definitions)
    assert err is False

    tr = trainings_list[0]
    assert tr.date == '12.9.2018'
    # need to find better way to test it
    assert tr.exercises[0].sets[0].repetitions == 10
    assert tr.exercises[0].sets[0].weight == 40
