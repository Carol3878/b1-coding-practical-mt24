class PDController:
    def __init__(self, KP: float, KD: float):
        self.KP = KP  # Proportional gain
        self.KD = KD  # Derivative gain
        self.previous_error = 0  # Stores e[t-1]

    def compute_control_action(self, reference: float, observation: float) -> float:
        # Compute the current error
        error = reference - observation
        
        # PD control action
        control_action = self.KP * error + self.KD * (error - self.previous_error)
        
        # Update the previous error for the next step
        self.previous_error = error
        
        return control_action

    # def reset(self):
    #     self.previous_error = 0
