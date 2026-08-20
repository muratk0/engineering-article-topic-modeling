# The Ultimate Goal of Industry 4.0

[TARİH: 01.04.2017 The Fabricator]

Chief Concerns

No typing in data, no poring over reports—just making good parts

F

or the past several decades, fabricators have spent a lot of time and money gathering data that, truth be told, they rarely use. In fact, if fabricators put good data into a system, they don’t really need to look at it. If the software is working, managers and supervisors really shouldn’t need to bury their head in reports.

Consider the status check. Shops spend thousands of dollars per day just by asking, "Hey, is this done yet?" It’s a completely meaningless task. If you can connect to the machines and automatically notify the next stage of production, no one has to ask that question.

Industry 4.0 is the future, and striving toward it will be essential if manufacturers want to compete in the coming decades. But to implement it successfully, metal fabricators need to focus on what matters: Industry 4.0 should help, not hinder, the people who sell, design, program, and fabricate products.

The Cultural Impact

Years ago, managing laser cutting operations at a large sheet metal job shop in the Midwest, I climbed atop a stepladder. Holding a large drill with a bit longer than my forearm, I proceeded to make a hole in the wall separating the front office and the shop floor. One of our employees walked by and asked me what the heck I was doing. I told him, "We need to talk to each other."

The hole was for Ethernet cable, and it was our first step in bringing the fab shop into the 21st century, at least when it came to software and communication protocols.

Before this, people were typing in job information multiple times a day into different systems. Sometimes we even printed a bar code from one system so that someone could just scan it into another system.

We also had a warehouse full of sheets and remnants. If people had a laser cutting job that would barely make up a whole sheet (even though material utilization wouldn’t be great), programmers usually chose to work with the whole sheet. Why?

It’s because if they used a remnant, programmers had to take a clipboard, a tape measure, and a sticky note; walk 150 yards to the warehouse; find the perfect remnant that would work for that job; measure it and draw it out on the clipboard; write the job number on a sticky note and slap it on the remnant (which often was pickled and oiled material, so of course the sticky notes just fell off). The programmers then walked back to the office, nested the job, and then just hoped the operators could find the remnant in the warehouse.

Besides this, programmers spent their days retyping job data and redrawing sheets in the CAM system. They manually imported jobs into CAM, then keyed in quantities for each and every part. And this was just a small part of all the meticulous work they did day in and day out. For an average nest, programmers spent at least 45 minutes just typing data, followed by 30 minutes of actual nesting. We had three machines running a shift and a half with five programmers, and we couldn’t keep the machines running. Go figure.

Within a few years, we completely eliminated all of this. We digitized our material databases and updated them constantly with the actual inventory we had on the floor. Software automatically chose which kind of sheet to use—full sheet or remnant—instead of giving programmers the choice. And programmers didn’t mind, because software knew the location of the remnant, which was tagged.

Work orders started flowing to the plant automatically from the ERP system. No longer did programmers need to type in part quantities for each job; the information just appeared. Programmers selected the parts, and the CAM software automatically populated the nest, which programmers could then alter and improve upon if necessary.

In 2001 it took one programmer up to an hour to produce just one nest; by 2008 they were pumping out 12 to 15 nests an hour.

Admittedly, this new system took some getting used to, especially for people on the shop floor. For instance, previously our welders simply retrieved a leftover piece of stock they needed for an assembly, such as one of the small remnant pieces. At the time these items weren’t tracked. Now we were defining exactly where they could draw the material from, so they couldn’t just pick up random pieces of material.

Other people were used to typing whatever notes and descriptions they felt were pertinent into the ERP system. But this wasn’t standard, and it could be misinterpreted. To avoid miscommunication, we needed to standardize the way people presented information to each other. In the modern system, they had to follow defined processes.

To be entirely honest, it was a culture shock. But eventually, after several months and (in some cases) several years, everyone appreciated just how smoothly jobs were flowing from one station to the next. No one was walking around and searching for things. The welders now could go to a terminal, pull up a list of jobs, and then email their material request to material handling. Soon after a material handler would have material the welder needed, staged and ready to go.

The new regimen required that people think differently, and people ultimately accepted it and were happier at work because of it. But it did take time.

The State of the Art

Today the latest software available in industry has made material requests automatic. Consider the welder scenario described previously. Although not implemented at that particular company, modern software eliminates the need for the welder to even email or communicate any material request, period. Working under a

kanban

-like replenishment system (though not tailored to one product), web-based software now can trigger material requests automatically as those jobs come up on the welder’s schedule.

Regarding sheet nesting, no one needs to program manually, and no operator needs to correct or tweak the program at the machine. Jobs flow to the floor, operators click the next batch of jobs, and nesting occurs within seconds.

Making Machines Talk

Consider this typical scenario: Parts are cut on a punch press. Material handlers shake the parts out and stack them on a pallet. And the parts sit there. And sit there some more. Why isn’t the job being formed? It’s because no one clicked the "job finished" button in punching to notify the next operation that the job was ready for processing.

This is where Industry 4.0 is going to take things to the next level. When the punch is finished punching, the

