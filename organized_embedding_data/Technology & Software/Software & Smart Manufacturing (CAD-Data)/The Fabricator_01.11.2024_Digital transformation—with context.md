# Digital transformation—with context

[TARİH: 01.11.2024 The Fabricator]

Cover Story

Improving machine uptime is great, but what about the whole value stream?

By

Tim Heston

Igor Borisenko/iStock/Getty Images Plus

M

odern metal fabrication is full of "islands"—islands of lean, islands of automation, islands of digitalization. A new laser or press brake might integrate well into an Industrial Internet of Things (IIoT) platform; it might even be completely automated, with towers and robots manipulating the work through blanking and bending. But what about the denesting process after forming or the masking station after the pretreatment and washing stations but just before powder coating?

Machine monitoring does help eliminate one island of hidden waste: The difference between clock-in and -out data from enterprise resource planning (ERP) or similar software, and the time the ram is

actually

moving on the brake; the arc is

actually

welding at the welding station; or the head is

actually

cutting on the laser, punch, or plasma machine.

Machine monitoring metrics require careful interpretation, however. A shop striving for optimal uptime and overall equipment effectiveness (OEE) might group like jobs together and yet increase work-in-process (WIP) and batch sizes, prolonging overall lead times.

Moreover, the high-product-mix nature of metal fabrication means that "poor" machine uptimes need to be put in context. For instance, a complicated staged setup on a press brake might yield poor green-light-on time over a particular shift. Still, that "poor" metric hides the fact that one setup can process an entire part family, perhaps enable smaller batches or even kit-based part flow, shortening the overall time it takes to ship an order. Brake uptime and utilization can seemingly suffer even as overall throughput rises.

Put another way, data requires context.

How Lean Complements Digitalization

"The true science is in OEE married with advanced planning and scheduling. You have different constraints. You’ve got machines up or down. You’ve got people coming in and out between shifts. You’ve got component suppliers and outside processes. And you have WIP. All these constraints become part of the production schedule. What if a certain person calls in sick? What if this machine is down at the wrong time? Can we move the job to another work center to mitigate on-time delivery issues?

"Real improvement isn’t just about machine monitoring, showing whether a machine is on or off. It’s about marrying that data with ERP data, the actual jobs and operations, combined with proper constraint-based scheduling throughout the plant. The science is about integrating machine data with jobs, part numbers, orders, and job routings, all to understand true job profitability and manufacturing variances. That’s the Holy Grail."

A worker monitors production status on the Guidewheel platform, which measures a machine’s productivity through its electrical draw.

Guidewheel

So said Mo Abuali, senior director of digital manufacturing, retail, and distribution at consulting firm Wipfli, who added that this is where lean manufacturing practices play a complementary role. "We can now use the data [from digitalization] for the purpose of value stream mapping and lean coaching. We’re now referring to it as ‘digital lean,’" he said, explaining that the effort is central to a new solution Wipfli is offering its clients. "We’re software-brand neutral. We’re a strategic Microsoft partner, but we’ve also built a partner ecosystem that includes various complementary digital solutions," Abuali said.

This overall equipment effectiveness (OEE) dashboard tracks run-time and compares it with job-specific standards. Machine monitoring is evolving to incorporate not just machine uptime but also job-related data.

Wipfli

Lean manufacturing, moving in lock step with shop floor digitalization, can help put metrics in the right context. As a first step, IIoT data can be correlated with data from ERP or manufacturing execution systems (MES), relating setup and cycle times to specific jobs. Again, a staged bend at a press brake will have a much longer setup than a single-bend bracket calling for a single punch and die—but that long setup time alone doesn’t make the staged bending approach less effective.

"You can integrate the data from the top floor, the ERP system," Abuali said. "This means we understand what jobs are running over a particular shift, day, or week, and compare the data with the established standards. This means they’re able to pinpoint manufacturing variances. What was the actual cycle time, setup time, and labor time? From here, we can start to understand job profitability. The system could flag an issue, which could then trigger a

kaizen

event based on a specific part number or job type for a particular value stream. It’s not just machine data. It’s integrated data from the shop floor to the top floor. This in turn helps drive continuous improvement events."

This broadens the focus beyond machine uptime. For instance, grouping like jobs together might reduce setup time, but producing ahead in the schedule also increases WIP—inventory that isn’t free to manage and comes with its own risks (obsolescence due to late engineering changes, rework from mishandling and damage, etc.).

"You can track WIP at each stage, including outside processes," Abuali said. "If, say, a fabricator needs to send a job out for powder coating, that constraint would be built into the schedule. Job profitability entails labor, setup, and machine cycles, but it also has additional elements, including overhead, WIP, and warehousing."

The data can be integrated with information from an entire value stream, gleaned from value stream mapping (VSM), strategic facility layout, and other tools within the lean toolbox. That data can in turn be used for intelligent scheduling and job routing.

