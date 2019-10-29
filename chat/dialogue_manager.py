from chat import nlg


class DialogueManager(object):
    def __init__(self):
        self.nlg = nlg.Nlg()

    def get_recommend(self):
        """get recommend result

        Returns:
            recommend_text [str]: recommend result text
        """
        recommend_text = self.nlg.gen_recommend_utterance()

        return recommend_text

    def get_inquiry(self):
        return "sample inquiry"
