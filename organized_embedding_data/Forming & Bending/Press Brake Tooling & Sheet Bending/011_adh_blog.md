# Diagnosing a Press Brake That Does Not Begin a Bend Cycle

## Scope and safety

A press brake may fail to move after the foot control is actuated, or it may stop during a bend-and-return sequence. The article supports a general diagnostic approach based on observing the machine’s displayed operating state and confirming that required axes have reached their commanded positions.

Diagnostic screens, state labels, and sequence definitions differ by controller, software version, and machine configuration. Use the machine manual to interpret the displayed information. Do not bypass guards, interlocks, or safety devices. Electrical, hydraulic, control-system, synchronization, or motion faults should be assessed by qualified personnel following the manufacturer’s service procedures.

## Check the displayed cycle state

Many press-brake controls show a current operating state or cycle stage. A displayed state can help distinguish between two broad conditions:

- The control has not accepted or initiated the downward-motion command.
- The cycle began but stopped at a particular stage, such as pressing, pressure holding, decompression, or return.

The source article gives one controller-specific example of a six-stage sequence: stop, fast downward movement, pressing movement, pressure holding, decompression, and return. This sequence should not be assumed to apply to other controls. Instead, consult the applicable manual for the meanings of the states shown on the installed machine.

If actuation of the foot control does not change the displayed state and the ram does not move, the useful initial observation is that the downward command may not have been executed. Further diagnosis should then focus on the machine conditions and interlocks required before motion is permitted.

## Confirm axis readiness before starting the cycle

The article indicates that auxiliary axes may need to reach their programmed positions before bending motion is enabled. Depending on machine configuration, these can include backgauge-related axes and table or compensation-related axes.

Compare actual axis positions with commanded positions using the controller’s normal position or diagnostic display. A machine may prevent the bend cycle from starting when an axis has not completed its commanded movement. This is especially relevant where multiple controlled axes or synchronized equipment are involved, because all required motion conditions may need to be satisfied before the ram is allowed to move.

Do not attempt to force an axis, alter motion parameters, or manually correct a positioning fault unless this is specifically authorized by the machine documentation and performed by appropriately qualified personnel.

## Use diagnostic information to locate the stage of interruption

When a machine stops unexpectedly, identify the cycle stage displayed when the interruption occurred. For example, a failure to return may be associated with a state corresponding to pressure holding or decompression on the particular controller. The displayed stage does not by itself establish the root cause, but it narrows the investigation to the portion of the sequence that did not complete.

Useful observations to record for qualified maintenance personnel include:

- Whether the foot control changed the machine’s displayed state.
- Whether required axes showed actual positions matching their targets.
- The last displayed cycle stage before motion stopped.
- Whether the issue occurred before downward movement, during pressing, or during return.
- Any diagnostic indicators or messages shown by the installed controller.

## Escalation

If axis readiness appears incomplete, if the cycle stops at a repeatable stage, or if the controller reports a fault, stop operation and follow the machine manual’s fault-reporting and service process. Avoid changing controller parameters solely to make the machine move. Accurate observations of the cycle state and axis condition can help qualified personnel diagnose the issue without treating controller-specific labels or sequence codes as universal.
