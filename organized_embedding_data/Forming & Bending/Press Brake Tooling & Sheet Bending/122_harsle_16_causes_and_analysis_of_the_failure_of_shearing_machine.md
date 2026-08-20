# 16 Causes And Analysis of The Failure of Shearing Machine

In my experience with metal fabrication, I have often encountered the challenges posed by machine failures, particularly with shearing machines. Understanding the causes and analysis of the failure of shearing machines is crucial for minimizing downtime and ensuring production efficiency. Through careful observation and analysis, I've identified several common issues that lead to failures, ranging from mechanical wear to improper maintenance practices. In this article, I'll delve into the root causes of these failures and share insights on how to effectively address and prevent them, ultimately improving the reliability of shearing operations.

## Table of Contents

- Malfunction 1: Main motor cannot start
- Malfunction 2: Slider Cannot Go Down
- Malfunction 2: Slider Cannot Return
- Malfunction 3:The slider vibrates greatly when the sheet is cut
- Malfunction 4:When cutting, the upper blade cannot cut down after cutting the sheet.
- Malfunction 5:The upper blade does not move during cutting, the clamp is slowly downward, but the sheet cannot be clamped.
- Malfunction 5: Increase or decrease of shear angle cannot be adjusted
- Malfunction 6: After the material can not move or move slowly
- Malfunction 7: The slider is heavily tilted
- Malfunction 8: Slider slides automatically
- Malfunction 9: The slider is at the lowest position, the slider cannot automatically return after the oil pump is started.
- Malfunction 10:Sometimes the main motor stops automatically, thermal relay, circuit breaker protection
- Malfunction 11: Any valve is stuck
- Malfunction 12: Oil temperature is too high
- Malfunction 13: Clamp oil leakage, skew
- Malfunction 14: The sheet is stuck by the upper knife and the clamp
- Malfunction 15: The workpiece burr is too large during processing
- Malfunction 16: Poor cutting accuracy

Analyzing the causes of shearing machine failures involves examining various factors that can contribute to operational issues. Here's a breakdown of common causes and their potential analyses:

### **Malfunction 1:**Main motor cannot start

Reason:

1.The main motor starts the circuit fault, such as: the emergency stop button is not released, the cable connection is loose, and the 24V control power supply is used;

2.The related components of the main motor starting part are faulty, such as: thermal relay, circuit breaker, AC contactor, etc., overload protection or damage;

3.Power problems;

4.When the motor starts, it is the sound of the car, and the pressure valve has been working;

Solution:

1.Check whether the main motor starting circuit has an emergency stop and is not released, the wiring is loose, and the 24V control power supply;

2. Check whether the components of the main motor starting circuit part have overload protection. If there is any need for analysis, check for component damage.

3. Check if the three-phase power supply is normal;

4. Check the pressure valve has a signal, mainly the following aspects: line, relay failure, top dead center switch damage, linear potentiometer damage, the slider is seriously skewed;

### **Malfunction 2:**Slider Cannot Go Down

Reason:

1.The system status is not "S2";

2. The slider is not at the top dead center, or the top dead center switch is not installed correctly or damaged;

3. The bottom dead center switch is damaged, and the PLC sends an error signal;

4. The linear potentiometer is damaged, and an error signal is sent to the system;

5. The PLC interface, relay and line of the control proportional pressure valve and the slider control reversing valve are faulty;

6. The pressure part is faulty and there is no pressure;

Solution:

1.Check whether the X-axis, the shear angle, and the blade-edge clearance are at the set position, and whether the slider is at the top dead center, if not, analyze reasons;

2. Check the reason why the slider is not at the top dead center, check the top dead center switch;

3. Check the installation and signal of the bottom dead center switch;

4. Check the linear potentiometer signal;

5. Check the PLC input/output signal, check the signal of the pressure valve and the slider control reversing valve, and check the line;

6. The hydraulic system has no pressure output, check the proportional pressure valve, oil pump, etc.;

### **Malfunction 2:**Slider Cannot Return

Reason:

1.No return conditions, such as: cutting position in place, slider to bottom dead point, release the foot switch;

2. Line faults, such as: proportional pressure valve, slider control reversing valve PLC interface, relay, line out malfunction;

3. Mechanical failure, such as: the occurrence of splint, mainly due to blunt blade, the actual gap is greater than the theoretical value, the guide rail loose and other reasons;

Solution:

1.Check the return condition according to the PLC signal table, and analyze the reasons, such as whether the linear potentiometer, the bottom dead center switch, and the foot switch are normal;

