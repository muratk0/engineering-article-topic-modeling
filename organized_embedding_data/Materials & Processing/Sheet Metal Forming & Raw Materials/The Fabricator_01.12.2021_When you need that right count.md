# When you need that right count

[TARİH: 01.12.2021 The Fabricator]

Tube fabricator relies on a new software module to track parts accurately

By

Dan Davis

What’s the count on those tube fabrications? That can be a real challenge for a machine operator, especially if the job spans more than one shift. UltraFit, Mississauga, Ont., found that an automated parts counting module of its enterprise software suite could help with this task.

Inok/iStock/Getty Images Plus

"Y

ou have dynamic workcells and short runs with a wide variety of products. This really is a difficult production equation," said Grant Hartley, business systems controller, UltraFit Manufacturing Inc., Mississauga, Ont.

That’s a statement a lot of folks in metal fabricating can appreciate, but context gives you a little more to think about. UltraFit started as a job shop more than 30 years ago and later branched into OEM production to serve customers in the automotive industry. The company’s vision states that it offers "the most innovative, competitive tubular solutions to customers," but it also provides welded structures and structural components to other industries, such as furniture manufacturing.

The shop floor has 63 major workcells, and many of them can be reconfigured to accommodate new work or legacy jobs that have scaled up. (It also has a few dedicated production lines.) The company has 470 active products, with an average of three work-in-process sequences per part. Typical production runs last three to nine shifts, or one to three days.

UltraFit employs 230 people, with it adding about a quarter of them over the last seven years. According to Hartley, the company tripled production over that time.

"The key to our success is our expertise with manufacturing processes involving complex tubular solutions. This involves tube bending, tube forming, robotic welding, and manual welding," Hartley said. "We need fast changeovers, and we need to minimize work stoppages to maximize production efficiency."

And this doesn’t even cover packaging requirements, which vary greatly according to customer demands. Bins typically contain between 72 and 1,650 parts. Totes also are used, and pallets typically hold up to 36 totes, which "creates a huge amount of labeling issues," Hartley said. To handle this variability, UltraFit still relies on operators manually loading and unloading materials and products.

Also, shipping labels aren’t just simple tags. The tote labels have to be linked to master labels that must be applied to advanced shipping notices. Everything has to be connected to expedite product delivery to the customer.

The machine operators had their own challenges, mostly dealing with counting parts and loading materials. When it came to part counting, the operators had to contend with older machines with counters that were reset after something like a visit from a maintenance technician, previous shift operators failing to report their own part counts, and partial labels from the previous shift being lost or ignored. The machine operator also had to keep up with bin counts and shift counts, and with up to 1,650 parts in each bin, that became quite a challenge. From a materials loading perspective, if a machine operator misreports, operators downstream of the workcell can’t do their own reports because they don’t have enough material. In other instances, some machine operators steal active labels from other jobs to cover up issues on their own jobs, which just pushes the parts shortage from one bin to another.

The end result of all of this was that people began to suspect that the entire system led to low overall equipment effectiveness (OEE). The operators were being asked to be mathematicians.

"I see what these guys have to go through to maintain their bin counts, and it is some advanced mathematics," Hartley said.

Additionally, UltraFit management frequently saw machine operators stop production to go report the part counts, scrap, and downtime. That further increased the concern about the production system’s perceived low OEE.

The concerns weren’t unfounded. Experienced operators knew what they had to do, but even on their most efficient days, they still needed to walk to the terminal, find the resource, enter the quantity, and get the label. They needed to do the same thing for scrap and downtime. (Sometimes when the machine was going to be down only for a short amount of time, even the experienced machine operators wondered if it was worth reporting the machine downtime. Well, it’s hard to get accurate performance numbers without realistic data.)

The temporary employees simply didn’t know any better. They voiced a simple question many times: "Why do I need to keep track?"

Automatic Part Reporting to the Rescue

Hartley and his colleagues suggested leaning on the company’s current enterprise software suite, Epicor CMS, to see if a tool might exist to help them with this parts counting challenge. UltraFit already was using the software’s EDI, accounting, MRP, inventory control, shipping/receiving, and work order management functions, and the latter was the place where the company would find what it was looking for.

