# The virtues of bend simulation

[TARİH: 01.05.2023 The Fabricator]

Bending

How to get trial and error off the shop floor

By

Tim Heston

ZhakYaroslavPhoto/iStock/Getty Images Plus and Viktoriia Nigmatulina/iStock/Getty Images Plus

Quoting software can flag manufacturability issues from the get-go, including issues with corner reliefs and tight bend radii.

Paperless Parts

T

he tentacles of bending reach all parts of a precision sheet metal shop. Metal elongates when it’s formed, and if you don’t account for that elongation correctly, the blank size is wrong upstream and you might have poor fit-up for welding and assembly downstream.

If bending is a mess, so is nearly everything else—hence the importance of good planning, process documentation, and any strategy that can help make sheet metal bending more predictable. To that end, bending simulation has stepped to the fore. In recent years, fabricators have used such simulations to effectively digitize preproduction and catch issues earlier, even in quoting, before they snowball into something larger and create chaos on the shop floor.

Operational Keystone

Bending can turn into a mess in so many ways, especially if those in engineering don’t consider the tooling and tolerances that each bend requires. Change the airbent radius, and you need to change the die opening and, subsequently, all the bend calculations required to achieve the correct blank size.

"Many fabricators might get a flat pattern from a customer," said Doug Wood, sales director, sheet metal solutions, North America, for Hexagon’s Radan soft-ware, Forest Lake, Minn. "They might think they don’t need to unfold 3D models. And yes, you might be getting the flat pattern from the customer, but how often do you need to modify it? Whoever designed that component, do they know the press brakes and tooling you have?"

A lot of this goes back to sheet metal bending fundamentals. In air bending, a different die width changes the resulting radius and bend allowance (arc length of the radius along the shifted neutral axis, with the axis’s position defined by the k-factor), which in turn changes the formed part’s final dimension; that in turn changes the bend deduction and required blank size to achieve the desired formed-part dimension. Sheet metal bending is, alas, not straightforward. Getting the radius wrong throws offnearly everything else, leaving operators struggling to "make it work" in front of the machine.

"In the programming world, bending comes before cutting," said Anupam Chakraborty, U.S. commercial director at Lantek, a software company based in Spain. "The reason is very simple. You create the flat pattern based on the press brake tooling you use."

Still common, on-machine press brake programming puts all the responsibility of tool setup and bend sequence development on the press brake lead or operator. "This often leads to a lot of trial and error and a lot of scrap," Chakraborty said, adding that the operator or brake lead aren’t at fault. The challenge comes from the way shops have traditionally processed bending jobs, putting the cart before the horse and shoving an order to the shop floor before all the variables have been accounted for.

Even when on-machine programming goes smoothly, it still represents unproductive time. When press brake rams aren’t moving and producing good parts, they aren’t making money. One challenging job can push other jobs behind schedule. Miscommunication between operators and between shifts creates more uncertainty. And excessive variability overall in forming can throw a wrench into other operations throughout the shop.

If operators receive a part that isn’t designed around available tools and a method of bending (usually air bending), operators might just muscle a job through. They change a bend sequence to push the dimensional error to a different, less critical portion of a part. They alter a setup to avoid a tool collision or implement a unique gauging strategy to ensure the piece could be held steadily and accurately throughout the bend program. How well operators document all this varies, and regardless, it’s just a Band-Aid covering a larger problem: Parts weren’t designed with available tools in mind.

The earlier an operation can verify a part can be bent, and that the design accounts for the tools and bending methods used in the shop (be it air bending or bottoming), the better. Also, could an assembly be formed as a single component eliminating all that welding, fixturing, and assembly costs? As sources explained, automated quoting and bend simulation help shops answer these questions earlier and, ideally, help set a fabricator apart from the competition. Asking these questions early and often can turn a parts supplier into a manufacturing partner.

It Starts With Quoting

Inefficiencies in bending stem from those metaphorical silos between sales, quoting, engineering, the shop, and (not least) the customers themselves. Quoting personnel and CAD/CAM jockeys in the fab shop might receive a SolidWorks, Inventor, STEP, or some other data-rich file for certain jobs. For other jobs, they might just have a PDF.

