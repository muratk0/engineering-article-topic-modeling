# Automation on the move

[TARİH: 01.12.2021 The Fabricator]

Cover Story

How mobile automation could change the fab shop

By

Tim Heston

The metal fabrication factory of the future might work with a heterogeneous fleet of mobile automation.

PhonlamaiPhoto/iStock / Getty Images Plus

C

ustomers don’t pay for parts to be moved from one process or station to another. Still, without such movement, value creation—cutting, bending, welding, coating—can’t take place. If parts don’t move, nothing happens. Even worse, inadequate material handling increases variability and unpredictability, which necessitates larger work-in-process (WIP) buffers between processes. The larger the WIP buffer, the longer the lead time, and the less competitive a fabricator becomes. It’s a vicious cycle worth breaking.

Most custom fabricators make such a variety of parts that they really can’t stray too far from the departmental, process-centric shop layout, hence the need for fork trucks. And no matter how streamlined the part flow, people still spend time stacking, lifting, and transporting—all non-value-adding processes. In the coming years, however, many shops might transfer all that nonvalue work away from employees and toward automated alternatives to the fork truck: specifically, the automated guided vehicle (AGV) and the autonomous mobile robot (AMR).

AGVs and AMRs

According to research from LogisticsIQ, the global AGV and AMR market is expected to reach $14 billion by 2026, with more than 270 vendors serving the manufacturing and logistics space. According to the study, AMR adoption in particular will be especially robust, with a combined annual growth rate of roughly 45% between 2020 and 2026.

AGVs have come a long way since they relied on wires or magnets in the floor. Many in use today use laser triangulation combined with reflective tape to achieve what the industry calls localization, or the ability for the AGVs to know where they are. Traditionally, AGVs navigate a fixed path while AMRs navigate freely in a dynamic environment, which changes how the vehicles avoid obstacles and deal with traffic congestion.

"[AMR fleet software] shares positional data between the different robots, which helps them avoid each other before they get close enough to each other so their sensors can detect each other," said Andrew Feeney, senior AMR engineer with Perrysburg, Ohio-based automation integrator Robex. Before that he worked for more than four years at AMR provider MiR.

Feeney added that AMR applications today usually help overcome the challenge of high-traffic areas. AMRs can avoid obstacles in sophisticated ways, and they don’t need to follow tracks with physical markers. But he added that many applications take advantage of another AMR trait: They can not only move parts from A to B, but also be designed to interact with other automated systems in various ways. "We’ve had applications where 6-axis robots pick or place onto an AMR," Feeney said, adding that in these cases the applications have used "docking markers to improve positional accuracy and assist with different types of equipment that want to pick and place goods to and from the robot." He added that AMRs also can have top modules that can be customized for specific jobs, roughly analogous to end-of-arm tooling on stationary robots.

As with so much in automation, AGVs and AMRs continue to evolve. For instance, AGVs too have demonstrated ability to interact with machines. For example, German AGV provider Jungheinrich has a partnership with DMG Mori on an AGV system that can load parts, interact with technology, and streamline the machine shop floor.

Regardless, whether it’s an AGV or AMR, what matters most is what it can offer the metal fabricator. Which is best depends on what an operation needs.

This AMR top module creates a mobile conveyor. The AMR with a part or box on top positions itself next to a delivery point, and the conveyor automatically offloads the work it’s carrying.

Robex

In this concept drawing, a mobile robot works with stationary automation to deliver and retrieve parts.

nay/iStock / Getty Images Plus

No Place for Walled Gardens

Automated vehicles can operate as a node under a plant’s production control or manufacturing execution system (MES). An automated vehicle itself is adaptive; if it wasn’t, it wouldn’t be safe to use out in the open. Sensors allow it to avoid obstructions and prevent collisions. But the true operational brains reside in plant software.

In some cases, though, automated vehicles aren’t connected to overall plant software but instead to triggers between specific operations. For instance, a downstream operation can trigger an automated vehicle to deliver work at a certain time.

Kai Beckhaus, president at Houston, Texas-based MCJ Supply Chain Solutions, an automation joint venture of Mitsubishi Logisnext Americas and Jungheinrich, described a

kanban

scenario where operators at the downstream operation deplete parts to a certain level (the "safety stock" level). They then push a button (or use a tablet, if the application requires different kinds of replenishments) to signal an AGV to deliver more parts. This concept could be applied in an automated fashion as well. Sensors at a pallet location detect when a pallet of buffer stock is removed, then send a signal for the AGV to retrieve more.

The MES-connected approach offers greater possibility to scale up mobile automation. And for AMRs that interact with machines around them, connectivity and interoperability have become especially important. Automated vehicles communicate via Wi-Fi, but the digital information stream being sent through the air needs to be translated. Such automation really can’t thrive in a walled garden.

