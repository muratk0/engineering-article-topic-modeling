# Robots on the move

[TARİH: 01.01.2022 The Fabricator]

Cover Feature

Flexible mobile robots reach the sheet metal shop

By

Tim Heston

Flexible mobile robots can be moved with pallet jacks, fork trucks, or automated guided vehicles with forks. After docking, the orange vertical arm, which has a safety area scanner on the end, is folded down and extended. An identical arm is mounted behind the robot.

OpiFlex and SICK

A

t a laboratory in the University of Skövde, a small city in south-central Sweden, Anna Syberfeldt spoke and gestured to a nearby robot. The robot did as she told, carrying an object in a certain way and orientation, transporting it at a specific speed and on a specific path. The professor of production engineering’s research focuses on human-automation interaction.

"We are developing robotic solutions that can interact with humans in an efficient way," she said, "and also in a way humans can understand. We humans communicate using voice and gestures. And we want to do the same with robots."

Several hours’ drive to the northwest, closer to Stockholm, Johan Frisk stood near a robot operating a press brake. Instead of safety fences, the system used area scanners coupled with software to provide safeguarding.

Frisk was monitoring what he called a

flexible mobile robot (FMR)

. It’s not a cobot but instead uses a traditional articulating arm able to carry full payloads at full speeds. As Frisk put it, "They’re coexisting robots, not collaborative robots."

Once the batch is finished, the operator moves the system to another press brake, a panel bender, a stamping press, or a variety of other machines. All can be operated manually or with an FMR. One press brake might have someone manually running a job, while an adjacent brake might be running a batch with an FMR.

Frisk is CEO of OpiFlex, a Swedish company he founded in 2013 with the aim of taking on the automation challenges in the high-mix/low-volume operations of small and medium-sized enterprises (SMEs), which together make up the majority of global manufacturing. Syberfeldt and Frisk have worked together in various laboratory and industrial settings, and both talk of a future of industrial robotics with far less restrictive physical and communicative boundaries. Safeguarding innovation has reduced those physical barriers. And instead of programming, people will "train" robots to work with certain machines and systems. After training, a robot will be able to "see" a machine, be fed a job from the manufacturing execution system (MES) or similar software, program itself, and begin the job.

Their vision is echoed in a paper presented at the 2016 IEEE/RSJ International Conference on Intelligent Robots and Systems, titled the "Fourth Robotic Revolution," by authors Dominik Boesl at the Technical University of Munich and Bernd Liepert with KUKA and euRobotics. "For a very long time, automation was driven by systems that were programmed, line by line, to repeat more or less complex tasks at the highest speed and accuracy. Unfortunately, this one-sided optimization hindered them from becoming flexible and versatile tools … Therefore, the desire for perceptive and cognitive robots is obvious. Machines should understand what their users and operators want to do, instead of being programmed to repeat basic tasks … [one day] we will be able to come up with systems that will understand what we want them to do and, maybe one day, even learn like a robot apprentice."

We’re not quite there yet. Still, judging by FMRs operating in European sheet metal shops today and work done by Syberfeldt and other researchers, we’ve come a long way just within the past few years. FMRs are out of the laboratory and now working in industry. A number of sheet metal operations in Europe have been operating with FMRs for several years. Opi-Flex also has partners in North America and hopes to start moving stateside sometime in 2022.

According to Frisk, all this progress in FMRs was made possible by starting with one of the most complex operations performed by robotics: bending sheet metal parts at the press brake.

Start With the Most Complicated

Shortly after its launch in 2013, Frisk’s organization completed a market study. After spending years in the robotics industry at ABB and elsewhere, Frisk wanted to know why so few small manufacturers used robots. Outside automotive, manufacturing has fewer than 10 robots per 10,000 employees, Frisk said. He added that in automotive—frequently thought to be one of the most robotized industries—the ratio is about 1,300 robots per 10,000 employees.

An operator refines a bending program for a large panel.

OpiFlex

The study found that the challenge boiled down to flexibility and the ability to follow manufacturing constraints. A highly automated cutting or bending cell can do wonders for throughput, but only if downstream processes can keep pace. And as anyone working in a metal fabrication job shop knows all too well, constraints move depending on the demand and product mix.

The study revealed a wish list for typical fab shops and other SMEs. First, they wanted robot programming to be more intuitive and quicker. Second, they needed safeguarding without fences while working with robotic arms that could operate at full speed and payloads. Third, they wanted to be able to move the robot where it was needed, effectively "decoupling" the robot from the press brake, panel bender, stamping press, machining center, or any other machine on the floor. During a shift, a machine might alternate between manual and robotic operation. Considering all this, Frisk’s team began with what remains the most complicated area in metal fabrication: the press brake department.

After a career in the robotics industry, including applications and management positions at ABB, Johan Frisk founded Opi-Flex in 2013.

OpiFlex

