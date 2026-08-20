# Getting to the Root of Pipe Welding Automation

[TARİH: 01.03.2015 The Fabricator]

Technology Spotlight

Adaptive welding spurs automation in spool fabrication

By Tim Heston, Senior Editor

In this automated setup, a robot arm performs the root, fill and cap passes of a pipe will, adjusting parameters on-the-fly.

A

full-penetration root pass in an open bevel joint represents the epitome of pipe welding skill, and this applies in the fabrication of pipe spools; that is, a subassembly of pipes and fittings welded in pipe shops and then sent into the field. If the welder deposits metal too far above the weld pool, it sinks and cools prematurely, so fusion is incomplete. But if the welder keeps the arc in front of the weld pool, and at just the right height, hot metal flows toward the root and, voila! he gets a full-penetration root pass that should pass muster.

To perform the root pass, an expert welder must "read" the weld pool carefully and react instantaneously to any changes, and it’s this skill that piqued Francois Nadeau’s curiosity in the 1980s. At that time Nadeau headed the welding automation group of the National Research Council (NRC) of Canada.

"This was a period when a lot of vision systems were being developed," Nadeau said. "If you went to the welding tradeshows at the time, you often saw about 15 companies that were putting together vision systems for welding automation." He added that many of these vision-system companies aren’t around anymore, mainly because manufacturers found it more cost-effective to adapt processes to automation by making weld preparations more consistent.

But pipe spool fabrication is different. "It’s not practical to have a perfect, repeatable preparation," Nadeau said. "You’d have to remachine all the flanges and pipe ends. It’s a delicate operation with a [weld] preparation that by nature will vary."

This is where Nadeau and his team saw opportunity. For years pipe welding operations had installed automated systems for the cover and cap pass, but they had yet to automate the root pass successfully. If the fabricator had any automation at all, it required additional handling between the hand welding and automated station.

"So we focused on this," he said, "and developed a vision system and control strategy that varies the welding parameters dynamically to control the penetration of the root pass."

From this came a new pipe welding automation technology. To commercialize it, Nadeau left the NRC in 1989 and launched Tecnar Automation, Saint-Bruno, Quebec, Canada. The company soon released the first iteration of Rotoweld, a DOS-based mechanized system with separate root and fill pass welding guns.

Last year the company released the third iteration of the technology, Rotoweld 3.0, which uses a custom robot to perform 1G girth welds. The robot arm performs the root, fill, and cap passes with one welding gun, though the system still can be configured with multiple processes. For instance, a thickwalled pipe might call for gas metal arc welding (GMAW) for the root pass and submerged arc welding (SAW) for the fill and cap passes.

Most spool welding jobs rarely consist of only straight pipe-to-pipe connections, but instead involve one curved elbow piece, a flange, or other shape that needs room to spin as the pipe is rotated under the welding gun. The robot and the rotary positioning system provide the necessary clearance so the pipe elbows and similar shapes can spin freely without hitting either the floor or the welding carriage.

Near the end of the robot arm is a vision camera that focuses on the arc at about a 90-degree angle. The welding gun approaches the joint at a 45-degree down-hand angle with an additional 30-degree gun angle, emulating a downhill pipe weld. The camera sees heat distribution in the weld pool, which correlates to how metal circulates within it. When the gap changes, so does the distribution of heat and the weld pool characteristics. Like a human pipe welder, the automation reacts by adapting weld parameters on-the-fly.

"It reacts by adjusting the travel speed, wire feed rate, arc voltage, and oscillation width," Nadeau said, "so that everything is kept at the right level in relation to the weld pool, and it pushes the hot metal to the bottom."

The adaptation calls for some complex control algorithms, because one parameter doesn’t necessarily relate in direct proportion to another parameter. When the system increases its travel speed, it also increases the wire feed speed, but not necessarily in the same proportion to the travel speed.

The system continuously analyzes an image of the root weld pool, as recorded by a video camera incorporated into the end of the robot arm.

The adaptive characteristics become very noticeable when it’s laying a bead over tack welds. "Those fullpenetration tacks, of course, stay in the weld," Nadeau said. "When you go over the tacks, you see the machine react suddenly as it changes the weld characteristics to increase penetration. Once it passes the tack, it changes immediately back to the previous parameters."

For the root pass, the system has used pure CO

2

to shield the shortcircuit transfer. "CO

2

increases the surface tension of the liquid steel," Nadeau said, "and that’s an advantage if you want to carry a lot of heat to your weld pool [for penetration] and yet not have it melt through." That’s why previous iterations of the technology used pure CO

2

shielding with specialized power sources, such as Lincoln Electric’s Surface Tension Transfer

®

, to ensure complete penetration during the critical root pass, then a conventional power source (GMAW, FCAW, or SAW, depending on the application) for the fill and cap passes. But the latest version of the technology uses digital mass flow controllers for the shielding gas, which allows the system to supply an unusual gas mixture. This, Nadeau said, helps provide good penetration characteristics even with a conventional power source.

"The material has got to flow. In a spool shop, minimizing handling is the key to profits."

—Francois Nadeau, Tecnar Automation

"We discovered that if you add a little argon into the CO

2

, you can get almost as good of an arc with a conventional power source as you can get with an STT power source," Nadeau said, adding that STT still is an option should the application call for it.

That unusual gas mixture—25 percent argon and 75 percent CO

2

—isn’t stable when mixed in a cylinder, so the flow controller mixes the gas from two bottles and sends it to the weld for the critical shortcircuit root pass to achieve complete penetration even over the weld tacks. If the configuration uses, say, spraytransfer GMAW for the fill and cap passes, the flow controller then switches to a gas mixture like 8 percent CO

2

and 92 percent argon.

Like any technology, the system has limits. Although it depends on the application, material, and pipe schedule, the automation can adapt to fit-up tolerances that are only so wide. According to Nadeau, though, the system can adapt to tolerance windows even a little wider than specified by Pipe Fabrication Institute (PFI) standards.

Most significant, he said, is that the system introduces automation to a traditionally manual process and, ultimately, helps minimize handling and increases productivity. "The material has got to flow," Nadeau said. "In a spool shop, minimizing handling is the key to profits."

Tecnar Automation, 1321 Hocquart, St-Bruno, Quebec, Canada, J3V 6B5, 450-461-1221,

www.tecnar.com