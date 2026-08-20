# Laser welding and the cobot

[TARİH: 01.03.2026 The Fabricator]

Cover Story

The middle ground of laser welding automation

By

Tim Heston

A cobot wields a laser welding gun as a workpiece is rotated vertically. Cobot welding systems, including those for laser welding, have moved beyond simple fixturing to include setups involving coordinated motion.

THG Automation

F

or years, laser welding has been looked upon as the "next big thing" in metal fabrication, a perfect complement to precision cutting and bending. Benefits include not only speed but also just how perfect the resulting laser welds are. Products are welded and then moved promptly to the next major manufacturing step.

Advanced robotic laser welding cells can be designed with high laser powers for extremely efficient, deep-penetration welding. Programming and process simulation also have come a long way. With modern software and intuitive user interfaces, dialing in a part program isn’t as arduous as it once was.

The technology has permeated certain sectors, especially automotive, but it has yet to dominate the custom and contract metal fabrication space. Hand-held laser welding has emerged as an alternative, especially for relatively lower-power-density applications.

Some challenges remain, though. Hand-held laser welding is far different from conventional gas metal arc and gas tungsten arc welding. Someone who’s wielded a GTAW torch for decades can have trouble adapting, as the laser welding gun’s wire feed guides the weld travel speed and standoff distance. Welders usually don’t "push" but instead "pull" the laser welding gun back toward themselves.

Growing quantities present a common conundrum. In low-volume settings, hand-held laser welding makes sense. But how does a fabricator scale the operation? In recent years, an alternative approach has entered the market: the collaborative laser welding robot. Like any technology, cobots don’t fit every laser welding application, but they do open the door to a host of new possibilities.

THE LASER WELDING COBOT

At FABTECH 2025, Matt Hendey pointed to a Universal Robots cobot positioned on a weld fixturing table. The founder of Indianapolis-based THG Automation held a tablet with a user interface designed to simplify programming; the cobot held a hand-held laser welding gun.

Cobot laser welding at THG goes back several FABTECHs, during a dinner conversation between company representatives and a custom metal fabricator. The shop owner spoke with the reps about the emerging coordinated motion capabilities of cobots, opening the door to the use of rotating and even multiaxis weld fixture tables.

"For his application, the coordinated motion was important," Hendey recalled, "because the robot needed to coordinate with a rotating frame."

The setup required the full range of coordinated motion, with the gun and workpiece moving separately and in concert. The motion system also supported the cobot itself moving on a linear track to, say, complete a very long weld.

He added that coordinated motion and cobot laser welding are two separate technologies, and one can build on the other. A shop might decide to add a cobot to a hand-held laser welding system, then augment that technology with coordinated motion.

That coordinated motion works with laser-welding-specific commands. For instance, consider a setup in which the part rotates and the robot stays stationary, creating a circular weld. The operator can choose to use welding wire until the very end, where the bead overlaps slightly with the start of the weld. "Here, you can choose to finish without welding wire for those last few millimeters of rotation," Hendey said.

Perhaps most significant, if a welder needs to use the hand-held gun manually, he can flip a switch, unbolt a bracket, and remove it from the cobot. Flipping the switch moves the laser welding system to manual mode. "The changeover takes about five minutes," Hendey said.

PERSPECTIVE ON PROGRAMMING

Walk the FABTECH show floor and you’ll see numerous vendors touting offline robot simulation. Programming time at the cell is nonproductive time, so the idea is to eliminate as much of that programming as possible. Thing is, most fab shops still use traditional teach-pendant programming.

"Offline programming has a lot of value, Hendey said. "And there are a ton of great software packages out there that support various robots, including cobots. But the challenge we find is that companies find it faster to program manually on the floor."

Offline programming demands engineering resources, and because the 3D model nearly always differs slightly from the actual part the robot works with on the floor, tweaks at the robot inevitably need to be made.

A cobot works with a rotating workpiece as it laser-welds a circumferential joint.

THG Automation

Modern control interfaces help simplify cobot programming, even for applications involving coordinated motion.

THG Automation

Intuitive programming interfaces have emerged, especially for cobot welding. For years, fabricators have used cobots mostly for simple, point-to-point welding, with a part fixtured. The welding was limited to where the robot could reach.

Today is different. Hendey described one application in which a cobot equipped with coordinated-motion capabilities rides on a long, linear track. "To use this, you’d tell the robot where to start, then use the control interface to move the cobot to the other end of the track to establish the end point. At this point, the cobot knows not only that it’s traveling along the stationary part, but it also knows that the base is associated with a world coordinate system. But operators don’t need to deal with all that."

