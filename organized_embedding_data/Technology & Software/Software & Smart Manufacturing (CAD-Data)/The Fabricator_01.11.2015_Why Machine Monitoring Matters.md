# Why Machine Monitoring Matters

[TARİH: 01.11.2015 The Fabricator]

Machine performance monitoring gains a foothold in metal fabrication

By Tim Heston, Senior Editor

W

hen Dave Edstrom speaks at manufacturing events, he likes to challenge his audience. He asks if anyone’s company is practicing lean manufacturing or other improvement techniques. A lot of hands go up. Next he asks how many are monitoring the uptime and performance of their equipment with overall equipment effectiveness (OEE) metrics.

"I then ask, ‘If you are doing either lean or OEE, please raise your right hand and keep it up.’ Then I say the following, ‘Please also raise your left hand if you are monitoring your shop floor. By shop floor monitoring, I do not mean simply counting good and bad parts, nor do I mean simply knowing what color is on the stack light. By shop floor monitoring, I mean the ability to know anywhere and anytime exactly what a given piece of equipment is doing in your plant or shop.’"

Not many raise their hand. He then makes a bold statement. "Unless you have both hands in the air, you might think you are doing lean or OEE, but you are not."

Edstrom told this story in his book

MTConnect: To Measure Is to Know

. His point is simple, and it’s nothing new to manufacturing: If you don’t measure something, how can you improve it?

Years ago if a manager at a custom fabricator asked a press brake supervisor about how long the average job changeover took, quite often he got a generic response. "Oh, about 15 minutes." When that manager performed time studies, he might have found that 15 minutes was a gross underestimate.

But wouldn’t it be great if that information and more—including OEE data and other performance metrics—were a click away for all machines, no matter their brand or their age?

The State of Data

Edstrom was chairman of the MTConnect Institute (

www.mtconnect.org

) from 2012 until January 2014. His mission (and the institute’s mission) basically has been to allow people to see what’s really going on with their equipment. MTConnect isn’t software but instead an open-source, royaltyfree standard that, using Internet-based protocols, helps connect the information in machine tools to the outside world.

The roots of MTConnect go back to 2006 when Edstrom, then chief technologist of the global system engineering business line at Sun Microsystems, walked the International Manufacturing Technology Show in Chicago. He was slated to give a keynote address, and representatives from show producer AMT, the Association for Manufacturing Technology, asked Edstrom his opinion of manufacturing and the machine tool industry. "I said it looked like 1985. We need an open way for these systems to communicate easily with each other and, most importantly, with the outside world."

From these conversations, Edstrom along with Dr. Dave Patterson from UC Berkeley began working on a standard. The idea was to go beyond basic interoperability and add definitions to make connections between systems easier. They built MTConnect using the same protocol as the web uses (HTTP) as well as XML.

"But the secret sauce," Edstrom said, "is the data dictionary, and we got the machine tool vendors to agree on what that dictionary will mean." With a basic interoperability standard, "You see the highway, but you don’t know what’s inside each car. With MTConnect, you know exactly what’s in each car."

Edstrom added that having a common interface is critical to make the idea of the "Internet of Things" a practical reality. "How do you have the Internet of Things unless you have a common definition of what the data means?"

Today Edstrom is chief technology officer for ME-MEX Inc., a company that produces interfaces that allow the machine to communicate via the MT-Connect standard. In his book, Edstrom compares MT-Connect with the Bluetooth

®

communication standard in consumer electronics. You don’t have Bluetooth "software," but you can purchase devices that can connect via the Bluetooth standard.

MTConnect has gained more traction in the machining arena, probably because of the nature of the work with its long cycle times for milling and turning parts with critical tolerances. If a machine requires eight hours to mill a massive component, and that machine isn’t performing as it should be, managers want to know about it immediately, lest an entire shift be wasted machining one bad (and extremely expensive) part.

All the same, various types of shop floor monitoring are gaining traction in metal fabrication. Some vendors offer production control software that connects directly with certain machines. Others offer ways to connect to machine control interfaces to record machine availability and capture OEE data, which is communicated to the manufacturing execution system (MES) or enterprise resource planning (ERP) system.

