# PC-based automated welding system nearly triples boiler manufacturer’s production speed

[TARİH: 01.01.2024 The Fabricator]

Applications

Situation

Dean Jacobs can describe the world of welding equipment in two words: bolt on.

"People bolt on this subsystem here, bolt on that one there," explained the principal automation engineer at LJ Welding Automation. "Soon, your welding cell has seven control panels and needs a massive power bar to feed them all."

The bolt-on approach was born of necessity. However, as technologies advance and equipment end users demand more modularity, the design and maintenance of such systems has become unsustainable.

LJ Welding Automation recognized early on that an integrated approach not only provides a cleaner look, but also a key differentiator for machines in a bolt-on world. The Edmonton, Alta., manufacturer of submerged arc welding manipulators has customers in more than 50 countries in the oil and gas, alternative energy, aerospace, transportation, infrastructure, and health care industries.

When the company introduced its Pipe Titan system, optimized for welding 2- to 24-in.-dia. pipe, one of the first customers to acquire one was the Cleaver-Brooks facility in Stratford, Ont. The manufacturer of packaged firetube and watertube boilers had several requirements for the machine, including reducing costs, improving quality, increasing productivity, and enhancing safety. In addition, the LJ Welding Automation engineering team needed to maintain a clean design with highly deterministic control and system modularity for changing production processes.

Resolution

As he has done before, Jacobs turned to Beckhoff Automation to meet the project’s challenges. EtherCAT and PC-based control technologies from Beckhoff helped consolidate functionality into a centralized control architecture and provide a flexible, fully integrated system.

The Beckhoff CP6700 economy built-in panel PC, which combines HMI and control CPU in one device, is Pipe Titan’s central machine controller. The pipe welding system has two separate positioners, each with its own Beckhoff CX series embedded controller.

"You can unplug one positioner, take it to the other side of the plant, and use it. We use this modular architecture on all our larger machines, Jacobs said."

TwinCAT 3 automation software from Beckhoff enables this architecture as an end-to-end engineering and run-time environment. Rather than the bolt-on approach, the software platform combines functionality for everything from PLC, HMI, and motion control to IoT, analytics, and even machine learning.

LJ Welding Automation uses Structured Text, JavaScript for HMI development, and other programming languages as necessary. TwinCAT helps the engineering team consolidate to a single tool chain to avoid switching among development environments. It also provides the team with advanced source control options to prevent confusion from and space requirements for unnecessary copies of projects with different dates.

The Pipe Titan implementation at Cleaver-Brooks needed to optimize costs, part quality, productivity, and safety through automated welding.

Images: Beckhoff

A Beckhoff CP6700 Panel PC combines the main control CPU with a 10-in. touchscreen for operator interface.

"Also, TwinCAT Library Manager speeds up development by allowing us to add or remove large blocks of code instead of writing it from scratch," explained Benjamin Vandenberg, automation engineering EIT at LJ Welding Automation. For the positioner modules, the Pipe Titan uses EtherCAT Automation Protocol for controller-to-controller communication and safety. The welding system has multiple e-stops across its modules, which communicate via Beckhoff’s TwinSAFE integrated functional safety system. TwinSAFE works over the standard EtherCAT network using a "black channel" approach. As such, it supports modular machine designs without any hard-wired safety controllers to physically adjust.

By leveraging PC-based automation from Beckhoff, the team at LJ Welding Automation implemented a system that surpassed the requirements of Cleaver-Brooks. It reduced arc time by 63% on average, which is nearly three times faster, and led to a 90% reduction in weld cleanup time, 10% reduction in rework, and 39% reduction in filler metal spend.

Using the IPC Security Guideline from Beckhoff, LJ Welding Automation can safely remote into customer machines for maintenance or troubleshooting. But the team isn’t stopping there. The next phase for the Pipe Titan and other LJ Welding Automation machines is higher-level connectivity for analytics and continuous improvement. With TwinCAT, standard analytics algorithms, no-code dashboards, and secure connectivity via OPC UA are built in.

BECKHOFF AUTOMATION LLC,

WWW.BECKHOFF.COM

LJ WELDING AUTOMATION,

WWW.LJWELDING.COM

SLAG REMOVAL, DEBURRING AND EDGE ROUNDING

OF THICK PARTS

High performance machine for plasma and oxy-fuel cut parts

Up to 6 mm warped parts and tolerance compensation

Reduction of dust and noise

Two-sided deburring - no turing of heavy parts needed

sales@lissmac-corporation.com

getthelissmacedge.com

17 Route 146 Mechanicvilfe, NY +1 518 326 9094