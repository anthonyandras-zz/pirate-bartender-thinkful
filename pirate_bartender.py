import random


questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with your poison?",
        "fruity": "Are ye one for a fruity finish?",
}        

ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def ask_questions():
    responses = {}
    for question in questions:
        response = input(questions[question] + ' ')
        if response == 'y' or response == 'yes':
            responses[question] = True 
        else:
            responses[question] = False
    return responses

def construct_drink(responses):
   preferences = [x for x in responses.keys() if responses[x] == True]
   drink = [ingredients[x] for x in preferences]
   return drink

if __name__ == '__main__':
    drink = construct_drink(ask_questions())
    print(", ".join(random.choice(drink)))
    
    
