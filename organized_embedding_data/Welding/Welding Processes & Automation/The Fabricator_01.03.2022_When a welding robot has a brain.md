# When a welding robot has a brain

[TARİH: 01.03.2022 The Fabricator]

Cover Feature

The potential of autonomous welding in the fab shop

By

Tim Heston

After scanning a workpiece and comparing it to the CAD model with embedded weld data, a robot commences welding—no teach pendant, off line programming, or kinetic teaching required.

Path Robotics

A

trained welder can look at a print, review a welding procedure, clamp a part in place, and start welding. Not so with a robot, at least not traditionally.

Historically, a combination of people, hardware, and software has taught the robot what to do, usually with an operator using a teach pendant. All this eats into a robot’s productive time. The teaching could happen kinetically, with the operator moving the robot arm along a particular path. It could even happen through simplified programming interfaces that are proliferating among cobot welding cells.

Another option involves off line programming and simulation. This often comes complete with digital representations of the robot, fixturing, the part itself, and even ancillary components around the cell, all there to prevent collisions and to verify the process.

All this reduces on-the-floor work to (at worst) a few programming touchups. Even so, someone needs to develop the fixture and run the off line program. Humans and software still must do the teaching, whether it’s off line in the off ice or on the shop floor. That takes time and programming resources. A robot can’t simply "look" at a part and start welding—a limitation that has prevented robotics from permeating the "long tail" of high-mix/low-volume, nonserial production.

That might be set to change. Advances in vision, software, and machine learning are building the foundation for a new kind of manufacturing robot—one with a brain.

Look, Then Do

The metal fabrication sector has seen some technologies emerge that can help robots see, then do. Omnirobotic, based near Montreal, has implemented self-learning robots and cobots for powder coating and similar applications. In Sweden, OpiFlex has developed flexible mobile robots that can be trained to "see" a specific job at a specific machine—be it a press brake, a panel bender, a machining center, a stamping press, or anything else—and know what to do next. (For more on this, search for "flexible mobile robots" on

TheFabricator.com

.)

Specific approaches differ, but in general, such automation is given a kind of "robotic training" that governs how the robot interacts with reality. So, when the robot "sees" a part hanging on a powder coat line in such a way, orientation, and speed, it knows to move and spray in a certain way.

A few companies have delved into finding similar solutions for robotic welding, and within the past few years several organizations have brought their technologies to market. Judging by their initial success, the robotic welding landscape might look a lot different in the coming years.

Accelerated Learning

Andy and Alex Lonsberry grew up around their parents’ custom motorcycle fab shop. The brothers learned to weld at an early age, but instead of going into the family business, the two ended up in academia. The Ohio natives pursued their PhDs at Case Western Reserve University. Alex focused on computational neuroscience, Andy on machine learning for bipedal walking robots.

"We focused on having systems learn like humans do," Andy said, adding that their work led to the two starting a consulting company. "The whole purpose of that company was to go and find a market pain point."

Eventually the two met a few engineering managers at a muffler manufacturer to discuss an issue that had nothing to do with welding. As Andy recalled, "In the middle of the meeting, the president of the company walked into the room and said, ‘Let’s talk about welding.’ He said they had a number of welders who were all aging. They were struggling to recruit new ones, and they weren’t able to scale the company because of it.

"They were a high-mix/low-volume fabricator with about 3,000 SKUs, and they would run lot sizes of 5 and 10. They were looking at multiple options, including offshoring. But they were a made-in-America company. They didn’t want to lose brand recognition, and they worried about a loss in quality." Besides, the company didn’t want to keep millions of dollars in inventory. "They were a cash-flow business. They wanted to take an order, make it, and ship it," Andy said.

The fabricator had tried robotic welding, but building custom fixtures for so many part variations wasn’t practical. Part tolerances were an issue too, and because the parts were made of thin stainless steel, the weld parameters were critical.

"Long story short," Andy said, "they just were never able to make it work. So the company came to us with an idea. ‘We love human welders. We want more of them but can’t seem to find them. We’re trying to grow this company. Is there a way for you to take this robotic arm and give it eyes and a brain?’"

Two welding robots work in collaboration to weld a large workpiece. They’re drawing directly from the CAD file and the welding information embedded within it.

