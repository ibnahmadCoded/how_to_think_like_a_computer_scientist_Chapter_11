class SMS_store():
    """SMS_store class represents and manipulates user messages"""

    def __init__(self, messages = []):
        """Create a new message object"""
        self.messages = messages


    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        # Makes new SMS tuple, inserts it after other messages
        # in the store. When creating this message, its
        # has_been_viewed status is set False.
        sms = (False, from_number, time_arrived, text_of_SMS)
        self.messages.append(sms)

    def message_count(self):
        # Returns the number of sms messages in my_inbox
        count = 0
        for message in self.messages:
            count += 1
        return count

    def get_unread_indexes(self):
        # Returns list of indexes of all not-yet-viewed SMS messages
        indexes = []
        for index, message in enumerate(self.messages):
            #check if message is unread
            if message[0] == False:
                indexes.append(index)
        return indexes

    def get_message(self, i):
        # Return (from_number, time_arrived, text_of_sms) for message[i]
        # Also change its state to "has been viewed".
        # If there is no message at position i, return None
        if self.messages[i][0] == False:
            #change status 
            self.messages[i] = (True, "") + self.messages[i][1:]
            return self.messages[i][2:]  

    def delete(self, i):
        # Delete the message at index i
        del(self.messages[i])
        

    def clear(self):
        # Delete all messages from inbox
        self.messages = []
            
    
