# A portrait of the software-driven shop

[TARİH: 01.03.2022 The Fabricator]

Management Chief Concerns

What used to take days or weeks can occur in an instant

By

Caleb Chamberlain

An order ready for shipment is scanned at Orem, Utah-based OSH Cut. When the order ships, the customer receives an email.

A

rtificial intelligence is a trendy term, often used loosely to describe all kinds of problem-solving software. It can seem arcane, but under the hood, AI is nothing more than a tool to take information and make decisions with it.

What might that look like? In the fab shop, AI might predict scrap rates and handling times, produce more efficient material nests, and create highly optimized production schedules.

The operative word here is

might

. The term "AI" properly refers to a particular class of decision-making algorithms. The reality is that many complex problems may be solved easily without the use of AI, but people will want to call it artificial intelligence anyway. That’s not a problem, per se. But as we explore the possible applications of AI in the fab shop, it’s worth pointing out that software automation is powerful not because it uses AI, but because it simplifies and automates things.

Software automation as a whole has a host of applications in the fab shop, doing in seconds what it used to take people days or even weeks to perform. AI is just one of many tools that make the magic happen.

Going Lean with Software

In the "2021 Financial Ratios & Operational Benchmarking Survey," published by the Fabricators & Manufacturers Association Intl., fabricators reported an average operating margin of just 8.7%, slightly lower than the long-term average of 9.1%. Slim margins are usually the name of the game in the highly competitive metal fabrication industry, and there is enormous competitive pressure to eliminate waste.

If a shop could conceivably eliminate a step without changing the finished product in any way, that step isn’t adding value. Under that litmus test, many normal and, until recently, unavoidable metal fabrication tasks are arguably complete waste.

Bidding is necessary, but much of that labor fails to produce work, and none of it intrinsically adds value. What if your shop didn’t have to hire and train estimators? The physical product wouldn’t be affected in the slightest, except to make it more profitable.

File prep also represents waste. Importing and converting customer-provided files, remodeling parts from prints, fixing design problems, and prepping production programs all add significant overhead. Billed nonrecurring engineering costs might provide added revenue, but at the expense of higher costs to the customer.

When parts finally go to production, a host of opportunities for waste arise. Creating production programs, nesting parts, tracking down raw inventory, loading material into machines, thumbing through paper travelers, tracking down missing parts, scrapping or reworking parts, setting up tooling, and other activities should be considered waste. It’s not enough to say that they are unavoidable. If they could be eliminated, the finished product would only cost less.

It’s not possible to remove all forms of waste, of course, but software automation is changing the landscape. Processes long seen as unavoidable can now be eliminated or dramatically streamlined, and some practices designed to minimize overhead are becoming obsolete. A software-enabled shop might be dramatically different from a traditional shop, from quote to cash. Here’s how that might look.

AI-driven Quoting

First, the front office is highly automated. There are no estimators, no accounts receivable or purchasing personnel. There are no dedicated design engineers, CAD designers, or CNC equipment programmers. Employees may have those skills, but most of that work is automated.

Quoting occurs online, where customers upload their files and obtain accurate pricing and lead time in any quantity. Software calculates everything that might affect the cost of the part, including production times, raw material and consumable usage, setup and handling labor, as well as scrap and rework rates. A customizable pricing model is then used to provide prices based on costs and a target margin.

To ensure that costing information is accurate, the quoting engine is fed detailed manufacturing data directly from the shop floor. Measured data includes production times, consumable costs, and labor costs for every part ever produced and for every step of the manufacturing process. Altogether, the quoting engine can see how long it has taken and exactly what it cost to produce similar or equivalent parts in the past. This detailed connection to data allows the software to bid both aggressively and accurately.

Part analysis is automated as well. Software performs design-for-manufacturability checks by analyzing the part geometry and highlighting potential issues that require attention. In clear cases, software automatically reports issues to the customer and declines the job, with no human involvement at all.

When computing lead times, the quoting engine analyzes real-time production data to determine availability and scheduling constraints. Lead-time options are provided along with pricing, and customers can select lead times as short as same-day delivery, at least when production capacity allows for it.

Manufacturing prep also is handled automatically. Customers’ CAD-native files are used to prepare production programs, and no engineering staff is required to reproduce geometry from a print or clean up customer-provided files. Design changes required prior to production are performed automatically, with clear, automated communication to both the shop and the customer. To the extent that large or complex jobs require human intervention, all required information is available at a glance.

The first time OSH Cut employees see a job, it’s already been scheduled and nested.

A web-based automated quoting platform at OSH Cut addresses manufacturability issues during the quoting process.

Automated quoting is perfectly scalable. With quotes and manufacturability checks provided automatically by software, tens of thousands of parts can be analyzed and quoted in a single day with zero labor overhead from shop personnel.

High-mix Fabrication at Scale

The AI-enabled shop receives hundreds of orders of varying sizes and types every day. To meet the high-mix demand, scheduling software analyzes parts, material types, and due dates to automatically combine orders, schedule them for production, and produce numerical code for production.

