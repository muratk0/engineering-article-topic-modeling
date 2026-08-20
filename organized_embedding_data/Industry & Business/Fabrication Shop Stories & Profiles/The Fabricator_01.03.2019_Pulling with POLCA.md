# Pulling with POLCA

[TARİH: 01.03.2019 The Fabricator]

How custom fabricators could improve flow with a new kind of production control

By Tim Heston

P

ull production sounds great in theory, and it’s not unheard of in sheet metal fabrication. Demand from customers, both internal and external, "pulls" products downstream and, ultimately, to the customer’s receiving dock.

This can work spectacularly well for specific products. In fact, it’s not unusual to visit a fabricator and see a multi-process cell dedicated to one major customer. Returnable containers arrive from the customer, which spurs the cell into action. If the containers aren’t there, the demand isn’t there, so the cell doesn’t produce that product but instead shifts to another (usually similar) product. It’s a simple adaptation of

kanban

replen-ishment concepts long used in lean manufacturing.

But then you look at the rest of the fabrication shop floor. It’s organized by process, like a typical job shop. You see large work-in-process buffers between processes. Then there’s the typical chaos: A big customer calls and needs a part immediately, and an expediter springs into action.

A custom fabricator doesn’t produce products that can be pulled down a value stream, because no one product has a dedicated value stream with dedicated equipment. A typical custom fabricator might produce thousands of different part numbers a year, all at low quantities and often at unpredictable intervals.

That said, for high-volume, repeatedly ordered products, kanban works so well. Could the ideas behind it be adapted for the high-product-mix, low-volume fabricator, a production control solution for the "long tail" of low-volume and custom products?

Rajan Suri has done just that, and he’s written a book about it:

The Practitioner’s Guide to POLCA

. Pronounced like the dance, POLCA is short for Paired-cell Overlapping Loop of Cards with Authorization. Far from self-explanatory, the name becomes very descriptive once you understand the system basics.

At its core, POLCA provides signals in the form of cards. The signals do not specify demand for a product, as

kanban

does. They instead signify available capacity. By itself, the system doesn’t require software at all, but it can be used with existing software platforms, be it an enterprise resource planning (ERP) system or a homegrown Microsoft Excel or Access worksheet.

As many custom fabricators say, their operations don’t sell products; they sell available capacity. Considering this, having a real-time capacity signal, on the fab shop floor and in the office, could have serious potential.

Some Context

Suri is the founder of the Center for Quick Response Manufacturing (QRM) at the University of Wisconsin-Madison. He developed QRM as an improvement method for low-volume, high-product-mix operations—those that could produce thousands of different part numbers over a given period.

In his book on POLCA, Suri never states that adopting the tenets of QRM is a requirement for the production control system, but certain elements of it, including the use of multiprocess manufacturing cells, are especially suited for it. And as stated in his other books, Suri developed POLCA to support his broader QRM concepts.

That said, knowing a bit about QRM gives some context. QRM focuses on shortening lead time (the "QR") by focusing on overall manufacturing time—what Suri calls the

manufacturing critical-path time

, or MCT. It follows a product through all of its complex routings: from the material supplier to the stockroom, machine to machine, cell to cell, out to service providers (like powder coating and plating), and back, until the job reaches the customer’s receiving dock. QRM also incorporates the time associated with purchased components, be it from the machine shop down the street or a casting operation in China.

QRM focuses not on machine uptime or utilization but instead on shortening the MCT. After all, a machine’s uptime metric can be absolutely phenomenal, but if more products aren’t shipping out the door in less time, a fabricator isn’t making more money. (And besides, running a machine at or near capacity can lead to some serious traffic jams—hence QRM’s focus on operating at well below maximum capacity levels.) QRM advocates analyzing the product mix and identifying families, grouped into what Suri calls focused target market segments (FTMSs). An FTMS could be tied to specific customers, but it could also focus on job or part attributes—volumes; demand trends; a range of sheet or plate thicknesses; routing or processing requirements; or perhaps a specific part size that requires certain equipment, like a press brake with specific tools or bed length.

