class Solution(object):
    def interpret(self, command):
        ans=''
        ans=command.replace('()','o')
        command=ans.replace('(al)','al')
        return (command)