2. Check the PLC input/output signal, check the signal of the pressure valve and the slider control reversing valve, and check the line;

3. Close the oil pump, adjust the gap to the maximum, and then restart the oil pump, the slider should automatically return, if you can not return, you can use the jack and other tools to raise the slider, and then check the machine to analyze the cause of the splint;

### **Malfunction 3:**The slider vibrates greatly when the sheet is cut

Reason:

1. The slider and the cylinder are loosely connected;

2. The blade edge wear;

3. The back pressure setting is too high, and the slider shakes when it is empty;

Solution:

1.Check the slider connection to find the loose position;

2. Check the degree of edge wear;

3. Adjust the back pressure according to the standard;

### **Malfunction 4:**When cutting, the upper blade cannot cut down after cutting the sheet.

Reason:

1. Reasons for operation, a, pressure selection is incorrect, and does not correspond to actual operation; b, the thickness of the sheared sheet exceeds the allowable range of the machine tool; c, the actual shearing plate thickness is inconsistent with the programmed program, and the shear angle is small;

2. For hydraulic reasons, the pressure is not enough, and the proportional pressure valve, main pressure reducing valve, filter element, oil pump, etc. fail;

Measures:

1.Check whether the gear position of the pressure selection switch on the electric cabinet matches the material to be cut; b. Check whether the sheared material is in the machine parameter range; c. Check whether the actual plate thickness, program, shear angle and plate thickness are Corresponding;

2. Check the main pressure with a pressure gauge. The maximum pressure is 28 MPa when the pressure selector switch is "3". If the proportional pressure valve and the main pressure reducing valve cannot be checked first, check the filter element and hydraulic oil, and finally check the oil pump and its coupling;

### **Malfunction 5:**The upper blade does not move during cutting, the clamp is slowly downward, but the sheet cannot be clamped.

Reason:

1. There is no main pressure, and the pressure part is faulty;

Solution:

1.First check whether the proportional pressure valve model is normal, and then gradually check the hydraulic part to analyze the reason;

Malfunction:

The clamp can not go down, the rest of the action is normal

Reason:

1.The clamping valve control part is faulty, and the PLC output point and relay of the clamping valve are controlled to be faulty;

2. The clamping valve is faulty;

Solution:

1. Check the corresponding PLC output signal, relay, and check the line;

2. Clean and control the clamped valve;

### **Malfunction 5:**Increase or decrease of shear angle cannot be adjusted

Reason:

1. The control part of the shear angle control valve is faulty, and the corresponding PLC output point and relay are faulty;

2. The shear angle control valve is faulty

Solution:

1. Check the corresponding PLC output signal, relay, and check the line; 2. Clean the shear angle control valve;

### **Malfunction 6:**After the material can not move or move slowly

Reason:

1.The control part of the gas valve fails, and the corresponding PLC output point and relay fail;

2. The gas valve is stuck, mainly related to the gas source;

3. The air pressure is too small;

4. The throttle valve is too small;

5. The internal lock nut of the cylinder is detached, resulting in failure to move;

Solution:

1. Check the corresponding PLC output signal, relay, and check the line;

2. Check the cleaning air valve, check the cleanliness of the air source, and check whether there is oil in the oil water separator tank;

3. Check if the air pressure reaches 0.4MPa;

4. Check if the throttle valve on the cylinder is too small;

5. Check the cylinder;

### **Malfunction 7:**The slider is heavily tilted

Reason:

1.The main cylinder is at the lowest position, the sub-cylinder is at the highest position, and is related to the linear potentiometer signal;

2.The main cylinder is at the highest position, the sub-cylinder is at the lowest position, and is related to the linear potentiometer signal;

3. The main cylinder is at the lowest position, The auxiliary cylinder is in the normal position and leaks in the main cylinder;

Solution:

1. Check the linear potentiometer and signal. After confirming the normal condition, use the iron piece to approach the top dead center proximity switch to make it move, then start the oil pump. Adjust the interface manually in the system to make the shear angle to the minimum and remove the iron piece. The machine will return to normal state, test the machine and confirm again;

2. Check the linear potentiometer and signal, confirm it is normal, start the oil pump, adjust the interface manually in the system, adjust the shear angle to about 1 °, the machine will return to normal state, Test the machine and confirm again;

3. Remove the main cylinder, check the damaged part and degree of the main cylinder, and then decide whether to change the seal or the cylinder, and analyze the cause to check the pollution degree of the oil;

