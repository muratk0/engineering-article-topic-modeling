# Misconceptions about cobots and safety

[TARİH: 01.04.2023 The Fabricator]

Robotics & Automation

Focus on the application, not the collaborative robot

By

Tim Heston

These power- and force-limited robots might not require hard guarding, but the cell needs to take welding safety into account, including weld curtains and fume extraction.

Yaskawa Motoman

A machine tending application for a cobot still requires a safety scanner and some hard guarding. The cobot might be safe, but it still needs to wield a sharp object and interact with a machine that, without guarding, presents hazards.

Universal Robots

C

ollaborative robots, or cobots, have begun to permeate the metal fabrication market. With every FABTECH show, more cobots appear in more booths, picking and placing, welding, even operating press brakes. The possibilities seem endless. That said, many applications on the trade show floor also have something that most don’t associate with cobots: at least some kind of safeguarding.

Cobots might look nonthreatening, even cute, but that doesn’t mean they’re inherently safe to use in every circumstance. How safe a cobot operation really is depends on the operation or application.

What’s in a Name?

"We need to recognize that

collaborative

robot began as a marketing term, not a technical term," said Roberta Nelson Shea, the Boston-based global technical compliance officer at Universal Robots. Although all of UR’s cobots are power- and forced limited (PFL), the term

collaborative

robot isn’t standardized across the industry. A robot system or application can be labeled "collaborative" and yet not use a PFL robot.

"PFL is but one characteristic that can make a robot application be a collaborative application," Nelson Shea said. "Hand-guided controls, or HGCs, [represent] another means to build a collaborative application."

Say you’ve determined that, yes, the system you have is indeed a PFL robot. If it is, the power and force it exerts is, of course, limited—hence the moniker. It’s common for the PFL robot arm to stop when it makes unexpected contact, a feat that opens new possibilities for automaton. With traditional automation and mechanization—an articulating robot arm, a welding carriage, a multiaxis backgauge on a press brake, or anything else—even the slowest movement can exert enough power to crush an extremity. Not so with a PFL robot. A PFL cobot arm seems to operate just as a human arm, so how could it possibly be dangerous? Well, a human wielding a knife can be dangerous, and the same can be said of a PFL robot wielding a sharp object.

"Many have the misconception that if a robot is running with PFL capability, the entire application is safe," said Bill Edwards, senior manager, collaborative robotics at Yaskawa Motoman, Miamisburg, Ohio. "Unfortunately, that’s just not true. In a collaborative application, we need to look at the entire application. That includes the end effector, the parts to be handled, and all the tasks involved, which can be both collaborative or not. And not all collaborative applications have 100% pure collaborative tasks."

Safety in Small Tasks

One reason PFL cobot safety can get complicated is the way they’re used. Large, traditional robots wielding large parts require safeguarding, typically interlocked guards (safety fencing), and they’re often part of large automated lines. Robots don’t emulate the tasks humans used to perform; instead, engineers redesign the entire process around automation.

Unlike traditional robots, PFL cobots "are typically not implemented in a totally automated line" Nelson Shea said.

Instead, they often replace manual tasks involving small, low-payload situations. In many cases, a PFL system is simply placed where a human used to be, mimicking the task that human used to perform. The process isn’t changed, and, quite often, isn’t automated entirely. A human still needs to intervene somewhere to get the job done.

"And when this happens, the perception is that the cobot needs no safeguarding," Neslon Shea said, adding that, yes, many of the early applications of PFL cobot systems were indeed safe without traditional guarding, considering the low speed, small payloads involved, and the PFL technology used. Still, there is a need for risk assessment, especially since the systems interact with humans.

Surface Area Factors

Like any piece of industrial equipment, PFL robots must abide by industry-accepted safety standards, including ISO/TS 15066, which is written specifically for collaborative robot applications.

Many of the details behind these standards boil down to speed and surface area of an object in motion. The cobot itself might not have a protruding sharp edge. "They can have a smooth exterior," Nelson Shea said. "They don’t have bolts protruding."

Its end effector, though, might have a sharp edge, and so could the objects it’s carrying—like a sheet metal blank. A PFL cobot wielding a sharp object in a certain orientation and speed may well require safeguarding of some sort, as detailed by the safety standards.

A welder manipulates the PFL robot arm to program a weld joint.

Yaskawa Motoman

This press brake, tended by a PFL robot, still requires proper machine guarding to ensure safety. This system has a combination of safety scanners and hard guarding.

Universal Robots

Four cobots weld within a dedicated booth, separated by welding curtains (not shown in the photo) and integrated with fume mitigation built into the welding guns.

Universal Robots/Vectis Automation

Sometimes, the risk presented by a workpiece’s sharp edge can be mitigated by the end effector design, not just with its surface design (that is, no sharp edges on the end effector itself) but with how it grips the part. As Nelson Shea explained, "An end effector can over-cup a part so that there’s no exposed edge while it’s being manipulated."

