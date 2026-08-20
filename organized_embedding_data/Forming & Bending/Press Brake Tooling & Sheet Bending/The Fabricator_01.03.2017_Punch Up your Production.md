# Punch Up your Production

[TARİH: 01.03.2017 The Fabricator]

How having the right data helps fabricators boost overall throughput

W

hen it comes to flexibility, the modern punch press stands apart in metal fabrication. It can punch and form, and it can be integrated well with material handling automation.

But as with any technology, punching also has its weaknesses. Operators and technicians need to manage a tool library and ensure tools are sharpened and ready to go when needed. And the process itself is subject to variability, like distortion caused by improper punching sequences (as with perforated sheet) as well as "sheet shake" if the skeleton doesn’t have enough integrity to keep workpieces steady near the end of a punch program.

Proper training is key, as it always is, and operators need to know how punching compares to other sheet metal cutting technologies, including waterjet, plasma cutting systems, nibblers, routers (at least to some extent), and, of course, laser cutting. But training should include not only punching fundamentals, but also ways to optimize the process through smart tooling management, scheduling, and maintenance. It is here that automation can play a primary role.

Historical Perspective

The turret punch press has been an important machine tool in fabrication shops since the 1930s (see

Figure 1

). The designs of punch presses have evolved from mechanical to hydraulic and, finally, completely servo-driven. Modern drive systems now give greater control over the upper and lower ram movements.

Figure 1

Turret punch press technology has come a long way.

Punching typically has been the very first production process, which of course makes the process critical. Something going awry in the primary cutting process can send ripples throughout the manufacturing chain.

So what can a punch press do? For one thing, it can combine various processes on a single machine, able to not just punch, but also form, mark, tap, and deburr. Adaptable to the ideas behind lean manufacturing and other improvement concepts, a punching machine can reduce material handling to gain better control of production.

Of course, punch presses come with their own baggage. Because the machines can perform so many processes, programming them can be a challenge. Programs have to be transferred to the machine and tools must be maintained, set up, and verified. Run times get longer as you integrate more processes such as forming, tapping, and deburring within the punch press work envelope.

Then come the difficulties of handling parts the punch press just produced. This may include manually breaking nests and sorting parts that go to bending, welding, painting, and assembly.

Modern automation, which includes both software and hardware elements, helps a shop mitigate these challenges. Automation doesn’t change the punching fundamentals, but it does help eliminate some of the manual, detailed tasks that, if overlooked, can reduce part quality and throw a wrench into production.

Automation Hardware

The hardware—that is, physical automation components like material handling towers and pick-andplace offloading systems—have been the most obvious automation advances in punching. Much of it has been designed with shortening the overall cycle time in mind.

This is different from the machine cycle time, as measured from when a punch press starts and stops punching a job. The overall cycle time instead takes into account the handling before and after the operation—that is, the time when the sheet is retrieved to when the cut part reaches the next manufacturing step, be it forming or anything else.

For instance, modern punching automation is able to sort and stage individual parts for transport to the next operation. In some systems, a punched part can be lifted out. Interior hits are optimized and punched normally. The perimeter hits around each part are punched, and the pick-and-sort device then grips the part as the final tab is removed. The part is lifted out of the nest with programmable suction pads.

This does prolong the machine cycle time. But depending on the shape, size, and number of parts on each sheet, the automation may in fact shorten the

overall cycle

time. That is, parts arrive at the next operation sooner, often at a more consistent rate.

Figure 2

Analytical software displays historical data of a machine operation including alarms, process (green-light) time, and standby time.

Yes, without the automation the punch press could produce more parts during a given time frame, yet quite often those parts sit on the floor as operators manually shake them out of nests and sort them (and sorting itself is prone to error). The punch press may be producing more parts, but it may just be feeding parts to a bottleneck in shaking and sorting. Moreover, automation reduces the chance for sorting errors, like when a material handler mistakenly groups two similar-looking parts from different jobs. The potential for these errors can increase with dynamic nesting, in which parts from multiple jobs are grouped on a single sheet.

For sure, the decision to automate isn’t always straightforward. A nest of parts may have a few components with high forms, like embossments or flanges, that may not stack easily. Still, some material handling strategies can overcome these factors by limiting the height of certain stacked parts, for instance.

The key is to measure the overall cycle time and consider how long it takes operators to shake and manually sort and send parts downstream. It’s true that automation may not make sense for some applications. Regardless, the overall cycle time, not the machine cycle time, should be a determining metric, weighed against the cost of the automation itself.

Software

The greatest hurdle in keeping a machine running has always been setup. This operation includes maintaining, retrieving, and installing tools as well as verifying material requirements.

For years the conventional practice has been to write turret tool placement information on whiteboards next to the machine. And quite often the data is questionable, particularly if operators on different shifts forget to update the information.

Today software keeps track of tooling on the machine. By doing so it can notify the operator of tool changes immediately. The tool change could be for one program or multiple programs; the change could call for swapping out both the punch and die or just entail a change in die clearance or tool angle.

Figure 3

Although it may affect punching cycle time, pick-andsort automation can shorten overall cycle time, as measured from sheet loading until the punched part reaches the next operation.

Machines with large turrets often have many unused stations during a production run, and yet, at the same time, some tools for different jobs may use the same station. So even though some stations remain vacant, one station may be dedicated to different tools that need to be swapped out between jobs. Software can identify this and move tools to vacant stations. NC programs are automatically updated with the new toolstations. The goal is to minimize the number of times an operator needs to stop the machine, open the door, and replace punch tools during a shift.

Because software allows machines to "know" which tool sits within each station, the system can identify when a program erroneously identifies a tool location and correct it automatically. It also can look at a history of different turret layouts and recommend a new turret layout that would help eliminate, minimize, or simplify tool changes between jobs.

