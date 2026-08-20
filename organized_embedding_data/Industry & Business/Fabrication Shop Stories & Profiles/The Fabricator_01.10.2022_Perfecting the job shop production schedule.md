# Perfecting the job shop production schedule

[TARİH: 01.10.2022 The Fabricator]

Timing the material release really matters

By

Tim Heston

Yuri_Arcurs/iStock /Getty Images Plus

S

cheduling a custom metal fabrication operation attempts to bring order to chaos. Most fab shops don’t have the luxury of a product line, and even if they do, they likely fabricate that product on some shared resources.

As in all kinds of job shops, the constraint in custom metal fabrication can move depending on the given mix of jobs on the floor. A constraint for a certain collection of jobs might start in bending, then move to welding and powder coating. That slow-moving group of jobs acts like a bump on the log for orders upstream. At the same time, most custom fab work involves multilevel bills of material (BOMs), with multiple parts and subassemblies feeding into a final assembly. All the complexity can set heads spinning.

To sort through the complexity,

The FABRICATOR

spoke with Prasad Velaga, PhD, founder of College Station, Texas-based Optisol LLC, a firm that focuses on job shop scheduling. Velaga emphasizes one key component of the scheduling challenge:

when to release material to the floor

.

As Velaga explained, releasing material at the right time "means that production control in a job shop will be simple, easy, and efficient if the shop starts each job at an optimal time."

Market Realities of the Job Shop

"Customers of job shops are quite authoritative," Velaga said, adding that "a small job shop isn’t going to say no to a large, influential customer."

Many fabrication shops grow on the backs of a few large accounts. The market power these customers have shapes many aspects of the job shop business—especially production scheduling. Fabricators will move heaven and earth to satisfy the needs of key accounts, and the effort can trigger chaos across the shop floor.

Most customers, no matter their size, place orders for low quantities. At the same time, demand for some products might be infrequent and highly unpredictable. Processing times vary significantly too. It can take less time to cut, more time to bend, and even more time to weld—but not for every part. Some parts don’t require any bending; others are simple to bend but difficult to weld; secondary processes like grinding and deburring add to cycle times as well.

Also, more and more products require preproduction time. This can involve some design-for-manufacturability efforts as well as procurement of special materials (material procurement being a particular pain point over the past few years). "Especially when job shops get into design," Velaga said, "there’s uncertainty in how long that work will take."

High-variety Production Systems

High-variety production can occur in a plethora of shop layouts. A factory might produce a single product with varying characteristics; it might send a few or even a large number of distinct products down the same production line. Some products might skip a few operations too. And still others might originate from a shared resource and then split into parallel lines dedicated to certain product families.

While some specialized job shops experiment with versions of these layouts (transforming into what Velaga called "flow shops"), most high-mix operations aren’t organized in this way. Instead, jobs flow in a network of shared resources (see

Figure 1

), often grouped in process-specific departments. Some operations might employ a dedicated cell for prototype work or perhaps combine certain common steps—like bending, spot welding, and hardware insertion—in a cell or workstation. But products still need to flow through a network of workstations.

Unexpected variations at each workstation—a rush order that pushes others aside, a grouping of blanks that require extra deburring, or whatever else—ripples through the rest of the shop. Moreover, one job might have a multitude of lowerlevel BOMs (subcomponents) that flow across multiple work centers, get sent to outside processing (like powder coating, plating, or heat treating), then reunite in welding or final assembly. Optimizing such a complex workflow web isn’t easy.

Solving Scheduling Problems

Velaga emphasized that no scheduling strategy can overcome a situation in which known variations—different materials, tooling setups, weld procedures, machine maintenance, and more—aren’t handled effectively. If a job shop’s machines break down continually, the organization has larger problems that even the best schedule won’t fix. Velaga called this "chaotic variation."

"Workers may conveniently select jobs on the shop floor without any rational strategy. Also, there may be high uncertainty in the lead times of certain materials."

That said, intelligent scheduling can help deal with some level of shop-floor variation. "Good scheduling can strategically create buffer times in the schedules of individual jobs, mostly by releasing jobs early, to absorb some of the natural variation that happens in most job shops," Velaga said.

Due Dates

Each job in a make-to-order operation has a specific due date. Sometimes the customer stipulates a date, while other times the fab shop includes a delivery date in the quote. "Sometimes, the due date is negotiated by both the customer and the [job shop]," Velaga said, adding that "quoting a due date for a new order can be quite difficult.

"Also, due dates are often negotiable," Velaga continued, adding that an expedited job might win a higher price, but with that comes the cost of overtime and, again, the production ripple effects that an expedited job creates.

A shop might have dozens or even hundreds of jobs either on the floor or ready to be released to the floor at any one time, each with a different due date. Even worse, that mix of due dates changes every day as new orders are released to the floor.

FIGURE 1

Most job routings in job shops flow through a network of workstations, often grouped in process-specific departments.

FIGURE 2

This shows four different scenarios of order flow in a job shop. Intelligent capacity planning helps finish jobs on time and the right material release strategy ensures that production lead.

Push and Pull

Traditionally, many metal fabrication job shops have relied on push production, with schedulers "pushing" jobs to the floor to maximize machine utilization. Many lean manufacturing experts opine about the merits of pull-based flow, where work completed at downstream workstations trigger orders to be processed upstream.