"By exchanging information, the fab shop should be able to reduce their cost," Wood said. "Ultimately, you’ll need to modify the flat pattern based on your tooling. So, although you might get a flat pattern unfolded by SolidWorks, you might be better off requesting an intermediate exchange file like a STEP file or, even better, the SolidWorks [or other 3D CAD] model file. That way, you can apply your shop’s press brake and tooling, and actually have it update the metadata in the SolidWorks model itself."

Simulating a bend offline catches manufacturability issues early and incorporates the actual tools available on the floor, such as the die widths and punch geometries, including reliefs for bend clearances.

Lantek Systems Inc.

From here comes basic design-for-manufacturability (DFM) issues, like features near or on a bend line or a very narrow, difficult-to-form flange. Also, does the design have the needed reliefs (weld notches) between two perpendicular bends?

"If you don’t have a [proper] notch, the metal will deform in a bad way when you bend it. That’s just one of many design issues that you need to get out of the way from the get-go. That might include calling the customer and asking about adding relief. It’s all about having these discussions upfront, as early as possible."

That was Scott Sawyer, co-founder and chief technology officer at Boston-based Paperless Parts, a cloud-based quoting and operations platform. The platform isn’t a machine-specific bend simulator, but quoting engineers can tweak various "threshholds" for DFM checks. He added that defining those thresholds involves striking the right balance. Place too many guardrails, and the company might miss out on some profitable work.

Before DFM can begin in erneast, quoting engineers need to determine the fidelity of the 3D CAD file itself. An engineer might use a sheet metal package within SolidWorks that unfolds a part to a flat pattern. It might not be perfect (it might not take a shop’s available die widths into account, for instance), but it’s a good starting point.

Issues arise, however, when the shop has to deal with CAD files without the proper information (that is, it doesn’t take the idiosyncrasies of sheet metal into account). It might also have undergone multiple conversions, "and now it lost some fidelity," Sawyer said. "Also, some CAD packages have trouble unfolding parts that weren’t initially created in those CAD packages. After years of unfolding parts, we’ve handled more and more strange cases." Edges and faces might not connect as they should, or a straight edge might actually be a spline (a collection of tiny segments), which muddles design-file processing overall.

Numbers signify the bend sequence for this complicated, feature-rich sheet metal part.

Radan, Hexagon Production Software

"Essentially, the design file looks fine, but we find all sorts of weird things under the covers," Sawyer said, adding that software’s ability to unfold sheet metal is getting better all the time.

Sawyer added that good unfolding makes for better nesting, especially critical for production jobs. Sure, a short-run job likely won’t be won or lost if the blank size isn’t predicted perfectly. But when volumes rise, "material then becomes a big portion of the job cost. Perhaps there are a bunch of components that are the same thickness, and you can nest all those components together." Getting the blank size wrong can change material yield in nesting. It might be a small difference, but for competitive bids, it might be the difference between winning and losing.

Depending on the design, even with the full model available, standardization can still be lacking. Callouts might vary, including how angle and dimensional tolerances are specified. A radius might be specified, but does the customer really care about what the radius is, or is another specified dimension critical?

Design for Bending

In small shops across the country, an estimator or sales engineer walks into someone’s office or the shop floor, with printouts in hand.

Can we form this? Will that hole close to the bend line be a problem?

The good news is that at least questions are being asked early, before a bid is submitted. The bad news is that the effort takes time, especially when a quoting department is working through a backlog. Too often, fab shops lose work not because they quote too high, but because they quote too late.

Hence the value of quoting software and bend simulation, especially when digital design files are available. Some quoting software can be customized to insert certain red flags—a hole or other feature close to a bend line, a flange too narrow for the optimal die width, maybe a tool interference issue with a return flange.

Some shops go a step beyond this and actually send the piece through an initial bend simulation. "You can do offline bend programming relatively quickly," said Dakota Baird, Cincinnati, Ohio-based product owner of SigmaNest and SigmaBend. "Some tools allow you to do these simulations without having to know how to use all elements of the software. You load parts into it, the software reviews and says whether it’s possible or not. If it’s not possible, that’s when someone with a little more experience [in bend programming] would need to get involved."

Software simulates a bending sequence, incorporating the capabilities of the multiaxis backgauge.

SigmaNest

Such simulations offer a quick check to see if the job can indeed be formed with available tooling. If not, could the bend strategy be changed (something an experienced brake programmer would know)? Or will new tooling from a supplier catalog do the trick, like a gooseneck with a deeper relief for return-flange clearance, or perhaps a wing die to mitigate distortion when bending near a hole or forming a narrow flange? To make answering this question easier, bend simulation packages integrate catalogs from the major tooling suppliers.

