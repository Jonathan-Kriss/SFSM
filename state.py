class state:
    """A class representing a node in the FSM graph"""
    def __init__(self,name):
        self.name = name
        self.transitions = {}
        
    def addTransition(self,transitionName,newState):
        print "add transition <" + transitionName + "> to " + newState
        self.transitions[transitionName] = newState
        
    def removeTransition(self,transitionName):
        print "remove transition: " + transitionName
        self.transitions.pop(transitionName)
    
    def toString(self):
        for key, value in self.transitions.items():
            print key, value
            
class FSM:
    """Finite State Machine Class"""
    def __init__(self):
        self.currentState = ""
        self.states = {}
    
    def addState(self,stateName):
        self.states[stateName] = state(stateName)
    
    def removeState(self,stateName):
        for currentState in self.states:
            if currentState == stateName:
                self.states.remove(currentState)
    
    def addTransition(self,fromState,toState,transitionName):
        if fromState in self.states:
            
            
        
    def doAction(self,transitionName):
        
            
    


    
        
      
