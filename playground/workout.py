import datetime

class ExerciseSetData: 
    def __init__(self, exercise_id, sets, reps, weight): 
        self.exercise_id = exercise_id
        self.sets = sets
        self.reps = reps
        self.weight = weight 
        
    def __str__(self):
        return "exercise_id: {}, reps: {}, sets: {}, weight: {}".format(self.exercise_id, self.reps, self.sets, self.weight)
        
    def get_json_properties(self): 
        return {
            "exercise_id": self.exercise_id,
            "sets": self.sets,
            "reps": self.reps, 
            "weight": self.weight, 
            "is_done": False
        }



workout_llm_data = [
    [
      {
        "exercise_id": 1,
        "sets": 3,
        "reps": 8,
        "weight": 52.5
      },
      {
        "exercise_id": 12,
        "sets": 3,
        "reps": 8,
        "weight": 42.5
      }
    ],
    [
      {
        "exercise_id": 12,
        "sets": 2,
        "reps": 5,
        "weight": 65
      },
      {
        "exercise_id": 45,
        "sets": 3,
        "reps": 6,
        "weight": 85
      },
      {
        "exercise_id": 32,
        "sets": 5,
        "reps": 8,
        "weight": 50
      }
    ]
  ]



# print(x)



# print(workouts)

def get_workout_objects(schedule_llm): 

    workouts = []
    for i, workout in enumerate(schedule_llm): 
        # print("workout: ", i)
        exercise_sets = []
        for exercise_set in workout: 
            ex_object = ExerciseSetData(exercise_set['exercise_id'], exercise_set['sets'], exercise_set['reps'], exercise_set['weight'])        
            exercise_sets.append(ex_object.get_json_properties())
            # print(ex_object)
        clean_workout = {
            "created_at": datetime.datetime.now(),
            "exercise_sets": exercise_sets
        }
        workouts.append(clean_workout)
    return workouts

res = get_workout_objects(workout_llm_data)

# print(res['exercise_sets'][0] )

print(res)