Say a job routes a part through a panel bender or precision folding machine, both of which offer quick changeover for small-batch or even kit-based processing. But what if that same job could be sent through a press brake with automated tool changes, or at least one with a staged setup that can process all the pieces of a certain kit. Some design for manufacturability (DFM) work might be in order, and the setup might not be easy, so traditionally, a shop might not bother. Digitalization, however, could change this.

All these details "can be defined as constraints in the schedule," Abuali said, incorporating data not only from the bill of materials (BOM) but also a so-called "setup matrix," showing which jobs share common or similar setups, and how proper sequencing could affect overall throughput.

Continuing with the bending example, the schedule would know that certain jobs share similar tools on specific press brakes—but again, would group like jobs together only if it makes sense in the broader context, including the needs of downstream operations and overall WIP levels. Similarly, it could develop alternative routings: one through the brakes and another through the panel bender.

Some DFM might be in order, considering the tooling differences between the two technologies. Even so, data gleaned from IIoT could justify the effort. And sure, a manual press brake might not be as fast as a panel bender, and the labor costs might be higher. But again, context matters. What if the panel bender has no excess capacity? At certain times, the brake with available capacity can at least move a job forward when downstream operations need it the most.

Good Connections

The ultimate goal is to spread digitalization up and down the value stream, to create that unbroken "digital thread"—a feat often easier said than done. A laser might cut amazingly fast, but what if some parts need to flow through a deburring machine, maybe a press brake with an old control, or perhaps an old drill press or tapping arm with no controller at all?

Here, the industry is finding new ways to monitor machine activity—and this includes measuring a machine’s productivity through its electrical draw. As just one example, Momentum Manufacturing Group’s (MMG) plants in New England are using an IIoT platform called Guidewheel, which reads the electrical signals from any machine that draws power. The company has even tied the system into shop air compressors. Tapping into the compressors’ electrical supply, MMG now can identify leaks in shop air lines, especially those that occur off shift or over weekends.

"We started using the platform at a very basic level. We identified the electrical signal when it’s processing parts and when it’s in idle mode. We then had the data we needed to see what utilization we got out of a specific piece of equipment," said James Meyers, senior vice president at MMG, adding that the fabricator has implemented a tagging system that allows operators to report why machines aren’t running when they should be.

"If machines are idle longer than expected, the system would send an email out to supervisors. And at this point, we’ve integrated tablets at the machine, so operators know what their day’s performance has been at the machine. So now, we can dive into why we have unplanned machine downtime. Is it free capacity, or is it something else? We then can start acting on that data. We can even work with our sales team and talk to them about where we have excess capacity."

A panel bender at Momentum Manufacturing Group performs a bending cycle. At present, MMG is using the Guidewheel monitoring platform to track uptime. The fabricator has plans to integrate the system with its ERP and CMMS platforms.

Momentum Manufacturing Group

"It can be a challenge to tie together the patchwork of different systems on the floor, so we can have one consistent source of truth, in real time, across all the assets, new and old equipment, on every make, model, and age."

Thinkhubstudio/iStock/Getty Images Plus

That was Lauren Dunford, Guidewheel’s CEO and co-founder, who explained how the platform analyzes the power draw of each machine on the floor. "The power draw almost looks like a human heartbeat, and we effectively get that heartbeat into the cloud through a nonintrusive sensor that clips into the electrical cabinet or other location close to the machine."

The sensor itself isn’t novel, but the cloudbased analytics and artificial intelligence (AI) are. The platform began as a simple tool to track run-time and downtime, but within the past few years it has evolved to capture nuances of the electrical heartbeat, analyzing it to capture the number of cycles a machine is running over a given period, then correlating that with the actual job machines are running.

"We can capture early indicators of quality and machine maintenance issues," Dunford said. "We also use APIs that can push data to and pull from other platforms, like an ERP, then layer that on top of the real-time sensor data, so we can correlate by part number, by job, by shift, so you can slice and dice the data in a meaningful way."

At this writing, MMG is using Guidewheel to track machine uptime, so far connecting the system to 52 machines in its northern Vermont facility and 18 machines in its Maine plant. In the future, however, the organization has plans to tie uptime data with job-specific information gleaned from the ERP.

Meyers described an integration measuring the electrical draw of a 110-ton press brake. Jobs with forming tonnage of, say, just 30 tons would produce a completely different "electrical heartbeat" than jobs closer to the machine’s tonnage capacity. In this case, instead of working by an "average" current draw, engineers used a minimum-maximum limit. Light-gauge jobs would be close to the minimum while heavy-gauge jobs would be closer to the maximum.

MMG also has plans to tie this data with job-specific information. If a light-gauge job is drawing similar current as a plate bending job, something might be amiss. It could be a programming or tooling issue (too narrow a die opening, for instance). Regardless, that direct machine connection aims to catch the issue before it becomes a larger problem.

The next step, Meyers said, is to use the data to enhance MMG’s predictive maintenance. "This is where AI functionality will help, tying the platform directly to our CMMS [computerized maintenance management system] software. The system could alert our maintenance team to check on anomalies." The goal: To prevent, not react to, unforeseen downtime.

Streamlining Data Entry

