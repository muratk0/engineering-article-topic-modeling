# Putting Together a Plasma Cutting System

[TARİH: 01.08.2015 The Fabricator]

An overview of the CNC, software, X-Y table, and fume control

By Jim Colt

P

utting together a complete plasma cutting system can be a daunting task. It starts with the machine that generates the plasma stream, a CNC, software, ventilation system, and the X-Y table. The phrase "X-Y table" sounds basic, like a 2-D cutting surface, but it’s much more than that; it includes the motors or drivers that provide coordinated, accurate motions for several torches, either plasma or oxyfuel.

If you were looking for an X-Y table in the early 1990s, you would find just one variety: high-end industrial machines designed for around-the-clock operation in steel service centers, job shops, and OEMs where the focus was on thick steel. The main applications were heavy equipment and barge- and shipbuilding industries. These machines were designed to be robust enough to stand up to decades of severe use and produce thousands of tons of metal parts at high production rates with minimal maintenance. A typical machine had up to four plasma torches or up to 16 oxyfuel torches and could cut plate in sizes from 5 by 10 ft. to 40 by 80 ft.

These days the industry offers no shortage of X-Y table styles. More than 100 manufacturers supply them to handle power levels from 30 to 1,000 amps to cut thicknesses from 26 gauge to 6¼ in. in mild steel, stainless steels, and aluminum. A small shop that doesn’t rely heavily on plasma or oxyfuel cutting can find an affordable, light-duty machine that has corresponding productivity and accuracy, whereas a big shop that uses these processes almost nonstop can find a heavy-duty, robust machine that provides higher productivity and accuracy.

As the styles have multiplied, the prices have dropped. Modern machines use many off-the-shelf electronic components and hardware, which keeps the costs down. Standard, off-the-shelf components include laptop computers, stepper drives, bearings, linear motion ways, gear reduction units, and rack-and-pinion systems. Now the smallest units measure 2 by 2 ft. and cost as little as $3,000. While these low-cost tables are not going to perform as well or last as long as industrial-strength tables, they have opened a lot of doors for small and medium-size shops and even hobbyists.

No matter the cost or size, every CNC-based X-Y table must have the following components:

• CNC.

The brains of the machine, the CNC converts a cutting program into electrical instructions that control the cutting direction and speed. It also issues instructions to the plasma cutter, height controller, and peripheral equipment.

• Mechanical components.

The guts of the machine include a gantry (long axis), a torch carriage, and a Z axis (for up-and-down motion) that manipulate the torches.

• Fume control system.

Plasma cutting generates a lot of fumes and smoke. Every machine requires a downdraft fume control or a water table control.

Automatic height control is an optional feature, but in nearly all cases, it’s well worth the additional investment. Effective plasma cutting relies on three height modes—one for piercing and two for cutting—to maximize consumable life and cut quality.

The pierce height is perhaps the most critical to nozzle life and cut quality. The system advances the torch until it finds the material’s surface, then retracts to the proper height. One pierce too close permanently affects cut edge angularity, dross, and overall edge quality.

After the torch pierces the material, the controller moves the torch closer to the material until it establishes the proper cut height. A torch height that is too low risks a collision with the workpiece, whereas one that is too high increases the kerf width and edge angularity while contributing to dross and warpage. After the cut height controller times out and shuts off, the arc voltage feedback controller takes over to maintain the proper torch-to-workpiece distance.

A properly functioning automatic height control allows you to program and nest hundreds of parts and walk away from the machine while it is cutting. If you are cutting one part at a time and don’t mind babysitting the machine, you can get along without a height control. The downside is that this is cumbersome and slow. You need to adjust the pierce height for every pierce, stop, adjust the cut height, then make the cut. Automatic height control is the key feature that makes these machines automated, and the additional investment usually pays for itself in short order.

CNC

A CNC is essentially an industrial-grade computer with internal motion- and machine-control software and a variety of inputs and outputs that can control all of the drive motors, plasma cutters, height controllers, and any other tools or peripherals mounted to the X-Y table.

It takes orders from the machine operator and the CAM software, then converts these orders to instructions that execute arc starts, control the drive systems, and carry out other machine functions.

Industrial CNCs are designed to withstand the harsh shop environment, which adds to their cost and complexity. They have to endure smoke and airborne debris from cutting and welding processes, vibrations from forklifts and other machines, interference from other electrical devices, and so on.

On low-cost machines, a personal computer or laptop is the brain of the CNC. These computers were designed for a relatively easy life in a clean, controlled office environment. They don’t have all of the protections of an industrial CNC, but they do have the capability to run plasma cutting machines that don’t have all of the bells and whistles. These machines are well-suited to hobbyists; prototyping shops; and small, low-production shops.