The more DFM work that can be accomplished at this stage, the better. This includes, again, designing parts around the tools the shop uses. "If the part is designed around a specific radius, then your toolset needs to be selected to achieve that radius," Chakraborty said. "Bend simulations calculate, based on these tools, that a certain radius will be achieved. Whether that’s acceptable or not gets decided, not on the shop floor, but during the bend simulation."

How deep into DFM a quoting engineer dives depends on a shop’s business practices and quoting strategy. The questions seem endless. Does the job fall within the shop’s core capability—that is, does the shop have redundant capacity for forming (common tooling and bends that require a conventional bed length)? If the part is large, can a single operator handle it repeatedly, or will that operator need help (which in turn affects a job’s labor costs)? A struggling operator creates safety and ergonomics issues on the floor as well as quality issues: Repeatable bends are tough to achieve when gravity weighs down a large, unsupported workpiece.

Or does the job involve a long bend that requires a minimum bed length or a certain press brake style: a C frame with clearance on the sides, for instance, instead of an O-frame brake? Do part features require special tooling? Are there tonnage concerns, especially for thicker work that might require a narrow die opening? Are there short flange lengths to worry about? Are there cosmetic or marring issues, be it from the punch tip or die shoulders, and will urethane tooling or tape be required? The shop might have tooling and the right machines available, but how often are they available?

Many like to quote as completely as possible and consider all the ramifications—but then again, the fastest quote often wins the bid. The more data that’s fed into the quoting process and the better quoting and simulation software becomes, the more accurate and comprehensive even the quickest quotes can be.

Simulate Before Sending to the Floor

Once the job is won, the order processing and scheduling begins in earnest, including the bend simulation. Here, the bend simulation takes into account the material, the machine style (upacting or downacting, O frame, C frame, bed length, tonnage capacity), and tooling (punch, die width, use of tooling extenders to achieve needed open heights), optimal bend sequence, depth of penetration, and resulting forming tonnage, ensuring it’s safely below the tonnage capacity of the machine.

"All these factors and more are taken into consideration during simulation," Chakraborty said. "This leads to the correct selection of not only the tools but also the bend sequence."

Some programmers might identify "favored" tools in the software, typically a group of commonly used tools that the shop usually has available for use. Additionally, they might take a few design files and have the software automatically process them for multiple press brakes to see which can form them and which can’t, given the tooling, bed lengths, backgauge capabilities, and tonnages available.

In many operations, some jobs might be simulated and then sent for cutting and bending on a machine (usually new) with an advanced control. The operator downloads the program and commences bending. And depending on company preferences and best practices, some software allows operators to choose, within certain constraints, a preferred bend sequence.

Newer press brakes offer 3D bend simulations right at the control, all with built-in error proofing, with top and bottom surfaces colored differently on the screen and visual step-by-step instructions. Older machines with older controls might not have this, but as sources explained, this doesn’t mean they can’t be simulated.

An older brake can be modeled so that a programmer can run a simulation through it. What happens next depends on the machine and application requirements. Sometimes, a programmer can export a job program and transfer it to the older controller, depending on the media those older controllers receive. Other times, the simulation allows the programmer to create detailed, step-by-step setup sheets with accompanying images. Either way, the program has been proven offline, eliminating or at least streamlining on-machine programming even on the oldest press brakes.

"On older machines, bend programs typically aren’t very long," Wood said, "so you’ve got ninetenths of the battle won if you’re able to provide step-by-step images and instructions, the right data, the backgauge settings, and all the relevant data to process that job."

For certain workpieces, or for brakes equipped with in-process angle measurement, the first part turns out to be a good part. Some tweaks might be necessary, but regardless, test bending at the brake becomes inconsequential.

The operator might make program notes, which are then fed back to the simulation file. A part might bend best from, say, 16-ga. A36 material from a certain supplier (every gauge has a thickness tolerance zone, and when thickness changes, so can the bending results). Any program notes are stored for future runs, there for all to see—no miscommunication between different operators or different shifts.