Software also keeps setup data for every tool in the library. So, for instance, if an operator sets up a form tool, all the setup information can be saved and recalled when needed in the future. Specifically, software can save the setup conditions of a tool for various material grades and thicknesses. Then, when that form tool is used for a new job, the software pulls up the setup conditions for that particular tool, all saved in the controller.

Of course, you don’t want to stop punching because a dull tool is causing problems. Modern systems track the number of hits, and operators can compare actual hit counts to maximum hit counts.

This means maintenance can be done not reactively but preventively, during scheduled downtime. These days NC programs are downloaded to punch presses automatically. And systems can be set up so operators or the software itself can modify the punching schedule, within defined constraints, to make the transition from one job to another as easy as possible. This may include grouping jobs with the same or similar sheet sizes, workholder positions, and tooling requirements.

Still, the most efficient schedule isn’t always obvious. Consider an operation in which sheets are staged manually near the punch press, and a sequence of jobs have similar tooling setups and yet use different sheet sizes—a common situation when implementing dynamic nesting. Striving for maximum material utilization, programmers nest various jobs on a single sheet; to minimize scrap, they switch sheet sizes often, striving for that "perfect" nest with high material utilization.

Similar tooling between jobs makes the operator or setup person’s job easier, but different sheet sizes makes the material handler’s job harder as he drives a fork truck back and forth to deliver batches of different sheets. The operator may not need to spend time switching out tools between jobs, but the machine still may sit idle waiting for raw stock.

In this case, it may be better to sequence jobs such that operators run identical sheet sizes together, instead of switching from one sheet size to another throughout a shift. The result: The material handler need only stage sheets once or a few times during a shift.

All this has always been considered part of best practices. In the past operators and supervisors looked at setup sheets for jobs that needed to be completed during the shift (or several shifts or days, depending on the operation), then sequence them in the most efficient way, with the most adaptable tooling layout in the turret. Software has simply automated this process by analyzing a large group of jobs and automatically reorganizing them, and then (if needed) updating the individual NC programs with the new tool locations.

All of these software functions aim to take a look at the pieces of the production puzzle and reorganize them into a more efficient picture, one with less reactive maintenance and fewer lengthy changeovers. But what if one of the pieces of the production puzzle—a segment of the NC program—is faulty?

As every fabricator knows, programs written in software may not translate perfectly to a specific machine. Today simulation utilities, based on the specific machine the job is running on, check the NC code to identify problems. The operator can perform a few simple edits before a first run, allow production to commence, and provide feedback to the programmer.

Punching the Big Picture

A punching cell can have unplanned downtime for numerous reasons. Some of it may have to do with nesting, programming, and scheduling, as described earlier, and sometimes it may have nothing to do with the punching process at all. Material may not be staged and ready when needed; the material itself may be inconsistent; or a bottleneck downstream may force machines upstream to stop production.

Maintaining excess capacity helps absorb variation, which, as fabricators know, is the reality of modern manufacturing, particularly in high-product-mix operations.

This is why production monitoring—much of which can be done with software—has become so critical. Such monitoring provides data that can answer several questions:

• What’s my machine doing now?

Technicians and managers can check current machine operation through a web-based platform, among other methods. Such monitoring reveals actual machine uptime; identifies when the machine stops and for what reason; and determines whether a program is complete or if the downtime is unplanned, such as after an alarm. Consider a situation in which a machine alarm always appears at a specific time every day. Supervisors can see this, ask the operator, who then reveals that particular part programs have overtravels—that is, the program is telling the machine to move to the wrong place in a certain condition. The operator might think it’s a minor issue because, after all, it takes him only a few minutes to go into the control and edit the program. But if the operator does that day after day, all that time adds up. With the problem revealed, the operator and programmer start talking, and the problem is eliminated.

• How has my machine performed in the past?

Data gathered over weeks and months allows operators and supervisors to target production issues, including when and why a machine isn’t running. Data can include a historical analysis of tool utilization. For instance, say two jobs use different but similar tooling or a different turret layout. Could these two jobs share certain tooling and turret layouts, and thereby reduce the number of required tool changes?

The production data from these analyses also allows shops to scrutinize capacity levels to see if any particular machine is near or at its practical maximum limit. If an operation has multiple punching machines, operators and supervisors can use the data to help balance the load, improve flow, and prolong equipment life.

The more reliable and streamlined a punching operation is, including quick changeovers as well as smart tooling management and job scheduling, the greater the practical maximum capacity can be. This includes optimizing programs for the punch press, such as knowing that travel in one direction (say, X) is faster than in the other direction, or balancing the need to reduce distortion (punching alternately one area of a sheet after another, as with perforated sheets) with the need for an efficient punching path.

Whatever the theoretical capacity limit may be, no machine should be pushed so hard that any change sends a ripple throughout the plant. It’s like a driver tapping on the car brakes in rush hour, causing everyone else to slow down or, worse, crash.

So, what is the practical maximum limit for a punch press? That depends on the machine and the product mix. But uncovering that data, now made available by software, can help establish it. Maintaining excess capacity helps absorb variation, which, as fabricators know, is the reality of modern manufacturing, particularly in high-product-mix operations.

It goes back to thinking about the big picture as well as what’s happening inside the turret punch press work envelope. This holistic perspective can help companies get the most out of punching and, for that matter, any metal fabrication technology on the shop floor.

Images courtesy of Murata Machinery USA, 800-428-8469,

www.muratec-usa.com

.

Editor’s Note: The following article is based on "Leverage Production on Your Punching Machine," presented by Donald Angel, lead applications engineer, Murata Machinery USA, presented at FABTECH

®

2016, Las Vegas, Nov. 16-18, 2016,

www.fabtechexpo.com

.