This can be great in the product-line-production world, but in Velaga’s view, in a job shop, it’s not necessarily the best way to schedule for improving on-time delivery and throughput. The pull system of lean manufacturing assumes smooth, consistent demand, and doesn’t consider the due dates of individual, diverse orders. "In job shops, pull systems help limit the amount of material on the shop floor, but they do not guarantee on-time delivery and they cannot predict the progress and completion times of individual jobs," Velaga said. "In high-mix, low-volume environments, distinct jobs have different routings and processing times for operations." Some jobs may flow through severe bottlenecks, others might flow through smoothly and quickly.

Push scheduling also can create problems, Velaga said, especially if jobs are released in an uncontrolled way. That is, a shop receives an order, and the scheduler pushes the order out to the laser or punch immediately. Sure, some orders might ship early, but most orders sit on the floor at bottlenecks for extended periods as expensive WIP.

Timing the Material Release

The ideal, Velaga said, could be described as a kind of

controlled push scheduling

, the key component of which involves delaying material release to the shop floor until the optimal time. "The idea is to judiciously limit the number of days material for a job is idle on shop floor," he said.

Velaga described four different job flow scenarios in a typical job shop, as shown in

Figure 2

. In the first scenario, schedulers push an order to the floor as soon as possible—the classic "push" scheduling. The thinking is the sooner a job is released, the less chance it has of being late. But as Velaga explained, this wellintentioned act has negative consequences. The job undergoes a few processing steps, then sits as WIP for days or even weeks as it waits for bottleneck resources to become available amid a shop floor flooded with work.

"The next scenario, the second line in the figure, shows flow of the same job when capacity planning is properly done to ensure that the job is finished by its due date," Velaga said. "The third line in the figure shows flow of the job when material release is delayed judiciously without the risk of delaying the job completion. The last line in the figure shows the ideal flow of the job involving no job idle time and job completion by the due date."

WIP, as shown in the figure by yellow bars, absorbs variability. "The WIP results from the material release strategy, known variation in process requirements of jobs, and finite capacity of resources," Velaga said. "It absorbs uncontrollable variation in the system.

"My premise is this," he continued. "If you release material for jobs at optimal times and let jobs freely flow through the system along their routings without any control, and let jobs compete for shared resources by certain priorities, then production control becomes much simpler and easier. Finding that optimal time is difficult. But when you find it, jobs flow smoothly from one work center to the next, and everything gets easier."

Scheduling Gets Intelligent

This is where advanced scheduling software can help. Certain packages use a controlled-push, forward-scheduling methodology that takes into account due dates, priorities and the routing information of jobs, available times of production resources like machines and workers, and all relevant production constraints. It factors in the mix of talent on the floor, reserves certain jobs for certain shifts, and schedules to ensure that WIP doesn’t sit on the floor for long.

This can include identifying all work centers that can process a workpiece and suggesting alternative routings. For instance, say a part is designed to be produced in an automated panel bender. Considering the machine’s immense capacity, the scheduler usually routes jobs through it. But what if the panel bender is running full-out? In this case, why not flow the job through a manual press brake that has available capacity? Yes, the bending job takes longer, but for the current mix of work, a routing through the manual brake is still the fastest way to process the job.

"Seeing the full picture is so important," Velaga said, adding that "this kind of intelligence can be built into software."

Material for a job might sit in raw stock, but the job isn’t released until planners "are confident that the job can flow through work centers without long intermediate waiting times," Velaga said. "Today’s scheduling software can help achieve a situation as represented in the third line of Figure 2. The last line in the figure shows the ideal flow of the job without intermediate idle times and without any delay in job completion. It is extremely difficult to attain this situation in complex job shops without having huge capacity at work centers or without drastically sacrificing shop throughput.

"I view scheduling as a sort of simulation of production. With scheduling, you’re predicting the work progress, how jobs will run through the system, where the bottlenecks will occur, and how long jobs will wait at different work centers. The schedule also shows the sequence of jobs to be done on each machine and the sequence of jobs to be done by each worker. It is practically easy to implement such job sequences, [shown in] resource dispatch lists, on the shop floor."

He added, however, that circumstances dictate how granular a schedule has to be. This again has to do with the variable nature of job shop work, what Velaga called the "uncertainty of requirements." Part deburring after laser cutting is a prime example. These days, new lasers can cut extremely clean edges that might not require deburring. The operator denesting the parts inspects the edges and sends only those blanks that require deburring through the deburring machine. In this case, the "laser cutting" step on the schedule can include time for loading, unloading, and deburring, even though it’s still unknown exactly how many parts will require deburring.

A buffer can absorb this kind of variability so that the scheduled job completion times are reliable. Velaga emphasized, however, that "we’re not adding a buffer to the schedule. We’re allowing the buffers to take place in the schedule to absorb variability."

He added that when a shop releases material early, buffers before bottlenecks naturally occur. At the same time, an operation’s "buffer sizing" strategy should avoid keeping those constraint resources idle. Right-sizing buffers in the schedule "absorb the uncontrollable, natural variation in the system and keep the constraints busy during their available times."

The idea is to maintain buffers to keep constraints busy in order to protect shop throughput, while not releasing material too early, which would increase WIP and lead times. Release material at just the right time, and everything gets a lot easier.

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

Portions of this article come from "Methods for efficiently managing shifting bottlenecks and proactively planning for capacity in high-variety, make-to-order production," presented by

R. Prasad Velaga

, PhD, Optisol LLC,

www.optisol.biz

, at FABTECH, Sept. 13-16, 2021,

www.fabtechexpo.com

.