Again, the more data the simulation has, the better, and this includes how specific material from specific suppliers forms. As Baird explained, "Some fabricators perform coupon testing. For different types of mild steel, for instance, they’ll take square test coupons, bend different angles, measure certain attributes, then type data within certain fields in the software. At that point, the software uses that data, using a specific kfactor for one mild steel, but for this mild steel from a different supplier, it’s a slightly tweaked k-factor."

Bending, Blanking, and Job Sequencing

Armed with the right software, programmers today can look beyond bending and focus on the big picture. What about the characteristics of the cut blanks? If they require microtabs, will those edges be deburred before forming? If not, will the location of those tabs interfere with the backgauge on the brake? Also, what are the grain direction requirements to ensure optimal bending repeatability while fulfilling cosmetic requirements? Many simulation packages share data between nesting and forming to ensure variables in cutting don’t contradict variables in bending.

Also, what’s the optimal order of jobs? Cutting operators want to optimize material yield and group like materials together; welding and assembly want all the pieces they need to move a job forward as soon as possible. In the middle is bending, where operators want to optimize throughput with common setups—that is, multiple jobs can be formed with one common tooling setup.

GET THE LISSMAC EDGE

Increase your quality and output with our full range of solutions for:

Deburring Deslagging Edge rounding Finishing

17 Route 146

E Mechanicville, NY 12118

518.326.9094

getthelissmacedge.com

sales@lissmac-corporation.com

"Bending software can optimize the order you process parts," said Baird. "It can look at the programs that have been solved already, their tooling setups, and essentially give you a guideline as to the job sequence. For instance, you might want to ensure that all parts requiring specific brake tools are cut first before a next set of parts. Then, that data is transferred to cutting, where nesting software can nest them in an order that gets them off the cutting machine at the optimal time."

Ease of scheduling also enters into the equation. An "ideal" job—which calls for common tools and conventional bed lengths on the brake—could be routed through a majority of the shop’s press brakes. But what if one job needs a special tool or a brake with a wide bed? What if another job requires the side clearance of a C-frame brake and, hence, can’t run on an O-frame machine?

"Bend simulation gives you a visualization, but it does not replace the real world," Chakraborty said, adding that simulation works with the data it’s given, but like any other technology, it can’t predict every potential outcome.

Here’s where the experienced brake operator plays a critical role. Software might flag certain issues, but the brake operator knows those issues can be overcome. It might be a tool collision issue for a large, thin workpiece (flexible sheet that the operator could manipulate without affecting bend accuracy). Perhaps there’s a complex hem bend where the tooling is air bending a hem’s double material thickness (the hem probably isn’t exactly double the material thickness, hence the challenge in predicting the outcome).

All this shows why bending knowledge is as important as ever. The only thing that’s changed is how it’s applied. Instead of experienced bending experts working through a tough setup on the floor, tying up an otherwise productive machine, they’re now running simulations, talking with operators about what works and why, and considering how parts are presented from the cutting operation and flow downstream after bending. It’s a cultural change, for sure, but that hasn’t diminished a fabricator’s need for bending knowledge.

Building That Digital Twin

"The future of bend simulation is machine learning and artificial intelligence," Chakraborty said, adding that even the most challenging jobs "can be tracked on the shop floor, built into the machine learning algorithm."

Today, production control software can help shop operations managers run various what-if scenarios to determine the best time to release an order and the best routing it could take. Once the job runs and data is collected, a virtuous cycle sets in motion.

"It’s about having a digital twin of your operation," Wood said, adding that today’s software can carry parts through various "what if" routing scenarios, including "virtual tryouts" of custom brake tools and even custom backgauges, all imported directly from the 3D CAD program they were designed on.

Armed with software that can capture that data, operations managers can perfect flow and, for future jobs, help bring actual costs closer to estimated costs. When this happens, a custom fab shop operation becomes more predictable, more profitable, and, ultimately, a better place to work.

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

Lantek Systems Inc.,

www.lantek.com

Paperless Parts,

www.paperlessparts.com

Radan, Hexagon Production Software,

www.radan.com

SigmaNest,

www.sigmanest.com

TRANSPARENCY REDEFINED

Scan to learn more

Analyze, Monitor,

Produce

.

MC Machinery’s remote360

® is a robust production monitoring and support solution, designed to provide transparency to your machining processes.

Our web-based app provides real-time data to increase productivity, improve efficiency and reduce down time. And now, with our new advanced features added, your efficiency will be better than ever!

For more info, call

630-616-5920

or visit

mcmachinery.com