"Automating sheet metal forming is much more difficult than other processes, like machine tending in machining," Frisk said. "So we asked, ‘Why not start with the most complicated?’ Then everything else will be relatively easy."

A press brake puts a robot through its paces, demanding it manipulate sheets in multiple ways, follow flanges up during the bend cycle, reposition its gripper, then stack work securely and reliably on a pallet. Frisk’s team aimed to design a robot system that could work with the press brake bed at the same height an operator would during manual operation; this meant the bed couldn’t be raised a few feet for easier robot access.

An operator puts the final touches on a program for a flexible mobile robot tending a panel bender. Compared to press brake operation, the pick-and-place machine tending required for panel bending is relatively straightforward to automate.

OpiFlex and SICK

They also designed the system to be mobile. Early design iterations had an articulating arm on an automated guided vehicle (AGV), but this concept had a few problems. First, it tied up the AGV during machine operation. Second, the robot itself wasn’t secured to a precise location, which created programming hurdles.

The final design incorporated a docking station placed at a precise location in front of the machine. The robot is moved into place, either manually (such as with a pallet jack) or via mobile automation using an AGV with forks. Once the robot is in position, the operator folds down and extends arms that hold the SICK area scanners mounted onto the mobile robot platform.

An operator moves the FMR into the docking station in front of a machining center.

OpiFlex

According to OpiFlex patents, these scanners work with a safety control unit that identifies the cell and the machine (or machines) within it. With the cell identified, the safety control unit sends information about safety zone configurations to the sensors about when to slow the operation and where to stop, should someone step too close to the robot.

"The technology works so that, even if we lose air or power, we will not lose the workpiece," Frisk said. "So, if we lose air, we will not lose the vacuum. For sheet metal, we can hold a workpiece for hours without losing the grip. Moreover, everything is dualchannel, and this includes the grippers."

According to the company, the technology meets the requirements of global robotics safety standards, including ISO 10218. "We are following the ISO standard," Frisk said, "and so the technology would comply with ANSI and CSA standards [for the U.S. and Canada] as well."

After extending the arms holding the safety scanners, the operator makes the necessary connections for air (for the robot gripper), the data input and outputs (I/Os), and power.

Training the Robot

Next comes programming, and here the company takes an approach that has elements of what Syberfeldt and other researchers have been working on in the lab for years. The robot isn’t programmed with a teach pendant or via offline bending simulation. An operator might tweak robot motion here and there and determine the best way to pick and stack parts. Otherwise, most programming happens automatically.

The robot can do this because, during its installation and initial setup, the FMR has been "trained"— not how to bend a specific job, but how to operate an entire machine. The company uses an integration wizard that effectively "creates a machine," Frisk said, providing a foundation for simplified programming. "The robot knows the location of the press brake and other elements of the robot cell," Frisk said. "We configure each robot and cell, and we create a program generator that the operator uses. The operator answers some simple questions, and we use sensors to identify parts and how to move them around in the cell."

The robot’s initial training incorporates the basics, including the available tools, backgauge positions, and the best ways for them to be set up for certain part geometries and bend sequences. The training also incorporates the full features of the press brake, such as adaptive bending in which the brake underbends, measures the angle, then completes the final 2 degrees (accounting for material thickness and property variation).

The training also goes into subtler details. For instance, the robotic setup draws information from sensors on the backgauge and elsewhere that checks for part alignment, including in the longitudinal direction along the bend line. In most cases, the gripper’s vacuum cups maintain contact with the flange as it swings upward during the bend. Regardless, vacuum cups can move ever so slightly, which could be enough to throw a complicated, multibend part out of tolerance.

Frisk described a recent workpiece with six bends. On every bend, sensors checked for alignment and bend-line position, especially critical for the initial bends, considering the effects of stackup tolerances on later bends. A small error on the first bend can snowball into a large error by the last bend. He showed a video demonstrating how, on the fourth bend, the system detected slight workpiece movement. "The robot moves slightly back and forth to perfectly align the workpiece in the longitudinal direction," Frisk said.

Robot training involves not just the brake but the entire bending cell system, including the incoming pallet of flat blanks and a pallet of formed parts. For instance, using a combination of sensors, software, and subtle robot motion, the system is designed to eliminate the need for an air knife when picking up thin sheets.

An operator refines the mobile robot’s program as it tends a stamping press.

OpiFlex

Training for formed-part stacking entails part orientation choices. Certain parts can be stacked straight on top of each other, while others need to be stacked at angles to ensure the stack is stable and doesn’t topple over on the pallet.

Again, all this training provides the foundation for the robot to program itself, with the operator finetuning the path, stacking options, and other elements as necessary. According to Frisk, simple program refinement at the press brake takes about two minutes; more complex pieces take about 15 minutes.

The Quest to Achieve Flexible Flow