### **Malfunction 8:**Slider slides automatically

Reason:

1. The back pressure valve, the throttle stop valve, and the hydraulic control check valve are stuck or damaged;

2. The back pressure regulation is too small;

3. Leakage in the auxiliary cylinder;

Solution:

1. Clean back pressure valve, throttle stop valve and hydraulic control check valve one by one. If cleaning is invalid, it needs to be replaced;

2. Re-adjust the back pressure valve pressure according to the standard;

3. Check the damaged part and degree of the cylinder, and then decide whether to change the seal or the cylinder, and analyze the cause to check the pollution degree of the oil;

### **Malfunction 9:**The slider is at the lowest position, the slider cannot automatically return after the oil pump is started.

Reason:

1. The throttle stop valve is in an open state;

2. No main pressure;

Solution:

1.Check the state of the throttle stop valve;

2. Check the main pressure and analyze the reasons;

### **Malfunction 10:**Sometimes the main motor stops automatically, thermal relay, circuit breaker protection

Reason:

1.The proportional pressure valve and the main pressure reducing valve are stuck, the machine tool is always in the pressurized state;

2.The filter element is clogged, the oil is not smooth, the oil pump pressure is always high; 3. The oil usage time is too long, it is polluted;

4. The quality of the oil is too bad;

5. Circuit breaker, heat relay problem, can not reach the rated current action;

6. Control proportional pressure valve PLC output point, relay failure, malfunction, so that the proportional pressure valve has been working;

Solution:

1.Cleaning proportional pressure valve and main pressure reducing valve;

2. Replace the filter element and check the degree of contamination of the oil;

3. Immediately replace the oil filter;

4. Replace with the recommended oil;

5. Replace the circuit breaker and heat relay;

6. Check the PLC output and related relays;

### **Malfunction 11:**Any valve is stuck

Reason:

1. The oil usage time is too long and it is polluted;

2. The quality of the oil is too bad;

Solution:

1. It is recommended that the customer change the oil on time;

2. Replace the recommended oil;

### **Malfunction 12:**Oil temperature is too high

Reason:

1. The hydraulic part is faulty, such as the filter element is blocked, the oil is contaminated, the quality is deteriorated, etc.

Solution:

1.Check the filter element and oil, and replace if necessary;

### **Malfunction 13:**Clamp oil leakage, skew

Reason:

1. There are two main parts of the oil leakage of the clamp, the upper end surface and the piston sealing ring. The oil leakage on the upper end surface is related to the end surface roughness and installation; the oil leakage of the piston sealing ring is caused by oil contamination, operation and impact;

2. The skew of the clamp is mainly caused by improper operation. For example, the clamp is often biased when shearing, and the sheet material hits the clamp when feeding;

Solution:

1.Check the oil leakage area, check whether the clamp is skewed, whether the piston has a strain or not, and analyze the cause of oil leakage;

2.After the operation to prevent eccentric load, if the workpiece size can only be clamped half of the clamp when cutting, the thickness of the sheet should be found and the other half should be added and then cut, pay attention to not hit the clamp when loading;

### **Malfunction 14:**The sheet is stuck by the upper knife and the clamp

Reason:

1. When the cutting end slider returns, the operator pushes the sheet backwards;

Solution:

1.Disassemble the front protective fence and slowly remove the deformed sheet. When cutting, the slider does not return to the top dead center, and the sheet material must not be pushed backwards;

### **Malfunction 15:**The workpiece burr is too large during processing

Reason:

1. The blade is blunt;

2. The gap is too large;

3. Improper operation;

Solution:

1.Check the degree of wear of the blade edge;

2. Check the gap of the blade edge;

3. Check whether the actual operation and the program are consistent;

### **Malfunction 16:**Poor cutting accuracy

Reason:

1.The dimensions of the two sides are inconsistent, mainly because the tailgate and the lower blade are not parallel;

2. The actual value is inconsistent with the programmed value and can be compensated or corrected on the system;

3. In different positions of the workbench, the shear size is deviated, which is related to the straightness of the tailgate;

4. The cut sheet is not vertical, and the side positioning is not perpendicular to the lower blade;

Solution:

1.Adjust the parallelism between the tailgate and the lower blade;

2. The X-axis reference point can be compensated or corrected in the operation interface;

3. Can adjust the straightness of the tailgate, but be cautious, must be confirmed repeatedly, and must be experienced by experienced people;

4. The positive side positioning and the verticality of the tailgate;

