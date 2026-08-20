# Top CNC Bending Machine Methods and Precautions Guide

As someone experienced in metal fabrication, I know how crucial it is to understand the various methods and precautions for using a CNC bending machine. In this guide, I'll share the top techniques for achieving accurate bends, along with important safety measures to keep in mind. Whether you're a seasoned professional or new to CNC operations, mastering these methods will help you improve efficiency and prevent costly mistakes. This guide covers everything you need to know to optimize your CNC bending machine usage for top-notch results.

CNC press brake bending of the plate in a variety of ways, for the principle of different and many ways of classification. This article specifically from the bending process when the relative position of the upper and lower die and bending into the shape of the different details of several common bending methods, and details of the bending process and precautions.

## Table of Contents

- ● Gap Bending
- ● Press Bottom Bending
- ● L-fold
- ● N-fold
- ● Z-fold
- ● Reverse Bending And Flattening
- ● Pressing Hardware

First of all, according to the different relative positions of the upper and lower molds when bending processing, bending processing is divided into two forms of gap bending and bottom bending, the characteristics and differences between the two are as follows.

### ● Gap Bending
CNC bending machine in the bending process between the upper and lower die is not pressed, by adjusting the depth of the upper die into the lower die opening to get the required bending angle, this bending method is called gap bending, the deeper the upper die into the lower die, the smaller the bending angle; vice versa, the larger. Due to the elasticity of the material bending also need to consider the use of overbending to control the amount of rebound.

The advantage of gap bending is that a smaller number of dies can be used to achieve a variety of angles of the forming process, and the required processing pressure is small. Usually, to obtain the best bending effect, the ratio of the material thickness B to the width V of the lower die V-shaped opening can be selected as follows.

1. material thickness below 12.7mm, B: V is 1: 8.

2. When the material thickness is 12.7~22.2mm, B:V is 1:10.

3. When the thickness of the material is above 22.2mm, B:V is 1:12.

The above three ratios are standard tooling ratio, the material is low carbon steel, material strength of 43.4kg/mm2. in the preparation of bending processing program, the above parameters can be set in the CNC system, the system automatically processed to generate the processing program.

### ● Press Bottom Bending
CNC bending machine using press bottom bending plate is pressed between the upper and lower die, so as to obtain the required bending angle and elbow radius. CNC bending machine bottom bending is suitable for processing sheet metal with a thickness of 2mm or less in the production of medium and large batches. Its bending bending radius is small – high bending accuracy – good precision. It should be noted that the working pressure of bottom bending is greater than the working pressure of gap bending, generally in three times more.

The angle of the bottom bending mold should be adapted to the plate angle and material. Usually in the bottom bending mild steel, the angle of the upper and lower die should be consistent with the required angle of the plate. The use of bottom bending method of processing, mold ratio that is the thickness of the plate material B and the lower die opening distance V ratio of B: V = 1: 6.

Determine the work tonnage bending process, the upper and lower die between the force applied to the material, so that the material plastic deformation. The working tonnage is the bending pressure during bending. Determine the working tonnage of the influencing factors are: bending radius, bending mode, mold ratio, elbow length, the thickness and strength of the bending material. Usually work tonnage can be selected according to the following table and set in the processing parameters.

1. The table value for the sheet length of one meter when the bending pressure: Example: S = 4mm L = 1000mm V = 32mm Check the table to get P = 330kN

2. This table is calculated on the basis of the strength σb = 450N/mm2 material, in bending other different materials, bending pressure for the data in the table and the product of the following coefficients: bronze (soft): 0.5; stainless steel: 1.5; aluminum (soft): 0.5; chromium-molybdenum steel: 2.0.

3. CNC bending machine bending pressure approximation formula: P = 650s2L/1000v where the unit of each parameter P – kN, S – mm, L – mm , V – mm.

According to the different shapes formed after the bending process, the bending process is divided into L-fold, N-fold, Z-fold, reverse-fold flattening, pressed hardware and other forms, the characteristics and differences are as follows.

### ● L-fold
According to the angle is divided into 90˚fold and non-90˚fold. According to the processing is divided into general processing (L>V/2) and special processing (L<V/2).

