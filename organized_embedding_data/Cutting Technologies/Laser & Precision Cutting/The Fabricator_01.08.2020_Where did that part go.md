# Where did that part go?

[TARİH: 01.08.2020 The Fabricator]

Identification and sorting strategies in the modern fab shop

By

Tim O’Donnell

A laser marked this QR code directly onto the sheet metal part during the laser cutting cycle.

Laser-marked QR codes can be very small and unobtrusive.

T

oday’s high-powered lasers cut at incredible speeds, and automation allows machines to reach sky-high levels of utilization. Of course, customers don’t pay for machine utilization; they pay for parts—and not the parts that go missing either. Losing or misidentifying parts leads to rework, which forces the shop to recut pieces that should have been identified correctly in the first place.

How do fabricators lose or misidentify parts, exactly? You have the usual suspects. A piece might get left behind when being removed from the sheet after cutting. Or perhaps someone sorts similar-looking parts incorrectly, sending some cut blanks on the wrong job routings; a brake operator then pulls up an incorrect bend program; and the problems snowball from there.

All these challenges stem from a larger problem: a lack of oversight or guidance with regards to part flow, especially around the laser cutting and part sorting functions. It’s a likely root cause of many downstream mishaps. Now that each laser feeds more parts to more downstream machines, strategic part identification and sorting has become more important than ever.

Measure What You Have

You send a nest to the laser to be scheduled among that day’s job list. The parts are cut, sorted, then sent downstream or stored as work-in-process (WIP) inventory. That seems straightforward enough, but how does the production control system know exactly when a nest was cut? In some shops a supervisor might simply ask the operator or area manager. In other operations, a part sorter or machine operator might scan a label on the job traveler or move ticket to let the production software know the job has been cut and is on its way downstream.

That said, the scanning always takes place separate from the machine itself. In this sense, the machine control and the production software live in separate worlds. The machine cuts parts, but nothing communicates automatically back to production control software to close the loop.

Thankfully, this is starting to change. Standard protocols like MTConnect now communicate information back to production control software and make the data available to machine OEMs and thirdparty platforms. For instance, some job management software can read MTConnect data and give feedback to the production system verifying that a nest has been cut. This tells the system that parts in that cut nest are no longer needed and so can be removed from the list of required parts to be cut.

Closing the "job is complete" loop in laser cutting—with no separate scanning or keying-in necessary—can reveal previously hidden operational pain points. It also can keep the focus on how jobs flow through the factory. A machine that isn’t cutting might be a problem, but an excessive amount of filler parts sitting weeks in WIP inventory might be an even bigger problem. More WIP ties up cash and also might add operational complexity and open the door to misidentified or missing parts.

There’s no "right way" of job scheduling on the laser that applies to every operation. The optimal schedule hinges on various factors, including a shop’s staffing strategy, like whether an operator or dedicated material handler or helper removes and sorts parts from a nest. It also depends on the job mix, the part geometries (like how many similar parts a laser cuts), job due dates, the cost of material (and potential rework), and other variables. All those variables matter, but you first need to know exactly when parts are actually cut, and communication protocols like MTConnect can help automate such process reporting and measurement.

Nesting Strategy

Once you have a complete picture of the part sorting and identification reality on the shop floor, you can start weighing options to make the task easier and part flow faster. For laser cutting, it all starts with programming, the nesting strategy used, and releasing the order to the machine.

A nest layout usually is built upon one or some combination of several general strategies. One uses a mix of current jobs and filler parts to fill the sheet and maximize material yield. Another involves only current jobs, which increases remnant management (sometimes called

remnant nesting

). Used in conjunction with these might be a kit-based strategy, where each nest layout holds all the needed components for a kit that will flow together downstream.

Then there’s strategic microtabbing. You want enough for a stable process but not so many as to make cut-part removal (that is, the shake-and-break) overly challenging and time-consuming, which in turn can lead to human error involving lost or misidentified parts. Tiny parts might need to be tabbed no matter what, but programmers still can minimize their number and make pieces easy for part sorters to snap out. Larger parts nested perpendicularly to the laser cutting machine’s slats might require few if any tabs, making sorting and part removal faster and easier; however, lower material yield might be a trade-off in some cases, since parts need to be oriented in a certain way.

Which combination of nesting strategies to use depends on the nature of the operation and, not least, material costs. For conventional carbon steel, an operation might choose a combination of filler and kit-based nests. The laser cutting operation might lose a little on material yield, but it’s a small price to pay for ease of sorting, part identification, and part flow.

When cutting stainless or other expensive materials, a shop might strive for high material yield and rely heavily on a remnant nesting strategy, especially if filler parts aren’t available or don’t effectively utilize remaining material. Besides, excessive WIP stainless inventory can get expensive. In a quest for better yield, a shop might dynamically nest various jobs on different sheets. This can complicate part identification and sorting, but the material savings makes the sorting effort worth it.

