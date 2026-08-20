# Cut, sort, stack, done

[TARİH: 01.05.2024 The Fabricator]

Automation

Automated part sorting for laser cutting gets flexible

By

Jacob Fogarty

L

aser cutting automation isn’t novel. Load/unload systems have been around for years, as have material handling towers designed to hold sheets as well as nests of cut parts. One element, though, has been conspicuously absent: automated part removal and stacking. An operation might have a collection of towers with lasers running constantly over multiple shifts—but right next to all this, laborers manually lift or shake pieces out of nests.

Part removal and stacking automation is finally getting some time in the limelight. As the chronic labor shortage meets ever-more-powerful laser cutting systems, fabricators are taking a second look at the technology and, in the process, rethinking their high-product-mix part flow strategy.

Part Sorting Basics

Sorting technologies vary greatly depending on the application, but most high-product-mix part sorting occurs with either a Cartesian system or a 6-axis robot. Each has its pros and cons, but all must accomplish three basic tasks: lift parts out of the skeleton, stack them, then dispose of the skeleton.

Each step is carefully engineered for optimal efficiency. For instance, modern robot systems rely on various grippers, both suction and magnetic, to grasp a variety of parts. And, theoretically, they also could remove the skeleton. That said, for best efficiency, some setups rely on a separate fork system that lifts the skeleton off the table and back into a specific cartridge in a material handling tower or other area for later disposal.

Finding Balance: Cutting and Sorting

Part removal automation stands apart from other laser cutting automation in that it often requires a new approach to the entire process. Fabricators start thinking about cycle times in both laser cutting and part sorting. Part sorting systems move from point A to B, so per-part sorting time is straightforward to calculate. Whether it’s picking a part just inches long or wide or a cut blank that’s nearly the size of the entire sheet, the robot moves the workpiece the same way.

The real trick is balancing the time it takes to cut with the time it takes to sort, especially on systems with a single offload station. In certain setups, two cutting tables shuttle back and forth between the laser cutting and part sorting work envelopes. The arrangement requires some careful load balancing between cutting and the part picking station. Ideally, the laser finishes cutting a nest just as the part sorting system finishes sorting and moving the skeleton off the table. This in turn changes how shops look at their parts and decide what, when, and how to nest.

Nesting for Part Sorting

Traditional approaches to nesting maximize material yield while accounting for certain constraints, like grain orientation and scheduling, not looking too far ahead to minimize work-in-process (WIP). Automated part sorting adds another layer to nesting strategy.

Programmers optimizing part sorting need to consider what nest layout would optimize the motion of part removal automation and, at the same time, make life easier for operations downstream. A complex part with many contours requires more laser cutting time, yet it doesn’t take any more time to sort. Meanwhile a laser can cut a dozen of small part profiles in seconds, yet it can take serious time for part picking automation to stack each small piece individually. For this reason, programmers might avoid a nest layout with numerous small parts, but instead mix large and small parts together.

Here, the mini-nest has become one relatively well-known strategy. Programmers group parts together so that part removal automation can lift them out in one motion. Nesting a variety of part sizes together can help here as well. If your mini-nest groups large and small parts together, it might not need any tabbing (though this, of course, depends on the exact part geometries and material you’re dealing with). No tabbing means no deburring and, ultimately, higher-velocity part flow.

Keep Sorting Stable

Part stability depends on what geometries you’re picking and what you’re using to grip with. Standard grippers can use magnets or suction cups. Larger parts can require specific kinds of grippers, but with certain kinds of automation, especially those with robotic arms that can change gripper heads, large parts don’t present many challenges.

Part thickness factors also come into play. A 12-ga. part and a 0.5-in. part will each require an entirely different picking strategy. Today’s grippers can be built with very strong magnets that can lift extremely thick parts out of a nest. To lift thick nonferrous parts likely will require a gripper with more suction cups in a smaller space to achieve the required part-weight capacity. Some part picking applications have been engineered to accommodate up to 1-in. plate.

This range of thicknesses for part picking has become possible thanks to gripper systems that can "jiggle" parts loose, if needed. This, combined with specific cutting strategies like small reliefs in corners, can make part picking an extremely repeatable process. Combine this with modern, high-powered lasers with beam shaping—that is, they optimize the kerf width for the application—and automated part picking becomes even more reliable.

Reliable part picking is the primary reason why some systems keep a cut nest on the same cutting table that was in the laser cutting work envelope, rather than transporting it to a separate sort table. Keeping that cut sheet on the same table means there’s minimal chance of parts being jostled before the gripper grasps them.

The act of automated part removal—and the fact that the cut sheet is never moved from the cutting table—can also increase the benefits of common cutting, a nesting strategy that might be otherwise avoided. And it’s avoided for good reason. Yes, common cutting can dramatically shorten cutting time (since you’re cutting two part edges at once) and increase material yield. But part stability can be a concern.