Hendey described a complex auger application to illustrate the kind of simplified programming interfaces now available. He pointed to a model on the tablet, showing how the operator can pinpoint different locations along the spiral joint geometry. "As it rotates, you can specify starting points. As it rotates, you then might see you start to have a downhill weld. To change that starting point, you can just choose one, and all the other points will change with it, with no need to reprogram and no need to do all the math in your head. To finish the program, you’d need to set a point every 45 degrees [of auger rotation] so the system moves along the [spiraling] weld seam."

SAFETY CONSIDERATIONS

Hendey added that coordinated motion systems aren’t necessarily "collaborative." Yes, many cobots (including UR’s) are power- and force-limited systems; when they sense an obstacle, they stop. But the level of safeguarding required depends on the application: that is, what tool the cobot is wielding (like a laser welding gun) and what it’s working on. The track the cobot rides on and the motion systems holding the workpieces have their own safety requirements.

"These specific systems aren’t collaborative in the sense that you can’t just physically move the linear axis by hand, nor can the axis detect something that it hits."

Conventional robotic laser welding cells sit in interlocked, light-safe enclosures—and for good reason. Just like fiber laser cutting machines, fiber laser welding uses 1-μm beams that can cause permanent vision damage. Yes, laser welding power sources do have systems that deactivate the beam when there’s no contact with the workpiece. Still, you can’t get around physics. There’s no arguing about the fact that a fiber laser’s 1-μm wavelength can harm the retina permanently.

Kirk McCauley knew this before purchasing his first laser welding system. After all, the president of American Engineering & Metalworking, a custom and contract metal fabricator in North Canton, Ohio, knew that his fiber laser cutting machines were fully enclosed. He treated hand-held laser welding in a similar way.

He opened the interlock to his laser welding room. There, a collection of weld fixture tables sits next to hand-held laser welding power sources from IPG Photonics and Lincoln Electric, along with a cobot laser welding machine from Pittsburgh-based Cobot Systems. Every person entering the cell dons personal protective equipment suitable for laser welding.

Several months ago, McCauley joined a safety council on hand-held laser welding at the Laser Institute of America, where he’s giving input on the safety training needed by those working with all levels of laser welding, from hand-held to cobot to traditional robotic systems. This includes laser safety officer (LSO) training requirements, especially for those operations new to industrial lasers and unfamiliar with the LSO’s role. (For more on this, see "Staying safe with hand-held laser welding," available in

thefabricator.com

archive.)

The light-safe laser welding room at American Engineering & Metalworking protects workers and allows the fabricator to take full advantage of hand-held and cobot laser welding. The exterior indicator light (top far right) shows those nearby when laser welding is taking place.

AEM

McCauley also is suggesting ways to communicate safety standards to make implementing them easy and intuitive—like QR codes on safety documents that take users directly to tutorial videos. "I’m there to give real-world advice and suggestions. For instance, those QR codes could show people the basics, like what a safety interlock actually is. We need to boil down and simplify, so the information connects with people. We need everyone thinking about safety."

Reflecting on this, he then pointed to the paneling of AEM’s laser welding space. "We tested those panels. The room is light-safe, and we have fans for circulation and fresh air. I tell everybody, buying the hand-held laser welding system is half the investment, at best. The actual [interlocked, light-safe] room can cost more than the laser system itself."

FILLING OUT THE MIDDLE

McCauley added, however, that AEM’s safety investments were worth it, simply because they allow the company to make the most out of handheld and cobot laser welding technology, including the elimination of postweld grinding and weld blending. He then gestured to the cobot laser welding cell, explaining that the technology covers a bit more space in the "middle" between manual welding and traditional robotic laser welding cells.

Hand-held laser welding is the baseline, streamlining precision welding jobs. Cobot laser welding brings that baseline up a level. He then moved his hand far above, signifying the highly productive space occupied by traditional robotic fiber laser welding cells. Those laser welding robots provide immense value but also require significant upfront investment. The investment can make sense in certain situations. But there remains opportunity in the middle, between those traditional robotic laser welding cells and cobot laser welding setups. He added that with more technology options will come greater adoption.

With precision cutting and bending presenting assemblies with tight fitups, the stage remains set for the laser to weld a joint clean, no grinding or polishing required. Realizing the potential efficiency, and having safety protocols in place, a fabricator’s next step is to determine the best laser welding technology to fit its current and potential product mix—manual, cobot, a conventional robotic laser welding cell, or some combination thereof. Considering the advancements in coordinated motion and other aspects of hand-held and cobot laser welding, the choices will become only more numerous in the years to come.

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

American Engineering & Metalworking,

www.aemquality.com

THG Automation,

thgautomation.com

Universal Robots,

www.universal-robots.com