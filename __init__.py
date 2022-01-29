from mycroft import MycroftSkill, intent_file_handler


class FaceRecognition(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('recognition.face.intent')
    def handle_recognition_face(self, message):
        self.speak_dialog('recognition.face')


def create_skill():
    return FaceRecognition()

