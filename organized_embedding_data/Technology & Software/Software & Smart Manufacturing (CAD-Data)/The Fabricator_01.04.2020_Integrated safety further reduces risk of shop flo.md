# Integrated safety further reduces risk of shop floor injuries

[TARİH: 01.04.2020 The Fabricator]

Using the same software, fieldbus, and hardware for safety as machine control offers a way to increase safety technology in machines

By Sree Swarna Grutta

Integrated safety systems allow metalworking and fabrication shops to put more safety technology in more places while simplifying the overall machine control architecture.

T

he high performance of metalworking tools, from plasma cutting to tube bending technologies, enables incredible possibilities but can also pose serious risks. The speed and force of press brakes, for example, make split seconds count more than in other industries. So, although safety is always an integral part of any machine’s design, it can seem even more crucial in metal fabrication.

Insufficient safety systems and policies both increase the potential for severe injuries or fatalities. However, to safeguard applications as well as possible, it is important to integrate intuitive machine safety technologies that also simplify the system architecture.

Integrated functional safety systems provide a way to enhance safe applications without adding unnecessary complexity. With integrated safety, the standard e-stops, safety mats, latches, two-hand controllers, and light curtains used in today’s metalworking shops all operate on the same network and machine controller as the general automation and control elements. This improves the reaction times and increases the data available for troubleshooting, while reducing component costs and commissioning times through the convergence of two previously separate programming architectures.

Streamlining of safety systems is possible with control system-integrated options for software, fieldbus communication, and safety hardware from I/O terminals to safe drive technologies. Through these technologies, fab shop managers and engineers can design more comprehensive safety systems, physical barriers, and policies. When implemented and followed properly, this can prevent many workplace injuries and help to safeguard companies’ most important and irreplaceable assets: their employees.

What Is Integrated Safety?

Integrated safety systems are the logical next step beyond traditional safety systems that are essentially relays and operate as stand-alone black boxes. Integrated options provide programmable safety using the same engineering environment, network, and form factor as standard machine controls. As a result, the safety components do not require the excessive time, space, and expense of hard-wiring between each device and point-to-point programming. In addition, PC- and EtherCAT-based control technology makes high scalability and flexibility possible in such architectures.

The benefits of integrated safety include reduced material costs and commissioning time while maintaining the necessary safety integrity level (SIL) rating in the application. More importantly, the amount of safety technology increases throughout the machines within the same footprint, further preventing accidents and injuries caused by malfunctioning or improperly used equipment. Of course, individuals who are determined to deliberately bypass safety policies and technologies can still pose a risk to themselves and others. Therefore, commonsense operation policies and installation of physical barriers play important roles as well. But functional safety integrated directly into standard networks, software, and hardware enables easier design and implementation of a comprehensive system.

Safe Communication Over Standard Industrial Ethernet

With integrated safety, the fab shop’s existing Ether-CAT industrial Ethernet network can transmit safety data on the same cable as standard machine control data using Safety over EtherCAT (FSoE). Approved by the EtherCAT Technology Group and certified by TÜV, FSoE meets all IEC 61508 and SIL 3 requirements by transmitting safety data using a "black channel" with all necessary redundancies. Combining safe and nonsafe information on one network without transfer speed and cycle time limitations improves the reaction time and increases available diagnostic information. Greater access to the diagnostics reduces downtime by helping engineers troubleshoot any damaged cables and connectors, faults in specific I/O terminals, or other physical issues. EtherCAT can precisely localize the exact point of potential faults or line breaks.

Some safe I/O terminals, including the Beckhoff TwinSAFE modules, incorporate safety logic at the device level rather than requiring a separate, stand-alone safety PLC.

Integrated safety technology can extend beyond I/O terminals to include safety logic directly inside servo drives and other components in the field.

