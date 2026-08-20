# Tube laser cutting, accessible to all

[TARİH: 01.11.2023 The Fabricator]

Tech Talk

Automated quoting for the tube laser

Caleb Chamberlain

F

ive years ago, my brother Jacom and I launched OSH Cut, a manufacturing service designed to make metal fabrication accessible. At the time, we found quoting from local shops inconsistent, time consuming, and a little frustrating. We could design new metal parts in a day and then spend weeks obtaining prices, getting design feedback, and waiting for delayed production. Our experience motivated us to write software to automate sheet metal quoting online.

That was the genesis of OSH Cut. Our tools allow customers to upload sheet metal designs, obtain instant pricing and manufacturability feedback, and order parts with lead times as short as the same day.

We are about to take another big step toward making metal fabrication accessible. By the time this article goes to print, we’ll have launched our new tube laser cutting service, complete with instant online pricing, manufacturability checks, and rapid turnaround. It has been an interesting technical challenge (for reasons I’ll discuss momentarily), but we are excited about the possibilities.

If sheet metal blanking and bending has traditionally been hard to quote and order, tube cutting has been even more so. Tube lasers can cost up to and beyond $2 million, and are usually earmarked for high-volume, enterprise-level production. That means small businesses might struggle to get bids for prototype, short-run, or low-volume production.

That’s a shame, because tube cutting creates incredible design possibilities. The fact that metal tube is produced in bulk by mills keeps the total cost down, and rectangular and tubular profiles are inherently strong for the material they use.

The problem is that manually fabricating parts from metal tubes is labor intensive and space inefficient. Raw stock from the mill or service center usually comes in sticks up to 40 ft. long; cutting to length with consistent accuracy can be difficult; drilling holes is time consuming and messy; and noncircular cutouts are even more problematic. Tube lasers solve all these problems, but not if small businesses have to spend weeks waiting for quotes and parts. And, of course, most small businesses who need only low quantities of laser-cut tube really can’t justify buying a multimillion dollar machine. We think that making tube cutting more accessible will change the way businesses design their products, and that will improve the industry in the same way sheet-metal-focused technology has.

Automatically Quoting Tube Parts

Automating tube part quoting has been much more challenging than for sheet metal. Once our software unfolds a bent sheet metal part, it produces a profile that is easily analyzed to figure out both cutting time and material requirements. But tube profiles don’t lend themselves well to a 2D-only flat pattern like sheet metal parts do. Accurately estimating cut time becomes even more complicated when accounting for variable bevel angles on cuts.

To solve the problem, we wrote software that analyzes the tube 3D model and detects the tube profile. It then processes the 3D model to extract a list of cuts that includes both the length and the chamfer angle of each cut segment. That information is finally fed into a mathematical model to estimate a cut time for the part. Cut time is combined with labor and other costs, along with the targeted margin, to determine the price for cutting.

Material pricing is also challenging. Compared to blank cutting, tube cutting is unique with respect to how remainders are handled, if at all. Our systems automate remainder management for flat sheets, and we do enough high-mix work that having small pieces on hand is a big win. But that may or may not be the case with tube cutting. The huge diversity of material types, profiles, and wall thicknesses might cause us to hold remainders for a very long time, tying up cash we’d rather have on hand.

And while the machine itself can handle small sticks, there’s still a limit on how small a piece can be fed to the machine, and whether it’s even worth it. At its $2 million price tag, we want that machine cranking, and changeover time is going to be more expensive than on a flatbed. We’ve built some of these considerations into our costing model, but we’ll need to keep our eyes on the problem.

FIGURE 1 An online checkout system provides instant pricing for both sheet metal and tube cut parts, in one place.

FIGURE 2 An operator console for tube cutting indicates what stocked materials are available for parts in the job, and where the inventory is located. It also performs rudimentary nesting (visible on the left) to aid in planning the amount of material that needs to be pulled from inventory.

All these systems are designed to minimize friction for everyone involved in the production of sheet metal and tube parts. That naturally includes our customers, but it also affects operators running the equipment and even people in the front office.

After building out the new pricing engine, we finally needed to augment our online checkout system to support both tube and sheet metal parts. Results are shown in

Figure 1.

Managing Production and Inventory

When we first launched our sheet metal blanking service in 2018, we learned quickly that quoting and ordering is just one small piece of the puzzle. Quoting a job and taking an order has its own complexity, but managing high-mix, on-demand production is a challenge on an entirely different level. We ended up writing software internally to help us manage and order inventory, track remainders, schedule and nest jobs, program our flatbed lasers, and program our press brakes.

We might write software to automatically create and program tube laser jobs, but generating NC code for a tube laser is significantly more complicated than for a flatbed machine. In the meantime, we needed a way for our laser operators to plan jobs, select inventory, track production results, and deal with remainders. (As an aside, we learned early on that everyone hates filling out inventory labels for remainders, so one of our first software tools automated that process for flat sheets. We are doing the same for tube cutting). Our first-revision operator console is shown in

Figure 2.

We expect that this design will change as our operators encounter workflow issues.

We’ve also had to overhaul our work order and production management systems, since our new tube cutting machine is in a different facility, and previous versions of our internal tools didn’t take facility-specific variables into account.

All these systems are designed to minimize friction for everyone involved in the production of sheet metal and tube parts. That naturally includes our customers, but also affects operators running the equipment and even people in the front office. Reducing friction at every touchpoint means that the operation can run more smoothly, with fewer exceptions, less stress, and more consistent experience across the board.

Right now, tube cutting technology is relatively inaccessible. But when anyone can get online and order both laser-cut sheet metal and tube in one place, it’ll expand design possibilities and enable small businesses to create new products faster and more efficiently. Like sheet metal, improved tube cutting accessibility will be better for the entire industry. Improved accessibility will mean more businesses design with tube cutting and sheet metal in mind, increasing demand for custom parts. And as the number of new products grows, production demand will grow along with it, a boon to manufacturers optimized for mass production. We can’t wait to get started.

Caleb Chamberlain

is CEO and co-founder of Orem, Utah-based OSH Cut,

www.oshcut.com

.

TRUE ROBOTIC

STEEL BEAM ASSEMBLY + WELDING

NO MANUAL LAYOUTS

NO MANUAL TACKING

NO HUMAN ERROR

WATCH HERE

THE PEDDIASSEMBLER

Peddinghaus

www.peddinghaus.com

|

info@peddinghaus.com

| (815) 937-3800