Of course, not every job is suitable for FMRs. Although they have a variety of grippers available, they can have trouble bending extremely small parts. Also, the robot isn’t mounted onto a rail, so it might not be able to access every tool on certain bending setups with toolsets that span across the entire bed. Frisk added that sometimes shops can overcome these challenges by altering tool placements.

Still, not every application is suitable for robotics, and in high-product-mix manufacturing, the suitability can change from day to day, shift to shift, even hour to hour—hence the need to move the FMR from one machine or area to another should the need arise. And with new safeguarding technology (without fencing), operators now can work at adjacent machines, perhaps bending parts that just aren’t suitable for the FMR. Sure, they likely could work to adapt the FMR to a challenging job, but why go through the trouble when a trained brake operator can set up the machine and just finish the order?

Like humans, not every robot will be suitable for every job. For instance, at this writing OpiFlex isn’t developing FMRs for welding, a process that requires ancillary components like wire feeders and shielding gas. Still, other flexible alternatives are emerging on the market, including cobots and robots that can be taught to weld kinetically (by physically moving the welding gun) and through simplified interfaces. Some technologies are eliminating the need for weld programming altogether; the robot "sees" the weld, compares it to the CAD file, adjusts, and commences welding. Similar technology is becoming available for powder coating and even blast cleaning. (For more on this, see

The FABRICATOR

’s coverage of FABTECH 2021, archived at

thefabricator.com

.)

Even so, the ability to move the FMR between multiple machines helps overcome the perennial job shop challenges caused by the moving constraint. As of late 2021, FMRs have been used to operate and tend panel benders, stamping presses, machining centers, hardware insertion presses, and a variety of material handling operations. In many of these applications, Frisk said, manufacturers are moving away from equipment like conveyors, many of which were used simply to carry parts away from an automated cell and through safety fencing for stacking. With advances in fenceless safeguarding, why have a conveyor?

The potential flexibility of FMRs is pushing some companies, even some large OEMs, to rethink their operations. Frisk said that in recent years, OpiFlex has received more calls from OEMs and large Tier 1s than small and medium-sized job shops and contract manufacturers.

"I have to admit, we didn’t expect that," he said, adding that these days, with customer demand ever changing and new-product development cycles ever shortening, flexibility has become paramount in just about every manufacturing setting.

Robots as Colleagues

Consider a sheet metal job shop with robots in bending. Such automation boosts capacity there, but what if a bottleneck in machining holds up operations in final assembly? In this case, an operator could move the FMR to the machining center, clamp it in place on the floor-mounted docking station, initiate the operation, and increase machining throughput. Because robot tending in machining is relatively simple compared to bending at the press brake, OpiFlex’s FMRs (after initial training) require no job-specific programming, a feat that makes single-piece part flow possible.

Considering the advent of automatic tool change and now FMRs, will single-piece part flow be possible on the press brake? Frisk paused and thought for a moment. "Yes, quick changeover is incredibly important," he said, but he added that bending at the press brake is a unique animal. "A press brake still is quite a complicated thing. We need to have some respect for that. Sheet metal in general is complicated [for robotics] because parts that come from laser cutting can be so different. In machining, we’re working with either round or square workpieces. It’s so much simpler." What he did say is that interaction between robots and humans will evolve significantly as robots’ cognitive ability increases. Like humans, they’ll be able to look, listen, and learn.

Back in Syberfeldt’s lab, the professor touched an adjacent robot to wake it (roughly analogous to waking computers up from sleep). The robot—equipped with visual and aural sensors feeding an artificial intelligence engine—is now ready to do work. "Touching it tells the robot, ‘Hey, I’m here.’ I then can gesture to show the robot what I want it to do and how. We aim to make the robot as human as possible."

Such interactions will become a critical part of what the research community calls

cyber-physical systems

. "We’re trying to distribute intelligence to specific units in the production system," Syberfeldt said, "and we introduce a lot of dynamics. So, regardless of the situation and the environment, the robot can actually see what’s needed, make a decision, then go where it’s needed."

The hardware, including safety systems and grippers, will continue to become more advanced. Syberfeldt foresees grippers in some applications becoming more handlike, mimicking the flexibility of the human operator. The greatest advances will be in software.

"The question we’re trying to answer is, ‘How can humans interact with a robot in the most efficient way?’ We’ve looked at it from a robotics perspective. I think now we need to look at the challenge from a human perspective. Humans need to adapt, because what we’re finding is that, while we are hard-wired to interact with each other and other animals, it’s just not natural for humans to interact with robots. We need to see the robot as our new colleague on the shop floor."

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

OpiFlex,

www.opiflex.se/en

ABB,

www.abb.com/robotics

SICK,

www.sick.com

University of Skövde, Production and Automation Engineering,

www.his.se/en

GET THE LISSMAC EDGE

Increase your quality and output with our full range of solutions for.

Deburring Deslagging Edge rounding Finishing

17 Route 146

Mechanicville, NY 12118

518.326.9094

getthelissmacedge.com

sales@lissmac-corporation.com