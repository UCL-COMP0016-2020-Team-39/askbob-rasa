from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher

import requests

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
# This is a simple example for a custom action which utters "Hello World!"
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionFetchWeather(Action):

    def name(self):
        return "action_fetch_weather"

    def run(self, dispatcher, tracker: Tracker, domain):

        try:
            gpe = next(tracker.get_latest_entity_values("GPE"), None)
            if gpe is None:
                raise RuntimeError("No GPE provided!")
        except:
            dispatcher.utter_message(
                text="I'm sorry - I don't know where that is!")
            return []

        r = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={
            "q": gpe,
            "units": "metric",
            "appid": "b6bea28b4b8e3d4ecf0355e92f30a217"
        }).json()

        try:
            dispatcher.utter_message(text="It's {0} degrees with {1} in {2}.".format(
                r['main']['temp'], r['weather'][0]['description'], r['name']))
        except:
            dispatcher.utter_message(
                text="Appologies - weather data is incomplete at the minute.")

        return []


class ActionFetchJoke(Action):

    def name(self):
        return "action_fetch_joke"

    def run(self, dispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="One joke, coming right up!")

        r = requests.get(url="https://icanhazdadjoke.com/",
                         headers={"Accept": "application/json"}).json()

        dispatcher.utter_message(text=r['joke'])

        return []


class ActionFetchTime(Action):

    def name(self):
        return "action_fetch_time"

    def run(self, dispatcher, tracker: Tracker, domain):
        from datetime import datetime

        dispatcher.utter_message(text="The time is {0}.".format(
            datetime.now().strftime("%H:%M")))

        return []
