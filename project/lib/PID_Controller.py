import time

"""
Initialization (__init__): Allows setting PID gains (Kp, Ki, Kd), sample time (T), and control signal bounds (max_control, min_control) during instantiation.
PID Computation (compute): Implements proportional, integral, and derivative terms with bounds checking for accumulated error and control signal.
The compute method returns a positive control signal when below the set point and a negative control signal when above the set point.

Example Usage
pid = PIDControl(Kp=1.0, Ki=0.5, Kd=0.1, T=100, max_control=255, min_control=0)
pid.setpoint = 50  # Desired setpoint
pid.sensed_output = 40  # Example sensed output

pid.compute()  # Compute the control signal
print("Control Signal:", pid.control_signal)
"""


class PIDControl:
    def __init__(
        self, Kp=0.0, Ki=0.0, Kd=0.0, T=100, max_control=100, min_control=-100
    ):
        """
        Initialize the PID controller with default or provided parameters.
        """
        self.sensed_output = 0.0
        self.control_signal = 0.0
        self.setpoint = 0.0
        self.Kp = Kp  # proportional gain
        self.Ki = Ki  # integral gain
        self.Kd = Kd  # derivative gain
        self.T = T  # sample time in milliseconds (ms)
        self.last_time = int(
            round(time.time() * 1000)
        )  # initialize with current time in ms
        self.total_error = 0.0
        self.last_error = 0.0
        self.max_control = max_control
        self.min_control = min_control

    def millis(self):
        """
        Returns the number of milliseconds since the program started.
        """
        return int(round(time.time() * 1000))

    def compute(self):
        """
        Perform the PID control computation.
        """
        current_time = self.millis()  # get current time in ms
        delta_time = current_time - self.last_time  # calculate time interval

        if delta_time >= self.T:
            # Calculate error
            error = self.setpoint - self.sensed_output

            # Accumulate the error (integral term)
            self.total_error += error
            if self.total_error > self.max_control:
                self.total_error = self.max_control
            elif self.total_error < self.min_control:
                self.total_error = self.min_control

            # Calculate the error difference (derivative term)
            delta_error = error - self.last_error

            # Compute the control signal
            self.control_signal = (
                self.Kp * error
                + (self.Ki * self.T) * self.total_error
                + (self.Kd / self.T) * delta_error
            )

            # Limit the control signal to max and negated max bounds
            if self.control_signal > self.max_control:
                self.control_signal = self.max_control
            elif self.control_signal < (0 - self.max_control):
                self.control_signal = 0 - self.max_control

            # Update last error and last time for the next computation
            self.last_error = error
            self.last_time = current_time
            return self.control_signal
        else:  # If the time interval is less than T, return the last control signal
            return self.control_signal
