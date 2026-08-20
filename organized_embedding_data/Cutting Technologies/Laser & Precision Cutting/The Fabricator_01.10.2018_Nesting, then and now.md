# Nesting, then and now

[TARİH: 01.10.2018 The Fabricator]

How efficient flow of information transformed metal fabrication

By Mike Boggs

I

t’s 1990. Operation Desert Shield is underway, the personal computer is making its way into more homes, and at the sheet metal fabricator, the CNC laser cutting system is starting to change everything. A shop with two CNC punches and a CO

2

laser could employ two full time programmers who use nesting software—technology that in 1990 has started to become commonplace but is still in its infancy.

In 2018 a custom fabricator may have a similar mix of products as its 1990 cousin, with a combination of repeat and custom parts, but the fabricator has more cutting machines—perhaps a single CNC punch, two CO

2

lasers, and a fiber laser with a load/unload tower. Even with all this cutting power, the shop probably employs only one full-time programmer with a backup to assist during heavy production.

Comparing a fabricator of 1990 with one today, how much has really changed? Travel back to, say, 1979, and the differences would be ridiculously obvious. The shop wouldn’t have a laser, and it’s highly likely that someone would be feeding tape into a punch machine’s controller.

But by 1990 nesting software was gaining ground in the market, and the laser cutting machine had a permanent foothold. Sure, the CAD software then had just two dimensions, not three, but on the surface, a progressive fabricator in 1990 looked much the same as a typical custom fabricator today.

That’s just on the surface, though. In 1990 you’d probably see piles of work-in-process (WIP), and the shop would have very long lead times, at least by today’s standards. What was the hold up? Machines certainly were a contributing factor; a fiber laser today can run circles around a 1990-vintage CO

2

laser. But another big holdup wouldn’t be obvious to the casual observer: the slow, tedious, unreliable flow of information. People in the shop certainly knew how tedious managing that information could be—and perhaps no one knew better than the CNC programmer.

Programming in 1990

The modern metal fabrication company in 1990 is transitioning to computer aided design CAD—2-D, of course, but CAD nonetheless. Engineers develop flat (unfolded) parts, and quite often they calculate the dimensions manually. As engineering releases new parts, they place CAD drawings in a directory that can be accessed by the CNC programmer.

The programmer receives a hard copy of open work orders for the upcoming production period. After manually sorting the work orders to separate new parts from those previously programmed, the programmer validates that all drawings have been received and then reports discrepancies back to engineering to determine the status of missing drawings.

He then opens each CAD drawing file to prepare the parts for import into the company’s computeraided manufacturing (CAM) software. Each CAD drawing is an orthographic part layout that contains dimensions and other notes that must be removed. Unfortunately, engineering has not done a good job of layering these drawing components, so the programmer must delete them manually. Once he removes the extraneous geometry from the drawing, he reviews the parts for geometric integrity.

Although most of the parts from engineering are good, some parts occasionally require manual cleanup—so this means all parts must be reviewed. Each part is then saved as a DXF file. The programmer imports the DXF files into CAM software, then applies punch tooling to parts going to the punches and a toolpath to parts going to the laser. Not long before, the shop primarily produced one part at a time. Now it’s starting to nest multiple parts on fullsize sheets.

Because of this change, the programmer must now accommodate multiple part production. The nesting software recently added an automatic tooling feature, but its results are dubious at best, and making tooling edits is a bear.

So the programmer has to apply tool hits manually by activating the desired tools and individually selecting the applicable part features. With manual tool selection and placement also comes the tedious work of placing shaker tabs, or micro-joints.

For the laser, the programmer still imports each part and applies the toolpath manually, allowing him to select the micro-joint locations on the applicable parts and verify the lead-in and lead-out on each cut. He also checks the cut sequence of internal part features and adjusts them as necessary.

After the programmer assigns the punch tooling and laser toolpath for each part, he saves them in the CAM part library. While doing so, he must enter all part information, including part number and material parameters, manually.

