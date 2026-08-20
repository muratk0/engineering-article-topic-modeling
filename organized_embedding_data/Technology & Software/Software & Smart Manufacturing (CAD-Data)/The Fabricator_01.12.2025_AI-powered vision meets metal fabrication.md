# AI-powered vision meets metal fabrication

[TARİH: 01.12.2025 The Fabricator]

Cover Story

Automation without manual programming

By

Tim Heston

FIGURE 1

This vision-guided grinding cell, installed at Accurate Metals Illinois (AMI), Rockford, Ill., has a camera mounted above the cell. This provides the big-picture view, while scanners integrated at the end of the robot gather the details. Similar systems are installed at Accurate Metal Products (AMP) in Milwaukee, and at Tosec in The Netherlands.

Images: Teqram

W

alk into Tosec BV, based in the Netherlands, and you’ll see the hallmarks of many custom metal fabricators. You’ll hear the buzz of plasma tables, laser cutting machines, and welding arcs. Walk farther into the facility, though, and you’ll start to realize this isn’t just another fab shop.

A robot feeds parts into a flat-part deburring machine. A part-picking system uses two robots to grasp and sort cut blanks into a unique tower system. Grinding and deslagging robots automate an arduous plate edge finishing process. Most notably, the robots’ end effector grasps a conventional right-angle grinding tool, and a camera looks over everything in the cell.

Even more notable is the logo on these automated cells: a stylistic T—the same logo as Tosec and its parent, Tollenaar Industries, a family company with operations in the Netherlands, Germany, and South Africa. Through its Teqram subsidiary, Tollenaar Industries has developed vision-based automation systems tailored for custom fabricators and similar highproduct-mix operations.

Tosec (along with Rime GmbH, its sister fabricator in Germany) initially served as the proving ground for Teqram’s products. If the concept worked at Tosec and Rime, it would likely appeal to other custom fabricators facing similar challenges. Today, Teqram has expanded to the point where it’s now developing new automation concepts directly with new customers.

A common thread runs through nearly all of the company’s automation projects: You won’t find any manual programming or operators using teach pendants. Instead, the automation is guided by vision technology powered by artificial intelligence.

Start With Vision

Frans Tollenaar, chief sales officer and co-CEO of Teqram, together with his brother Roland, co-CEO and chief technology officer, pointed to a vision-guided robot—called the EasyGrinder—as it finished the edges of a plasma-cut plate. The end effector had no specialized grinding head but instead used a commonly available right-angle grinder equipped with a standard disc designed for manual operation.

"We made a very conscious decision when we chose to use hand tools, simply because of the wide range of processes they offer. We can use chisels, belts, carbide burs, grinding stones. We needed that flexibility," said Frans Tollenaar. "And for us, some of these [right angle grinders] can last a year or more. And the abrasives last a long time as well. We’ve had companies like 3M come by, and they’re just amazed at the performance we get out of the abrasives, because we use them perfectly."

Three elements help make this cell possible. First is vision, which eliminates the element that often makes automation impractical for the high-mix, low-volume shop: robotic programming. Why invest in a robot when operators need to spend valuable time on the floor teaching it? Offline simulation can work, but because simulation never matches reality perfectly, operators still need to touch up that program once the job hits the floor. And even the simplest cobot programming interfaces require at least some operator inputs. That time adds up, especially when processing thousands of different parts in small lot sizes.

Back on the shop floor, Tollenaar pointed to a camera above the grinding cell—the EasyEye (see

Figure 1

). The unit incorporates a time-of-flight laser (which measures distance) and a high-optical-zoom lens.

"That camera generates the XYZ coordinates [and correlates them with] the pixels it sees," he said. "Basically, it gives us the coordinates of pixels in space, and with this we can use vision algorithms to determine exactly what the robot needs to do." Scanners integrated near the end of the robot provide the detailed view. "That provides details like holes, protrusions, and other information we need to process the part accurately."

Once the robot knows the exact part it has, it then must extract the features it needs to process the part. Here’s where application-specific logic comes into play. If the robot "sees" a certain set of part features, it knows it must choose a certain tool—be it a grinding disc (see

Figure 2

), a chisel to chip away slag, or another hand tool—to address those features. The robot moves to an adjacent rack to change out tools. It first chooses an end effector holding a chisel hand tool (see

Figure 3

)—the same hand chisel that a human would use. Once it removes the slag, it swaps the chisel for an end effector holding a right-angle grinder, which it uses to smooth and apply a radius to the top edge.

