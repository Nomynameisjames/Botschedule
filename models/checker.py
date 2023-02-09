#!/usr/bin/python3i
from models.Schedule import Create_Schedule
import os
import openai
import json

class Checker:
    def __init__(self):
        """
            class modifies the Average and Target column of the User
            database
        """
        self.schedule = Create_Schedule()
        self.task = self.schedule.View("daily")
        for key, value in self.task.items():
            text = self.task[key]['Topic']
            self.message = f"where can i best learn the following topic {text}\
                            recommend alongsides resources"


    def Review(self, my_id):
        """
            class method modifies the Create_Schedule class instance
            based on the provided
            parameters
        """
        allTask = self.schedule.View()
        if my_id in allTask:
            print('''Course average are calculated based on the following parameters,
                5. Topic Fully Covered, with practice  5pt
                4. Topic covered without practice 4pt
                3. Topic 50% covered 3pt
                2. Topic 25% covered  2pt
                1. just started 1pt.'''
                    )
            print(f"\n>>>completed the following tasks? {allTask[my_id]} <<<\n")
            choice = int(input("rate your productivity based on above: "))
            score = None
            if choice == 5:
                score = (100/100) * 100
                self.schedule.Update(my_id, score, 4)
            elif choice == 4:
                score = (75/100) * 100
                self.schedule.Update(my_id, score, 4)
            elif choice == 3:
                score = (50/100) * 100
                self.schedule.Update(my_id, score, 4)
            elif choice == 2:
                score = (25/100) * 100
                self.schedule.Update(my_id, score, 4)
            elif choice == 1:
                score = 0
                self.schedule.Update(my_id, score, 4)
            else:
                print("invalid selection, please read above prompt")
        else:
            print("Course ID not in list")

    def Help(self, message=None):
        """
            class method uses the openAI API to invoke a chatbot to recommend
            resources based on the daily topic queried from the database
            or questions asked
        """
        if message is None:
            opt = self.message
        else:
            opt = message
        openai.api_key = os.environ['OPENAI_API_KEY']
        response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt= opt,
                    temperature=0.3,
                    max_tokens=150,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                        )
        """
            returns a JSON value of the API response
        """
        with open('response.json', 'a') as file:
            json.dump(response, file)
        answer = response.choices[0].text
        return (answer[2:])