Personal computers or laptops should be used only on machines that have blowback torch starting technology rather than high-frequency, high-voltage, or capacitive starting. Blowback starting produces less electrical noise and therefore is less likely to cause electrical interference.

The human-machine interface plays a big role in the machine’s productivity. While many basic machines use a standard office keyboard and mouse to control functionality, the higher-end machines have touchscreen controls, which tend to be more intuitive. The operating software is a related concern. Many programs are adapted from machining processes such as routing and milling and are rather clunky when used for cutting. Software and human interfaces that were designed specifically for plasma cutting tend to be much easier to learn and to use.

Mechanical Components

Every machine has quite a few moving parts: gantry, torch carriage, and torch height control (X, Y, and Z axis). On large industrial machines, all of the components are robust, heavy-duty, and precise. On entry-level machines, the components aren’t as sturdy, which means they aren’t as heavy. Using lightweight components allows the machine builder to use less powerful drive motors and lighter-weight gearing systems, which keeps the cost down while still providing productive cutting speeds and reasonable accuracy.

Lighter-duty machines tend to use stepper motors, whereas the more robust machines usually have servo drives. Both provide very good precision, although modern, properly sized servo drives usually have a wider speed and torque range, which is beneficial when cutting at very fast and very slow speeds.

Steppers and the associated drive electronics are simpler and less expensive than servo systems, and so are often used on machines controlled by PCs or laptops. Servos can be more intuitive for machine operators as they use encoder feedback to the CNC, providing less likelihood of lost positioning on the cutting table in the event of a collision with a tipped-up part, a power failure, or other cutting interruption.

Fume Control

Plasma cutting generates particulate in various sizes. The smallest particles, which come from mill scale and rust preventives, are so small and hot that they are lighter than air and turn into smoke. The largest particles come from the material being cut and usually are heavier than air. Regardless of the power level or type of plasma cutter, the fume control system has to capture particles of all sizes. The two types used for plasma cutting are downdraft tables and water systems.

Downdraft Tables.

These tables require a flow rate powerful enough to move the heaviest particles through a duct. Matching the system’s airflow to the table size is the first criteria. A 2- by 2-ft. table needs about 1,000 cubic feet per minute (CFM) to remove all of the debris and smoke. A 4 by 4 table needs about 3,500 CFM, and a 4 by 8 table needs about 7,000 CFM.

If the local air control ordinances allow venting the fumes outside the building, a downdraft table is the easiest way to go; however, keep in mind that during cold-weather months, the system will remove heat from the building as well. A cold air makeup duct placed near the table uses outside air rather than the shop’s ambient air to vent the fumes. Some large downdraft tables use zoned sections with movable louvers so that the suction removes air only in the localized area where the torch is cutting, not from the entire table. Of course, many downdraft tables have large, self-cleaning filtration systems that remove the particulate before circulating the air back to the shop.

Each option requires careful consideration. Air makeup, zoned, and filtration systems add cost and complexity.

Water Tables.

Water systems are available in two types, water trays and water tables. A water tray sits beneath the workpiece. The water touches the material and the pressure generated by the plasma jet forces the particles into the water where they cool and sink. Water trays are simple, effective, and inexpensive.

A water table is usually deeper than a water tray and allows underwater cutting. Cutting underwater has some advantages, particularly for cutting stainless steel and when the current exceeds 200 amps. The water level can be adjusted: it can be low enough so that the water doesn’t splash onto the metal, yet still high enough to trap most of the fumes.

Allowing water to contact the material does have a couple of drawbacks, affecting edge quality in terms of roughness and dross as the melted metal solidifies along the bottom of the cut edge. However, its cooling effect helps to control warpage that occurs, especially on long, thin parts.

This isn’t to say that one type is better at fume control than the other. Whether it’s a downdraft table, water tray, or water table, a properly designed and sized system can be sufficiently effective at fume control.

CAD and CAM

CAD and CAM software packages have become indispensable to the manufacturing industry. CAD is used to design the part, whereas CAM deals with the machine’s capability to make the part. CAM determines the pierce location, lead-in, kerf width, and lead-out so they have minimal effect on the part. This information goes to the CNC to make the part.

Modern CAM programs often have additional capabilities, such as part nesting. Finding the optimum part location and orientation minimizes material waste, and many programs generate reports that detail part cost, material utilization, and other accounting information. Some CAM systems automatically set and control most of the cutting parameters, such as arc current and voltage, gas flow, pierce height, cut speed, and cut height.

On some basic machines, the CAD and CAM functions are combined, allowing a seamless transition from designing to cutting. This is usually less complicated and easier to learn than using two separate software packages.

Jim Colt is applications technology manager for Hypertherm Inc., 21 Great Hollow Road, Hanover, NH 03755, 603-643-3441,

www.hypertherm.com

.