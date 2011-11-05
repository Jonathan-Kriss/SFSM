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
    
    def getTransisitionDestination(self,tName):
        if tName in self.transitions:
            return self.transitions[tName]
        return "Invalid Transition"
        
    def isValidTransition(self,tName):
        return tName in self.transitions
    
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
        for iterState in self.states:
            if iterState == stateName:
                self.states.remove(iterState)
    
    def addTransition(self,transitionName,fromState,toState):
        if fromState in self.states and toState in self.states:
            self.states[fromState].addTransition(transitionName,toState)
        
    def doAction(self,tName):
        for iterState in self.states.values():
            if iterState.isValidTransition(tName):
                self.currentState = iterState.getTransitionDestination(tName) 
                
                
                      

    
