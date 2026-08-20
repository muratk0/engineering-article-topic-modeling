# Is the cobot ready to step in and help?

[TARİH: 01.01.2021 The Fabricator]

The time when a robot can be wheeled from one fabricating cell to another might be near

By

Dan Davis

Thanks to standard interfaces, advanced programming software, force sensors, and tools to help dial in the location of the collaborative robot in front of a machine tool, a fab shop might be nearing the day when it can roll a cobot in front of a press brake when an operator calls in sick.

S

ince the Great Recession more than a decade ago, metal fabricators aren’t necessarily employing people unless they are absolutely needed. Manufacturing companies are lean, which helps to keep fixed costs down and the business more manageable when business slows.

It’s also a gamble. Unless shop floor personnel are cross-trained, the absence of a machine operator can sabotage productivity goals for the day. While more automated bending systems are being sold to North American fabricators, many shops still require an operator to be in front of the press brake to get parts formed.

But it’s not only skilled labor. A lot of manufacturing operations rely on temporary employees to tackle projects such as grinding of parts that come off the cutting table. What if they don’t show up or are unavailable? The parts need to be finished before advancing to the next downstream process, and those parts aren’t going to grind themselves.

Josh Mayse, an applications engineer with fabricating machinery distributor Mid Atlantic Machinery, recognized the metal fabricator’s plight. He just thought that robotic automation might have progressed more by now so that a dearth of operators wouldn’t be as much of a problem.

Mayse has spent more than 15 years working with fixed automation systems and robots as an employee for large metal manufacturers and now as an automation applications expert. It wasn’t until a couple of years ago when he started working with collaborative robots from Universal Robots that he realized these devices could help fabricators remedy their productivity dilemma while still remaining committed to being lean enterprises.

(Unlike typical industrial robots that will finish a programmed movement no matter who or what is in its way, collaborative robots, or cobots, can sense pressure and will stop if they come into contact with something. Also, because these cobots are often smaller, they don’t pose as much of a threat to nearby human workers. They don’t require extensive guarding as a result. This creates the opportunity for the robots and humans to collaborate.)

"These metal fabricators focus on return on investment. That’s what I always cared about when I was working for a manufacturer. How do I deliver ROI? How do I give my employer an opportunity to compete?" Mayse said. "So the thought became, let’s move the robot around."

Mayse literally describes his vision as a cobot on a table with casters, moved throughout the shop to where it’s needed at that moment. If a shop needs a bunch of small parts bent on the second shift, the cobot is wheeled to the front of the press brake, and the bending operation begins. If parts need to be ground, the cobot can be set up in front of a fixture where it can grab and then grind the parts. (This is where end effector tooling for the robot gets creative.) Those are two of the applications for which Mayse sees potential now, but really many more opportunities exist on the shop floor.

To describe how we have arrived at this point, Mayse described some of the steps that he has taken to make this type of automation more accessible to the majority of metal fabricators. His initial work has focused on the press brake.

Developing a Standard Interface

A metal fabricator might not give it much thought, but robotic integrators and automation experts recognize that a robot cannot immediately interact with a machine tool. The industry simply isn’t at that plug-and-play level yet.

Mayse knew that had to be one of his first projects—developing a way for the cobot to "talk" to the press brake. Nothing else existed that he could buy off the shelf, so he had to design his own interface.

He designed a box that connects to the press brake’s control hardware and acts as the point of recognition when the cobot is plugged into it. The cobot sits on a portable cabinet that has a cord set hardwired into it. When the cobot is needed for a forming job at the press brake, the technician can move it into place and connect it to the interface on the press brake. An installation file, which provides details about the press brake application, such as whether a light curtain or a safety scanner is present, is downloaded by the cobot. Once the cobot has processed the file, the bending process is ready to begin.

"I could have mapped out everything required for that setup through that interface," Mayse said. "Then if I want to take the cobot over to a simple pick-and-place application after the bending job, which is more collaborative, I load a new installation that configures the robot for the collaborative tasks. I can tell the robot basically what all of the instructions are and it’ll be ready to go."

Rethinking Robotic Programming

One of the obstacles to just putting a robot of any kind in front of the press brake is all the programming required. It’s not a matter of using a teach pendant to guide the robot along a seam for a welding application. Traditionally, a press brake operator must guide the robot to pick up the part, move it to the backgauge, hold the workpiece until the ram engages, grab the workpiece again as the ram disengages, repeat the cycle for subsequent bends, and deposit the workpiece on a nearby pallet. That’s a lot of work even for a job with a minimal number of bends.

