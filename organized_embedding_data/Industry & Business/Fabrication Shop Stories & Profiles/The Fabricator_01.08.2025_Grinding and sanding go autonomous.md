# Grinding and sanding go autonomous

[TARİH: 01.08.2025 The Fabricator]

Tech Spotlight

Automating the least-sought-after jobs on the fab shop floor

By

Tim Heston

W

hen you look at how a modern metal fabricator uses automation, it might have automated laser cutting, maybe even a robotic press brake or welding system, especially for the higher-quantity runs. Move down to grinding and surface finishing and you see a different story. Those processes remain largely manual—a fact exacerbated by manufacturing’s labor shortage.

"Across the board for this application domain, we see anywhere from 40% to 80% labor churn."

That was Ariyan Kabir, explaining that the problem pervades the high-mix, high-variability manufacturing space. Robotics rule in automotive and other arenas of high-volume, low-variability production, but for high-variability and high-product-mix operations, not so much. Thing is, the latter group happens to comprise the largest segment of manufacturing, not just in the U.S. but around the globe.

Kabir is co-founder and CEO of GrayMatter Robotics, a company that’s developed a way to automate one of the most highly variable process areas in metal manufacturing: surface finishing, including grinding, blasting, polishing, and buffing. The company is hardware agnostic. "We look at the application, then we combine the right robots, sensors, and tools with our proprietary GMR AI technology, which makes the robot autonomous."

The company’s roots go back to 2016, when co-founders Kabir and Brual Shah worked at the Center for Advanced Manufacturing at the University of Southern California, along with center director Prof. Satyandra Gupta, GrayMatter’s chief scientist and third co-founder. While there, the founders talked with myriad manufacturers, large and small. They learned about the skilled labor challenges, especially for tedious jobs like sanding and finishing in high-mix manufacturing. Even shops with robust investments in offline programming and simulation couldn’t spend time simulating robot programs for thousands of different parts. Researchers knew that, to make automation practical for these environments, robots needed to be autonomous.

"All this motivated us to launch GrayMatter Robotics in 2020," Kabir said.

No Model Required

While most autonomous automation focuses on self-driving vehicles and material handling applications, autonomous technologies are beginning to crop up to some degree throughout the metal fabrication value chain. With welding in particular, certain emerging technology compares a solid CAD model to the part assembly in front of it, identifies where the weld is needed, then on its own figures out how best to make it. Some of these have come to market using the robot-as-a-service model. Shops don’t "own" the systems outright but instead pay a subscription for usage.

GrayMatter follows a similar robot-as-a-service model, but as Kabir explained, grinding and surface finishing have a few idiosyncrasies that separate them from other autonomous fabrication technologies. For one thing, the GMR AI platform doesn’t use a CAD model. Instead, vision sensors scan every part put in front of them. From there, AI determines the geometry and where surface finishing is required, then starts the job.

The robot runs a finishing program, reading feedback from onboard sensors and making necessary process adjustments. It also changes discs or other consumables automatically as the job requires. The system also scans for unwanted contacts of cables and other components of the robot cell to ensure they don’t become entangled with the work. Dust also is collected at the source.

"Certain parts don’t require fixturing either," Kabir said, as long as the workpiece is large and can sit securely on a surface, and the robot can reach all required surfaces. "Operators can roll in a part, lock the wheels, and that’s about it."

Other setups involve two robots working in tandem. And very large workpiece applications can involve robots mounted on rails, on overhead gantries, and a variety of other arrangements. Some applications involve multiple processes. Kabir described one that involves grinding of corner welds. After this, the robot changes to a sanding disc and applies it to the entire workpiece surface, prepping it for powder coating.

"For grinding in particular, the robot can detect heavy weld lines on its own from the scan data," Kabir said. "The operation remains autonomous. But for certain applications, the weld lines can be very fine. In these cases, an operator can highlight the weld lines with a marker." From there, the robot "sees" those marks and grinds only those areas.

Similarly, for sanding or buffing, if the product requires a sanded surface in only certain areas, an operator can use masking tape to mark (such as with a taped perimeter and an X in the middle) what areas to avoid. From the scan data, the robot figures out what to sand and what to avoid.

Pushing the Process

When it comes to robotic grinding and finishing, optimizing the process physics really matters. As Kabir explained, what works for a manual process won’t necessarily work for a robot. For instance, a manual grinder or sander taking breaks gives the grinding media, sanding disc, and backup media time to cool down.

Robots, on the other hand, can apply much more force and run continuously for hours. If not designed and chosen correctly, consumables can start degrading quickly. Automated systems need the right recipe of force, RPM, contact angle, abrasive sequence, and a dozen other parameters. Such systems can require, for instance, a different step-down sequence from coarse- to fine-grit media.

The company uses a combination of structured light scanners, laser scanners, and high-fidelity 2D scanning. What combination each cell uses depends on the required field of view, the accuracy required, cycle time needed, and other application-specific variables. The material also matters, of course, including its opacity and reflectivity.

"We’re now producing mirror-finish surfaces on certain aerospace parts," Kabir said. "To scan highly reflective material, we sometimes rely on blue lasers. In other cases, we use a guide coat," which is a thin layer of a contrasting color, typically a fine powder—a method that’s been used for years in manual metal polishing applications.

Autonomous grinding and sanding technology uses tactile as well as pressure sensors to adapt the applied force. Even so, the robot never emulates a person. Skilled people manipulate the finishing media in specific ways, but robots aren’t people. "With robots, we usually produce two to six times the throughput compared to the manual alternative," Kabir said. "And we’re only able to do so by pushing the process physics."

The company has focused its efforts on grinding, sanding, blasting, and polishing, but it also has ventured into other process areas like coating and painting. Robot systems have not been installed on in-line powder coating systems yet, but they have worked with stationary parts in large spray booths. "For now, we’re keeping our focus in the domain of surface finishing and surface treatment," Kabir said. "But in the future, we’ve got a longer roadmap for different toolin-hand-process operations."

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

GrayMatter Robotics,

graymatter-robotics.com

www.lasermech.com

We Have The Angle On Robotic Cutting.

When it comes to robotic laser cutting with Fiber Lasers, Laser Mech’s

FiberCUT

∗

Series

has all the angles covered. From the compact, ninety degree

FiberCUT RAC

to the zero degree

FiberCUT

∗

ST

, there’s a model available to handle even the most difficult part access and cable management challenges. And with multiple FiberCUT configurations to choose from, Laser Mech

®

has one that’s just right for your application.

Visit Us In

Booth 833047

(248) 474-9480 •

info@lasermech.com

Laser Mech

®

and FiberCUT

®

are registered trademarks of Laser Mechanisms, Inc.