Automated vehicle manufacturers tout agreements with machine manufacturers. Jungheinrich has a partnership with TRUMPF, for instance, but it also has middleware software that can communicate with a variety of MES and production control systems. "[Automated vehicle] vendors now follow the customer specifications," Beckhaus said. "It’s not the other way around." A fabricator’s IT and ops managers need not move heaven and earth to adapt to the connectivity requirements of automated vehicles.

In September, FABTECH hosted an interoperability panel among various AMR players and users, including one of mobile automation’s largest customers, FedEx. Aaron Prather, senior adviser, technical research and planning for FedEx, focuses on integrating new technologies into the overall enterprise.

"That could be anything from robotics to RFID tags," he said during the panel discussion. "We take technology through its paces and see if it’s ready for enterprise use. And interoperability is key. As we acquire new technologies, we need them to all work together."

"You can build an autonomous mobile robot that can do one type of thing really well," said panelist Jason Walker, CEO/co-founder of Waypoint Robotics, a Nashua, N.H.-based company that makes a variety of AMRs for transporting tools and materials, even in high-traffic, unpredictable environments. "But no matter how cool our robots are, they don’t have forks. We’re never going to pick up a pallet. Likewise, that pallet robot is never going to be able to slide up to a CNC machine and grab something out of it. The reason you have all these form factors is that each one of them is hard to do at an economical price; they are all made by individual startups. So if you want to solve all the problems in a facility, you will want to mix and match a lot of different companies. You’ll have a heterogenous fleet."

An automated guided vehicle (AGV) with forks stands ready to retrieve a pallet of parts at the TRUMPF Smart Factory near Chicago.

MCJ Supply Chain Solutions

Walker’s Waypoint Robotics is part of a group called MassRobotics, a nonprofit that in 2021 released the

MassRobotics AMR Interoperability Standard

. "It allows for our robots to be in the same building, understand what the other robots are doing, avoid potential collisions, unify traffic flow, and it sets the stage for tons of other capabilities."

Eighty-Twenty

Although growing more common in warehousing, distribution, and certain manufacturing environments, AGVs and AMRs haven’t permeated metal fabrication widely in the U.S., but it probably won’t stay that way forever. Various laser cutting, punching, and press brake OEMs have presented their ideals of the future fab shop, showing mobile automation in tradeshow exhibits and testing them in showrooms.

Today, TRUMPF’s Smart Factory outside Chicago has a fleet of Jungheinrich AGVs delivering and retrieving cut blanks and formed parts. As Kartik Iyer, director of the TRUMPF Smart Factory, explained, as with so much in metal fabrication, the 80-20 rule applies when it comes to using automated vehicles. "Avoid going into a project thinking you’re going to automate everything. You need to use the 80-20 rule. You need to go find your high runners, or the parts with high volume, that require frequent transport, and then try to create autonomous transport for those parts."

He added that one chief characteristic to consider is a part’s size. "The larger the size of the part, the bigger AGV you need. You need a wider aisle, and the safety zones need to be larger."

Parts need to be within a certain length and width to fit on top of a standard pallet, and AGVs can have issues when parts extend beyond and overhang, potentially interfering with the vehicle’s laser sensors.

Sure, AGVs come in all shapes and sizes, and some can handle massive workpieces, but if a shop processes those large workpieces only on occasion, bringing in such an AGV to handle those rare cases—and incorporating the wide aisles and other elements such a setup requires—probably wouldn’t make sense.

"Try to tackle problems where the solution would have maximum impact," Iyer said, "rather than trying to solve every single problem in your shop."

As MCJ’s Beckhaus explained, once a shop determines what it will automate, it needs to know what kind of material handling it needs during times of peak capacity, as well as the frequency of those peak-capacity periods. Most automated vehicles are battery-charged, and they automatically return to their charging stations when not in use. Peakdemand periods that occur only occasionally, like once a week or shift, might require a different number of vehicles than an operation with peak demand that occurs every few hours.

Another overarching strategy regarding automated vehicles is to avoid complexity by reducing process variability. AGVs can have all sorts of bells and whistles, but many of them might not be needed if the process is stable and the parts are accurate.

For instance, AGVs have hydraulic sensors that give an estimate for a load weight (to ensure the load is safe to lift), but it’s not a precision scale. Theoretically, an AGV could integrate such a scale to weigh the load on top of the pallet it’s carrying, then report back to the MES saying that the weight of a certain batch is off, meaning that parts might be missing.

Thing is, all this capability creates a reactive, Band-Aid fix that doesn’t get to the root of the problem. Process consistency upstream, be it through automated parts stacking or other process control measures, all managed by production control software and the IT infrastructure, might be the better strategy. It’s garbage in, garbage out. The long-term solution isn’t to catch and remove the garbage, it’s to stop the garbage from being produced in the first place.