A robot sorts a nest of disparate parts. Once sorting is complete, a fork system lifts and removes the skeleton.

A robot gripper places a part on a pallet. To the left, additional grippers, designed for a fabricator’s product mix, are staged and ready for use.

Suction grippers neatly stack various parts onto a single pallet.

For automated part sorting, where the sheet remains clamped in place as it’s presented to the robot, the situation changes. In fact, common-cut parts can

make it easier

for grippers to lift parts out of a nest. A common cut effectively eliminates the possibility of a part getting caught in the skeleton on that common cut edge because, well, there is

no skeleton

between common-cut parts. Yes, common cutting complex part geometries can cause issues, and programmers still need to ensure those common-cut parts will remain stable and stationary after cutting. But for automated picking of simple parts especially, common cutting should have no negative effect on overall stability.

Exceptions exist, of course, and today’s part removal automation can account for many of them. For instance, say you have a cutting issue that causes a stubborn part that’s difficult to lift. Instead of trying to lift it blindly, the robot gripper can detect the issue and will actually release the piece, then move on to picking other pieces in the nest. It then returns to that stubborn part and attempts to lift and shake it out again. If subsequent attempts fail, the system flags the part in software, notifying personnel that the piece is being offloaded with the scrap. If needed, someone can manually retrieve the part from the skeleton.

The True Value of Good, Flat Material

Uncontrolled movement is the enemy of reliable part sorting. If material warps after cutting, part removal simply becomes less reliable. Some clever moves of the cutting head and part removal automation, as well as good sheet clamping, can account for some level of warpage. But if material, say, bows up between 0.5 to 1 in. after cutting, part sorting becomes very difficult.

As always, "engineering out" the problem remains the best approach. This could involve using better laser-flat material with balanced internal stresses so that parts don’t bow after cutting. Of course, some part geometries—like long, thin pieces—are more susceptible to bowing in general. If the problem truly can’t be engineered out, some systems do allow for flexibility.

For instance, say you have a bundle of material you know isn’t going to sort well. In this case, you could cut those nests and simply bypass part sorting, turning the laser cutting automation into a conventional load/unload system. This isn’t ideal, but it’s at least one solution that can help maintain throughput even with subpar material.

Best Cutting and Maintenance Practices

Increased fiber laser cut quality has been driving more fabricators toward automation in general. Years ago, many parts emerging from a fiber laser had to be sent through a deburring machine, which then became a choke point. Today, parts denested from the laser can head right to the next major manufacturing step, no secondary processing required. To make this happen requires good operational and maintenance practices.

Maintenance of part removal automation can be straightforward, especially in robotic systems. Robot joints need to be greased and sensors need to be cleaned. Outside that, the system can keep working for years without any major incident.

Of course, automation is only as reliable as the laser cutting machine it’s working with. It can’t lift parts or skeletons that have been inadvertently welded to dirty slats. Regular slat cleaning is a good practice no matter how automated a laser is, especially with today’s high laser powers. Dirty slats can alter a sheet’s position in Z and, hence, change a laser’s cutting characteristics, leading to long setups and rework. When you add automation, the cost of poor slat maintenance gets even more obvious.

The same could be said for other best operational and maintenance practices in laser cutting. If parts tip or experience a loss of cut, with the molten kerf metal welding back together behind the laser beam, part removal automation won’t be able to do its job.

This calls for a collaborative effort between programmers and operators. The operator must inspect and prep a system for an automated run. Are the slat tips clean? Is the protective cover glass on the cutting head free of contamination, and has it been changed recently? Are nozzles clean and in good working order? Is the assist gas flow that surrounds the laser beam creating a clean path down the kerf?

On the programming side, how are parts susceptible to tip-ups or bowing being addressed? For parts susceptible to bowing or tips, does the head raise in Z after cutting? Are programmers taking advantage of heat mitigation techniques, like cutting alternately in different quadrants of the sheet so heat doesn’t build up in a single area and cause distortion?

Also, considering the speed of modern lasers, slug-destruct toolpaths have become the norm. Rather than risk a slug tipping up and getting caught within a part, the laser cuts it into pieces small enough to fall through the slats without issue. Some parts highly susceptible to tip-ups could, again, be tabbed together with other small parts in a mini-nest.

Similar toolpath strategies apply for corners, where corner-relief-cutting routines can make part removal easier. This might require thicker web sections in the nest, but again, that slight material yield reduction is usually a very small price to pay for the predictability of a well-implemented automated system.

The same could be said for all best practices when it comes to laser maintenance. An automated laser that’s down just results in a lot more capital equipment sitting idle, waiting to work—and, not least, a lot of lost capacity.

Flexibility, Kitting, and Part Flow

Imagine someone bends five parts the wrong way on the press brake. One big reason part removal automation is starting to gain traction, outside of the labor shortage, is intelligent software. If the brake operator scraps five more workpieces than anticipated, he can report that to software, which immediately communicates the situation to laser programming. The programming software "remembers" what it needs to do to cut and sort those specific workpieces. So, it inserts those five parts into the next available nest. In short order, five extra parts appear on a pallet at the press brake.