Abagy Robotic Systems Inc.

After designing many iterations, the brothers did just that, and in 2018 the two formed Columbus, Ohiobased Path Robotics. The company has been selling its systems under an automation-as-a-service model. Path retains ownership of the equipment while the manufacturer pays Path a set monthly fee, all hinging on certain guarantees of productivity and quality.

Today an operator of a Path cell, using simple toggle clamps and other off-the-shelf items, can fixture a part anywhere and in any orientation on a welding table. The exact location doesn’t matter as long as the robot can physically access the weld joint.

The system’s sensors scan the area, then compare what they see with information embedded in the CAD file. The CAD file can include a plethora of weld data points, including those that follow instructions spelled out by the welding procedure specification (WPS). But weld information in the CAD file can be minimal too. At the very least, the file needs to specify the weld size and whether the weld will be stitched or continuous.

The technology’s genesis stems from the brothers’ research. "It’s about machines being able to assess the data given back to them, and allows them to explore inside their environment, connecting patterns between what is good and what is bad based on their own exploration."

A welding robot suspended from a moving gantry welds a large workpiece.

Abagy Robotic Systems Inc.

Oversimplified, their research deals with a way for robots and other automation to "learn" without requiring a massive data set. Traditional approaches in machine learning and artificial intelligence improve over time by drawing from enormous amounts of data. It’s how your smartphone seems to get smarter every year. The learning methods employed by Path certainly can benefit from all the relevant data they can get, but they don’t require it.

"It’s really the only way to make [the kind of machine learning we need] to work in a welding environment," Andy said. "We need to be able to drive value with small data sets."

Path uses its own vision, sensing, and software technology that allows the robot to see and assess the welding challenge clamped in front of it. Sensors feed back data during welding and view workpiece geometry just ahead of the arc to accommodate for fit-up variability. While the details are proprietary, according to Andy, "We’ve been able to correlate what is happening in real time with what just happened [a few moments before] to determine what the weld penetration actually was, without having to cut a sample or perform ultrasonic testing." He added that the technology doesn’t eliminate the need for destructive or nondestructive testing for the welds that require it. Regardless, the inspection technology does add a layer of security when it comes to ensuring high weld quality and proper penetration.

Path also uses adaptive fill technology, which can help in multipass welding. Inadequate heat on a root pass can prevent good wetting characteristics (how the molten metal flows and fuses with the joint root and sidewalls), which in turn throws off the weld parameters on subsequent passes. "We adapt on the fly to make sure that doesn’t happen," Andy said.

The technology also adapts for weld shrinkage, viewing the workpiece geometry just before the welding arc, then adjusting parameters to suit. "If we see shrinkage, we see it on-the-fly," Andy said, adding that vision data as well as information embedded into the CAD model come into play.

Andy explained that such adaptation works within the constraints of the WPS, especially critical for code-level work in structural welding. In many cases, the WPS governs the technique (stringer bead versus weave, for instance), travel, and other characteristics. "Drawing from this, the system makes choices based on the WPS, and this can vary from application to application and from company to company."

Path Robotics demonstrates its vision and welding systems at FABTECH 2021, held in November in Chicago.

Path Robotics

Clamp and Go

Alexander Domanitsky, a Los Angeles-based vice president of strategy and business development for Abagy Robotic Systems, showed a video of a technician clamping a workpiece in a robot cell using simple toggles and stops, securing the part in a random location. He walked outside the cell to a computer workstation and viewed a 3D CAD model. The model included only the part and weld data—no models of clamps, stops, or any fixture whatsoever.

The gas metal arc welding robot cell has a vision system that makes multiple scans, after which a red "cloud point" appears on the computer screen. The system can match the cloud-point data and the 3D model, understand how they differ, and be able to perform trajectory planning for the actual workpiece, not the theoretical 3D model.

At that point the system adjusts for any weld access issues; in the video, the technician monitors the system as it adjusts the robot path to accommodate a clamp. "During the old days, a robot cell was developed for a particular part, SKU, or perhaps a product family," Domanitsky said, "all requiring complicated tooling. Now we’re switching to a different concept that involves analyzing a working zone volume. Whatever fits in that space can be welded. As long as the robot can physically reach it, it can weld it. You don’t need special fixtures or 3D models of those fixtures."

