# How robots program themselves

[TARİH: 01.05.2020 The Fabricator]

Artificial intelligence could usher in a new era of automation

By Francois Simard

A robot powder-coats an aerospace part, with a simulation of the same process, all self-programmed in real time, shown alongside it.

Photo courtesy of Omnirobotic.

F

or decades the robotics story has been the same: You need a huge batch size to get any benefit. In many areas robotics has been a game restricted to mass manufacturers, while any shop churning out a variety of SKUs has been left out of the question.

High-product-mix manufacturers avoid robots for many applications. The primary reason for this isn’t the cost of the robots themselves, but the costs of adapting the environment for robots (locating jigs) and the cost of programming them.

Most high-product-mix environments constantly change. Movable jigs, objects hanging the wrong way on a conveyor, or any piece of equipment off to the side can render a traditionally programmed robot entirely off-limits. A $50,000 robot might have $150,000 or more in integration costs for just one task, part, or operation. If the application requires complicated part or batch changes, the costs can explode.

This hasn’t stopped manufacturers from doing their work, but with the ongoing skilled labor challenge, the cost of robotics has to come down fast, and this includes the cost of programming. Most robots are positioned on six axes, and programmed instructions need to account for them. This includes the position and the mechanical limitations of each of the robot’s joints. In most cases, instructions must be accurate down to the millimeter.

But with artificial intelligence (AI), automation’s cost-benefit equation could change dramatically for high-product-mix manufacturers. That’s because some robots now are effectively programming themselves.

"What" Versus "How"

Let’s say you ask a colleague to grab you a coffee on the way back from a break: "Could you grab me a coffee on your way back?" That’s enough for a human, but for a robot, you’d need specific instructions: "Walk through this door, go down the hall 90 ft., step out for a few minutes, step back in, grab a coffee at the far left of the counter, go back the other way down the hall 90 ft., re-enter the work area, and deposit the coffee in my hand." And if someone has moved the coffee machine since the last time you saw it, the operation will fail.

In recent years manufacturers have programmed robots in one of three ways: sequential programming using a teach pendant, kinematic manipulation, and offline programming. Advancements in teach pendants have attempted to make robot programming more intuitive. With kinematic manipulation, the situation gets a little easier, with the operator physically positioning the robot and registering the position. From that the path is developed, though the program does need to account for velocity and the robot’s mechanical limitations. Offline programming and simulation can save shop floor programming time, but operators do spend time validating, rewriting, and touching up the program to account for differences between the simulated and real world.

In all of these cases, the programmer is telling a robot "how" to do its task—like those detailed instructions to get coffee. Self-programming robotics take a fundamentally different approach. They don’t need to be told how to do something. Instead, they just need to be told "what" to do.

What Is a Self-programming Robot?

A self-programming robot generates a plan for a task automatically. It perceives the environment, knows the process constraints to the extent that it can, then executes the task with no manual intervention required.

Unlike conventional industrial automation, self-programming robots are given specific "goals," such as a task description like "paint this surface." AI considers the robot’s specifications and limitations, such as how fast it is allowed to move, as well as the position of the object it’s working on; it then creates a valid plan for each part, all in real time.

The same way that people use their eyes, self-programming robots use 3D vision to perceive every aspect of the object in front of it, such as its shape, size, and relative position. The robot relates all this information back to the assigned task and then, using AI-based algorithms, interprets the information and figures out the most efficient path to reach the goal set for it. This can include situations where the object is in motion, like sheet metal parts hooked on a continuously moving conveyor line.

When a robot generates its own program for a task, it uses information from 3D vision—a "digital twin" of the environment—to validate each part of the plan. This kind of AI works similarly to how skilled operators use their eyes and brain. It adapts to changes in position, orientation, and the shape of the object in front of it.

Powder coating is an application ripe for automation, especially if it involves putting workers in environments that, especially after years of exposure, can lead to health problems.

Photo courtesy of Getty Images.

Teach pendant programming for some applications has become more intuitive over the years. But it still ties up a robot and prolongs changeovers between jobs.

Photo courtesy of Getty Images.

The Potential for Spray Processes

High-product-mix manufacturers can deploy self-programming robots in a variety of operations. For instance, such robots are now being used to paint aerospace parts.

Spray processes in general are the fastest track to market for self-programming robotics. Powder coating, liquid painting, shot peening, sandblasting, thermal spraying, and glue dispensing all apply, primarily because vision sensors and robot accuracy can be relied upon within the realm of a few millimeters.

For powder coating and liquid painting in particular, self-programming robots have come online first because the need for a solution is simply so high. For industrial painting and powder coating, the challenge has been threefold: How do you deliver a high rate of quality output, limit costly reworking, and protect the health and safety of workers? As their shift goes on, workers not only grow tired, but their visual acuity and accuracy diminish and the consistency of their work suffers. Rework costs can be significant, sometimes enough to make entire batches unprofitable. If proper safety and ergonomics practices aren’t followed, long-term employment in some industrial painting and powder coating environments can lead to respiratory illness, orthopedic challenges, and chronic pain.

For self-programming robots, once their vision sensors are set, their accuracy never diminishes below what they’ve been calibrated for as long as they receive periodic maintenance, which is no more than the limited maintenance most industrial robots require. Robots don’t wear masks or use air filtration systems, and they don’t develop the illnesses that can plague so many skilled workers in the long term.

Today’s sensors can overcome lighting and reflectivity challenges, and the robot can operate at a high line speed and with various parts placed in any orientation. Self-programming robots use heuristics to determine the amount of coating they spray and the volume of coverage that produces. The aim is to achieve the most consistent finish possible with the least amount of powder wasted.

Liquid painting does add some additional complexity. For instance, if the robot pauses or passes repeatedly over a spot, the system must consider the risks of paint dripping, which ends up being an additional variable. However, once this variable is accounted for, a robot can achieve high consistency, precision, and repeatability.

Beyond spray-based applications, there are no limits to what self-programming robots can do. There’s just further work to be done. Sensors, jigs, and other components need to be cost-effective, and manufacturers need to be able to deploy these robotic systems quickly.

For instance, contact processes like welding, grinding, and polishing require greater accuracy than spray processes like painting or powder coating. This simply means a different solution needs to be engineered. Even so, the principles of a self-programming robot remain.

AI for High-mix/Low-volume Manufacturing

By putting AI to work, manufacturers can automate many of the most repeated, least engaging tasks that still require human levels of perception, know-how, and precision. Painting and powder coating are just the first of many examples.

Nobody benefits from holding automation back, but automation for its own sake won’t necessarily be cost-effective either. The first step is to identify and validate that an operation’s most tedious, repetitive, and hazardous jobs can in fact be automated. By using robots in these situations and proving out the solutions, a manufacturer then can evolve its automation efforts to include entire cells and production lines. As this transition occurs, companies will see where the existing workforce can fill in the gaps, bring their own ideas into play, and help generate better results.

Within all this, self-programming robotics can play a critical role. This new kind of automation will help free resources and allow manufacturers to operate production more effectively, all without having to redesign facilities just to get robots installed in the first place.

Francois Simard is the founder and CEO of Omnirobotic, 420 Armand Blvd., Frappier #100, Laval, QC H7V 4B4, Canada, 450-897-1005,

www.omnirobotic.com

.