FIGURE 2

A manual grinding tool mounts to a robot end effector with a hinge mechanism that acts as a counterbalance, designed for optimizing pressure for specific tools.

FIGURE 3

A robot removes slag from thick plate using a chisel, the same hand tool a human would use in a manual operation.

As Tollenaar explained, certain applications do require a CAD file, like parts that require only one edge to be finished, or perhaps one side that needs to be ground to a 45-degree bevel. But in typical setups, about 80% of parts don’t require a CAD file. "We scan the pallet, pick up the part, drop it on the [worktable], scan the part in detail, and we grind."

Whether the robot uses only vision or a combination of vision and the CAD file, the only input the operator makes is choosing a predetermined "recipe." Which to choose depends on the quality required. For an oxyfuel-cut part, for instance, the robot would "see" the slag on the edges of the part and know how to perform the following steps: chisel, grind to an edge radius, remove lead-in and lead-out marks, then flip the part and repeat.

"Our goal is for the technology to work like a human would," Tollenaar said. "You give someone a batch of parts and say, ‘Please grind them and give those edges a radius.’ We just want to give a simple set of instructions, and from that, the robot does its job."

Those batches of parts sit on pallets staged in specific places within the grinding cell. Changing pallet positions does take some programming work to establish baselines. But once pallet positions are established, the vision system knows where to look to complete the job. It "sees" the pallet with parts and knows they need to be lifted and placed onto the worktable, processed with different tools (all of them placed on an adjacent rack for automatic end effector changes), then placed on an offload pallet.

About Positioning

Tollenaar next pointed to the EasyFlipper, the cell’s worktable that operates like a clamshell. When the robot is working, the clamshell is open, and powerful magnets secure the plate. Once the robot is finished with one side, the clamshell closes and flips the workpiece, as magnets on one side deactivate to hand off the plate to the magnets on the other clamshell (see

Figure 4

).

This technology covers the second element that makes this kind of high-product-mix automation possible: simple and flexible fixturing requiring no operator intervention. The cell has no hydraulic clamping mechanisms or even simple toggle clamps, just some powerful magnets.

Tollenaar conceded that this does limit the technology to carbon steel and other ferritic material (though the cell can process austenitic stainless steel and nonferrous plates heavy enough to be secured without clamping). Again, this is a highproduct-mix environment where every part can be different. If operators had to enter the cell to rearrange even simple toggle clamps after every grinding cycle, the automation’s value would be diminished.

About Pressure

Hand tools are designed with the human in mind. That is, they’re meant to be manipulated at a specific angle and pressure relative to the workpiece. They’re not built for robots. So, how can the robot adapt—

without

programming?

FIGURE 4

A magnetic fixturing table has a clamshell design. When the robot completes grinding the top edge, the clamshell closes to flip the part. An adjacent rack (near the top of the image) holds various end effectors: a magnetic part lifter, a chisel hand tool, and a grinding disc, among others.

FIGURE 5

A robot positions a right-angle grinder vertically, addressing the heat-affected zone left by the thermal cutting process. In this configuration, a spring mechanism helps maintain the optimal pressure.

The more productive a machine, the easier it is to exacerbate a bottleneck downstream and more often than not, that bottleneck operation is manual. In fact, even the most automated fabricators today have islands of manual operation.

To explain, Tollenaar pointed to a hinged component protruding from the end effector. It’s a counterweight (see Figure 2). "We’ve patented this. We use that counterweight to apply the right pressure and use an encoder to read out the angle." The software uses the data from the vision system, the process logic for each specific tool, the counterweight, and encoder readings to apply the right pressure, feed rate, and RPMs to process the part.

"Consider how the robot uses the tool with a grinding disc in the horizontal position. The disc can be between 0 and 30 degrees. We’ve optimized the counterweight so that we have the right pressure for the tools within those different [approach angles]."

A separate spring mechanism helps establish the correct pressure for tools in the vertical position—say, a right-angle grinder applying a radius to the top edge of a plate (see

Figure 5

).

Cutting, Leveling, Deburring

