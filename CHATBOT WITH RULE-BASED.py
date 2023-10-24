import random

sci_qus = {
    "biology": [
        {
            "question": "The human heart is \n"
                        "A) Neurogenic heart	B) Myogenic heart C) Pulsating heart	D) Ampullary heart",
            "answer": "b"

        },
        {
            "question": "Some species of which of the below kinds of organisms are employed as biopesticides?\n"
                        "1.Bacteria  2. Fungi  3. Flowering plants",
            "answer": "1"
        },
        {
            "question": "Spermology is the study of \n"
                        "A) Seed	B) Leaf C) Fruit	D) Pollen grain",
            "answer": "a"
        },
        {
            "question": "Who is known as father of Zoology \n"
                        "A) Darwin	B) Aristotle C) Lamark	D) Theophrastus",
            "answer": "b"
        },
        {
            "question": "Animal without red blood cells\n"
                        "A) Frog  B) Earthworm  C) Snake	D) Peacock",
            "answer": "b"
        },

    ],
    "physics": [
        {
            "question": "The working principle of a washing machine is \n"
                        "A) reverse osmosis	B) diffusion C) centrifugation	D) dialysis",
            "answer": "c"
        },
        {
            "question": "Nuclear sizes are expressed in a unit named \n"
                        "A) Fermi	B) Angstrom C) Newton	D) Tesla",
            "answer": "a"
        },
        {
            "question": "The speed of light will be minimum while passing through \n"
                        "A) water	B) vaccum C) air	D) glass",
            "answer": "d"
        },
        {
            "question": "Which of the following is not a vector quantity? \n"
                        "A) speed	B) velocity C) torque	D) displacement",
            "answer": "a"
        },
        {
            "question": "The most suitable unit for expressing nuclear radius is \n"
                        "A) micro	B) nanometre C) fermi	D) angstrom",
            "answer": "c"
        },
    ],
    "chemistry": [
        {
            "question": "The purest form of iron is \n"
                        "A) wrought iron	B) steel C) pig iron	D) nickel steel",
            "answer": "a"
        },
        {
            "question": "Among the following the maximum covalent character is shown by the compound \n"
                        "(1)MgCl2 (2)FeCl2 (3)SnCl2 (4) AlCl3",
            "answer": "4"
        },
        {
            "question": "Hydrogen bomb is based on the principle of \n"
                        "A) nuclear fission	B) nuclear fusion C) natural radioactivity	D) artificial radioactivity",
            "answer": "b"
        },
        {
            "question": "Boron cannot form which one of the following anions? \n"
                        "(1) BO−2 (2) BF3−6 (3) BH−4 (4) B(OH)−4",
            "answer": "2"
        },
        {
            "question": "SI unit of equivalent conductance \n"
                        "A) ohm/cm	B) Siemens m2/equivalent C) Siemens/equivalent	D) mho/cm",
            "answer": "b"
        },
    ],
}


def start_quiz(name):
    while True:
        topic = input(f"Mr {name} Please select the quiz topic by entering its name:\nBiology\nPhysics\nchemistry.").lower()
        if topic not in sci_qus:
            print("Sorry! please select from the topics given above.")
        else:
            break
    question = sci_qus[topic]
    random.shuffle(question)

    score = 0
    for i in question :
        print("\n Question: ", i["question"])
        user_ans = input("Enter your option: ").lower()

        if user_ans == i["answer"]:
            print("Correct!!")
            score += 1
        else:
            print(f"Wrong answer :( the correct answer is : {i['answer']}")
    print(f"Mr {name}, Quiz completed! Your score for this quiz is: {score}/{len(question)}")




while True:
    user = input("Hello!! Welcome to the Codsoft quiz of science.\n").lower()
    if user == "hello" or user == "hi":
        user_name = input("Please write your name: ")
        user = input(f"Mr {user_name} would you like to conduct a quiz? y/n").lower()
        if user == "y" or user == "yes":
            start_quiz(user_name)
        else:
            print("Nice talking to you. Have a great day!!")
            break
    else:
        print(f"I do not understand please write your message again.")


