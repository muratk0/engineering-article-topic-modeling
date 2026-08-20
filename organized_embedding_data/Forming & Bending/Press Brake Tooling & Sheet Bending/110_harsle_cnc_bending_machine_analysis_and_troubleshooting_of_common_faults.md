# CNC Bending Machine Analysis And Troubleshooting of Common Faults

In my experience with CNC bending machines, I have encountered a variety of common faults that can disrupt production and affect the quality of bends. Analyzing these issues and implementing effective troubleshooting techniques has been essential for maintaining optimal machine performance. Over the years, I've developed a systematic approach to diagnosing and resolving these faults, ensuring minimal downtime and consistent output. In this article, I will share insights on the analysis and troubleshooting of common faults in CNC bending machines, providing practical tips that can help operators quickly identify and rectify problems to enhance their bending operations.

## The Noise of the Oil Pump is too Large (the Fever is too Fast) and the Oil Pump is Damaged.
1. Oil pump oil leakage or low tank level cause oil pump suction.

2. Oil temperature is too low, the viscosity of the oil is too large, resulting in large oil absorption resistance.

3. Oil suction filter plugging, oil dirty.

4. Pump damage (injured during pump installation) subjected to any beating.

5. The installation problems of the coupling, such as the axial tightening, the shaft of the motor and the shaft of the oil pump are not concentric.

6. When the pump is installed, it will turn over for a long time without refueling.

7. The outlet high-pressure filter is blocked or the flow rate is not up to the standard.

8. The oil pump is empty (there is oil, but there is air at the suction side of the oil pump).

9. If the plunger pump is probably too low, the height of the return port is too low.

10. If it is a HOEBIGER oil pump, it may be deflated.

11. Oil temperature is too high, resulting in viscosity reduction (less than 60 C).

12. Hydraulic oil contains water, resulting in blockage of high pressure filter element.

## There is no Pressure or Pressure to Build the System.
 1. Oil pump steering error or oil pump damage.

2.Is the pressure gauge damaged?

3. Is there any electrical signal or valve blockage in the pressure control valve?

4. The pressure cartridge valve is blocked and stuck.

5. The filling valve is jammed.

6. The compensation amplifier is too small.

7. The pressure can only reach a certain value. Use direct 24V to determine whether there is a problem with the valve oil pump.

## Slow Construction of Pressure (REXROTH hydraulic system)
 1. The pressure port of the pressure valve X can be blocked up.

2. The cartridge valve at the pressure valve may not act flexibly.

3. Electrical Problem: Test the solenoid pressure valve with 24V voltage directly, or test the solenoid pressure valve spool with something.

4. Is there any blockage in the high pressure filter?

## There Will be Impact Soon.
 1. Impact sound caused by loose rail

2. The position of the grating ruler is not right.

3. The setting time of the delay parameter is too small.

## No Quick Action on the Slider.
 1. Fast down valve with or without electric signal.

2. Electromagnetic proportional directional valve with or without electrical signals or valve spool action, stuck (check feedback voltage)

3. The mechanical part is too tight, for example, the guide plate is too tight and the cylinder is too tight.

4. The filling valve is closed, which can not be opened and thus can not attract oil.

5. Grating ruler problem

6. Foot switch is intact, check wiring.

7. Slow down the valve after power, the filling valve closed, the upper chamber can not suck the oil.

## The Slider Speed Conversion Point has a Long Pause Time.
 1. The upper chamber of the oil tank inhales the air, and the pressure is set up for a long time.

2. The filling valve or self suction pipe has a low flow rate, or the slider is too fast to absorb vacuum.

3. The filling valve is not completely closed, and the upper chamber pressure decreases slowly.

4. Slow down the valve after power, the filling valve closed, the upper chamber can not suck the oil.

5. The wrong position of the proportional valve causes the opening to be different.

6. Will speed down quickly to see if there is any pause in the test.

7. The size of the down pressure has an effect on the closure of the liquid filling valve.

8. The adjustment of pressure parameters during the delay stage before entering work.

9. Filling valve control pipe damping hole is too small, forming pressure difference.

10. CNC system parameters (slow before delay)

11. CNC system parameters (slow down gain parameter decreases)

## No Slow Down Action of the Slider.
 1. Whether the electromagnetic proportional reversing valve has electric signal or whether the spool has action or not.

2. System can't build pressure.

3. The filling valve is stuck, or the sealing ring of the liquid filling valve leaks.

4. Slow down valve with or without electric signal.

5. The back pressure is too high or slow, the pressure is too low.

## When the Slider Slows Down, it Vibrates, Swings and Has Noise.
1. Cylinder pressure, oil contains bubbles.

2. Is there too much friction between the slider rails and lubricants?

3. The gap between the surface of the guide plate is large or uneven.

4. Rack and bench level is not adjusted well.

5. Balancing valve jam.

6. Check whether the valve is energized or not.

