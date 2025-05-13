def is_valid_exercise_set_object(exercise_set_object):
    '''Given an exercise set object, return True if it is valid, False otherwise.'''
    if not exercise_set_object: 
        return False
    for field in ['exercise_id', 'sets', 'reps', 'weight']:
        if not exercise_set_object.get(field):
            print(field, "failure")
            return False
    return True

def is_valid_workout_object(workout_object):
    '''Given a workout object, return True if it is valid, False otherwise.'''
    if not workout_object: 
        return False
    exercise_sets = workout_object.get('exercise_sets')
    if not exercise_sets: 
        return False
    for exercise_set in exercise_sets:
        if not is_valid_exercise_set_object(exercise_set):
            return False
    return True


workout_object = {
    "workout_id": 14,
    "execution_date": "2025-04-28",
    "created_at": "2025-05-08",
    "exercise_sets": [
        {
            "exercise_id": 5,
            "sets": 1,
            "reps": 12,
            "weight": 123.0,
            "is_done": False
        },
        {
            "exercise_id": 8,
            "sets": 1,
            "reps": 12,
            "weight": 393.0,
            "is_done": False
        }
    ]
}


print(is_valid_workout_object(workout_object))