Fieldbus-neutral FSoE works over real-time EtherCAT I/O systems, which can directly connect legacy DeviceNet, PROFIBUS, and CANopen fieldbuses, plus EtherNet/IP and PROFINET industrial Ethernet protocols with the addition of corresponding EtherCAT I/O gateway devices. Most operations have equipment on heterogeneous networks, increasing the value of FSoE as a standard safety protocol. As a result, FSoE can provide safe communication over EtherCAT for a light curtain around a waterjet cutter, for example, and just as easily do the same for a safety gate in front of an older press brake by networking EtherCAT I/O to a legacy fieldbus.

Harness Universal Programming and Control

Integrating safety technology into a universal platform makes training easier for engineers and programmers to successfully create robust safety applications without having to learn numerous systems. Flexible and scalable software enables the programming of safety projects in the same engineering environment used to program PLC, motion control, HMI, and IoT functionality. The graphical editors in the same platform enable intuitive programming with TÜV-certified function blocks and customized, user-defined function blocks created by a company’s engineering staff. This provides significant flexibility to tailor the safety system to best fit a specific metalworking machine.

Because improper use of metalworking, forming, and fabricating machinery can put operators at significant risk, the software should be able to restrict editing of the safety program to only authorized programmers to prevent accidental or unauthorized alterations. For authorized users, though, the software should not create barriers. The editing function in today’s integrated safety systems, for example, supports easy reuse of the same safety program in additional applications without having to rewrite the code entirely from scratch. Safety programs can be used as is or configured as needed to suit different machines and applications. In addition, engineers can transfer projects to the safety controller using only built-in loader tools to make changes at the software level without having to adjust hardware or wiring between safety devices, such as e-stops, and the safety controllers.

Safe Hardware in All the Right Form Factors

The idea of system integration extends to hardware. Many different devices in various form factors now contain programmable safety logic onboard, accommodating nearly every machine architecture. Rather than just looking for a yellow or red housing, engineers should select safety components for their flexibility and scalability. For example, safety systems should support both standard digital and analog safety options. These analog options extend the benefits of integrated safety to process applications through speed and temperature monitoring, among other tasks.

Safety I/O modules should be available in a variety of form factors. IP20 versions for control cabinet installation should connect directly into the same segment with nonsafety I/O and PC-based machine controllers, so that all these can communicate via a shared network. In distributed architectures, the safety modules communicate back to the controller via a standard Ethernet cable and a bus coupler. This design also works for IP67 I/O boxes that mount directly onto machines and robots. Having flexible options for each unique application reduces commissioning times by eliminating cumbersome requirements for hardwired controllers and allows more safety technology in more places.

Applications with a significant level of motion control, such as CNC plasma cutters, benefit from safe technologies, such as servo drives and servomotors with integrated safety technology. Built-in Safe Stop 1 (SS1) and Safe Torque Off (STO) functionality, along with the option to easily incorporate additional safety options via software and I/O extensions, aids in safe machine designs. For example, if a horizontal axis moves outside of the defined speed or increment parameters, drives connected to the integrated safety system can cut all torque to the motors and return the axes to a safe state. These capabilities and the range of safety hardware on one platform can help to simplify designs.

Integrating Safety Into Policies and Training

Simplicity is a key to ensuring engineers and operators have a thorough understanding of any machine. This leads to better implementation of physical safety barriers, programmable safety devices, and employee policies. The first step is assessing the necessary safety level based on how grave the injury to an operator could potentially be. The next step is implementing the necessary technologies to prevent it.

With press brake applications, for example, light curtains or safety gates, along with external safety-rated locking devices, are recommended in addition to an integrated programmable safety platform to make a complete system. Simplified commissioning, greater performance and diagnostic data, and faster communication speeds in one platform are all important ways to elevate and strengthen safety system design.

Sree Swarna Gutta is I/O product manager—USA, Beckhoff Automation, 13130 Dakota Ave., Savage, MN 55378, 952-890-000,

www.beckhoff.com/twinsafe

.