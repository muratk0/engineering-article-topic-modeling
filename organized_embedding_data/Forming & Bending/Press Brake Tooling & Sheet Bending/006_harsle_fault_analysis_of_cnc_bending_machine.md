# Fault Analysis of CNC Bending Machine

As a seasoned technician, I've encountered various challenges in the operation of CNC bending machines. In this article, I will delve into the fault analysis of CNC bending machines, highlighting common issues that can arise during operation. Understanding these faults is crucial for maintaining efficiency and ensuring high-quality outputs in metal fabrication. By sharing my insights and experiences, I aim to provide valuable guidance on identifying, troubleshooting, and resolving these issues, ultimately helping others optimize their CNC bending processes.

## CNC Bending Machine Mechanical Failure

● The guide gap between the slider and the guide rail is too large, make an abnormal sound. This type of failure is due to the long time the rails are used,wear caused by gap increase. Need to check the degree of wear on the rail press plate, determine whether to replace the rail presser according to the degree of wear and re-adjust to the required clearance.

● The guide rail of the slider must be lubricated once a day, generally, before starting the machine, the slider is at the bottom dead center, clean and lubricate ball screws and linear guides every week, lubricate the guide rails and lead screws or other sliding parts every week. After running the new machine for half a year, must replace 46# or 32# anti-wear hydraulic oil and high-pressure filter. Replace hydraulic oil and high-pressure filter once a year. Check if the connection between the cylinder and the slider is loose every month, whether the back gauge timing belt is loose, check the clearance between the longitudinal rail and the side rail every month, and adjust in time.

● Back gauge transmission failure. The rear gear drive fails because the drive shaft is disengaged from the timing pulley's key strip or the timing belt slips off. Such failures require reassembling the key strips and timing belts and checking the electrical parts.

● When the back gauge beam linear guide is parallel to the center line of the mold, the deviation is too large. This type of failure requires loosening the 'X' – axis timing belt, re-adjusting to the parallel tolerance range, and re-installing the timing belt.

● Loose cylinder and slider connection, causes the bend angle to be inaccurate or the machine cannot find the reference point. This type of failure requires a re-check of the tightening slider and the cylinder connection nut.

## CNC Bending Machine Hydraulic Failure
● Hydraulic system without pressure:

①Whether the electromagnetic coil of the proportional relief valve is energized, and the proportional solenoid voltage meets the requirements. For the above reasons, please check the relevant electrical reasons.

②Check if the cartridge valve is stuck or the main spool is stuck, and the damper orifice is blocked. If the above reasons are concerned, please remove the overflow valve and clean it.

③Three-phase power phase modulation, resulting in motor reversal.

● The slider rotates slowly and the time is too long:

①Check if the fuel tank is too low, the filling port is not flooded, and the liquid filling in the upper chamber of the cylinder is insufficient to cause liquid filling. For the above reasons, the oil in the tank can be added to the top of the filling port by more than 5 mm so that the liquid filling hole is completely flooded.

②Check if the fast forward speed is too fast, causing insufficient liquid filling. For the above reasons, the fast forward speed can be reduced by modifying the system parameters.

③Check if the filling valve is fully opened, If it is because of oil pollution, the valve body of the filling valve is inactive and stuck, causing insufficient liquid filling. Need to clean the filling valve and reinstall it to make the valve core flexible.

● The valve block returns normally, fast forward is normal, manual can't slow down, the flap is weak:

①Check if the '2-way four-way' reversing valve that controls the filling control circuit is working properly. If it is, the filling valve is not closed, so that the upper chamber and the fuel tank filling port are unreasonable, and no pressure can be built. The cause of the valve not working properly is that it is not energized or stuck.

②Check if the filling valve is stuck. If it is, please clean the filling valve and reinstall it to make the valve core flexible.

● The slider return speed is too slow and the return stroke pressure is high. This type of fault is mainly caused by the filling valve not being opened. This phenomenon is just opposite to the logic of the above fault three. It can be handled by referring to the solution of fault three.

## Electrical system category
● After the oil pump is started, the low-voltage disconnect switch trips. This type of failure requires the following checks.

①Check the phase loss of the power supply.