7. CNC system parameters (gain) or working speed setting is too large.

8. Back pressure valve loose, both sides of the resistance is not the same.

9. Whether the electromagnetic proportional valve coil is biased or not, and whether the median signal of the proportional valve is correct or not?

10. Whether the signal of proportional servo valve is disturbed or not, and the inspection method is the same as above.

11. Cylinder seal holds the piston rod to a standstill with great resistance (test of replacing rigid PTFE seal ring)

12. The spherical washer on the grating ruler is not installed, the sliding seat is not moving smoothly, and the communication line of the grating ruler is in trouble.

13. Pressure curve is not correct, pressure is not enough when working.

14. The filling valve pressure seal O ring produces a small leak.

## Slow Down Time Synchronization Error.
 1. Synchronous detection system failure (grating ruler)

2. Proportional directional reversing valve

3. Quick release valve leakage

4. There is a big gap between the two sides.

5. Oil temperature is too low.

6. Oil in upper and lower oil cylinders

7. CNC system parameters

## The Slider Oscillates and Jitters at the Lower Dead Center.
1. Grating may have problems.

2. Cylinder pressure, oil contains bubbles.

3. Balancing valve jam

4. CNC system parameters (gain)

5. Back pressure valve, both sides of the resistance is not the same.

6. Electromagnetic proportional valve: the median may not be correct.

7. Cylinder lifting bolt loose lower dead point jitter, the wrong contour, bending angle is not accurate, bending when there is a sound

## The Slider has no Backhaul or Slow Return.
 1. Is there any commutation of electromagnetic proportional reversing valve, whether it is damaged or not?

2. Whether the system has built up pressure or the return pressure is too small.

3. It may be jammed or not fully opened on one side.

4. When the slow valve is energized, the filling valve is closed, and the return valve can not be quickly returned.

5. NC system: the programming angle is too small to reach the dead point of bending programming.

6. NC system parameter zero adjustment

7. Grating ruler damage or wiring problem

8. Check whether the system pressure is built slowly.

## Vibration and Jitter When Slider Returns.
 1. The return pressure is too high or too low.

2. System parameters or PLC and DM02 modules

3. Is there any deflection of proportional valve coil?

## Slider Slide (Top Dead Center)

1. Back pressure valve adjustment

2. Back pressure valve leaks or leaks quickly.

3. Oil in upper and lower oil cylinders

4. Proportional valve offset

5. The support stability of the sealing ring is not enough. After deformation, the slider slipped.

6. Determine the cause of the slide.

## Bending Angle Error is Large.
 1. Check whether compensation cylinder deflection is large, can not fully restore zero.

2. Check whether the quick clamping is loose.

3. Check whether there is any change in the dead point under each bending.

4. Check whether the installation of the bow spanner is standard, and whether the screw hole is dead or not.

5. The change of sheet itself (thickness, material, stress)

6. Is there any loosening of grating ruler?

7. Inaccurate positioning accuracy: proportional valve zero offset value is appropriate, positioning can not reach the bottom dead point so that can not return.

## Fifteen. The Bending Error is Large.
 1. Check whether the compensation cylinder is suitable for compensating deflection.

2. Check whether the quick clamping is loose.

3. Check the deformation of the horizontal and vertical die surface on the slide.

4. Check whether the upper and lower die deformation.

5. The change of sheet itself (thickness, material, stress)

6. Check whether the worktable (neutral plate) is deformed.

## Leakage of Hydraulic Line or Tubing Failure.
 1. Check whether the tubing installation meets the requirements (extension length, pipe diameter, wall thickness, jacket, nut too tight, too loose, bending radius, etc.)

2. Is there any impact or vibration on the tubing?

3. Check whether the pipeline is in collision with other interference.

4. There is no pipe clamp.

## Matters Needing Attention in The Installation and Maintenance of Hydraulic System:
 1. The valves sealed by paints must not be dismantled on their own, and must not be adjusted.

2. After the valve is cleaned, it will work normally. The new oil must be replaced immediately and the oil tank should be cleaned.

3. Oil pump installation shall not be subjected to any percussion and impact.

4. When the valve is installed, it can only carry its valve body and must not touch any solenoid valve.

## Common Fault Analysis of Rear Stopper
 1. The rear stopper can not move: (1) check whether the driver has an alarm or not.

Check all shaft limit switches.

Check the reliability of connectors.

2. Drive alarm

3. X and R axes are unstable and jitter.

4. Change of positioning accuracy: (1) mechanical problems (whether loose or impacted)

Electrical to unidirectional location

Parameter adjustment

5. Loosening of the tightening wheel and loosening of screw connection screws

6. Overload alarm: can the ball screw be easily rotated or damaged?

7. R axis drive 16 alarm to gas spring bad.

8. Z1, Z2 axis 22 alarm to replace the encoder cable.

9. alarm No. 38, loose connection.

10. Servo motor noise: gain setting is too large.

