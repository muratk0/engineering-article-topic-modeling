# Avoiding the offload bottleneck

[TARİH: 01.04.2020 The Fabricator]

Do your denesters keep pace with the laser?

By Jason LeGrand

Automated sorting lifts individual parts and places them in a known location.

T

he industry has two schools of thought when it comes to automated offloading in laser cutting: sorting and picking. Picking, the more common approach, is when completed sheets, skeletons and all, are offloaded and stacked on a pallet; in more advanced picking systems, individual parts can be picked out of the skeleton, but not necessarily placed in an organized way. Sorting is when individual parts are removed and automatically placed in a known location for future use.

Before we dig in further, it’s important to understand the state of play. In recent years both the power and speed of laser machines have increased and gradually become more accessible; technology like the fiber laser has the potential to boost throughput for shops of all kinds. There has been an unintended consequence as well: Lasers are starting to outperform the offloading operation. Where a shop’s bottleneck may have once been—at the laser—has now moved to organizing the parts.

Does your shop host denesting parties? These "parties," at which the team gathers at the stacked sheets to remove and organize parts from skeletons, aren’t as fun as they sound. Manually sorting through dozens of sharp-edged metal parts per sheet can be not only dangerous, but also result in a tangled, damaged mess.

Don’t forget other inefficiencies in manual denesting, like when the part needed next is at the bottom of the stack (a common occurrence because the first part needed is often cut first), the mixing up of tough-to-distinguish left- and right-hand parts, as well as parts being tangled or damaged.

These difficulties have sparked a wave of picking and sorting innovation. These automated systems are gaining popularity because they are becoming easier to use and integrate. That said, every technology has its strengths and weaknesses. To make the most of picking and sorting automation, you need to explore the beginning, middle, and end of your picking and sorting process.

Positioning the Sheet

Whether picking or sorting, it all starts with the system knowing where the cut sheet is in reference to the table. Most use the laser cutting head to identify edges and square the coordinate system once the sheet has been set down, a perfectly fine approach.

The alternative, however, aerial positioning, can save 20 to 30 seconds a sheet. As the sheet descends to the surface, pneumatic blocks move against the edges and square it to a known location. By the time the sheet comes to rest on the table, it’s already at a predefined origin. After the load frame withdraws, no additional position adjustment or confirmation is necessary.

Consider the size of the parts that will be cut. This will be a little different for each laser depending on the table, but parts should contact at least three slats. If it’s less than three, the pressure from picking or sorting automation’s vacuum or magnet module can force the part to tip or fall down and become an obstruction or tangle.

If part size isn’t flexible, there is a nesting solution for picking small parts. You can tab smaller parts together—leaving small slivers of material connecting them—to make a part cluster that won’t slip through the slats. The automation can then pick the cluster as one piece, and employees can separate the parts later by hand.

Removing Parts and Sheets

When removing entire sheets for manual sorting, factors like gripping method, weight, and material come into play. A clamshell can remove whole cut sheets, of course, but so can arrays of magnets or vacuum-gripping modules.

The configuration of these magnet or vacuum arrays is of less importance when picking whole sheets, but removing individual parts for sorting is a different story. To avoid damage and tangling, it’s crucial to lift parts straight out of the skeleton. Parts should be gripped as close as possible to their center. More vacuums or magnets in the array allows for more granular locating, improving the chances of on-center gripping.

Systems today range from 10 or 12 large vacuum modules to up to 320 small vacuum modules. Even with numerous vacuum modules, you still need to consider some important variables. First is material thickness: ⅜ in. thick is a safe limit, though some systems can handle thicker material depending on the application and the nest layout. Even so, since lifting from the part’s perfect center of mass isn’t always possible, the thicker the materials get, the more tendency there is for that part to bind.

Sheet flatness is also important. A sheet of steel might look flat and solid, but once you heat it up with laser cutting, whatever internal stresses have been hardened into it will begin to release. The sheet might start to distort, and some distortion—like oil-canning or potato-chipping—can have serious effects on the ability to pick and sort automatically. If the parts or skeleton warps, edges can get caught or the center of mass can move, running the risk of damage.

Unfortunately, there is no surefire way to predict such movement. However, today’s most advanced systems can be programmed to attempt to pick a certain number of times and notify the operator of unclaimed parts on a sheet.

With the right nesting and cutting strategy, even narrow or oddly shaped parts can be nested and cut so that grippers lift the pieces smoothly out of the skeleton.

In this automated picking application, grippers lift a cut part and place it in a designated area. In this simple laser cutting operation, the kerfs span the width of the blank, so there’s no scrap or skeleton. Unlike automated sorting, automated picking does not stack parts in an organized way.