Each day’s objective for the 1990 programmer is to create dynamic nests to run a day’s production on the laser, along with a nest of custom jobs for the punching machines. To accommodate production changes, the programmer has NC programs complete two days ahead of scheduled production.

He schedules production by manually sorting parts into nest groups based on the work order, due date, material, and machine. To create the nests, he looks up individual part numbers in the CAM software part library and assigns the desired quantity. He creates a nest on standard sheet sizes for each machine. He then scrutinizes hot parts individually, deciding whether to add them to an existing job (which would require a nest recalculation and reprocessing of layouts) or create a new nest and prioritize it in the production schedule.

With the nests created, the programmer evaluates each layout for acceptable material utilization and generates the NC programs. If the programmer finds he needs to achieve better material utilization, he can add parts (either filler parts or parts from different jobs) and recalculate the entire nest, or he can open the layouts and position additional parts manually.

To create NC programs for the punch, the programmer opens each nest layout, validates the virtual turret tool load, assigns and verifies the tool selection sequence, adds points where the sheet repositions as necessary, optimizes the punch toolpath, and generates the NC program. For the laser, he simply optimizes the toolpath and generates the NC program.

Throughout all of this, the programmer always has an eye on material utilization—that is, filling the sheet as much as possible. If a nest isn’t filled, he looks to see if he can combine more jobs on a single nest or make filler parts, like commonly stocked components used on a range of sheet metal assemblies the fab shop produces. Of course, this often leads to overproduction and the sorting and storage ramifications that go with it. But those ramifications are better than the alternative: managing remnants.

Having a remnant is considered a last resort, and for good reason. Remember, this is 1990, and the shop really has no automatic way to track remnants. When remnants are created, the shop can’t push them back into inventory. If a remnant is used at all, it’s usually because the machine operator and programmer collaborate to squeeze a small job on available remnants stored by the machine. Still, those small jobs rarely fill remnants perfectly. Usually, those jobs consume only a portion of the remnant sheet, and the shop simply scraps the rest.

Managing remnants is a manual process, and, in this sense, very much like many other tasks carried out among programmers and machine operators. Overall this 1990 shop has very little digital information. Paper rules the day. Employees transfer paper work orders to the programmer, and they attach physical nest reports and setup information to the routing packet and carry it to the shop floor. As jobs are finished, the machine operator completes a job report that allows for inventory adjustment. If a customer or anyone else wants to know where a job is in production, people need to walk to the floor, talk with operators, and continue hunting until they find the work.

Nesting Terms

Nest Job:

A group of parts designated to be cut together to fulfill production requirement (such as customer order or production period).

Nest Layout:

The arrangement of parts on a sheet metal blank.

Nesting Strategy:

How a shop determines what parts will constitute a nest, be it static or dynamic. Which nesting strategy works best depends on a shop’s production goals, which hinge on factors that include production style (job shop or original equipment manufacturer), volume, part mix, CNC machine capacity, programming capacity, material-efficiency goals, and acceptable lead times.

Static Nesting:

A static arrangement of a part or parts that are run repeatedly. A static nest may consume one or more sheets and often contains all parts necessary to manufacture a specific product or fulfill a repeat order. Static nesting is most common when producing a lower quantity of unique part numbers in high volumes.

Dynamic Nesting:

The nesting of parts that individually meet defined criteria at a given point in time. The criteria could include the work order, due date, priority, material parameters, cutting or punching requirements, or material utilization. Because new orders are introduced continually, the mix of parts available for nesting changes constantly. As each subsequent nest is built with new parts meeting current (and possibly changing) criteria, the nested patterns created are probably unique. Dynamic nesting responds to the fluid nature of a production environment.

Batch Nesting:

The creation of multiple dynamic nests to be run over a period of time. An example might be a series of dynamic nests to run a full day’s production on a specific CNC machine.

JIT (Just-in-time) Nesting:

Real-time nesting, often performed at the CNC machine. The machine operator creates a nest from parts in the current production queue. Each nest is created just as processing of the previous nest is completed.

Programming in 2018