She described an application at a large automotive factory that used a robot system with a large, foam-covered clamshell end effector. When it grasped a large sheet metal blank to transfer it to another machine, the clamshell covered all of the part’s sharp edges. "In this case, the end effector provided safeguarding."

As Edwards explained, the safety standards "spell out the force and pressure limitations, which translate to speed limitations based on the surface areas exposed to the operators. When the surface area is reduced to a certain level, that will dictate the speed the PFL robot can operate. Once it gets down to a sharp edge, when you run the initial calculations to ensure you’ve built the right safety system, you’ll find that such a small surface area, combined with the robot’s mass, will limit your speed to nothing, or at least very little. And there’s usually no ROI on a robot that’s moving so slowly." In these cases, additional safeguards are a must to make the application both safe and economically viable.

Tend With Care

All this deals only with the cobots themselves, not from the machines they’re tending. Typical robotic press brake and power press lines have interlocked guarding or perimeter safeguarding, giving the robot system the freedom to interact with the machine in manners that would be completely unsafe for a human: For instance, a press brake robot grasping an odd part from behind the toolset in the middle of a bending sequence.

Of course, the reason many are drawn to cobots is the fact that they can, under the right circumstances, tend a machine without safety fencing (guarding). Again, this depends on the application. But if the risk assessment deems guarding isn’t necessary for the robot system, safeguarding of the machine still needs to be factored into the equation.

PFL cobots also often are decoupled from the machine and moved elsewhere as needed. The operation might be robotic at certain times and manually tended at other times—and that means the machine itself needs safeguarding as if it were any other machine without a robot.

This also applies to a cobot-tended machine that’s never operated with a person tending it. In this case, the machine the cobot’s tending still needs to be safeguarded; people could inadvertently enter or put an extremity within the work area of the machine.

Nelson Shea interjected, "In these cases, what’s wrong with guarding [safety fences]?" They aren’t expensive, and in cases where a machine is never tended manually, an interlocked guard could simplify things.

"Many people think that just because there’s a [PFL] robot on the machine that all the danger is gone," she said. "The danger of that machine always exists."

Edwards described a CNC machine tending application. The part itself might lack sharp edges, and the PFL robot arm might move in a low-risk manner. "But what about the gripper? Does it have sharp edges? Is the machine guarded? I need to look at the entire application. Is the machine safe to load? And when it pulls the finished part out, does it have sharp edges? In a PFL application, I need to stay within the specifications of TS 15066, which means I need to stay below certain pressure and force limits. And when the part’s surface area decreases to a sharp edge, I won’t be able to [stay below those limits]. So, for this task, I’d need some additional safety devices like a scanner or light curtain, to keep the operator safe. Again, when it comes to safety, we look at the application, not the robot."

Edwards described an operator bringing a stack of sheet metal blanks to a cobot workcell. "If the robot has to grasp a part with sharp edges, we’ll know we’ll exceed those pressure and force threshold limits. Perhaps the robot can work collaboratively if it’s moving without holding a part." At that point, the arm and end effector, both with blunt surfaces, fall below those pressure and force threshold limits. "Once the robot has the part, however, I might need to deploy additional safeguarding, because now it’s swinging around a sharp edge."

End effectors that grasp parts also need built-in safety factors, accounting for loss of suction and power. "For instance, in a sheet metal application [involving magnetic material], I might choose to use magnets that can retain their hold even if the plant loses power," Edwards said.

Cobots might look nonthreatening, even cute, but that doesn’t mean they’re inherently safe to use in every circumstance. PFL cobot applications might or might not require a safety fence or guarding, but eliminating safeguarding shouldn’t be the goal. Everything still must be assessed for safety, one application at a time.

An application could require optoelectronic safety scanners, hard guarding (fences), or a combination of safeguarding technologies—again, the details are spelled out in the safety standards, both for robots (ANSI/RIA R15.06) and machinery (such as ANSI B11 machine safety standards).

Welding With a Cobot Safely

Unlike pick and place or machine tending, cobot welding usually doesn’t involve the end effector wielding a workpiece. Instead, the end-effector is moving a welding gun that could have sharp edges, including an exposed welding wire. It’s common to witness such applications running safely without scanners or interlocked fencing. The cobot might move when the wire is exposed (and not welding) in a slow and specific manner, such as with limited reach, so that "sharp edge" risk can be mitigated with proper PPE and other safety considerations. ("During welding, a weld screen is needed as well as PPE specific to welding," Nelson Shea said.)

Sources cautioned that each application must be assessed individually. "We still need to look at these components during the risk assessments to make sure I’m not going to exceed these pressure and force limits," Edwards said.

