class Queue(list):
    """A basic FIFO queue implementation.

     This is implemented as an extension of the `list` datatype.

     New items come in at the TAIL and go out (popped) at the HEAD.

         Head is at index 0
         Tail is at index -1
     """
    def enqueue(self, nick):
        self.append(nick)

    def in_queue(self):
        if len(self) > 0:
            return len(self)
        else:
            return "No one is in queue."

    def pop_next(self):
        if len(self) > 0:
            return self.pop(0)
        else:
            return None

    def clear(self):
        del self[:]

    def next_nick(self):
        if len(self) > 1:
            return str(self[0]) + " ask your question and " + str(self[1]) + " ready with your question."

        elif len(self) > 0:
            return str(self[0]) + " ask your question."
        else:
            return "No one is in queue."