②Check if the high-pressure filter element is seriously blocked, resulting in too much oil pump motor current.

③Check if the low-voltage disconnect switch is set too small.

● After powering on, no reference point can be found when referring to the reference point.

①Due to the looseness of the scale head connection of the scale, the machine is on the return journey, The read head cannot coincide with the reference point of the scale and the stroke of the cylinder has been used up, the oil pump is in a working load state. If this is the case, you need to press the red stop button of the CNC system, stop the reference point and reconnect the connecting plate that corrects the scale,then enter the manual mode working state, make the slider manually down,When the slider is overlapped with the lower mold, enter the manual or semi-automatic mode, and return to the reference point to eliminate the fault.

②After the last operation of the machine, the operator did not strictly follow the production shutdown,stop the slider at the top dead center position before powering off the machine, and the next time you turn it on, did not manually slide the slider down, place the position where the upper and lower molds are coincident, and perform the operation of referring back to the reference point. Cause the operation to not find the reference point. If this is the case, you need to turn the system into a manual state. Manual mode down the slider to the upper and lower mold coincidence positions, re-recover the reference point when entering the semi-automatic or automatic mode.

● There is no display for the DNC60 or DNC600 CNC system display, and the gray-white programming button indicator flashes. This kind of failure is mainly caused by the operator of the system not clearing the product program that is not used in the time when the product editing operation is performed, but directly modifying it on the last working product program, and repeatedly causing the system to be caused.

The buffer memory program is full and the system program is not working properly. First , disconnect the main power supply, press the '++"–' key on the system keyboard at the same time, then turn on the power, and the system will enter the initialization state. The system display will appear as follows: Then, you will need to empty your needs. Enter before the project: '1' means to clear the item, then enter the password '817', press the confirm key to confirm, the screen will prompt you to 'executed' and the required content is cleared.

● The scale is 'technically inaccurate' and causes an error in the bending angle. Such failures mainly reflect the cumulative increase of the repeated positioning accuracy error of 'Y1''Y2' porridge, and the angle error of the bending work piece is large, and the angular error is cumulatively increased on the previous basis. The main reason is that the grating scale feedback signal counts the number of pulses that are broken. It is necessary to take dust-proof measures for the removal and cleaning of the grating ruler, redesign the unreasonable installation method to the reasonable installation, and return to the manufacturer for repair or replacement of the grating rule fault.

● After the product is programmed, the back gauge 'X' axis 'R' axis safety distance alarm. This kind of failure is mainly the setting of the safety distance of the upper and lower molds during the mold preparation, and the setting of the limit position of the X-axis R-axis in the system and the program 'X' axis 'Y' axis stop position programmed by the current product. Contradictions and the system prompts an alarm. For security reasons, the system will not operate and cannot operate normally. It is necessary to reprogram the product or modify the parameters of the product mold to meet the requirements, that is, the alarm is released before the operation can be performed.

● A drive motor error alarm occurs on the X-axis R-axis of the back gauge. Such a fault needs to first open the electrical box, look at the drive to display the alarm code, and consult the driver manually to find out the cause of the alarm according to the alarm code indicated by the drive. There are two kinds of common alarms: 16# alarm, suggesting that the drive motor overload alarm.

We can check whether the transmission of the X-axis Y-axis of the back gauge is flexible, the resistance is too large, and whether the X-axis R-axis has reached the mechanical limit, if so, Eliminate mechanical failures. 22# alarm, indicating the encoder feedback signal alarm, causing this phenomenon, maybe 'connector' bad contact, desoldering or disconnection and signal interference need to be checked one by one.

● The computer display position of Y1 and Y2 does not match the actual position. This type of failure is mainly due to the inaccuracy of the original reference point and reinitialization of the reference point.

● The system computer X-axis R-axis positioning does not match the actual positioning. This kind of fault is mainly caused by the position of the X-axis R-axis being moved when the machine is powered off. At this time, the computer still remembers the position before the shutdown, so the actual position of the X-axis R-axis changes and the X-axis R needs to be re-initialized. The position of the axis.

● System signal interference alarm. This kind of fault is mainly due to poor shielding grounding or loose grounding

