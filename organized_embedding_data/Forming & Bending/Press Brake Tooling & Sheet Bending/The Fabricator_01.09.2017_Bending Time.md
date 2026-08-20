# Bending Time

[TARİH: 01.09.2017 The Fabricator]

Software helps fabricators boost forming throughput

By Doug Wood

T

ime is money in manufacturing, and it’s all about time when you’re trying to get a new design to market or get a revision released to fix a critical problem. To meet the time crunch, designers use the latest generation of solid-modeling tools and push limits with their latest creations. As a result, fabricators must figure out how to turn art into parts, including how best to cut and bend complex designs, if bending is even an option.

Historically, prototype fabrication involved an operator cutting a few parts, then taking them to the press brake operator or setup person to see if they could be bent. The press brake operator then went through a few different options for tooling and maybe a few different options for the bend sequence. Fast-forward to a few scrapped parts later, and people finally realized that they couldn’t make the part, either because tooling wasn’t available or because the design itself made forming impossible.

This is costly, especially considering that you’re taking your press brake offline from production and turning it into your prototype machine. This also ties up one of your skilled press brake operators as he evaluates the bend sequence to determine if a part can be bent the way it was designed.

Cutting test pieces wastes material and detracts from valuable punching or laser cutting time. Depending on the material being scrapped, this frustrating game of trial and error creates costs that really add up.

In some cases, it’s not just the physical costs, but about the process of getting information to the press brake operator. Developing flat patterns from parts in assemblies, creating a series of DXF files to be imported into your CAM system for cutting, preparing the nests and programs, and creating dimensioned prints to take out to the shop floor are costs paid in valuable labor-hours.

What if the part is off by a few thousandths? Perhaps you do not have the right tools, but you do have something close. A part revision ensues, possibly followed by more test pieces that need to be cut and bent. The entire process can take hours.

Technology now exists that moves the entire process upstream. Prototyping, press brake tool selection, and bending tryouts have largely become digital.

Virtual Testing

To begin, the customer or your engineering department releases the assembly for prototyping and selects a part from an assembly in your off line press brake programming software. From there the press brake on which you intend to bend the part is selected, and the system instantly evaluates whether the part can be made, delivering live feedback to designers.

This can be accomplished without creating multiple files and transferring them to your CAM system for cutting, creating programs for your laser or punch press, or walking the parts out to press brake operators in the shop.

Figure 1

According to the original design and flat pattern, the part has an overall dimension of 22.735 by 29.34 in. Unfortunately, the shop’s available or preferred tooling cannot form this part from a blank of this size.

Figure 2

After available tools are selected, the effects of those tools are fed back to the 3-D model and flat pattern, including the new bend radius (shown at top). This changes the overall flat-blank dimension from 22.735 by 29.34 in. to 22.593 by 29.114 in. The simulation then proves out the new

Tooling Factors and Safety

offline press brake software can determine the bend sequence and, in most cases, gives you the opportunity to override the sequence if necessary. Additionally, these software packages automatically select tooling from a library that reflects current tooling inventory. Some software packages also allow you to expand the automatic selection to include the library from your preferred tooling supplier. You can use this instant feedback to make decisions using accurate, current tooling data. This vital tooling data also can be used to adjust project budgets and account for any lead time required to receive additional tooling.

If you have a tool that is close to what the part requires, what repercussions will this have on the part and possibly the fit of the assembly? You can now run the simulation, check for collisions, and adjust accordingly. If a tooling change is required, press brake software will make changes to the metadata on the part and send it back to the design system, such as SolidWorks

®

or Autodesk

®

Inventor

®

.

Consider

Figure 1

, in which the original design and flat pattern specifies a dimension of 22.735 by 29.34 inches. After the engineer selects the tools, software sends that information back to the 3-D model and flat pattern. In this case, the tooling alters the overall dimensions to 22.593 by 29.114 in., a change that significantly affects the finished part and assembly. To take the scenario a step further, an engineer can select a bend on a part right in the assembly and compare it to the tool library for the press brake during the design process (see

Figure 2

).

The technology also allows you to make decisions about secondary costs. Could you combine multiple parts that were made separately into one? This would save time, eliminating fixturing and welding. Being able to run a 3-D simulation will allow you to form the part virtually and check for collisions. If the simulation reveals a collision, you can resolve it by changing up the bend sequence or by altering the way in which the backgauges are used.

