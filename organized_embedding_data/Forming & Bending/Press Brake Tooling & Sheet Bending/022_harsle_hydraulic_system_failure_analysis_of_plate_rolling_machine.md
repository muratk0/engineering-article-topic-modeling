# Hydraulic System Failure Analysis of Plate Rolling Machine

In my experience working with plate rolling machines, I have encountered various challenges, particularly regarding hydraulic system failure. The hydraulic system is crucial for the machine's operation, and any failure can lead to significant downtime and costly repairs. Understanding the causes and implications of hydraulic system failure is essential for maintaining efficiency and productivity in manufacturing processes. In this article, I will share insights from my analysis of hydraulic system failures, discussing common issues, preventive measures, and solutions to ensure optimal performance in plate rolling operations.

The plate rolling machine is a general-purpose forming equipment that bends and rolls metal plates into cylinders, cones, curved surfaces or other shapes, and is widely used in petroleum, chemical, machinery manufacturing and other fields.

## Working principle of hydraulic system
The **40 × 4000 symmetrical upward adjustment three-roll plate rolling machine** is designed for bending steel plates with thicknesses ranging from 16 mm to 40 mm at room temperature. It consists of several key components, including the main transmission mechanism, upper roller lifting mechanism, support and movable bearings, pressing device, braking device, and other supporting systems. The machine operates on the principle of three rollers applying pressure to the steel plate, which causes the material to bend and form into the desired cylindrical shape. This makes it highly efficient for manufacturing large and precise rolled components.

During operation, the rolled cylindrical workpiece can be easily removed from the inverted end of the machine. The process involves tilting the movable bearing at the discharge end away from the upper roller. At the same time, a hydraulic cylinder pressure block installed at the upper end of the roller presses downward, creating a slight upward tilt at the discharge side of the upper roller. This controlled adjustment ensures that the finished workpiece can be smoothly released and discharged without deformation. Such a mechanism enhances reliability, improves productivity, and ensures stable performance for continuous metal forming operations.

The hydraulic system of the three-roller rolling machine (as Figure 1) has two oil cylinders, A and B, which are controlled by two electromagnetic directional valves. A cylinder controls the lifting of the movable bracket, and B cylinder lifts and presses the upper roller to make the unloading work smoothly.

The operation sequence of the hydraulic system begins with pressing the **start button**, which activates the motor and drives the hydraulic pump into operation. When the three electromagnetic directional valves are set in their intermediate positions, the system enters a pressure relief state. This design effectively reduces power consumption, as the hydraulic system does not continuously maintain pressure when no specific action is required. This initial step ensures energy efficiency and protects the system components from unnecessary wear, creating a stable foundation for the upcoming machine operations.

Next, the operator presses **solenoid valve 6** and **solenoid valve 4** at the low-pressure end. This action activates **cylinder A**, causing the movable bracket to descend steadily. As cylinder A lowers the bracket to approximately **85 degrees**, it encounters the stroke limit switch. At this moment, **solenoid valve 9** and **solenoid valve 4** (reversing to the high-pressure end) are engaged, which activates **cylinder B**. Cylinder B then presses the trailing end of the upper roller. Once the roller tilts to about **3 degrees**, it reaches the limit switch, the operation stops, and the workpiece is successfully discharged.

After unloading is completed, the process continues by pressing the **reply button**. This command causes **cylinder B** to retract, restoring the upper roller back into a horizontal position, confirmed by the limit switch. Following this, **cylinder A** moves the bracket upward, guiding it back into its original position and aligning it precisely with the **upper roller cone sleeve**. At this stage, the entire hydraulic sequence has been completed. The system is now reset, fully stable, and prepared for the next cycle of operation, ensuring efficiency and reliability.

## Failure analysis and treatment of hydraulic system
During the one-time use of this hydraulic system, the A cylinder appears to be able to rise and sometimes cannot rise, and can not stop at any position, it will automatically fall down, and the B cylinder will occasionally move.The general hydraulic system is composed of filter elements, pipelines and various pumps and valves. The hydraulic pump provides pressure, and the overflow valve prevents the system pressure from being too high and can unload in time.

The reversing valve controls the expansion and contraction of the hydraulic cylinder by controlling the flow direction of the hydraulic cylinder oil. The throttle valve controls the speed of the hydraulic cylinder oil. The hydraulic components involved in the hydraulic system include a hydraulic pump, an overflow valve, a three-position four-way directional valve, a one-way throttle valve, a hydraulically controlled one-way valve, a hydraulic cylinder, and other accessories.

The **hydraulic control check valve** is a specialized valve that allows fluid to circulate in reverse when controlled by pressure. Unlike a standard check valve, it is equipped with an additional control oil circuit. When this control circuit is not supplied with pressure oil, the valve functions as a normal check valve—fluid can only flow from the inlet to the outlet, preventing reverse flow. However, when the control oil circuit is pressurized, the piston rod is pushed by the pressure, opening the valve and connecting the inlet and outlet. In this condition, reverse flow becomes possible.

The failures of the hydraulic system are analyzed as follows:

(1) Analyze cylinder B. In the absence of pressure, the problems of relief valves, pumps, and cylinder seals were considered.

① Check the spool of the relief valve, there are traces of scratches. So the new overflow valve was replaced, but the fault was not eliminated.

② Test the quality of the pump. Plug the end of the cylinder head of B cylinder, the pressure can reach the full scale, indicating that the gear pump has no faults.

③ Remove the B cylinder. After removing cylinder B, it was found that the piston rod seal was completely broken. After replacing the new seal, cylinder B worked normally.

(2) Analysis of cylinder A. Consider hydraulic control check valve and A cylinder seal.

① Check the hydraulic control check valve, the valve core has flaws. After grinding, the hydraulic control check valve was reinstalled, but cylinder A still could not be raised, and the fault was not eliminated.

② Disassemble the front-end pipe joint of the hydraulic control check valve, and it is found that no hydraulic oil flows out at all. In the working state, push the spool of the electromagnetic directional valve with a screwdriver, and hydraulic oil flows out of the pipe head, indicating that the electromagnetic directional valve 6 is faulty. After replacing the new valve, cylinder A can work, but there is still the case that it will not be sealed halfway.

③ Replace A cylinder seal, the hydraulic system is normal.

## Conclusion
With the continuous improvement of electromechanical integration and equipment automation, hydraulic drives rely on the advantages of simple structure, small size, large output power, stepless speed regulation, easy to realize frequent commutation and easy to realize automation. It is widely used in machinery, aviation industry and other fields. Therefore, engineering and technical personnel must master the performance of hydraulic components and learn to analyze and eliminate the faults of the hydraulic system to better serve the enterprise.

