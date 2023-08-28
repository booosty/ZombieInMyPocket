class DevCard:
    def __init__(
        self,
        item,
        nine_message,
        nine_action,
        ten_message,
        ten_action,
        eleven_message,
        eleven_action,
        nine_action_amount=0,
        ten_action_amount=0,
        eleven_action_amount=0
    ):
        self.item = item
        self.nine_message = nine_message
        self.nine_action = nine_action
        self.ten_message = ten_message
        self.ten_action = ten_action
        self.eleven_message = eleven_message
        self.eleven_action = eleven_action
        self.nine_action_amount = nine_action_amount
        self.ten_action_amount = ten_action_amount
        self.eleven_action_amount = eleven_action_amount