And though it might sound counterintuitive, part sorting automation actually makes smaller batches and even kit-based flow a lot more manageable. This again has to do with software control. With manual denesting, a fabricator might choose to avoid dynamic nesting and run large batches of single pieces just because they’re easier to sort manually and less likely to get lost. That large batch lumbers on to bending and welding, where it sits as mating components make their way through the job routing.

Dynamic nesting coupled with part sorting changes this scenario. The system can sort various small batches and kits onto numerous pallets. Software instructs what parts should go on which pallet. Once those kits are complete, pallets can be transported immediately downstream. WIP inventory doesn’t stay WIP inventory for long before being bent or welded.

Remnant Management

Demand variability is another reality, especially for high-product-mix fabricators. This is why, traditionally, nesting software uses "filler parts" or looks far out into the schedule to fill a nest layout—all done to boost material yield in the face of variable demand that would otherwise force a shop to deal with a lot of remnants.

But are remnants really a problem? The need for them often keeps high-product-mix operations away from automation. But, contrary to what you might think, robotic part sorting actually makes remnant management easier. Say you have a nest that takes up just half of the sheet. The robot can pick and stack parts, then switch grippers (if needed), grasp the remnant, and place it on a separate pallet or vertical rack.

Another laser could process the remnant, but so could the laser with automated parts picking. The remnant does require manual loading into the laser, but once the laser cuts the material, the part picking automation treats that remnant like it would any other job.

Think Anew About Throughput

Imagine you’re at a fabricator that’s updating a 10-year-old system with a new fiber laser. Considering the advancements in recent years, even a new fiber laser with automated load/unload (no part sorting) will double or even triple the amount of throughput you’re used to seeing. What used to be a two- or threeshift operation now just needs one shift to cut all the blanks downstream operations need.

Demand increases, so you push more cutting into second and third shifts. But what happens to those cut parts? Do they sit in the skeleton and wait for sorting? At this point, you decide it’s finally time to automate the sorting.

Now the laser cutting strategy changes. Parts aren’t "finished" cutting until they’re stacked on a pallet, ready for forming or another operation downstream. Automatic sorting does come with some constraints and tradeoffs. The programmer might choose to create a mini-nest to ensure part sorting reliability or to balance the sorting and cutting cycle times. And material yield might suffer a little, since parts really can’t be placed just anywhere on a sheet, especially if it makes for difficult or inefficient sorting.

Even so, automated part sorting has made the complete laser cutting cycle time, from sheet loading to blank stacking, extremely predictable. If the system says parts will be stacked and sorted at a specific time, there’s a very good chance they will be. For a fabricator’s primary cutting operation, that predictability has incredible value. It helps reduce WIP, streamline flow, and, ultimately, boost the throughput of the entire shop floor.

Jacob Fogarty

is automation specialist at Mazak Optonics Corp.,

www.mazakoptonics.com

.

For the fabricator looking to maximize

their production time and profits, the Lightning Rail is a smart decision.

Eliminate the countless manual labor hours involved in laying out handrails, stair stringers, trusses, and more!

Cut fabrication time by more than 50%

Ensure the highest level of accuracy

Boost your profit margins

Lay out complex geometry in seconds

Designed to replace your existing fabrication table

Patent No. US 10,576,588 B2

Patent No. US 11,426,826 B2

by Automated Layout Technology™

603-402-3055

AutomatedLayout.com

Why Choose

RELIANT Finishing Systems

Whether you need a small industrial oven or a turn-key finishing line, we can help! We’ve designed and manufactured over 1,000 systems since 2005. We offer a great warranty and free lifetime phone support.

Since we sell factory-direct and don’t use distributors or sales representatives, the same team of people will be with you before, during, and after the sale.

We’re dedicated to providing a 5-star customer experience. Don’t take out word for it, check out our online reviews.

256-290-7907

3 ROLL HYDRAULIC PINCH PYRAMID PLATE BENDING MACHINES

The 101 Series from WDM.

Over 40 years of experience with 3 generations working in the business.

Built in USA with American and global components.

30 gauge to 1" thick, 1’ to 12’ wide.

Custom and built to order options available.

Have a rolling question? Call and speak directly to the designer, engineer and manufacturer of WDM machines, right in the USA.

Waldemar Design & Machine LLC

224 Pierpont Street

Petersburg, WV 26847

606-787-8474

drisser@wdmrolls.com

www.wdmrolls.com

From complete custom forming cells to many popular/standard machines in stock.

Contact us direct, or contact your favorite machine tool distributor and ask about WDM Machine Tools.

3 & 4 Roll Hydraulic Double Pinch Plate Bending Machines Initial Pinch Sheet Plate Bending Rolls • Bending Systems & Complete Forming Cells