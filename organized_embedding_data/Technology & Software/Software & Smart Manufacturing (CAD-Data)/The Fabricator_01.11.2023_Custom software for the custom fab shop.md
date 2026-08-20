# Custom software for the custom fab shop

[TARİH: 01.11.2023 The Fabricator]

Data Management

Software startup has roots in the precision sheet metal business

By

Tim Heston

greenbutterfly/iStock/Getty Images Plus

Z

ach Ernesti and Brian McMichen know the world of custom metal fabrication. For years they worked at Metalworks Inc., a large, highly automated operation in Lincoln, Neb. They programmed machines, moved into administration, then focused on the fabricator’s data framework and its legacy enterprise resource planning (ERP) platform.

From there, the headaches began—headaches many shops might be familiar with. As Ernesti recalled, "That data framework consistently hindered operations, bloated administration, and to be honest, made us way less lean."

Many fab shops might relate to this experience. It’s a common dichotomy of modern sheet metal fabrication: Walk the floor, and you might see rows of robots along with sheet cutting and bending automation—yet go to the front office, and someone is working with printouts of Excel documents. People manually view, interpret, and key in data.

Ernesti and McMichen saw this as an opportunity to start fresh. "As we became more familiar with the data, we would try to patch what we could, and try to make things work with what was available," Ernesti said. "It eventually dawned on us that we could create our own system."

They went further than that. Not only did they create their own system, they launched a new company, Cortex Data Services, founded on the concept of software customization. Instead of companies changing processes to fit the structure of a particular software platform, Cortex builds software to fit a company’s process, be it at a custom fabricator, another kind of manufacturer, or outside manufacturing altogether. Today, Metalworks Inc. remains a key client for Cortex, but it also has customers in other manufacturing niches and in other industries.

Born out of a custom metal fabricator in 2021, Cortex operates under a seemingly logical principle: No two companies are exactly alike, so their software shouldn’t be exactly alike either.

Streamline Everything

"One common theme among many ERP systems is that they’re really good at having a place for every data point," Ernesti said. "Still, some [data points] really don’t pertain to the company using the software. It’s all very generically designed, and some options are just clutter, only there to distract."

Legacy systems require time-consuming data entry and tedious file exporting, and with that comes the inconsistency with any manual, undocumented task. Let’s face it—few view manual data entry as their dream job. Some enter data a certain way and in certain formats, and those formats might change over the years.

"For instance, the system [at Metalworks] goes back to the 1990s," Ernesti said. "To get data out, you just export a heap of CSV files, and it’s up to the company to format it into usable, actionable reports. And because it’s just a raw CSV file, there’s only so much you can do with it. That’s a severe limitation."

The seeds of Cortex were planted when Ernesti and McMichen both still worked for Metalworks, and each realized what needed to happen to make the fabricator’s heap of data usable. "We needed to find a way to get the data into a modern SQL database. From that, we were able to write more consistent reports."

(From left) Brian McMichen and Zach Ernesti took a hard look at Metalworks Inc.’s legacy ERP and, ultimately, decided to start fresh. In 2021, they launched Cortex Data Services.

Images: Cortex Data Services

The two built a system around key data points that Metalworks actually used. They did so using a combination of hard coding around a SQL database, then by using a low-code platform to rapidly build applications to interface with the database in specific ways. Adding that low-code "top layer" can be straightforward—with, that is, the right database structure.

"The real value in what we do," Ernesti said, "is in the database design and tailoring it to the processes a specific company needs, then writing code that manipulates that data in a way that supports those processes."

Order Releases, Routings, and Sequencing

One key data point, Ernesti explained, helps determine a critical component of Metalworks’ scheduling: when exactly to release an order to the floor. After analyzing the data, the two found some faults in releasing orders simply by due date, whether or not resources to produce those orders were actually ready and available. Releasing orders only by due date also ignored variables like other jobs on the floor and the needs of downstream processes. Some orders should be run back to back, simply because they share a similar setup on a press brake or other machine. That said, just because similar jobs can be run sequentially doesn’t mean they should be. Other factors come into play, including the capacity and availability of downstream processes.

Consider two jobs, one due four days before the other. Years ago, the job with the earlier due date would of course be released first. Armed with data presented in the right way, though, a shop can uncover hidden capacity

just by delaying that order release

. It has to do with differences in routings and resources. The soon-due job has a simple routing, just cut and bend. These areas have plenty of capacity, so once the job lands in laser cutting, it’s off to the races.

The other job, however, has a complex routing involving welding and some minor assembly. It isn’t due for a while, but because certain resources downstream will be available at only certain times, the shop releases the order first, cuts and forms it, then preps it for welding at just the right time. Only after this order is through does the shop release that simpler order, which is cut, bent, inspected, then quickly sent out the door.

A job’s potential for rerouting plays a role here too. If it can be rerouted through various machines, it might not need to be released to the floor so soon. If a machine goes down or has limited capacity, the job can always find another path through the shop. On the other hand, if a part has, say, a bend length that requires a specific press brake with the right tools and tonnage, releasing that order earlier can make sense, to ensure the job doesn’t miss its slot on that scarce resource (the brake with the long bed).