Amid all this, MTConnect is just starting to gain a foothold in the sheet metal business. Earlier this year, for instance, Ingersoll Rand’s Commercial HVAC division (which includes Trane) started using the MTConnect standard in its Clarksville, Tenn., plant to monitor the OEE of its new Mazak laser. The HVAC division already tracked OEE of other sheet metal cutting machines using a system it developed in-house, so adding a system using the MTConnect standard seemed like a logical move.

"I work in Cincinnati, and if ever I want to see what’s going on [in Clarksville], I just log in and see the display," said John McCaughey, advanced manufacturing engineer at Ingersoll Rand.

According to McCaughey, Ingersoll Rand soon plans to use machine control interfaces, produced by MEMEX, to track the performance of its older turret punch presses. The monitoring software will connect to those machines by using the MTConnect standard.

Monitoring in Metal Fabrication

Plant managers may not care about the intricacies of software development, but they do care about what the monitoring software can produce. With MTConnect, this depends on the problem at hand—that is, what a company wants to track.

Mark Mercurio, applications and technical support manager at Mazak Optonics Corp., Elgin, Ill., described several data points that can be tracked for laser cutting, including the starting of a machine cycle, when the machine is idle, its performance during the machine cycle, and whether an operator has performed any manual overrides on the control. Alarm signals, such as those that trigger action items like oil changes, also can be communicated.

Put together in the right way, the data points can produce a useful OEE score. For instance, consider a machine that’s running with very little downtime between sheets. Sheets are being loaded, parts are being offloaded, and beam-off time is mere minutes between jobs. All seems right with the world. Still, downstream operations are suffering; managers are shuffling the schedule because all the parts for certain subassemblies don’t arrive at the welding department in time.

Wouldn’t it be great if overall equipment effectiveness (OEE) data and other performance metrics were a click away for all machines, no matter their brand or their age?

Now consider the same cutting laser, this time with not only uptime monitored but

performance

as well. The monitored laser surprisingly has a low OEE score, even though downtime between jobs is minimal. Why? It turns out that the feed rate is lower than it should be.

The monitoring system also may involve some manual intervention. For instance, if an operator sees that a few parts from the nest need to be scrapped, he needs to enter that information into the monitoring system, which in turn lowers the machine performance score.

Any monitoring of this type doesn’t solve problems on its own, but it does allow managers to ask the right questions: Why is the feed rate down? Is it a machine problem, or is there an issue with operator training? "It could be something as simple as an operator not being able to find a piece of steel," Mercurio said. "Or he may need to do a focus lens cleaning, and he can’t find the tools."

About Asking Questions

A low performance score spurs people to ask questions. The machine may have been down because of unavailable material, or perhaps the nest wasn’t available from programming—so why was that material or nest program unavailable?

Consider the following hypothetical example. For several weeks an operator finds that he had to tweak the laser program, lowering the feed rate to ensure he could produce the required parts. Eventually the entire machine went down, thanks to a faulty part, and the shop had to wait six weeks for a replacement to arrive.

Thing is, the laser didn’t just crash out of the blue. The operator had known something was amiss for weeks. The problem occurred in part from lack of communication between the shop floor and management. The operator knew it was his job to maintain throughput, and he felt he was using his expertise to tweak the program parameters to "make it work."

Dave Edstrom, past chairman of the MTConnect Institute, has asked, "How do you have the Internet of Things unless you have a common definition of what the data means?"

What if the laser communicated information directly to a monitoring system? This would have added some predictive elements to the maintenance situation. A low OEE score (from all the machine idle time, when the operator tweaked the cutting program) would have been posted, which in turn would have thrown up a red flag, a harbinger of big maintenance problems.

What if a machine is available to produce and yet is still idle simply because of the lack of orders? The OEE score still takes a hit. McCaughey explained that his operation has run into this issue, particularly during the slower winter months.

He added that in these cases, the company sends enough work to a limited number of cutting machines. This ensures these machines run at full capacity while still fulfilling

kanban

-triggered orders and delivering them on time to the next process, usually in the forming department. This raises the OEE score for these machines and lowers the scores for other machines that are now mostly idle. This also frees the other machines to produce should unexpected demand arise.