Part Identification Technology

In a manual part sorting situation, the material handler looks at a printout or screen (and in some cases the screen is more likely to be up to date), sees which parts on the nest in front of him go with which job, and sorts accordingly.

This of course is where human error can come into play. Manually sorting parts all day takes patience and concentration, and accidentally sorting parts to the wrong job is easy to do.

To mitigate this problem, many operations today place a small, unobtrusive QR code on certain parts or even every cut blank. Laser machines are so productive these days that adding a laser marking routine for every piece doesn’t add much time to the cutting cycle. Some systems now apply a simplified QR code (one with arcs rather than sharp corners) that takes the laser head even less time to apply.

Operators downstream—be they at the sorting station, press brake, or anywhere else before powder coating—can scan the QR code to reveal the part number, the job it’s attached to, customer information, due date, the part program for the machine or operation at hand, and more. The codes are marked in such a way that they should be invisible after painting or coating.

But what if applying a QR code isn’t an option? For instance, a customer might not want a visible code on a stainless steel appliance. In these cases, applying easy-to-peel-off physical labels is an option. These labels can have a small drawing, part number, or other elements that show anyone on the floor, after a quick glance, what the part is and where it should go.

That said, applying that label remains a manual process in many operations. A part emerges from cutting, a nearby printer connected to the production control software spits out a label, and someone manually applies it to a cut piece.

Some operations, however, have successfully automated the process, integrating it into a flexible manufacturing system (FMS). And just like manually printed labels, the labels applied by the FMS can be configured for the application.

Typically, an elevator pallet transports a sheet from a tower and presents it to the machine loading area. But an FMS with automated label printing adds an intermediate step. Before being presented to the laser cutting machine, the sheet moves to a staging area with a label printer positioned overhead. The system prints a label and then descends to apply it to a sheet, traversing in X and Y and rotating 360 degrees, according to a location defined in a program created offline with the laser program itself.

Opportunities in Sorting

Sorting accurately requires parts to be correctly identified. Labeling helps, but so too can sorting automation, which effectively eliminates human error. Such automation has come a long way in recent years, especially when it comes to highly configurable suction cups that can lift various part shapes out of a nest. On the software end, certain programs have predetermined configurations that instruct the automation exactly how to grasp the pieces and orient them for sorting and stacking.

An automated labeler prints and applies removable labels to a sheet prior to laser cutting. Once the laser finishes cutting, each part emerges with the correct label already applied.

Part sorting automation can help eliminate human error at the offload station.

Automated sorting does require some programming tweaks. For instance, kerfs around certain part geometries need to be wide enough so that grippers can lift pieces from the skeleton without catching. And certain small parts might need to be tabbed together in a "mini-nest" that a gripper can remove. Regardless, once the job is stacked and ready to go, a material handler can assign each pallet of parts a job traveler or move ticket, then transport the blanks downstream. In other words, part sorting just got a lot simpler.

One Problem, Many Strategies

Part labeling is an important element, but it’s just one piece of the identification and sorting puzzle. Automation can help remove human error from the sorting process. Job scheduling enters into the picture too, including how far into the future a system looks for parts to maximize material yield. Too much WIP inventory might exacerbate the part identifying and sorting challenge.

Or it might not, depending on the job mix and the nature of the operation. Regardless, the part identifying and sorting challenge has many potential solutions. The trick is to consider the big picture, choose one or a combination of strategies, and fine-tune the recipe to achieve a result that’s closer to perfection.

Tim O’Donnell

is software supervisor at Mazak Optonics Corp., 2725 Galvin Court, Elgin, IL 60124, 888-629-2587,

www.mazakoptonics.com

. Kaylee Swearingen, marketing manager, and Al Bohlen, president, Mazak Optonics, contributed to this article.

SIMPLE. VERSATILE. EFFECTIVE.

Mayfran International’s

shuffle conveyors

are an easy way to seize big operational benefits in

any scrap application

.

Backed by our lifetime service commitment, trust Mayfran to deliver operational benefits for years to come.

MAYFRAN.COM

I QUALITY, BUILT IN.

ADVANCED LASER APPLICATIONS WORKSHOP

Sept. 29-Oct. 1, 2020

Weber’s Boutique Hotel & Restaurant Ann Arbor, Mich.

Members $595 | Nonmembers $795

For schedule and programming, visit

fmanet.org/alaw

CutFusion from weil technology

Sequential Laser Cutting & Welding

The new benchmark in Laser Processing

Cut, manipulate and weld in one fixture for maximum precision. CutFusion can be configured with up to three cutting and welding heads, pick & place and robots. Quick change tooling pallets with built in power, pneumatic, and cooling connections ensure fast, repeatable job changeovers. Precise automated laser processing for complex assemblies!

www.well-technology.com