Would it benefit an operation to purchase additional tools? Perhaps a custom tool could bend an off set or hat section in one hit. Do the brakes on the floor have the tonnage for such an operation? Would there be any gauging or collision issues? How much time could that tool save? Simulation software could provide answers before any tool is purchased or made.

An additional consideration with 3-D simulation is press brake safety. You can scrutinize safety hazards using visualization tools, which include collisionchecking capabilities. For example, press brake operators viewing the simulation will see if a part will hit the top of the press brake at the end of a bend, allowing them to take precautions when forming the part.

Figure 3

The designer can specify a specific radius (shown in blue) and assign punches and dies from the fabricator’s tooling library.

Software helps document tribal knowledge. This doesn’t necessarily lessen the blow when a talented setup person leaves the company, but it does change the setup person’s role. That person is no longer solely the "database" of current press brake setups, but also a valuable source of ideas for improvement.

Minimizing Tribal Knowledge

Qualified setup personnel are becoming increasingly difficult to find, as we are simply not seeing a great number of graduating students who want to be press brake operators. Losing an experienced staff member can be devastating. In many companies, setup people are the "database" of forming jobs. They know that when you run a particular part, you need to do

this

special operation or

that

specific sequence for the job to bend correctly. If that person leaves the company, so does that database of information on how to form the parts.

Simulation software moves that database—the current state of bending operations—out of someone’s head and into the virtual realm. Companies build up a digital database of bending operations; if an operator does leave the company or retires, a wealth of knowledge can be retained.

In this sense, software helps document tribal knowledge. This doesn’t necessarily lessen the blow when a talented setup person leaves the company, but it does change the setup person’s role. That person is no longer solely the "database" of current press brake setups, but also a valuable source of ideas for improvement. Operators can still rely on the setup person to verify that bending jobs conform to documented procedures. But the setup person’s real value emerges when he or she can scrutinize the current state of bending and make it better, be it through more efficient use of tooling, a simpler bend sequence, or anything else.

Uncover Best Practices

The reality is that it can be very tough to train operators on how to bend components. Simulation from offline press brake software can provide step-by-step instructions on how to form a part, which eases the learning curve for new operators.

Another challenge, particularly with companies that have multiple press brakes with multiple operators, can be repeatability. One operator may choose one set of tools to form a part, and another operator may choose a completely different set. The result is two different parts.

Most offline programming platforms allow fabricators to designate preferential tooling to shorten setup time and establish standards. If all press brake operators making the

same

part use the

same

program, including the same tooling and bend sequences, they will form parts correctly.

Shops also can optimize the order of forming jobs to minimize setup time. The precaution to take here is that the order does not affect downstream operations. For example, perhaps seven of the parts required for an assembly are bent and waiting on the last three because they require another tool setup that will be used later in production.

While rearranging the order of jobs in the press brake department may increase bending capacity, it might not shorten the overall manufacturing time (receiving dock to shipping dock) for the order. Grouping like jobs together may increase work-in-process and hold up urgent orders. Would it have been better to bend all parts for the assembly in sequence, rather than grouping like jobs together to eliminate or simplify changeovers?

Simulation software helps people see myriad options, but all need to be considered within a larger context. The goal is to standardize procedures and shorten each setup so that regardless of how many tools need to be replaced and rearranged, or how often, the time between jobs is minimal.

Offline programming and simulation protects investments in both equipment and personnel.

The Value of Going Virtual

Virtual prototyping and offline programming for press brakes help fabricators spot costly design errors early and give them the information they need to make decisions that affect cost and delivery times.

If a press brake isn’t making the

right

parts, it’s not making money. What if the brake makes the

wrong

parts? That is, what if the machine is forming a prototype design that can’t be made; or a production part has to be scrapped because of faulty programming or a "let’s just make it work" tooling setup; or a part that’s not yet needed is destined to sit as WIP for days or weeks? In these and other cases, your press brake isn’t just not making money, it’s

losing

money. Similarly, if people on the floor struggle because processes aren’t documented and the "go-to" person left the company, a shop loses money on its personnel investment as well.

Offline programming and simulation protects investments in both equipment and personnel. People shouldn’t spend their days trying to figure out how things are done; they instead should keep producing and—thanks in part to digitally documented procedures and simulations—uncover ways to make quality parts in less time, from raw stock to the shipping dock.

At the end of the day, it’s still about time.

Doug Wood is general manager, Americas, at Radan, 800-875-7232,

www.radan.com

.