The use of cobots isn’t limited to press brake operation. For example, they can be configured to pick up and place metal parts into automated deburring machines.

Being aware of that tedious programming work, Mayse said that he started breaking down press brake forming activities into different types of families. He created programming for angles, where the bend is done just on one side; channels, with bends on two sides; and boxes. This programming for these part families provides general movement templates for the robots. When the programming development is finally finished, according to Mayse, a technician won’t have to spend as much time teaching a new part to the cobot that sits at the press brake.

"What you basically do is just walk the cobot through the sequence one time, and then we adjust those points for the next part," he said.

He added that the development of more powerful robotic CAD software will allow for this type of improved programming to be done offline. At that point, the technician will only need to call up the next job and ensure the right blanks are nearby for the cobot to begin the bending process.

Ensuring Accurate Positioning

Rolling a cobot up to a press brake isn’t as simple as it might sound. If that cobot is off just a few millimeters, the whole program is going to be off. Correct positioning is key to making this sort of bending automation work.

In response to this manufacturing requirement, technology developers have created positioning technology that helps cobots to be placed in the exact spot they need to be to do a job accurately. This location tool, affixed to the cobot’s arm, acts as a sort of coordinate measuring device as it takes into account where it and the press brake tooling are.

Mayse described the setup procedure as a few easy steps. He moves the cobot to the press brake, places the arm with the location device so that it touches the press brake tooling, ensures that the tooling is clamped into the brake, and lets the positioning device do its work. Once the cobot has its new base position, all of the bending programs are automatically updated, and the cobot is ready to start bending workpieces.

"This is huge for the collaborative robot industry because it allows me to move this robot and spend a lot less time and money trying to fix the location," Mayse said.

Cobots also are equipped with force sensors in their wrists. Mayse said that he can program the cobot to move the workpiece into position until it receives the proper feedback force, which in this case would be an indication that the workpiece is flush against the backgauge. This ensures that the parts are in place and the press brake can deliver square bends.

Developing the Right Gripper System

Some metal fabricators might be familiar with older-style robotic press brake cells in which one robot arm moves parts onto a staging area and another robot grabs the part to engage with the press brake. Such a cell also might have a repositioning shelf where the robot can rest a workpiece so that the robot can grip it from another angle to accommodate another bend in the job sequence.

Obviously, that type of setup does not lend itself to flexibility in a fab shop. Now the cobot does demonstrate its ability to be shuttled quickly between workstations, but what about staging of parts between bends? It can be a bit of a challenge to keep up with these automation accessories depending on the type of bending job.

Mayse said that’s where he has spent some time working on new gripper designs, some of which he is looking to patent. One is a rotary gripper system that creates a seventh axis of movement at the end of the robot.

"If you have an up-and-down bend and it has to happen on both sides of the part, we can now do that without setting the part down between bends because I can now turn the part with the sixth axis of the cobot to get the up-and-down bends and then I can access the other side of the part by rotating the seventh axis," he said.

Mayse added that he has worked to develop a hub model for the gripper so that a technician doesn’t have to change out the entire gripper for a new job. Attachments, such as a vacuum bar, can be placed and bolted on the gripper base for the next job. In many instances, these attachments can be 3D printed.

"I’m getting better at using grippers to do more parts. The goal is to minimize changeover as much as possible," he added.

The Right Technology at the Right Time

Metal fabricators have struggled for decades to find people willing to take on shop floor work for the wages being offered, and Mayse said that the emergence of cobots and what they are capable of doing may change that discussion in the future. Shops now can dedicate automation to boring and monotonous work and dedicate their most talented technicians to more complex—and profitable—work.

As an example, Mayse said that he sees finishing as a large opportunity for using cobots. It’s a physically demanding task, but still needs to be done. He’s eager to start hearing from customers about their finishing applications so that he can start to put the time into developing and trying to standardize the activities.

The presence of these cobots also has the potential to change someone’s perception about manufacturing, Mayse said.

"Today’s youth don’t want to necessarily be grinding stuff all day," he said. "But you introduce them to a robot, they think that’s pretty cool."

Automation has arrived to do the jobs that no one is showing interest in doing. The cobot is here to help, not steal jobs.

John Mayse, an applications engineer with fabricating machinery distributor Mid Atlantic Machinery, believes that cobots can help metal fabricators become more competitive, doing the jobs that shops currently can’t find anyone to do.

Editor-in-Chief

Dan Davis

can be reached at

dand@thefabricator.com

.

Mid Atlantic Machinery,

www.midatlanticmachinery.com

Universal Robots,

www.universal-robots.com