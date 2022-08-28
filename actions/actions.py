# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_tipo_tarjeta"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tarjeta=tracker.latest_message['entities'][0]['value']
        message="Esta tarjeta le servira para "
        if str(tarjeta)=="credito":
            message=message+"realizar compras y abonarlas a fin de mes"
        else:
            message= message+"realizar compras y abonarlas en el momento siempre y cuando usted cuente con saldo en su caja de ahorro"
        dispatcher.utter_message(text=str(message))
        return []

class ActionTime(Action):

    def name(self) -> Text:
        return "action_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(text="Los horarios de atencion son de lunes a viernes de 8:00 a 14:00 hs")
        if str(intent)=="horarios_atencion":
            return [SlotSet("time", "fin")]
        return []

class ActionTime(Action):

    def name(self) -> Text:
        return "action_turno_fin_de_semana"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time=tracker.get_slot("time")
        if str(time)=="fin":
             dispatcher.utter_message(text="Los turnos disponibles para el fin de semana son Sabados y Domingos de 8:00AM a 9:00AM")
        return []