It’s not unusual to see machine operators manually typing in job information. It could be related to inventory, part counts, or inspection. Whatever the purpose, typos can cause confusion and sometimes wreak havoc on workflow.

Ideally, operators shouldn’t need to key in so much information. Sometimes, though, the nature of the operation makes manual data entry unavoidable. A part might be rejected due to a masking error before powder coating. Masking, a manual process, leaves no digital signature. And no matter how automated data collection and entry are, operators still need to review and verify information fed to them. As the saying goes, garbage in, garbage out.

3 ROLL HYDRAULIC PINCH PYRAMID PLATE BENDING MACHINES

The 101 Series from WDM.

Over 40 years of experience with 3 generations working in the business.

Built in USA with American and global components.

30 gauge to 1″ thick, 1′ to 12′ wide.

Custom and built to order options available.

Have a rolling question? Call and speak directly to the designer, engineer and manufacturer of WDM machines, right in the USA.

Waldemar Design & Machine LLC

224 Pierpont Street

Petersburg, WV 26847

606-787-8474

sales@wdmrolls.com

www.wdmrolls.com

From complete custom forming cells to many popular/standard machines in stock.

Contact us direct, or contact your favorite machine tool distributor and ask about WDM Machine Toolls.

3 & 4 Roll Hydraulic Double Pinch Plate Bending Machines

Initial Pinch Sheet Plate Bending Rolls • Bending Systems & Complete Forming Cells

Multi-articulated spot welder Perfect for fabricating Cabinets

MYSPOT makes it possible for anyone to perform welding with the same high quality, no burn marks or distortion. MYSPOT saves our operators from manhandling bulky items - the copper tabletop acts as a work bench whilst welding. This process requires far less man-hours than traditional welding and is very effective in high volume production applications.

Less Sanding & Finishing

Easy Parameter setting

No Training required

koyogiken Inc. JAPAN

In these cases, Abuali said, AI, coupled with intelligent process automation, could help mitigate these challenges. For instance, he sees generative AI helping to catch data-entry errors. Say an operator types in a scrap rate incorrectly, adding a few extra zeros. Generative AI could detect and flag the aberration, allowing the operator to correct the typo before it snowballs into a larger issue.

Good Processes

It’s been said that automation and digitalization really can’t get to the heart of cultural problems, but in recent years, some digital tools on offer might help make a cultural impact. Consider employee onboarding and training. Many cultural issues boil down to people keeping their job knowledge to themselves and, more broadly, an overall feeling of apathy toward inconsistency and dysfunction.

Second and third shift can’t process this job as well as I can. Well, let them figure it out

.

Here, digital onboarding, training, and documentation tools can help. Digital work instructions should reflect what new employees learned in training and onboarding. AI writing tools might point out areas of ambiguity, and videos can spread best practices through entire departments and across all shifts.

"We can digitize the knowledge transfer," Abuali said. "You can digitize the knowledge that the retiring veterans have and use it to train and onboard the younger digital natives coming into today’s workforce."

From Fighting Boredom to Streamlining the Complex

Traditional automation in the fab shop has hinged mostly on volume or difficult-to-handle work. A large-quantity job is robotically welded because a shop doesn’t want to tie up its welding talent on repetitive, even boring work. A robot bends a workpiece because it presents an ergonomic nightmare for operators.

Digitalization can help streamline the complex. It can intelligently plan and schedule to not just make best use of available machines but also propel jobs through their routings as fast as possible.

"When we think of AI in manufacturing, we usually think of industrial AI, predictive maintenance, vision, and machine learning. But we also see opportunities in generative AI that can help planners make intelligent decisions," Abuali said. "Imagine asking a system, ‘Which machines and jobs are going to be delayed within the next week?’ With AI solutions, you need good data to train the models. As manufacturers accumulate machine, part, and scheduling data, the training of the models becomes more powerful over time."

When models become more powerful and accurate, even the most high-product-mix operations get less chaotic and more predictable. To be sure, the models

need

good data, and fabricators

need

to establish a good foundation of lean practices. If practices aren’t standardized, training falls short, and ineffective processes stay in place, no amount of fancy machines and software is likely to help. Even so, the potential of digitalization could help separate a fabricator from the pack, enable it to scale, and become an employer of choice for a new generation.

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

Guidewheel,

guidewheel.com

Momentum Manufacturing Group,

www.mmgmfg.com

Wipfli,

www.wipfli.com

YOUR NEW BENCHMARK IN

FIBER LASER CUTTING PRODUCTIVITY

GV

SERIES & TOWER

LASER POWER MAX.

ACCELERATION

MAX. POSITIONING

Up to 60kW

6G

984 ft/m

400% //

FASTER

300% //

STRONGER

100% //

SMARTER

REDUCED //

LABOR COST

"THE PERCENTAGE REFERENCED IS IN COMPARISON TO HSG’S ECONOMICAL MODEL.

SHAPE METAL //

SHAPE TRUST

HSG Tech Inc.

www.hsglaser.com

780 Belden Ave, Addison, IL 60101

(630) 359-5861