Figure 1

This shows a job packet and bin sitting at Cell K. The U/K card shows where the parts came from (Cell U), and the K/V card shows where the job is going (Cell V).

Figure 2

Each cell has a POLCA board. Downstream cells deliver cards to this board to signify they have capacity.

Figure 3

The arrows in this chart detail the direction of flow—from Cell A to B to G, while the bottom of the loop (with no arrows) signifies the return trip of capacity control cards. These loops overlap at Cell B.

After establishing those FTMSs, an operation designs multifunction cells around them. Cells can handle just one FTMS, some, or all, depending on the operations in the cell and the nature of the jobs (such as volume and demand trends) the shop fabricates.

Consider a custom fabricator that makes a steady volume of a few agricultural equipment products, as well as a long tail of low-volume custom work with relatively unpredictable demand. That shop might have five FTMSs—one for the high-volume work and four others for the low-volume work: (1) for plate, (2) sheet, (3) aluminum and stainless, and (4) for customers with unusual work or tight-tolerance requirements.

In this situation, one multifunction "planning cell"—a cross-trained team that estimates, engineers, works with purchasing, and prepares jobs for the floor—could focus on the high-volume FTMS. Another planning cell could focus on the other four segments (the true job shop part of the business).

What about cells on the floor? Again, specifics depend entirely on the fabricator and its product mix, but just to follow our hypothetical example, this fabricator may decide to have one cell dedicated to laser cutting and punching, which in turn feeds a collection of multiprocess cells with press brakes, hardware insertion, grinding, and welding—all dedicated entirely to one or several FTMSs.

Cells in QRM require co-location—but all these processes may not go together well, either from a part flow or quality assurance standpoint. Dust from welding can be problematic for laser cutting machines, for instance. So the shop may split equipment into two cells: one with press brakes and hardware insertion presses and another with welding, grinding, and polishing or paint prep.

Regardless, the people and machines in those cells would be capable of fabricating the FTMS’s entire product range. And like the planning cells in the office, workers in cells on the floor would be cross-trained, able to move where needed to maintain flow.

Still, laying out a shop full of multiprocess cells probably won’t maintain flow alone. No matter how "cellular" a fabricator becomes, workers still need to know what to work on next, and this is where POLCA comes into play.

Basics of POLCA

Again, POLCA is short for

paired-cell overlapping loop of cards with authorization.

Sure, it doesn’t roll off the tongue, but breaking this name down helps describe how the system works.

Paired Cell. In a fab shop, no cell (or machine or workcenter, for that matter) operates in a vacuum. The cell usually sends work to one or more downstream cells. For instance, a bending-hardware insertion cell sends some work to a welding-grinding cell, and perhaps other work to the powder-coating cell. The "pairing" concept shifts the focus away from a cell’s "local efficiency" (machine uptime, parts per hour) toward how work flows from one cell to the other. If work doesn’t flow smoothly from one cell to the next, the operation isn’t productive.

Cards.

"Overlapping loop" comes next in the name, but to understand that, it’s helpful to understand the role of cards (see

Figures 1

and

2

). Cards act as capacity signals. Say you have Cell A that feeds work into Cell B. To control work flow between these two cells, workers would use a certain number of "A/B cards." When workers in Cell A finish a job, they attach one or more A/B cards (depending on the size of the job) to it and send it to Cell B. At that point, if workers in Cell A see they have no A/B cards available, they

cannot

start any job that’s destined for Cell B. They can work on jobs destined for other cells (following certain rules, described later), but not Cell B.

Meanwhile, workers in Cell B keep those A/B cards until they’re finished with the cards’ associated job. Only once they finish a job can they send those A/B cards back to Cell A—effectively signaling people in Cell A that Cell B has available capacity.

Overlapping Loop.

Sending that card back creates a loop. Jobs with cards flow from Cell A to B. Once Cell B finishes, A/B cards loop back to Cell A. The "overlapping" term comes in because, of course, few if any products flow through just two cells or workstations. A complex routing can entail a dozen or more manufacturing steps