Today, Teqram has an expansive R&D facility about a block away from Tosec, in an industrial area outside Zwolle, in the Netherlands’ northeast Overijssel province. That facility today has rows of robots and several areas for testing flexible automation concepts for a variety of industrial applications.

The place still has roots in custom metal fabrication. Walk that block back to Tosec and you can see many of those concepts in action. In laser cutting, an expansive part sorter organizes laser-cut parts (see

Figure 6

).

Here again, vision plays a role. The laser-cut nest is shuttled to the offload table, where the EasyEye "looks" at the sheet to establish its true position. The robot refers to the DXF nest layout file and sorts parts onto individual pallets, which then are stored in the adjacent tower. The robots lift parts as heavy as 400 lbs., up to a certain dimension. "These can be installed on existing cutting machines, and could be configured with robot manipulators that can pick up parts up to 1,300 lbs.," Tollenaar said. "And the operator interface is intuitive. It asks operators how they want to group parts, such as by project or what’s needed at a downstream operation."

FIGURE 6

Robots denest a laser-cut sheet at Tosec. The fabricator also uses a hoist system (not pictured here) to lift out entire slat tables so parts can be sorted as cutting continues.

The system can’t handle all cut profiles. Articulating-arm robots can maneuver to lift some challenging profiles, and they make several attempts before deciding to log that a part is stuck and needs to be removed manually; it then moves on to the next part.

"The system is highly dependent on high-quality cutting results," Tollenaar said. "It needs kerfs to be wide enough and parts to have sufficient clearance to denest consistently." That said, the system is designed to handle a range of part sizes. Robots can lift mini-nests of tiny workpieces, while at some installations (though not at Tosec), hoists lift cut blanks that span a significant portion of the entire cutting table.

Walk downstream and you’ll see robots feeding flat-part deburring, and Teqram has similar technology available for feeding part leveling systems. For part leveling in particular, vision technology works on multiple fronts. It recognizes the part the robot is lifting and knows when a part is being reversed through the machine for another pass. It also can measure the ultimate part flatness and sort each part accordingly—either onto a "good part" pallet or another pallet with rejects.

When feeding a deburring machine, robots can place multiple parts next to each other on the belt. Vision also monitors the offload station after deburring. When there’s a backup, the automation slows or halts the operation until the bottleneck is cleared, "just like a human operator would," Tollenaar said.

Automate the Constraint

Modern metal fabrication machinery has become extraordinarily productive. Still, the more productive a machine, the easier it is to exacerbate a bottleneck downstream—and more often than not, that bottleneck operation is manual. Even the most automated fabricators today have islands of manual operation. Lasers cut lights-out, but workers arrive the next morning to sort hundreds of cut blanks, then manually feed at least some of those blanks into a deburring machine, perhaps even a part leveler.

As the automation employed by Tosec and developed by Teqram demonstrate, vision and AI technologies show significant promise, even for the most high-product-mix job shops out there. As innovation marches forward, those islands of manual operation could gradually go away.

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

Automated Fabrication Systems,

automatedfabricationsystems.com

Teqram BV,

teqram.com

Tollenaar Industries,

tollenaar.industries

Tosec BV,

tosec.nl

The Tollenaars in Metal Fabrication: A Brief History

Frans Tollenaar is part of the second generation of a family business that’s come a long way since his father left the Netherlands for South Africa. "He did it for the adventure of it all," he said, "and in Pretoria, he founded a small tube manufacturing plant, Tubecon, which today is a leading tube manufacturer in South Africa. That’s where it all started."

In the late 1980s, Tollenaar’s father returned home to the Netherlands. The family acquired Tosec in the 1990s and, in the ensuing years, also acquired Rime GmbH, a large-workpiece fabricator in Riesa, Germany, between Dresden and Leipzig. In 2012, they launched TME, a mechanical engineering firm specializing in offshore and bulk handling equipment, which later purchased Martec, a specialist in wear-resistant materials.

In 2016, the Tollenaars launched Teqram to develop and sell automation systems using AI-powered vision technology. Today, the company has partnered with Automated Fabrication Systems to sell and support installations in North America.

Efficient deburring and leveling.

Deburring and leveling technology from a single source:

www.arku.com

Increase productivity:

with double-sided deburring and edge rounding.

Optimal downstream processing:

thanks to flat and stress relieved parts, sheet and plates.