In the progressive metal fabrication shop of 2018, digital information reigns. The company maintains 3-D CAD files for all products. During the design phase, engineers assign part numbers, revision numbers, material properties, grain orientation, and other data. The company’s CAM software has an integration add-in for 3-D CAD software; as engineers complete a new product design or engineering change, they execute a command that unfolds the parts, validates the part geometry, and uploads them along with manufacturing data to the shared CAM part library. Throughout, the CNC programmer intervenes only if a part is determined missing during actual programming and nesting.

Most production work has shifted to the lasers, which require no toolpath assignments. Hole-intensive jobs, along with work that takes advantage of onmachine forming and tapping tools, remain at the punch presses. Although soft-ware assigns tools to parts based on the tooling library, the CNC programmer still validates the tooling on each part, simply because of the frequent use and complexity of special tools.

In 1990 the programmer was involved in all aspects of programming and nesting, touching every part. Today the programmer performs a few tasks that are not yet automated and handles the exceptions.

The CNC programmer does minimal scheduling, most of which is carried out by the company’s enterprise resource planning (ERP) software. Each nest is released as a comma delimited file containing information including job number, part number, revision, priority, quantity required, routing information, work order, customer details, and inventory information.

The release of nests spurs nesting software to create the nesting layout. The nest layouts are created on sheet inventory as dictated, with the exception of the fiber laser. For this, nesting software analyzes several available sheet sizes and selects the sheet that provides the best material utilization.

Regarding scheduling, flexibility is the name of the game. Schedulers can make changes in the ERP scheduling module until the nested layouts are processed and NC programs are created. This means that if an urgent order comes in at the last minute, slipping it into the schedule shouldn’t be a problem. A "hot job" becomes, well, just another job with increased priority. As for the truly hot jobs, the ones submitted after the NC program is created, CNC programmers can handle those individually, squeezing them into production where they can.

The programmer of 2018 doesn’t create nests per se, but instead reviews each nested layout for anomalies that require manual intervention. He does scrutinize the punch nests to verify tooling strategies. As nest layouts are approved, software generates the NC program automatically.

Remnants also are tracked automatically. In fact, remnant management has become so seamless that programmers no longer work to fill up a nesting layout. They no longer need to worry about overproducing.

The nesting software automatically detects material drops and creates the remnants. The remnants are placed back into inventory and often are selected by the programmer for future use. As remnants are created, the nesting software generates a report that the machine operator attaches to the remnant.

Information in 2018 no longer lies hidden in silos, trapped in a certain department and job function—and nesting software is helping to break down those silos, creating an industry-standard XML file containing every piece of information about the nest job and individual parts. This includes material utilization and runtime information per job, layout, and individual parts, as well as information about the inventory consumed and remnants created, routing, work order, and customer information. As the machine operator completes a job in the shop floor management software, the nesting data is accessed and relayed back to the ERP software. Inventory levels are adjusted; work orders and routing information are updated; and material, machine, and labor costs are applied for accurate part costing.

Perhaps most significant, nesting reports detailed part routing information that helps simplify part sorting and streamline downstream operations. After all, what good is a nest with extraordinarily high material utilization if those cut parts flood the downstream workflow? With so much WIP, parts get lost and have to be recut—which, of course, doesn’t help throughput.

Now versus Then

The programmer’s role has obviously changed dramatically over the years. In fact, the programmer’s changing role illustrates just how much metal fabrication has changed in three decades.

In 1990 the programmer was involved in all aspects of programming and nesting, touching every part. Today the programmer performs a few tasks that are not yet automated and handles the exceptions. The CNC programmer spends much less time with the details of punching or cutting; today, the role is more about facilitating the overall production flow.

Everyone now has access to production information. Raw stock inventory can be reduced as inventory levels are updated in real time. Combine this with better remnant management, better nesting algorithms, and better CNC technology, and you have a fabrication shop floor that can deliver parts extraordinarily quickly.

▸ Mike Boggs is sales manager, Striker Systems, 104 S.C.T. Drive, White House, TN 37188, 800-950-7862,

www.strikersystems.com

.