Here again, while the cobot motion might be safe, the application in which the cobot moves might dictate other safety requirements. So, if something in the cobot welding cell moves, like a welding positioner, safeguards need to account for that positioner motion as well as the fixture and parts the positioner is moving. Of course, most cobot welding cells involve a stationary fixturing table that (depending on what the risk assessment says) don’t require guarding. But other weld cell safety items are likely needed: weld helmets worn, arms and legs covered with nonflammable clothing, fume extraction keeping the air clean, and weld curtains or similar perimeter guarding.

Got Large Weldments? Multiple Fixture Locations?

WELDPRO 360 Mig Weld Booms move quickly from weld to weld, anywhere within a 56’ semi-circle.

They will revolutionize the way your weld shop operates. Your productivity will soar with the ability to quickly move unhindered from one location to another.

Weld Process Controls are placed at the end of the boom, close to the operator, minimizing wasted time spent making changes.

Increased Productivity

Effortlessly Move from Weld to Weld

Complete Area Coverage - No Dead Zones

Robust Design - Built to Perform

760.246.8766

www.andersenmp.com/weldpro-360

Smart Factory Powered by Lantek

Unleash the efficiency of your factory

Take your sheet metal factory to the next level with Lantek. Our cutting-edge software streamlines operations and optimizes workflow with automation tools and real-time analytics. Stay ahead of the competition and thrive in today’s manufacturing landscape with Lantek’s innovative multivendor software.

CAD/CAM | MES | QUOTING | ERP | INTEGRATIONS

www.lantek.com

Trust the leaders in Dust and Fume Extraction

Superior performance. Proper engineering. Sensible pricing.

Get your dust and fume extraction solutions from one of Canada’s most trusted manufacturers with over 30 years of experience.

Industrial Vacuums

Dust Collectors

Wet Collectors

Downdraft Tables

Fume Arms

Vac Ready Welding/Tools

Contact us for a quote

1-800-365-DUST (3878)

info@eurovac.com

www.eurovac.com

"Again, we need to look at the entire application," Edwards said. "It’s not just the robot. It’s fumes. It’s light. It’s heat. It’s electrical hazards, cables, and tripping hazards. We need to take a holistic look, and not just what the robot and end effector are doing. It all needs to be baked into the risk assessment, which drives whether a solution can be done safely or not."

Teach With Care

An application’s safety depends not just on what the cobot carries but also how it moves. Here, the teaching method matters. Offline simulation can avoid disrupting production, and a teach pendant can be convenient, but both methods separate the user from the actual cobot. In doing so, an operator can unwittingly instruct the robot to move in a hazardous way. "It’s the very reason why, when you do use a teach pendant, the arm moves at a reduced speed," Nelson Shea said.

For many precision applications, hand-guided control isn’t practical. "You really can’t move something by hand for just a few millimeters," Nelson Shea said. She added, however, that when hand-guided control is possible, it sometimes can help make teaching safer, "because a person will not cause movements towward themselves."

Consider a pick-and-place task. Using a teach pendant, programmers might just look down at their screen and tell the robot to move from point A to B, never looking up to notice that the cobot arm moves in a way that could easily get in the way of nearby personnel. Even if programmers do look up, operators might not catch how unsafe (and perhaps inefficient) some of those moves are, since he’s looking at the operation from a different orientation. According to sources, the latest teaching software mitigates some of these problems by aligning orientations, so what’s on screen matches what the operator sees in real life.

Regardless, physically moving the arm, and being right there with it as the arm moves from Point A to B, changes the operator’s perspective. They naturally keep the cobot arm low and out of the way.

About Productivity, Not Eliminating Safeguards

Sources emphasized that while certain techniques and methods, like hand-guided teaching, might make an operation safer, they’re no guarantee the application is safe. It still requires a proper risk assessment that scrutinizes all aspects of a cobot application, from the cobot motion and its end effector to the pieces being carried to other aspects of the workcell, like the machine being tended or the welding being performed.

Cobots continue to find new uses too. Some are even being mounted on autonomous mobile robots (AMRs), which come with their own safety considerations like stopping distances, aisle-width factors, and those dictated by where both the automation and people can roam the floor. It’s a complex puzzle.

Both AMRs and PFL cobots have the possibility of fully integrating automation with manual tasks. Done right, such technology could help create the quintessential factory of the future. Such PFL cobot applications might not require a safety fence or guarding, but eliminating safeguarding shouldn’t be the goal. Everything still must be assessed for safety, one application at a time.

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

Universal Robots,

www.universal-robots.com

Yaskawa Motoman,

www.motoman.com

THE

FIRST

ONES IN EUROPE.

30kW

SEE US AT FABTECH

See our Complete Line-up of Flat and Bevel Fiber Laser Cutting Machines at

cutlitepenta.com

Cutlite Penta

Via Baidanzese 17

50041 Calenzano Florence Italy

SAW CITY

The largest sawing showroom in North America

Behringer Saws

Home to our full line of band saws and circular cold saws for every application

610.286.9777

721 Hemlock Rd

Morgantown, PA 19543

behringersaws.com