Within Production Manager, the manufacturing execution system module in Epicor CMS, UltraFit realized that it could get information from the production machines to provide essential shop floor data. The Automatic Part Reporting (APR) function within Production Manager could give Hartley and his team the specific tool that would allow them to tackle this low OEE situation.

When fully implemented, APR becomes a new app button on the Production Manager interface. When the button is clicked, the user is taken to an automatic reporting screen, where the quantity per cycle from workcells is reported. The counts are derived from PLC signals from the machines or from digital interface devices. When the count is green, the operator can report. Also, when that full count is achieved, a label is automatically printed out.

Bent and perforated tubes are a couple examples of the tube fabrications provided by UltraFit Manufacturing.

This workcell requires one operator to engage in at least three production steps before placing the part into a bin. On top of all this activity, the operator needs to keep a part count. Now software helps to maintain accuracy in part counts; the operator’s count is a backup in case of a faulty PLC signal coming from the fabricating equipment.

At the end of the shift, operators report partial production, and those labels are then loaded back into the system, which recognizes the partial report as it keeps track of the next full bin. Operators also are tasked with reporting scrap. If needed, anyone working in the APR interface can adjust the current count for the job and the pack size and order quantity.

To make this reality on the UltraFit shop floor, the Epicor technical team needed to have the machines connected so that information could be fed into the Production Manager module. That meant digital interface devices were needed for the older production machines ("They basically take the pulse of these machines," Hartley said), and connections were made to the newer machines’ PLC signals that represented completed part production.

The implementation team used an OPC server product to connect the shop floor machinery with Production Manager. The connectivity provided by the server allows for the translation and data brokering of the manufacturing data and allows the software module to map all of the PLCs and digital interface devices to the specific machine in Production Manager.

Production Manager is the hub where operators, setup technicians, and management can access this part counting information. The setup techs log in to record changeovers, reset run counters, and report scrap. Managers can oversee the pallet builds, which is important for coordinating the right labels for the right jobs.

Epicor CMS handles the master data management and all of the support functions, like routings and bills of materials. Managers also can use this interface to access Production Manager and its functions.

Now when a part is completed on the last machine in a workcell, the PLC or digital interface device sends a signal that reliably corresponds to that completed cycle. The OPC server maps the signal from the machine being used to the resource in Production Manager. Even with this automation, operators still are required to report scrap as incurred. It can’t wait until the end of the shift because the bins will get out of sequence.

Production Manager automatically prints the labels. Master labels come from CMS, and they are at the correct pallet quantity.

The Second Part of the Automation Push

With this push to automate part counting, UltraFit management also wanted to get a more accurate record of machine status. What was the real scoop on machine downtime?

Because many of the machines on the shop floor can’t provide a state bit, a signal that can trigger a downtime cue when a fault is detected, the implementation team decided to rely on PLC signals for state monitoring for all of the machines. (For older machines, digital interface devices were used to pick up the signals.) Using advanced tag counts, the OPC server uses an interval of two times the machine cycle time to determine if downtime is occurring. For example, the server receives the PLC signal that a manufacturing process has begun, but if that second PLC signal, which would normally note the end of the fabrication cycle, doesn’t reach the server within that determined two times fabrication cycle time, Production Manager deems that machine to be down and unable to process parts.

The server has no way to ascertain what the actual cause of the downtime might be. The operator, as a result, has to input the appropriate downtime code. The operator also can add detailed comments about the downtime.

When the machine comes back online, Production Manager is set to run for the next cycle. The operator doesn’t have to engage with the system, just begin the production work.

"This is a very important function for us," Hartley said.

The Results

After implementation of APR, UltraFit found that it had achieved an operator efficiency gain of 15%. "That’s a big number for us," Hartley said.

Six percent came from reporting and label application automation. The operator doesn’t have to go to the terminal to report production. In some situations, for example in the busy tote areas around the tube perforating machines, some shop floor workers have been designated to go from the common label printers and actually take the labels to the workcell so the operators don’t have to interrupt their workflow.

The rest of the 15% came from simplifying the tasks and enhancing the workcells’ "rhythm," as Hartley described it. As an example, he described a workcell where an operator takes cut-to-length tube stock, inserts it into a flaring machine, and then into a perforating machine. If the operator is keeping that perforating machine going, UltraFit is making money, according to Hartley. When the parts are taken from the perforating machine, the operator inspects the tubes and places them in the totes if all checks out. Meanwhile, as part counts are reached and jobs are complete, the system prints labels automatically.