(see Figure 3).

This creates what Suri calls a

POLCA chain

. Figure 3 shows a chain where Cell A feeds Cell B, which feeds Cell G. Cell B is where that A/B loop overlaps with the B/G loop. This dictates what cards workers need when starting a job. Again, for workers to start a job, they need to know that downstream cells have available capacity.

Say you’re working in Cell B and see a job arrive with an A/B card attached to it, and that you’ll need to send the job on to Cell G. Before starting the job, you need to make sure that Cell G has available capacity. You look at a board in your cell (Suri calls these

POLCA boards

) to see if there’s a B/G card available. But before grabbing the card and placing it in the job packet, next to the A/B card (which, again, isn’t sent back to Cell A until the job is finished), you need to do one more thing. In fact, you need to do this first, even before looking at any material queued before the cell. You need to look at the authorization list.

Authorization.

"With authorization" is a critical part of the POLCA name. The authorization list at each cell shows everyone not when a job is due but when a job can start, based on the estimated flow times derived from existing scheduling data from a shop’s existing ERP software or other systems (see

Figure 4).

Jobs that are behind schedule will have an authorization date in the past; they go at the top of the list. As Suri explained in the book, this doesn’t necessarily mean a job will ship late. The authorization date will force the job to at or near the top of every authorization list at every downstream cell. This effectively expedites the job through the rest of the routing without significantly disrupting the flow of other work.

Figure 4

Scheduling determines authorization dates based on available data from an ERP or other scheduling system. Here, each cell has several work-center operations that add up to a certain number of days. Authorization dates can be fine-tuned over time.

Figure 5

A typical authorization list for a cell gives the job identifier, when it’s authorized to run, and the next cell it’s destined to go.

The authorization list in

Figure 5

shows a job on the schedule for Cell A and the next cell. It’s Jan. 15, and you see material has arrived for the job R2D2. Its authorization date, Jan. 13, is in the past, so you know it’s authorized to run. The job is destined for Cell D, so the POLCA board needs an A/D card. If you see it, you grab it, attach it to the job packet, and start the job.

If you don’t see an A/D card, you go through the same process for other jobs on the list. Again, to run, it needs to be authorized, and it needs a card signaling available capacity at the cell downstream. If you go through the entire list for the day and nothing is ready, you then can either conduct improvement activities or move elsewhere to help free a bottleneck.

Suri sums this up in what he calls the "decision time flow chart":

1. What’s the next job on the authorization list? If there are no more jobs, go to No. 4.

2. Has the material needed to perform the job arrived? This can include material from the upstream cell and also, for certain operations like assembly, purchased components. If not, go back to No. 1.

3. Do you have the right POLCA card for the job? If yes, launch the job into the cell. If not, go back to No. 1.

4. If no jobs are available to launch, work on secondary activities based on a prepared list, until an event (like arriving material from upstream or POLCA cards from downstream) triggers another decision time.

As Suri explained, this moves the focus away from local efficiency (machine up-time, parts produced per hour) and toward flow. If a machine produces parts that a downstream process can’t handle, it just builds WIP and adds waste.

Moreover, if a cell uses that capacity to produce products that downstream cells can’t handle, then the fab shop can’t use that capacity for more pressing work destined for downstream processes that do have available capacity. To put it in a job shop’s terms, a custom fabricator sells capacity, not products. If it uses capacity that downstream processes can’t handle, it wastes capacity and, hence, can’t sell that capacity to someone else. The POLCA rules ensure that upstream cell capacity is used wisely.

POLCA Chains and Out-sourced Processes

Each job need not have a POLCA chain that spans the entire factory, from the office to the shipping dock. Sometimes it’s impractical to do so. If work is, say, sent outside for heat treating or powder coating, that step really can’t be another "cell" in the POLCA chain. If it were, then a card would have to be sent with the job to the heat treater. Workers need to receive a signal of available capacity downstream (that is, the right POLCA card) before they work to fill that available capacity. So if everyone follows the POLCA rules, removing a capacity signal from the shop floor (by sending the card to the heat treater) effectively "removes" available capacity— though, of course, in reality the capacity is obviously available.