With installations and support teams in Europe and in the U.S. (with an office outside of Houston), Abagy’s roots go back to a global exhibitions fabricator based in Russia. "The founder had a production floor of about 200 people, all working in metal as well as wood, and he was very surprised when he realized that when you need to produce a batch of one, there was really no way to use a robot," Domanitsky said. "He committed to solving that issue four and a half years ago. Our first commercial installation was in February 2020."

Abagy’s approach involves proprietary software that’s deployed using a combination of on-premise and cloud-based processing. The cloud performs the heavy calculations and planning, while local software manages the robot cell. "That said, we can create an on-premise solution if the manufacturer requires it," Domanitsky said.

The software works with a variety of existing vision and robotics systems. "We are fairly agnostic when it comes to the hardware," Domanitsky said. "We work with the major robot brands and a variety of welding power source manufacturers, including the major ones. And we work with a variety of vision systems, depending on the application."

He added that the company’s systems have been deployed on various part sizes, including jobs involving large structural beams and plates, using one or multiple robots. The technology works with multiwelding-robot setups in several ways. One way is to set up two virtual welding cells with each robot working on specific tasks. Another option involves setting up the cell so that two robots can work collaboratively.

"Two robots can work next to each other, and we can check the connections between them to make a collaborative operation," Domanitsky said. "Imagine that one robot runs out of wire. In that case, we can automatically redistribute some of the welding tasks to the other robot."

He added that the software can work with robots that move in conjunction with gantries and positioners. "We basically don’t have any limit on the number of axes we can support. And we use a digital twin to do all the trajectory planning, to check for collisions and singularities. Whenever we allow the operator to press the button to execute the job, we’ve already tested it with the digital twin."

As Domanitsky explained, the system also detects and makes real-time adjustments for weld shrinkage. "When we do the weld, we know exactly where the tip of the wire should be … When we have heat distributing along the path, then we know we are going to experience some distortions in terms of the part geometry. So, we continuously correct the position of the wire tip to accommodate the seam geometry."

An Autonomous Future?

Popular perception has it that robots are everywhere in manufacturing. But anyone who works on the plant floor—especially in metal fabrication—knows that’s not true.

Fabricators work with integrators to develop robotic automation around specific products with predictable demand. Most work, though, flows just like it always has, from cutting to bending to manual welding.

In 2022 the industry might show the beginnings of a gradual sea change, where autonomous automation makes robotics practical not just for one product family or value stream, but just about everywhere on the shop floor. When robots have a brain, their potential grows.

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

Abagy Robotic Systems,

www.abagy.com

Path Robotics,

www.path-robotics.com

Bending & Finishing Solutions

Knowledge & Experience Working for You

Angle Roll Benders

Multiple machine and control configurations

Attachments available for bending angle iron, serpentine shapes, spiralslcoils

Up to 8″ Sch. 40 Capacity

Mandrel Tube Benders

½″ to 10″ Capacity

Alt-Electric & Hybrid

Draw + Push Roll Bending

Surface Finishing Machines

Suitable for Straight and Bent workpieces

Auto Loading & Unloading Systems

Deburring, End Finishing, and Tube Notching

J&S Machine, Inc.

Ph: 715-273-3376

E-mail:

sales@jsmachine.com

www.ismachine.com

Sales & Service since 1998

Admiralsteel.com

4152W. 123rd St.

Alsip, Illinois

60803-1869

Ph:

800-323-7055

Fax: 708-388-3412

sales@admiralsteel.com

Se Habla Español

Whether you’re stamping, forming, or fabricating, Admiral Steel is proud to help you leave a lasting impression. Since 1949, skilled craftsmen like you have relied on Admiral Steel to provide a wide •range of carbon and alloy steel products. In these challenging times, we know how important every order is to your business, and we are here to help you in an way we can.

Admiral is a registered trademark of Admiral Steel LLC. Alsip, Illinois. Reg. No. 2430959. All rights reserved.

Abrasive automation is possible.

3M Automation. Support within arm’s reach.

Learn more at

3M.com/automation

.