"State monitoring provides machine truth, and this is a critical enabler for continuous improvement."

—Grant Hartley, UltraFit Manufacturing

"When we have a number of operators all working on totes, it is common for us to have a runner just dedicated to taking those labels from the label printer, bringing them over, and putting them on these totes. That way our operators can focus on making money," he said.

Operators still have to keep track of counts to act as a backup in case a PLC signal is lost, for instance. Even with this requirement, Hartley said the operators still think the automation investment has saved them a lot of time and allowed them to focus on making parts.

"Our president has a way of crystallizing the gains that we have received. I like his quote, ‘It is like having an electronic supervisor at every workcell,’" Hartley said.

Newly introduced state monitoring is beneficial as well for UltraFit. The microstops, short periods of downtime that the operators didn’t think were worthy of reporting, are now being recorded. Management has a much better picture of shop floor performance.

Now, that alone won’t lead to operational improvement, but it does provide the evidence that can be shared with shift leaders and workers. If the issues affecting the microstops can be addressed, more uptime can be gained. Additionally, a root cause for such interruptions, such as tooling or material problems, might be identified and corrected.

"State monitoring provides machine truth, and this is a critical enabler for continuous improvement," Hartley said.

Introducing Electronic Oversight

Around the same time that UltraFit started the APR project, it set forth on a plan to offer more shop floor visualization. The idea was to provide evidence to anyone in front of a monitor that these microstops were occurring and to inform machine operators just how they were doing in terms of producing parts.

Hartley said that the company did a study before formally launching the project just to see how machine operators were performing before they were made aware that they were being formally tracked. When the operators were given real-time visual proof of their performances, production jumped by 15%.

"When we rolled this out across the plant with a more focused board that included shift comparisons, we found that we had shifts trying to compete with other shifts’ performances," Hartley said. "That’s a wonderful thing."

Big-screen monitors were placed in a central location so that supervisors could more easily track departmental performances. Reporting terminals with scan guns were installed at each workcell to make the process of data delivery easier.

Hartley added that since the early days of this shop visualization project, results have diminished over time, so it remains the responsibility of management to make this visibility an ongoing achievement.

Getting to the Next Level

Hartley said with the APR and state monitoring projects underway and the shop visualization effort complete, UltraFit now can take steps to produce more operational gains:

• Finding a way to take all of the data and present it in a way that will help managers and workers identify and resolve production issues.

• Establishing a culture of engagement will bring everyone to the continuous improvement table, not just leaving it up to supervisors and management.

• Engaging teams to identify improvement projects, assigning project responsibility, and incessantly following up with those team members will deliver continuous improvement results.

"This is plant management 101. This is hard work," Hartley said. "But this is automotive. We deal with thin margins, and our customers are expecting continuous improvement."

Editor-in-Chief

Dan Davis

can be reached at

dand@thefabricator.com

.

UltraFit Manufacturing,

ultrafitmanufacturing.com

Epicor Software,

www.epicor.com

"We BARCODE Difficult Stuff."™

100% Employee Owned

sales@infosight.com

Identification and Traceability Solutions for Galvanizers and Fabricators

Laser Metal Tag Printes

KettleTag

®

Plus

PaintTag™

ShotTag™

PowderCoat™ Tag

InfoSight Means Innovation — For Identification And More.

Our proven record of developing new products for customer’s unique requirements means we can help you, too.

Chillicothe, OH ∼ 740-642-3600 ∼

www.infosight.com

CORNER NOTCHER

www.punchtools.com/corner

NOTCHES THICK / THIN : ALUMINIUM

STAINLESS MILD STEEL

SEE OUR VIDEO LINK BELOW

www.punchtools.com/corner

www.punchtools.com

Email:

orders@punchtools.com

• tel

604.521.6444

• Toll Free

1.800.668.4996

Made in North America by Punch tools

Editor’s Note: The following is adapted from a virtual presentation, "Efficiencies Gained With Automatic Part Reporting," made earlier in 2021 during an Epicor Software user event.