Figure 6

shows a job that has most operations in-house except for zinc plating. Suri recommends that jobs requiring outside services flow through two POLCA chains. One starts with planning and ends with the subcontracting planning team (which could be the same as the initial planning team). The subcontracting team then acts as the beginning of a second chain. When it sends a job out for zinc plating, it sends a POLCA card (in this case, an FM/SUBC card) back to the finish machining cell. When the job comes back in a few days, the team releases the job into the second POLCA chain.

Stuff Happens: The Safety Card

Following the POLCA rules, when the material isn’t available, you just move on to the next job on the authorization list. But what if the material is missing, or a purchased component from an outside supplier is late? Or perhaps there’s a quality problem, be it with the part or tooling (wrong tooling specified for the job, or setup or communication issues)?

This is where the safety card comes into play. The job is moved out of production, a safety card is attached to it, and the normal POLCA cards are returned to the appropriate cells. This allows the POLCA chain to operate as normal as managers, supervisors, and purchasing personnel work to fix the problem.

For instance, a supervisor may see a drawing of a part that’s impossible for the press brake operator to make with available tools. The brake operator could "make it work," but that takes time, can add inconsistency, and puts a huge damper on flow. So it makes more sense to pull it out of the POLCA chain, attach a safety card to it, and allow personnel to fix the problem outside of production (like, say, in engineering or the prototype shop).

Sure, ideally this problem should have been caught in engineering, and the part shortage should have been addressed by purchasing before the job was released. But again, stuff happens. And in the book, Suri describes ways that these safety cards can be used to track and analyze these problems during continuous improvement efforts. As the operation improves over time, a shop should need fewer and fewer safety cards.

One final note about safety cards: Suri does not recommend using them when a machine unexpectedly breaks down. Safety cards work only when jobs are stuck at a cell, and yet the cell still has capacity; the problems are with the

job itself

, not the tools or machinery.

Figure 6

Depending on the situation, jobs that don’t have any outside processing could flow through one POLCA chain, from planning to packaging and shipping. A job that’s sent to outside processing needs at least two POLCA chains.

There’s sometimes a fine line here. For instance, say a job gets stuck because of a challenging press brake setup. With enough time a brake operator can make it work, but again, it will also seriously hinder flow. And if the current job were planned properly (right tools, radii, setup documentation), bending it wouldn’t take so long. The brake cell still has the capacity to produce other jobs efficiently, just not the current one, so using a safety card makes sense.

But if the press brake machine breaks down, that’s different. The problem is with the machine, not the job, and the breakdown removes available capacity. If the repair is quick and doesn’t seriously disrupt flow, it’s sometimes easiest to just wait; in the interim, workers can perform secondary activities and develop improvement ideas (No. 4 in Suri’s "decision time" flow chart). If the delay is long enough, managers can decide to move the job back to the planning cell, which can either relaunch or out-source the work.

An Expediting Option

According to Suri, POLCA reduces the firefighting. Increased flow velocity turns what used to be a "hot job" into just the "next job"—at least in most cases. But manufacturers know that stuff happens, and despite their best efforts, some jobs just need to be shoved through the system. In these (ideally) rare cases, POLCA has a way to accommodate.

If the job is late before the job is released, a manager could renegotiate a delivery date and change the authorization date for those in the POLCA chain. If a late job is discovered after it’s released to the POLCA chain (or if due date renegotiation just isn’t an option), then a manager or supervisor could pull one of a limited number of so-called "bullet" cards. A job with a bullet card takes precedence over all other jobs. As soon as it arrives at a cell, it becomes the "next job" no matter what and is sent to the next cell immediately.

