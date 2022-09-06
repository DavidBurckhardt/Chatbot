# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from cgitb import text
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "accion_verificar_dia"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dia_respuesta=next(tracker.get_latest_entity_values("dia"),None)
        if str(dia_respuesta)=="lunes":
            message="Se asigno el turno para el dia "
            dispatcher.utter_message(text=(str(message) + str(dia_respuesta)))
        else:
            message="Ese dia el banco esta cerrado"
            dispatcher.utter_message(text=str(message))
        return []
    
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_cuenta"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        respuesta=tracker.latest_message['intent'].get('name')
        if str(respuesta)=="deny":
            message="Desea crearse una?" 
            dispatcher.utter_message(text=str(message))
            return [SlotSet("cuenta", "crear")]
        else:
            message= "Desea loguearse ingresando sus datos?"
            dispatcher.utter_message(text=str(message))
            return [SlotSet("cuenta", "ingresar")]

class ActionTime(Action):

    def name(self) -> Text:
        return "action_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(text="Los horarios de atencion son de lunes a viernes de 8:00 a 14:00 hs")
        if str(intent)=="horarios_atencion":
            return [SlotSet("turno", "sacar")]
        return []
