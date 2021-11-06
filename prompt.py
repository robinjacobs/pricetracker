


class Prompt():
    def __init__(self, children_nodes = None, prompt_calling_str='', prompt_question='', action=None) -> None:
        self.children_nodes = children_nodes
        self.prompt_str = prompt_calling_str
        self.prompt_question = prompt_question
        self.action = action
        print(self.children_nodes)

    def __call__(self, *args, **kwds,) -> None:
        print(self.prompt_str)
        if self.children_nodes == None :
            self.action()
        else :
            self.prompt_chooser()

    def prompt_chooser(self) :
        number_nodes = len(self.children_nodes)
        for i in range(number_nodes) :
            print(f'[{i}]'+ self.children_nodes[i].prompt_question)
        
        z = int(input("Enter your selection: "))
        self.children_nodes[z]()


def foo() :
    print('fooo')
    pass



if __name__ == '__main__' :
    a = Prompt(prompt_calling_str='This is a calling', prompt_question='Choose a', action=foo)
    b = Prompt(prompt_calling_str='This is b calling', prompt_question='Choose b', action=foo)
    c = Prompt(prompt_calling_str='This is c calling', prompt_question='Choose c', action=foo)
    start = Prompt([a,b,c],prompt_calling_str='This is start calling')
    start()
    