Similar thinking goes for job identification on the floor. As Beckhaus described, some manufacturing applications use passive identification of pallets. Although the individual jobs on the pallet have work tickets with QR or bar codes, the pallet itself might not have an identifying bar code. That’s because in any given situation, the AGV—receiving instructions from the MES—has only one pallet to retrieve. "You know where the pallet is, and the AGV is instructed to bring the pallet from A to B. Because just one pallet of parts was produced, there is just one pallet, so there cannot be a mix-up." This exemplifies the advantage of single-piece (or in sheet metal, single-pallet) part flow. The less WIP an operation has, the easier that WIP is to identify.

Of course, some operations might require more complex staging. In this case, Beckhaus said that AGVs can work in conjunction with bar code scanners or RFID. "But again, you would never want to overload such an application. If you have enough security [for success] from an IT system, you’d go with that, because when you add more complexity, you add more potential causes of failure."

First Steps

First comes good housekeeping. Ideally, aisleways should be well-defined, debris-free, and clean. The floor need not be perfect and entirely free of cracks, but it should at least be decent enough, and it certainly shouldn’t be littered with empty pallets. If AGVs need to retrieve material from racks, the racks themselves need to be in a consistent position; excessive bowing of certain rack beams while under load might cause an issue. "You need to build a reliable environment to ensure reliable AGV automation," Beckhaus said.

AMRs rely on sensors as well and, hence, need a reasonably smooth floor. "You need a somewhat smooth floor," said Cal Bowers, vice president for growth at Robex. "The sensors can get jarred if the AMR drives over a very rough surface, so we do look at the floors during an initial site visit."

Beckhaus added that some extremely dusty environments might not be suitable for an AGV, mainly because the dirty air can clog the vehicle’s sensors. Still, most precision sheet metal environments with proper ventilation and dust extraction should be perfectly suitable for automated vehicles. When dust covers a vehicle’s sensors, it can’t "see" and so just stops. At worst, someone might periodically need to wipe the vehicle’s sensors with a clean cloth.

Another initial step toward mobile automation is to establish the

load unit

—in the context of a sheet metal fab shop, this would be the pallet that the work sits upon. "We care about the load unit," Beckhaus said, "but we don’t care what sits on top of it. It picks up a load unit and brings it from A to B, as instructed."

The load can’t exceed a maximum weight. Moreover, the load can’t be so off-center as to cause the vehicle to tip. The load also shouldn’t have loose parts that could shift in transit. And the work itself cannot overhang from the pallet in an unexpected way as to interfere with the vehicle’s safety systems. As Beckhaus explained, AGVs can deal with certain part overhangs, but "they need to be defined and there are certain limits. A very long part [with extensive overhang] will probably not be feasible, but a less extensive overhang can work."

That overhang just needs to be defined in the vehicle’s safety system so that aisle widths are sufficient for the vehicle to travel and make turns with the appropriate radius. The overhang should never collide with objects or, especially, people. As Beckhaus explained, the overhang limitation is often why the initial material handling—truck unloading, moving raw stock—is still manual. The handling by automated vehicles occurs downstream.

Beckhaus added that anything having to do with safety "has to have redundancy in an AGV environment." Sensors can fail, so backups must be there to ensure that both the automated vehicle and the load it carries do no harm.

This is why process consistency and simplicity are so important. The less predictable a process is, the more sensors it can require, and if those sensors are applied in safety-related situations, they’ll need built-in redundancies. It’s always best to "engineer out" the unsafe condition so that the hazard doesn’t occur in the first place.

Streamlining Indirect Processes

Mobile automation opens the door to all sorts of ways to streamline part flow. Emerging developments in artificial intelligence and machine learning offer new possibilities as to how mobile automation interacts and learns from the environment around it. In the near term, however, automating the act of moving pallets of parts from workstation to workstation could relieve an industry that can’t find enough fork truck drivers and other material handlers.

As Iyer put it, the goal is to streamline indirect processes. "These are the hidden latencies that are built into production where making faster machines wouldn’t solve."

Overall, he said, only about 20% of metal fabrication involves direct processing—laser cutting, bending, welding—and about 80% of the processes in metal fabrication are indirect. "Materials management is a big part of that."

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

LogisticsIQ,

www.logisticsiq.com

MassRobotics,

www.massrobotics.org

MCJ Supply Chain Solutions,

www.mcj.team

MiR,

www.mobile-industrial-robots.com

Robex,

robex.us

TRUMPF,

www.trumpf.com

Waypoint Robotics,

www.waypointrobotics.com

MIAMI

| MARCH 1-3, 2022

In three action-packed days, you will learn from top-notch presenters and network with 300+ metal manufacturing professionals who have the same challenges you are facing. Learn more on page 36.

Keynote

Sheryl Connelly

Manager of Global Trends & Chief Futurist Ford Motor Company

Speaking on:

Future Trends & Business Strategy

Save $200

when you register by Dec. 17, 2021 at

fmamfg.org/annualmeeting

or call 888-394-4362.