Monitoring the Press Brake

McCaughey recently toured Mazak’s production plant in Florence, Ky., and when walking through the fabrication area, he noticed press brakes being monitored via MTConnect. McCaughey added that Ingersoll Rand hopes to be tracking its press brakes soon in a similar way.

The press brake tracking resembles OEE tracking on lasers and machining centers, but with a few differences. The score produced isn’t the same OEE score used for other machines.

Considering the nature of the press brake bending operation, the monitoring system doesn’t compare the ram stroke speed (a brake’s "feed rate," so to speak) to an "ideal" speed. Instead, it tracks the time the brake is stroking and, most important, when it isn’t stroking. If an operator does have a bending problem—be it because of the tooling, thickness variation in the material, or anything else—the time between those ram strokes can add up quickly.

Having a little time between bending strokes, of course, is a normal part of press brake operation. An operator needs a little time to fetch the next part, and he also needs time to check workpieces periodically.

To account for this, the monitoring system allows for a certain amount of idle time between strokes—say, 30 seconds—to give the operator the needed time to fetch blanks and check parts. If the operator strokes the machine again within 30 seconds, the monitoring system records it as a continuous operation. But if it takes

longer

than 30 seconds, the monitoring system counts it as idle time and incorporates it into the final machine performance score.

The machine performance score isn’t the only metric used, of course. Throughput is considered as well. Still, because the brake is monitored, people know exactly how much time elapsed between the last good part of the previous job and the start of the next job, all recorded as idle time by the monitoring system. And they know if an extensive amount of time elapses between brake strokes. If the uptime score is low enough, people again can start asking questions: Why did setup take so long? Were the tools or materials unavailable? Were there problems with the size or thickness of the part blanks? And again, improvement ensues.

The Argument for Machine Monitoring

Machine monitoring can reveal the tip of the iceberg of larger problems. Consider this hypothetical example. If a laser cutting machine has a low OEE score posted near it, the supervisor knows to start asking questions. He finds that excess machine idle time is driving down that OEE score. Why? It’s because material isn’t available. Why isn’t material available? The purchasing department chose another supplier. Why? The supplier had a good price, but (as it turns out) it lacked in reliable on-time delivery.

More questions are asked about purchasing, order processing, and engineering. Further analysis shows that it takes an extraordinarily long time to process a new job through the front office, and inefficiencies and inaccuracies pop up everywhere. Eventually an improvement team gets everyone on the same page and streamlines front-office operations dramatically, from weeks to a few days.

All this started with a supervisor noticing a low OEE score at the laser.

Standardization and Market Dynamics

In his book,

MTConnect: To Measure Is to Know

, Dave Edstrom recounts the story of William Sellers, a tool builder who back in the 1860s came up with a uniform system of screw threads. Sellers’ screw threads could be easily measured (the 60-degree threads are one-third of an equilateral triangle). The struggle wasn’t over the technical merits of the screw’s design, but whether there should be a standard at all.

Ultimately, a few large machine shops recognized the merits of Sellers’ design, and its popularity ultimately pushed industry to adopt one uniform standard.

As Edstrom wrote, "While the idea of standards was very controversial, it proved to be brilliant, because something as simple as a standard screw created many, many industries."

As Edstrom said in an interview, "Customers [of machine tool vendors] ultimately will drive this. "They’ll say, ‘I need to know what’s happening on the shop floor, and I don’t want to spend a lot of money per device to get information off the machines in a standard format.’"

Edstrom added that an open standard like MTConnect introduces a kind of Bluetooth functionality to the machine tool world. If you don’t like your Bluetooth-enabled phone headset, you can just buy another one. Similarly, if a shop isn’t happy with its machine monitoring system, it’s free to switch to another MTConnect-enabled monitoring software.

Senior Editor Tim Heston can be reached at

timh@thefabricator.com

.

Mazak Optonics Corp., 2725 Galvin Court, Elgin, IL 60124, 847-252-4500,

www.mazakoptonics.com

MEMEX Inc., 3425 Harvester Road, Suite 105, Burlington, ON L7N 3N1 Canada, 866-573-3895,

www.memex.ca