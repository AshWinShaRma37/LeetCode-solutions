class Solution:
    def interpret(self, command: str) -> str:
        '''
        command = command.replace("()","o")
        command = command.replace("(al)","al")
        return command
        '''
        #the same could be done in one line
        return command.replace('()','o').replace('(al)','al')