When you get into sorting, the removal devices get more sophisticated. Some robotic pickers and cantilevered vacuum systems, for example, use a cartesian gantry system with X/Y axes and a Z that lowers a magnetic or vacuum gripper to collect and, if necessary, rotate parts up to 360 degrees for placement in a known location. Whether picking or sorting, each arm and tooling must support the weight, size, thickness, and material of the parts. If an arm can handle 1,100 pounds but the tooling only a few hundred, or vice versa, the system is not optimized.

The relation of the shapes and angles of the parts on a sheet plays a huge part in the ability to pick parts cleanly. Fortunately, we have some control over this in how sheets are nested and edges are cut.

Planning the Cut

If you’re programming a laser without automation, there are very few offloading considerations. You can put parts at any angle or very close to each other. It’s not a big problem if the skeleton loses some integrity when removed. If a part starts to bind, you can intuitively move it in the right direction to free it.

While today’s automated picking and sorting systems do have intelligence, they do not have intuition. With automation, you might need more rigidity around the edges.

Consider any acute or sharp edges that could get caught. Think of a star. Large or small, it’s going to have several sharp edges. Even removing it manually is going to be a challenge. To accommodate automated part picking, you can cut outside corners with reliefs, inside corners with fillets, or use a combination of both.

But even these strategies might not be enough. What if you also cut a circle around the star? In this case, the picker would lift the circle piece as well as the star inside it smoothly and easily, with no catching or tangling.

Certain internal contours must be cut with care. If the inside scrap piece is just large enough to tip up and catch on one of the slats, it can cause issues. A common remedy is called slug-destruct. Here, a single large slug is cut into several pieces, allowing the smaller bits to fall easily through the slats.

Long-edged parts next to each other also can be of concern when picking or sorting. Common wisdom, if perhaps a bit outdated, states that the minimum distance between nested parts should be at least equal to the material thickness. Even if you do follow this rule of thumb, the aforementioned internal stresses can cause the web between the two parts to bow or move to one side. This can lock parts in the sheet. The most effective programming solution here is common-line cutting, where two parts share a cut edge.

What’s Next?

Offloading technology has advanced dramatically. Robotic arms, gantries, suction, and magnetism are nothing new, but the software included in systems is game-changing. If nesting software has to populate a virgin sheet and automatically account for things like corner relief, fillets, or common cutting, sorting software has to take that nest, know where those parts are, calculate the centers of mass, choose the right tooling, and distribute those parts to any number of pallets based on part type and the next operation or customer.

Cutting and offloading are still two separate operations. The end game is to combine them to achieve sorting of this detail in a single software that includes both cutting and offloading.

The Industry 4.0 initiative that’s been on everybody’s lips for a decade now cannot come to fruition without this type of marriage between software and machinery. When it comes to the realm of laser processing, some systems now can be integrated with a quality system and notify it when a set of parts is done, so the next operation can retrieve the parts. Knowing that parts are somewhere in the processing stream is great, but there’s even more power in knowing exactly where those parts are within that stream.

Is It All Worth It?

There’s a lot to consider when installing or even considering picking or sorting automation. Is the system going to keep up? Will the laser wait for the pickers? There’s investment. There’s time involved.

So is it all worth it? As always, it depends on the application, but for many situations it can make a world of sense. Consider one fabricator that processed an elaborate 20-sheet nest on one laser. It took two people (with some help from the operator) two and a half hours to denest and stack all the parts. In this situation, automated picking and sorting could shorten denesting time to 37 minutes.

Even more dramatic was the downstream effect of that manual denest. The next operation was bending, and the manual stacking process paid no attention to grain orientation and how parts were presented to the press brake. As grain direction can have a significant impact on the ability of the press brake to maintain angular consistency, this caused additional setups and tweaking at the brake, further compounding the issues.

This brings us to the final point: Picking and sorting are part of an overall process, and an automated system can never be an end-all-be-all solution. It doesn’t matter how many parts you cut if you can’t get them to the next operation efficiently, or if there isn’t capacity for them. When you remove a bottleneck in one area, one can easily show up in another.

Crawl, Walk, Run

Try taking a one-step-at-a-time, crawl-walk-run approach to picking and sorting. It’s one reason that certain advanced sorting systems can be retrofitted onto a shop’s existing automation. An operation need not implement complete picking and sorting automation all at once.

That said, taking steps toward automation is easier than it used to be. Nesting, cutting, picking, and sorting systems have gotten much better at communicating with each other in recent years, so much so that they are capable of keeping up with today’s powerfully fast lasers. Ultimately, finding the right automation is a must to take full advantage of today’s cutting power and to help the efficiency trickle down throughout the rest of your operation.

Jason LeGrand is automation specialist at MC Machinery Systems Inc., 85 Northwest Point Blvd., Elk Grove Village, IL 60007, 630-616-5920,

www.mcmachinery.com

.