Say you work in a press brake cell and see a job with a bullet card arrive. When deciding what to work on next, you go to the bullet job first, no matter what—even if downstream cells haven’t sent up a capacity signal card. In effect, the bullet card allows a job to "butt in line" through its entire POLCA chain.

Suri cautioned, however, that shop floor managers must use bullet cards sparingly and have a limited number available—two is plenty, only one is ideal. These cards essentially send a ripple through flow, delaying other jobs as the bullet card shoves through the POLCA chain. The bullet card does the job, but it’s really a path of last resort. If dozens of jobs get bullet cards, you have chaos, and capacity control falls apart.

A Different but Simple System

Again, a fabricator need not adopt all of the elements of QRM to adopt POLCA. Having multi-process cells is the best approach in most cases, but it’s not entirely necessary in every circumstance. Some examples in the book identify cells around specific processes, like heat treating or finish machining. One small shop Suri profiled in the book defined a "cell" to mean a "machine." As he explained, this can work if a shop has a limited number of machines. But if machines number in the dozens, the method becomes unwieldy in a hurry.

Regardless, according to the author, implementing POLCA doesn’t take long. Half of his book comprises case studies by guest authors describing POLCA implementations at their own companies, from high-product-mix metal manufacturers to companies serving the pharmaceutical industry. One book chapter (written by guest author Ananth Krishnamurthy, Suri’s colleague at the University of Wisconsin-Madison) describes how POLCA was implemented in one shop in three days.

The book covers many more details, including how to deal with POLCA chains that go in a circle—for instance, grinding and deburring, welding, hardware, then

back

to grinding and deburring, before moving on to finishing and assembly.

It also covers how much work each POLCA card should represent, and how many POLCA cards a pair of cells should have. A small job (say a few dozen pieces) could get one card, while a large job (one that, for quality or practicality reasons, needs to be kept together) could have several cards attached to it. Suri delves into a few simple calculations that would help a fabricator get started—but the author stresses that these are just initial calculations. According to Suri, POLCA is a self-correcting system. As the system matures, the number of cards can be fine-tuned.

The book also describes how (and how not) to launch POLCA in only a portion of the shop and/or office. Implementing all at once is often ideal, but Suri conceded that, because of a host of external factors, it sometimes just can’t be done.

The author clarified that by itself, POLCA can’t solve all problems. For one thing, it’s a capacity-control tool, not a capacity-planning tool. It can’t magically level-load a shop with seasonal work that creates steep demand peaks and valleys. Shops need to be able to do "rough cut" capacity planning. Results from POLCA can then be used to fine-tune future planning.

A shop also needs to operate with spare capacity. Suri recommends at least 15 percent spare capacity for critical work centers. Like a highway during rush hour, if a fabricator operates at near 100 percent capacity, the smallest hiccup can snowball into a massive traffic jam, regardless of the production control system used.

Also, POLCA’s effectiveness hinges partly on a shop’s batch size management. Huge batches of hundreds or thousands of pieces create lumpy flow. POLCA won’t change this; in fact, it may make the problem more apparent. In the book, Suri describes how POLCA can handle the occasional large batch for work that just can’t be split into more manageable sizes. But if material handlers spend every day lugging around huge batches of work from department to department, POLCA probably won’t improve matters.

And of course a fabricator needs reliable machinery and a good preventive maintenance program. If machines break down continually and reactive maintenance runs rampant, POLCA isn’t likely to mitigate the chaos.

Ultimately, POLCA is about allowing workers to make an intelligent decision on what to work on next. Instead of keeping their heads down having no information about upstream or downstream capacity, workers under POLCA know what’s going on around them. With that knowledge, they can then make the best decisions to create efficient flow.

Senior Editor Tim Heston can be reached at

timh@thefabricator.com

. The Practitioner’s Guide to POLCA: The Production Control System for High-Mix, Low-Volume, and Custom Products

is available through

amazon.com

and other booksellers. For more information on QRM, visit the Center for Quick Response Manufacturing at the University of Wisconsin-Madison at

www.qrmcenter.org

. Images are copyrighted material reprinted with permission from Productivity Press.