Using the same historical data as the quoting engine, the automatic scheduler predicts operation and handling times for every part, in every stage of production. Bottlenecks are predicted days in advance. The scheduler uses this data to perform production leveling. Part production is spread out to help eliminate bottlenecks, and jobs are planned and released strategically to keep all machines and stations busy without overwhelming them.

If new orders arrive that might affect the schedule or an existing nest, the production plan is dynamically and automatically adjusted to accommodate the change. The same is true if in-production parts are scrapped. Software automatically notices a deficit, selects raw material from inventory, nests with other parts to improve efficiency, and releases the job to production.

With hundreds of high-mix orders received and fulfilled every day, it would usually be extraordinarily difficult to predict material needs and keep the right inventory on-hand. Instead, scheduling software automatically creates purchase orders for approved vendors if there isn’t enough inventory on-hand. Purchasing becomes as simple as sanity-checking the schedule and approving POs, significantly reducing the amount of cash that has to be tied up in inventory.

The first time anyone at the shop sees a new part, it has already been analyzed, priced, prepped for production, scheduled, nested with other orders, and released to production. If there is insufficient inventory on hand, a PO has already been created. This all takes place without human interference.

When a job finds its way to production—often just minutes after a customer orders it—automation equipment is used to retrieve raw materials and start production. Here, shop workers finally become involved in the production process.

CNC laser and punch programming is performed automatically by software, with lead-ins and micro-joints placed strategically based on heuristics and historical data about tip-ups. If relevant, punch tooling is selected to minimize production time.

While the automatically generated production programs are usually just fine, a human operator can intervene if there are unforeseen issues. Without leaving the machine, the operator can open the program on a touchscreen, modify it, and redeploy. On-demand operator intervention minimizes downtime in the event of a manufacturing exception.

Such changes are recorded automatically by production management software. As more issues are caught and fixed by skilled operators, production software learns from its mistakes and becomes continuously better at predicting and avoiding issues that could stop a machine. In effect, the human operator’s job is to keep an eye on production and train the AI so that it does a better job in the future.

After a sheet finishes at the laser or punch, denesting and sorting are performed automatically by automation equipment. Parts are removed from the deck and placed on autonomous, unmanned ground vehicles (UGVs) that safely move parts to the next production step. Human operators intervene only to handle edge cases, like small parts that might have fallen into the machine, or large parts that can’t be moved by a UGV. Production software automatically detects missing or abnormal parts during denesting and signals a request for attention if there is an issue.

Inventory is managed automatically during denesting as well. If remainders are produced, they are labeled, added to the inventory database, and stored for later use. Every raw sheet and remainder maintains full traceability, with production history going back to the original PO used to order the original raw sheet. Similarly, the system can report every part produced on any sheet of material, with traceable certs and lot/heat information from the mill.

Every manufacturing step is equipped with a software console that clearly communicates design needs and constraints and provides operators the tools they need to do their job. Operators can access and modify production data, mark parts as finished and ready for the next production step, scrap parts or task them for rework, leave notes, and communicate with their managers or other operators.

Production consoles provide the bulk of the data collection used by the quoting and scheduling engines. Software measures scrap rates and setup, processing, and handling times for every part ever produced. This rich and detailed data is used to continuously train the scheduling software and the quoting engine. The more parts received, the better the system gets at predicting prices and avoiding scheduling bottlenecks.

Finally, shop workers are automatically notified when orders finish production and pass quality control. When orders require shipping, workers scan finished parts into boxes. A matching packing list is then automatically printed, along with a shipping label. When the order is shipped, the customer automatically receives an email.

Outcomes

In some ways, this software-driven shop is theoretical. In others, it is already a reality. New shops are rethinking traditional fabrication and applying software tools to extraordinary effect. Orem, Utah-based OSH Cut, a software-driven fab startup co-founded by the author, yields net margins approaching four times the FMA-reported industry average, and revenue productivity per employee more than three times above the average.

It’s worth noting that software automation isn’t a silver bullet. A shop specializing in mass production might rightly look askance at tools that benefit a high-mix shop. And even among high-mix operations, the scenario described here is rather specific. Every shop operates a little differently.

A shop should evaluate its own needs and take action step by step. Going paperless could represent a major and easy step toward improved efficiency. Off-the-shelf production management software might help eliminate waste, even if it doesn’t tie into a quoting system. Nonsoftware solutions can move the needle and set the stage for growth. For example, a whiteboard

kanban

system for production tracking could reduce headaches and help organize things on the floor, all for the cost of a rolling whiteboard, some markers, and a pile of sticky notes.

At the end of the day, the problem should drive the solution. A tightly integrated, highly automated, software-enabled operation represents one vision of a particular kind of shop. Only you can decide where you lose most of your time, and what you can do to get it back.

Caleb Chamberlain

is CEO and co-founder of OSH Cut, 165 N. 1330 W #C4, Orem, UT 84057, 801-850-7584,

oshcut.com

.