1. The mold is selected according to the material, plate thickness and forming angle.

2. Principle of leaning position.

①Two post-definition gauges are used as the principle, and the workpiece shape is used for positioning.

②A post-definition gauge against the position, pay attention to the skew, and require the workpiece bending size in the same center online.

③Small bending bending, anti-bending processing is better.

④To rely on the middle of the back of the fixed gauge down is better. (Leaning position after the fixed gauge is not easy to warp)

⑤Leaning side to close to the back of the fixed gauge is better.

⑥The long side is better.

⑦To use the jig to assist in positioning (beveled edge irregular positioning).

3. Note: Pay attention to the processing method and the movement of the back gauge in various processing methods. Bending when the mold is mounted, the back gauge should be pulled back to prevent the workpiece from being deformed during bending. Large workpiece internal bending, because the workpiece shape is larger, and the bending area is smaller, so that the tool and bending area is difficult to overlap, resulting in difficult positioning of the workpiece, or bending workpiece damage. In order to avoid the above, a positioning point can be added in the longitudinal direction of processing, so that the two directions of positioning processing, so as to facilitate processing positioning, and improve processing safety, to avoid damage to the workpiece, improve production efficiency.

### ● N-fold
N-fold to use different processing methods depending on the shape. When bending, the material size should be greater than 4mm and the size of the X dimension is limited by the shape of the mold. If the size of the material is less than 4mm, special methods are used to process.

1. According to the material thickness, size, material and bending angle to select the mold.

2. Positioning principle: to ensure that the workpiece does not interfere with the tool

①Ensure that the angle of leaning is slightly less than 90 degrees.

②The best use of the two post-determination gauge against the position, except in special circumstances.

3. Notes.

①After bending L-fold, the angle should be guaranteed at 90 degrees or slightly less than 90 degrees to facilitate the processing of leaning position.

②When processing the second fold, it is required to lean against the position of the processing surface as the center to lean against.

### ● Z-fold
Z fold is also called segment difference, that is, a positive and negative bending. According to the angle is divided into beveled edge segment difference and straight edge segment difference. The minimum size of the bending process is limited by the processing tooling, the maximum processing size is determined by the shape of the processing machine. In general, Z-fold material size less than 3.5T, the use of segment difference die processing. When it is larger than 3.5T, the normal processing method is used.

1. Leaning principle.

①Convenient to lean against and good stability.

②General leaning is the same as L-folding.

③Secondary leaning is required to process the workpiece and the lower die flat.

2. Precautions.

①The processing angle of L-fold must be in place, generally required at 89.5~90 degrees.

②When the post-definition gauge is to be pulled back, attention should be paid to the deformation of the workpiece.

③The sequence of processing must be correct.

④For special processing, the following methods can be used: centerline separation method (eccentric processing), small V processing (need to increase the bending coefficient), easy die forming, repairing the lower die.

### ● Reverse Bending And Flattening
Reflexive flattening, also known as dead edge, dead edge processing steps are: first bending insert depth to about 35 degrees, and then flattened with the flattening die until the flattening and tightening.

1.Mode selection: choose 30 degrees of insert depth according to 5 – 6 times the material thickness, the width of the V groove of the lower die, according to the specific situation of the processing of the dead edge to choose the upper die.

2.Note: The dead edge should pay attention to the parallelism of the two sides, when the dead edge processing size is long, the flattened edge can be folded first after a warped angle flattened. For the shorter dead edge, can use the pad processing.

### ● Pressing Hardware
The use of folding machine press dovetail hardware, generally to use concave mold, jig and other auxiliary mold processing. In general, there are: press nuts, press studs, press screws and some other hardware.

1. Notes.

①When the shape of the workpiece needs to avoid processing, it should be taken to avoid the position.

②After processing to test the torque, thrust is up to standard and hardware and workpiece is flat and tight.

③Pressing diao after bending, to be pressed next to the machine tool, we should pay attention to the processing avoidance and parallelism of the mold.

④If it is expanding diao, we should also pay attention to the expansion diao side can not have cracks and the expansion diao side can not be higher than the surface of the workpiece.