punch machine itself

will inform the forming operation that the job is ready for processing, no manual button-clicking required.

This will have tremendous cultural implications. No longer will an operator need to scan or type job information into anything on the floor—not on the CNC and not on a separate PC terminal. Instead, a job number comes up on the schedule, which the operator sees as the next job in the queue; he then retrieves the staged material, sets up the job, and initiates the machine cycle. He spends his time running his machine and producing and inspecting parts, not logging in and out of jobs or entering data.

Behind the scenes, the controller will interpret data from sensors on the machine and feed it back to various software systems, all of which "talk" with one another. If the laser head is running hot or if any machine component is out of sync, the machine’s controller will (if it can) correct for these errors automatically and feed data to other software systems.

If a machine is capable of in-process measurement—like the angle measuring devices on a press brake—it will communicate that information to business software, which will correlate those adjustments with a certain batch of inventoried material, including the heat number, grade, thickness, and origin. No machine, controller, or software will be an island.

During inspection, the operator or quality technician will measure the part, and the measuring device itself will transfer the data to software, which will compare the measured datum to the original drawing. No longer will quality personnel or operators spend their days keying in inspection data.

Just like today, if a customer calls in about a job, a salesperson or shop manager can call up job tracking information with a few clicks. But unlike today, all the information will be there without machine operators needing to key in or scan anything. After all, the laser machine has the job information in its software and knows when the job was loaded and completed, so it can send that job status information to ERP.

The people on the floor probably won’t notice when Industry 4.0 truly matures. That will all happen in the background, automatically. The focus in the shop will be on shipping good products quickly and making more money in a sustainable manner.

Data Collection Must Be Automatic

Fabricators love to post charts showing productivity measures of this department or that workcell. This sometimes can lead to a healthy competition between shifts or departments. Everyone competes to "improve the numbers." But people sometimes overlook the fact that it costs money to have someone manually input data. Consider the following true story.

A manager at a fab shop, looking at the company’s new manufacturing execution system (MES), noticed that green-light-on time in laser cutting was declining. So he talked to the department supervisor. It turned out that the MES didn’t talk to the legacy work order system. And because the MES license was expensive, the company had just one MES computer terminal that five laser operators had to share. Those operators spent much of their workday waiting in line at the MES station to record job data.

The operators were

less efficient

because they were spending more of their day waiting in line and typing information into an MES, so that managers could track jobs and make things

more efficient

. Wait … what?

This illustrates why data collection really needs to be automatic. Gathering data isn’t a bad thing at all, but there are better ways to do it.

Too Late to Solve the Problem

As on Wall Street, a fab shop’s past performance does not dictate future results, and past performance is all that a chart posted on the wall really shows. This is especially true in custom fabrication, where one job may be completely different from the next. When you post data that reveals a problem, it’s usually too late to solve that problem.

Processing time depends on myriad factors, like sheet thickness, grades, and geometry. And as it turns out, this information comes baked into CNC machines, including laser cutting machines and press brakes, in the form of technology tables. Machine vendors have set standards for specific material grades, thicknesses, cut geometries, and so forth. You can validate these tables with time studies as well. In the coming years, this source data could be integrated with software systems like CAD/CAM and quoting.

That data will tell you not only whether a machine is producing parts, but

how well

it is producing parts—that is, how close is the actual production rate to the benchmark data in the technology tables? If a job should be cut at 120 inches per minute (IPM), is it really being cut at that speed? If not, the problem can be fixed immediately, before the job is complete and shipped. If you find out that you lost money on a job after it leaves the building, it’s too late.

An Open Future

Custom fabrication and other high-mix, low-volume operations are complex. Job routings send work every which way, and purchased components and services (such as heat treating and painting) are incorporated into the schedule. The sequence and status of one job relates to all the other jobs in the part mix, which in a job shop changes constantly.

One day Industry 4.0 will help optimize everything—not just one machine, but the entire process chain, from art to part. To make this happen, production data from one machine will be integrated with data from other processes throughout the value chain, from the front office to the shipping dock.

In the shop of the future, jobs with radio frequency identification (RFID) tags may talk to a systemwide architecture that incorporates everything in the shop: CNCs, CAD/CAM, ERP, quoting and sales systems, even accounting systems. And again, all the data gathering and job tracking happen automatically in the background.

The ideas behind Industry 4.0 require a common communication standard that allows one system to talk to another, with little cost or effort. Ideally, there should be no need to hire a software developer to handle all the machine and software communication protocols.

The path toward standard communication protocols and interoperability among manufacturing software and hardware will be unique and full of challenges. But considering the potential benefits, it’s a path that many are now wanting to take.

SigmaTEK Systems LLC, 513-674-0005,

www.sigmanest.com

Editor’s Note: This article is based on "Bridging the Gap: Integrate Business Systems with Machines Powered by Software in a Fabrication Job Shop" by Monty Brown, business development sales manager, SigmaTEK Systems LLC, presented at FABTECH

®

, Nov. 16-18, 2016, Las Vegas,

www.fabtechexpo.com

.