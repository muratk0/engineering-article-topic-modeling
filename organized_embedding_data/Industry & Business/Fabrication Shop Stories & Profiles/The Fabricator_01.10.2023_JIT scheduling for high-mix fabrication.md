# JIT scheduling for high-mix fabrication

[TARİH: 01.10.2023 The Fabricator]

Tech Talk

Balancing WIP, material yield, and downstream constraints

Caleb Chamberlain

A just-in-time scheduling tool helps balance production needs against nesting efficiency.

S

ingle-part, just-in-time production is often considered a manufacturing gold standard. Work-in-process (WIP) has a real cost in space, labor, machine time, and cash.

Let’s consider cash: A manufacturer spends money to acquire raw materials, pays labor and overhead costs to convert that material into finished goods, delivers product, and then invoices customers. If the entire process from material purchase to invoicing takes two months, then at any given moment, you will have at least two months of cost of goods sold (COGS) tied up either in raw material or WIP inventory. Shortening that cycle from two months to one month takes 50% of that value and puts it back into your bank account, where it can be leveraged to grow the company in other ways. And cash isn’t the only factor. Storing piles of WIP and raw materials clutters the workplace, increases confusion, and decreases revenue-per-square foot achievable in the space.

Reducing WIP sounds great, but sheet metal is something of a special case. When cutting or punching parts out of flat sheets, nesting parts can yield significant material savings. When raw material costs potentially represent a significant percentage of COGS, that can really matter. There is also a significant benefit to consuming full sheets, to avoid the cost and overhead of stocking and tracking remainders.

So we have competing requirements. Yes, reducing WIP saves space, reduces cash tied up in inventory, and rations valuable machine time. But cutting just one or two parts might produce other waste that completely eliminates savings from reduced WIP. Single-part flow is a strategy, not a silver bullet.

Balancing nesting efficiency against limited WIP is an ongoing challenge at OSH Cut, a high-mix, on-demand sheet metal manufacturing service. We regularly fulfill between 100 and 200 unique orders a day, each containing a high mix of parts and materials. When scheduling production, we can almost always look far enough ahead to top off a sheet with parts that aren’t due for another week or two. That’s great for material efficiency. But our lasers can quickly overwhelm downstream processes with parts that don’t need attention yet, creating piles of parts that cause delays while our people sort and hunt. It’s a complex tradeoff.

To that end, we are developing a new software tool to improve our scheduling processes. We call it the just-in-time (JIT) scheduler, as shown in the figure. The premise is that we’ll always want to start with the bare minimum number of parts required to fulfill orders due today, and that we’ll prefer to fill a sheet so that we avoid creating remainders and minimize the waste due to laser deck changes.

But if a downstream process like deburring, bending, or powder coating is overwhelmed, we’d like to avoid sending extra parts there. When "topping off" a sheet, parts that don’t require any downstream operations are prioritized, as are parts that are due sooner.

There’s a lot happening in the figure, and a lot under the hood to support it. First, the user configures the "due-by" date for parts to include in first-pass nests. Parts due by that date or earlier will always be added to a nest. A "top-off look-ahead" date indicates how far to look forward when considering parts to top off a sheet.

We can prioritize parts going straight from laser cutting to final QC, since those can enter and exit the production process very quickly, and it’s easy for us to scale our quality and shipping operations by adding people (as opposed to laser cutting or bending, which requires more equipment and a lot more space). If any downstream operation is backed up, we can remove parts requiring that backed-up operation from consideration when topping off sheets. We also can consider the current state of production when deciding how far to look ahead, and whether downstream operations should be fed extra parts.

We start with a full list of all unique materials containing parts needed on or before the "due-by" date. Once we select the material, we see a list of all parts requiring that material, with nesting priorities based on when they are due and what operations they require. The software creates a first-pass nest, which includes only parts due right away, and which prioritizes remainder sheets since (for us) they are faster and easier to load, and we like to limit the total number of remainders we have in stock. Then, the sheet is optionally topped off with other parts based on their priority.

We offer same-day turnaround, which means a nest that was optimal five minutes ago might now exclude a hot job that needs to jump in line. Our ability to rework scratched material is limited, so a failed part almost always requires a requeue at the lasers. New raw materials arrive every day, and remainders are created when other jobs finish, changing which sheets are available to produce the best nest.

If the lasers themselves are falling behind, we might want to avoid topping off sheets entirely. If a machine is down or otherwise backed up, we’ll want to avoid sending more parts to it. Finally, if we are far enough behind, we might enter a "triage mode" where we prioritize parts with the understanding that some are going to ship late, no matter what we do. Optimizing and then releasing nests just before the laser cuts them allows us to pull parts into production using the best information available.

Under the hood, the simplified JIT scheduling view shown in the figure is enabled by tight integration with our inventory and nesting systems. The scheduler understands what we have in stock, whether it is a full sheet or a remainder, and where it is stored. That information is fed to our nesting engine, which chooses the smallest sheet(s) necessary to cut the parts due right away. Chosen sheets then can be topped off with reduced impact downstream, since there is less material area to fill with parts.

Of course, tracking inventory is a constant challenge. At OSH Cut, measuring remainders, filling out labels, and scanning them into our ERP system was such a pain that it often didn’t happen. So we built a "denesting" step that automates the process. Now our system uses its knowledge of the nest, the parts on it, and the location of sheet cuts to automatically identify remainders, generate labels, and perform the inventory. Remainders are then scanned either onto flat pallets or onto vertical storage shelves with scannable locations. This ensures that our system knows what is available and where it is when generating nests.

Eventually, our goal is to automate even this scheduling process. Right now, we make decisions about how far ahead to look and what operations to prioritize or deprioritize. But once we understand the process well enough, we’d like to build that decision-making into the software itself. For example, a digital twin might keep high-accuracy detail about the current state of the production floor, down to how many operators are working in each area at any moment. That intelligence might be coupled with a Monte-Carlo simulation, which makes statistical predictions about what will happen if and when certain combinations of parts are released into production.

The JIT scheduler would run continuously in the background, creating concept nests and simulating them all the way through production. If a bottleneck or starved workstation is likely, nests could be adjusted on-demand to mitigate the problems. The JIT scheduler would keep a list of "current best" nests, adapting as circumstances change. We would need only review and release nest candidates as the lasers become ready for new work.

There’s an open question about how impactful this kind of automation might be for most shops. A manual JIT scheduling tool has obvious benefits. But automating that process with complex statistical tools and simulations might be only marginally helpful except for large, high-mix operations. On the other hand, in our complex, competitive manufacturing world, even slight increases in efficiency can matter. Whatever the case, optimizing high-mix sheet metal fabrication is a tricky and mostly unsolved problem. It’ll be interesting to see where new technologies can take us!

Caleb Chamberlain

is CEO and co-founder of Orem, Utah-based OSH Cut,

www.oshcut.com

.

TRANSPARENCY REDEFINED

Scan to learn more

MC Machinery’s remote360

®

is a robust production monitoring and support solution, designed to provide transparency to your machining processes.

Our web-based app provides real-time data to increase productivity, improve efficiency and reduce down time. And now, with our new advanced features added, your efficiency will be better than ever!

Analyze, Monitor,

Produce

.

For more info, call

630-616-5920

or visit

mcmachinery.com