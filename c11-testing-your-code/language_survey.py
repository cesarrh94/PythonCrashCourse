from survey import AnonymousSurvey

question = "What language do you speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break

    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.get_results()