Cortex helped Metalworks develop a scheduling system that requires a broader perspective. It’s not just how productive a machine or department is anymore. It’s about how much work actually ships during a given period.

Prep • Paint • Powder Factory-Direct Pricing Lifetime Support

888-770-0021

reliantfinishingsystems.com

Service Lamp Corp.

the accent is on service

PUT YOUR FACILITY IN THE BEST LIGHT

LAMPS • BALLASTS • FIXTURES

We all know that seeing the details is key.

This is why your facility needs to have the best lighting available for better productivity, less margin of error, and for energy savings.

Service Lamp has been helping warehouses and manufacturing facilities improve the quality of lighting since 1975. We can help you determine what is best for your facility because we know how to light your business.

800-222-LAMP |

servicelamp.com

Service Lamp — Your One-Stop-Shop

For All of Your Lighting Needs!

3 ROLL HYDRAULIC PINCH PYRAMID PLATE BENDING MACHINES

The 101 Series from WDM.

Over 40 years of experience with 3 generations working in the business.

Built in USA with American and global components.

30 gauge to 1″ thick, 1′ to 12′ wide.

Custom and built to order options available.

Have a rolling question? Call and speak directly to the designer, engineer and manufacturer of WDM machines, right in the USA.

From complete custom forming cells to many popular/standard machines in stock.

Waldemar Design & Machine LLC

224 Pierpont Street

Petersburg, WV 26847

606-787-8474

drisser@wdmrolls.com

www.wdmrolls.com

Contact us direct, or contact your favorite machine tool distributor and ask about WDM Machine Tools.

3 & 4 Roll Hydraulic Double Pinch Plate Bending Machines Initial Pinch Sheet Plate Bending Rolls • Bending Systems & Complete Forming Cells

Metalworks Inc., a custom fabricator in Lincoln, Neb., fully embraced automation. Still, many data entry and reporting tasks remained manual, tedious, and error prone.

"This can be a hard mindset for people to break," Ernesti said. "If I’m in charge of the press brake department, it feels good to get a lot of work done, but if all that work is just sitting on a shelf waiting for welding, that work [in the brake department] isn’t time well spent. It’s actually better for a machine to sit idle for 30 minutes to process the right job instead of starting right away on the wrong job."

Actual Versus Estimated Costs

"We store all aspects of a quote when it’s built," said Ernesti. "This includes the cost of every aspect of the job—the cost of quality and programming, the current cost of material by vendor, the cost of production itself, the overhead, and the material handling. We then continually measure whether an estimate is accurate, which helps us quote in the future. If we’re losing on a part, why? Did we run it completely different than what the initial estimate stated? We then need to requote it."

None of this is revolutionary, of course. The real payoff is the way the data is aggregated and used for business strategy and improvement. To realize this payoff, the estimate needs to be all-encompassing. Material doesn’t move itself, and that cost can vary depending on quantities, part geometries, and the mix of jobs on the floor. Some jobs need helpers, others don’t, and those specifics affect direct labor costs.

"We map all the steps, the materials we consume, and which stations we’re going to run the job across, at what rate," Ernesti said. "We include any outside services and incorporate specific quality steps, like checking 10% of parts of a certain lot size."

Quotes use machine rates derived from machine-specific data. The shop’s quoting database also stores exactly how long it takes for jobs to run across a

group of machines

. This is what makes rerouting so effective. If a job needs to be rerouted on the fly, the shop can make it happen and be rest assured that the cost range still falls withing acceptable limits per that initial quote.

Freeing Time, Adding Value

The custom software at Metalworks not only helped meet the fabricator’s unique data needs, it also freed people from tedious, non-value-adding labor. In one sense, mindless data entry for a technician in the office is just as wasteful as a skilled operator spending hours on a manual task that automation could easily handle.

Consider material price updates on jobs. "The admin time on that used to be huge," Ernesti said. "We’d have to open up each material and each part and manually run a new price. Now, the system just asks, ‘Do you want to use current material pricing for this estimate?’ With a few clicks, the entire job is updated with the new material price."

Metalworks custom software platform also streamlined order entry for loading production jobs for the week. Five people used to enter orders manually. Not anymore.

"We now have automated this process," Ernesti said. "We basically saved 40 hours a week of high-end administration time involving really talented, critical thinkers who were simply reading records and typing them into a system. Now, we’ve freed them to do actual problem-solving, such as analyzing workflow and specific shop processes. A huge part of what we do is just finding things that are tying up valuable employees."

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

. For more on Metalworks Inc., see "One metal fabricator’s holistic automation strategy" from the September 2023 issue, archived at

thefabricator.com

.

Cortex Data Services,

www.cortexdata.net

Metalworks Inc.,

www.metalworksinc.net

FABRICATION EQUIPMENT

NOW ACCEPTING DEALER INQUIRIES

4820 US HWY 29 N // GREENSBORO, NC 27405 // 800.299.7664 //

WWW.WYSONG.US