# How Collaborative Robots could Disrupt Pipe Welding

[TARİH: 01.08.2016 The Fabricator]

A new approach to pipe welding automation

By Soroush Karimzadeh

Figure 1

A pipe welder works with a collaborative robot on the root pass. The collaborative robot keeps the torch at the center of the joint at the right stick-out, allowing the operator to work closely with the system, monitor the weld joint, and make in-process adjustments on-the-fly.

Figure 2

In this setup, the collaborative pipe welding robot is on the end of a boom so it can be positioned to access a variety of weld joints.

H

umans have been working collaboratively with machines for years, on everything from driving cars to running household appliances. But the relationship between human and machine has taken a very different path in factories, where industrial robots automate repetitive, sometimes dangerous work.

From the 1960s to 2000s, industrial robots were widely adopted in automotive and other industries that needed high speed or accuracy for their high-volume, low-product-mix production lines. But these robots weren’t cheap, and they required a highly skilled programmer. Moreover, while the robots could automate the motion part of each task of high-volume production, performing cognition, reaction, and adaptation proved much more challenging.

The industry began shifting a little more than a decade ago with a new category of automation,

collaborative robotics

, which allows people to work safely beside a robot without safety cages or extensive programming. Robots began to benefit from the cognition of an operator. This human-machine collaboration proved very successful, and today most major robot companies offer some type of collaborative robotics. It’s now the fastest-growing segment of the robot industry.

Working With the Robot

A traditional robot has to work with a programmer and a machine tender. The robot has to be programmed for each motion and task. Once the robot is programmed, a machine tender or operator monitors the robot, brings in raw parts to the cell, and takes away finished products. He also performs other machinetending tasks, such as clearing jams.

With collaborative robots, the programming and machine tender roles are combined. One person can teach the robot by hand or with live interactions using a pendant. Without any significant programming skills, that person teaches the robot what to do and works with it to complete a task.

"Work with" is the important phrase. In traditional robotics, an operator programs a workcell and fixtures the workpiece, and the robot performs the work. If a robot doesn’t perform the task correctly, the operator can’t interfere midprocess to correct the problem. He needs to either wait until the end of the cycle or stop the workcell entirely. This is the important differentiation of collaborative robots, which, again, are able to benefit from operator collaboration to react to changes in the welding conditions (For more on this, see the

Safety Standards for Collaborative Robots

sidebar).

Collaborative Pipe Welding

Historically, a lot of pipe spool welding has not benefited from traditional robotics because of its high-mix, low-volume nature. Highly trained welders weld pipe spools of different lengths and diameters to elbows and T’s.

Given that each joint is in a different location on the pipe spool, a traditional robot has to be programmed for each joint location. Moreover, variances in pipe prep and fit-up make every joint different. In addition, many pipe spool fabrication shops have busy floor layouts with overhead cranes and high forklift traffic—not very conducive to traditional robots, which require a large area blocked off by safeguarding.

When it comes to pipe welding automation, collaborative robotics probably doesn’t come to mind. After all, today most collaborative robots in industry are helping assemblers perform simple tasks with light, small workpieces.

For instance, these anthropomorphic machines (some with "eyes") are able to pick up a part and place it in a specific drop fixture. When a new part or task comes up on the schedule, the operator guides the robot’s "hands" (end effectors) through the new routine. The robot works with this basic instruction and refines it, taking physical obstructions and other environmental factors into account.

Still, to weld a rotating pipe actually doesn’t require a wide range of movement. The challenge is for the robot to weld, react, and make slight changes to its position and welding conditions on-the-fly. Now collaborative robotic systems have overcome these pipe welding challenges.

For instance, a spool-welding robot with 3 degrees of freedom can imitate the arm of the welder (see

Figure 1

). This machine (which falls into the "power and force limiting" category, as described in the sidebar) has safety sensors that ensure speed and force are always below the required thresholds. Violating any of these limits will trigger a safety-rated stop.

A pneumatic manipulator holds the welding arm in place. An operator can move the welding arm from joint to joint on the pipe or from one welding bay to another (using a large boom, as shown in

Figure 2

) by pressing a pneumatic button on the welding arm and roughly positioning the welding torch in the joint.

Once the arm is in place, the operator fine-tunes the starting point with a joystick, then, on a touchscreen human-machine interface (HMI), selects a predefined program for the pipe diameter and thickness. Based on this information, the machine automatically loads the right welding procedure and motion parameters, such as welding parameters, weld speed, and weave amplitude and frequency, for the weld pass. The operator then presses the start button, and welding begins. The total setup time for each joint is less than three minutes. With no light curtains surrounding the robot, the operator can stay close to the welding zone to monitor the progress.

In the preprogrammed welding procedure mode, once the robot completes one pass in the joint, the operator presses the "next" button on the pendant and loads the new set of weld and motion parameters for the next pass. This way, the operator can weld continuously from root pass to cap pass.

The system automatically handles fine adjustments that require precision or speed, such as height control and seam tracking. Using a 2-D laser camera, the machine discerns the torch-to-pipe distance and horizontal position. This information is then fed back to the main controller, which instructs servomotors to maintain a consistent torch height and position in the middle of the joint. Closed-loop controls are designed to ensure precise stick-out and seam position accuracy.

Collaborative Robots and Operator Skill

A good welder knows what makes a quality weld, reads the joint during welding, and, perhaps most significant, has the muscle memory to guide the welding torch on the right path. For many, that muscle memory can take months or even years to develop, and it may be a significant contributing factor to the skilledwelder shortage.

Collaborative robotics tackles the skilled-welder shortage in a new way. A collaborative spool-welding robot with a relatively inexperienced operator can produce the same volume of work as several highly skilled people welding pipe manually.

However, the inexperienced operator isn’t just a machine tender that initiates the process and moves workpieces in and out of the robot cell. He also observes what’s happening in front of him. He’s engaged in welding and the overall pipe fabrication process. He isn’t just pushing buttons and moving parts.

Put another way, a new operator quickly learns what makes a good weld and how to read a weld pool. Meanwhile, the collaborative robot handles the muscle memory, the skill that takes many welders so long to develop.

This means that it doesn’t take very long for a new operator to start welding certain jobs with such a robot. Junior welders can do the 1G pipe welds and highly skilled welders can be freed up to tackle more challenging welds.

At the same time, collaborative robots can handle constant physical work much better than humans. Robots don’t get tired. The operator doesn’t need to continuously manipulate the welding torch by hand, which reduces operator fatigue and the probability of human error.

Adapting to Variation

A collaborative robotic system can automate the rapidly changing facets of the pipe welding process, like height control and seam tracking. But the robot still has a difficult time compensating for big variations, like poor joint fit-up or inconsistent part geometry.

This is where the operator working with the robot can help. Using a pendant and joystick, the operator can change key welding parameters on-the-fly. He monitors the joint and reacts to any variations.

For instance, if he wants to correct the torch position set points, he moves the torch using the joystick. To compensate for a widening gap, he pushes a button on the pendant to increase the weave amplitude. If the puddle is running too hot, he adjusts the trim or wire feed speed. If the tip of the wire is at the leading edge of the puddle, the operator modifies the speed of the positioner.

Safety Standards for Collaborative Robots

In response to the surge of collaborative robots in industry, ISO released safety requirements (ISO/TS 15066) for these robots in February 2016. The ISO document also defines the guidelines for how operators can work with them.

According to the new safety requirements, a collaborative robot may include one or more of several operation modes. The

safety-rated monitoredstop

mode is used to stop the robot before an operator enters the workspace—for example, to load a part onto the end effector.

In the

hand guiding

mode, an operator uses a hand-operated device to transmit motion commands to the robot. Before the operator is permitted to enter the workspace and conduct the hand-guiding task, the robot achieves a safety-rated monitored stop.

In the

speed- and separation-monitoring

mode, a person must be a specific distance away from the robot at all times. If a person gets too close—to a value less than the protective separation distance, as defined by ISO—the robot system stops. This distance decreases as the robot reduces its speed.

In the power- and force-limiting mode, physical contact between the robot and an operator can occur either intentionally or unintentionally. Risk reduction is achieved either through inherently safe means in the robot design or in a safety-related control system. This keeps hazards below threshold values determined during the risk assessment.

The Future

We can see the driverless cars on the horizon thanks to advancements in computation power, artificial intelligence, and machine learning. In the future, more pipes may well be welded with full automation.

But to work well in a highly variable environment, automation needs the cognition, reaction, and adaptation of a human operator. Pipe fabricators are now taking the first steps in this direction by replacing the welder’s arm with a collaborative robot.

Soroush Karimzadeh is CEO of Novarc Technologies, 604-428-0050,

www.novarctech.com

. Photos courtesy of Novarc Technologies.