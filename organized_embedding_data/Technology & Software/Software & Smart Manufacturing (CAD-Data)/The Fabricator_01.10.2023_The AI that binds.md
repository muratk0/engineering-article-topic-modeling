# The AI that binds

[TARİH: 01.10.2023 The Fabricator]

Cover Story

When information flows, a fabricator grows

By

Tim Heston

V

isit a custom metal fabricator today, and you might see some extraordinary machinery— maybe an automated punch/laser combo, an ultrahigh-powered fiber; press brakes, panel benders, or folders with automatic tool change; some with robotics feeding parts and conveyor systems carrying parts away. Robots, both conventional and collaborative, dominate the welding department.

The fabricator has invested millions in manufacturing technology, and it’s seeing results—until you walk into the office. There, estimators and production planners manipulate spreadsheets. Paper is everywhere, and some can be seen manually keying in data. The shop has digital devices that can collect mountains of measurement data, and yet throughout the plant sit technicians—operators, department leads, quality assurance personnel—typing in results.

Look closer at other areas of the operation, and you see variations on a theme. Operations managers peer at spreadsheet printouts and key in data onto the screen in front of them. It’s an odd picture. They’re surrounded by digital devices gathering data, yet they still buy printer toner in bulk and deal with mistakes that stem from someone fat-fingering an extra zero on a keyboard.

The shop might have invested in advanced software: enterprise resource planning (ERP), customer relationship management (CRM), a manufacturing execution system (MES) or similar production monitoring and planning software (which may or may not be integrated with an ERP), a scheduling system (again, separate or with the ERP), maybe even a product lifecycle management (PLM) platform—the list goes on. The engineering department might have advanced nesting for cutting and offline simulation software for both bending and robotic welding.

Yet everything sits in a separate sandbox, each full of useful data that isn’t always the easiest to extract, especially for older software systems—purchased when few thought about sharing data and Industry 4.0 hadn’t yet reached buzzword status. A simple press or lathe will probably age well; manufacturing software, not so much.

Years from now, the early 2020s might be looked upon as a turning point in manufacturing software and information systems for manufacturing, especially for the custom metal fabricator. At this point, artificial intelligence (AI) is actually

writing

certain portions of customized software to meet the unique challenges of the job shop.

For years, the industry has used software platforms that work extraordinarily well, save for a few isolated cases—a unique process, an overlooked detail. And so fab shop managers manually export the data into a spreadsheet and develop yet another homegrown solution.

That era might be gradually drawing to a close. Just as a panel bender or an automatic-tool-change brake can switch seamlessly from job to job, shop information systems will adapt as well, share data, and help shops optimize throughput like never before, with no isolated "data silos" in their way.

About the Job, Not the Product

"It’s an exciting time for ERP systems again." That was David Lechleitner, a senior product manager at ECi Solutions. He’s spent a career serving the job shop market, and he’s now working toward his PhD and completing a dissertation on ERPs for those small and medium-sized custom manufacturing environments.

A lot of issues with legacy software platforms, he said, stem from the fact that they were never really designed for the job shop. "Almost without exception, most of them were designed for manufacturers with standard products, or at least a low mix of products."

Their core architecture reflected this. Any function related to manufacturing centered on a so-called "part master," which incorporated all the manufacturing steps to make the item in question. Those who designed this part-master-based software assumed that a factory would make products over and over, for months or even years on end.

Transferring a similar architecture over to the job shop environment was a bit like fitting a round peg into a square hole. When shop supervisors wanted to change a routing due to capacity or loading issues, or because certain work centers were just more capable than others, they saw this as a simple change. A job shop is bit like a road map, with intertwining arteries of job routings. What’s so hard about taking a different route? But because the traditional part-master ERP based everything on "the product," it had to undergo a plethora of steps to make that seemingly simple change.

Put another way, instead of just taking a different route on a map, the part-master-based software, quite quixotically, started with a fresh map with every new job routing. In one sense, the software architecture looked at a new job routing like a new factory line—something that would run for months or years, not just once and never again.

Some modern ERPs tailored for custom manufacturing run not on a part master but on a system based on jobs. Each job has various elements with various materials that could wind their way through different job routings in various ways, all depending on an operation’s capacity and capability.

In this case, changing a routing is indeed like choosing another route on a map. Sure, traffic conditions will change, which in turn will send ripple effects elsewhere in the operation. But computationally, at least, the routing change doesn’t require ERP software to move heaven and earth.

The "job" (or estimate, if the job hasn’t been won yet) can have a bill of material (BOM) and routing attached to it. That said, jobs in the estimating phase aren’t rigid. They might not have a complete BOM or detailed routing, just enough there to produce an effective estimate quickly. "Once the job is won, I can really finalize what that BOM and routing should look like on the job," Lechleitner said.

Once the job runs a few times, the routing might change as a shop perfects its production methods. Perhaps a certain material cuts better on a certain laser or is better suited for a particular brake. Similar adjustments can be made on the material side. The manufacturing method isn’t static, and the job-based ERP records the data to make those improvements possible, providing actual-versus-estimated cost and time comparisons at every step along the way—a feat not always performed by a product-master-based system.

"For part-master-based systems, they’re assuming those parts have been run many times before," Lechleitner said, "so it’s not critical to capture those actual times. Everything is based on a standard. And yes, periodically, factories might run time studies to improve and then update the part master. But for job shops, they need to capture the real production times and real material usage with every job."

There’s an (ERP) App for That

Job-based ERP systems aren’t entirely new, but today they’re evolving in new ways. User interface is as important as ever, of course, but so is how a particular software interfaces with other software packages.

Lechleitner sees the future landscape reflecting that of the iPhone app store. People choose the iPhone not just because of the interface that Apple provides but also the apps that can run on it seamlessly. Apple can’t be everything to everybody, and the same holds true for software vendors in the metal fabrication space. Vendor collaboration and open application protocol interfaces (APIs) are becoming more important than ever.

"People want capability and configurability in ERP systems," Lechleitner said. "I see us moving away from this monolithic, single-solution ERP approach to that iPhone experience. If you need an estimating solution, you can go to an app store and download it. Several players in the market are taking this approach. That really is the wave of the future. We’re moving away from that single-source, single-vendor approach."

For instance, ECi’s JobBoss has a partnership with Paperless Parts. "Quoting capability in ERP is pretty basic, and it requires some knowledge from the user," Lechleitner said. "Add on Paperless Parts, though, and it can digest a part file and create the routing and bill of material for you, using the part geometry, material, and material estimates."

Enter the Low-Code App

The future software landscape will involve not just traditional software, but also platforms that effectively give users the tools they need to develop their own program. This is the world of the low-code app.

"More than any other market, job shops appreciate flexibility."

That was Wayne Byrne, founder of Tangle, a low-code platform that allows users to build their own apps with a drag-and-drop interface. "I’ve been building low-code, drag-and-drop interfaces for 25 years, though they weren’t called ‘low code’ until the past few years or so."

Until recently, low-code apps really focused on dashboards and communication tools. "They were still based on spreadsheets," Byrne said, "though with a bit of analytics built in."

Think of low-code apps as a bag of LEGO building blocks. Users can click them together in various ways to create all sorts of custom applications, but they still need to use those LEGO blocks. This, Byrne said, "gets you about 80% there. You have your solution, but you also have to manually fill out notes to describe the exceptions. It doesn’t handle every scenario."

The latest low-code apps, Tangle included, still use those LEGO building blocks, but it also allows users to add their own code, effectively allowing them to create their own LEGO blocks to accommodate specific, often unique problems.

This overcomes the customization conundrum many fabricators face. So many platforms, ERP or otherwise, could be the perfect solution if they could just do …

fill in the blank

. A company might be tempted to ask for a software package to be customized, but that adds costs and complexity, not to mention the potential lack of support. Low-code apps bring shops that last mile without having to customize off-the-shelf software.

AI and the Low-Code App

When ChatGPT burst onto the scene last year, many thought low-code apps might be doomed. If AI has the potential to write software from scratch, why do you need those LEGO building blocks that limit what low-code apps can accomplish?

WHY IT MATTERS

Good part flow demands good information flow.

Spreadsheets and other homegrown solutions, be it for quoting, scheduling, data reporting, or anything else, still pervade the industry—standing in stark contrast to advanced machinery on the floor.

New tools are boosting interoperability between existing software platforms and specialty software.

AI technology is helping low-code software customize platforms to meet a fabricator’s unique needs.

"It turns out, AI is the low-code-app’s best friend," Byrne said.

Today, most software programmers are using AI to accelerate development. "Now, why would you write a program from scratch? Let the AI at least get you started," Byrne said.

In most situations, developers really can’t rely on AI to write every single line of code. Those working with low-code apps, however, can use AI to help write that last bit of code and provide users, fab shops included, with a highly customized solution.

Recently, Tangle added a ChatGPT interface that can write that last bit of code on a custom app. It can also help users solve complex problems like scheduling—not by clicking around a complex platform, but by literally talking to the AI. "Star Trek," here we come.

"We’re now doing smart scheduling using AI," Byrne said. "You tell ChatGPT what you’ve got going on, you tell it a rule set, and it gives you a suggested schedule."

He emphasized that the scheduling technology itself isn’t new. The method used for this custom app happens to use the drum-buffer-rope methodology from the Theory of Constraints. The scheduler also still works with the data that it’s given—the run times, changeover times, and all the rest. As it always has, garbage-in garbage-out still applies. If wasted activity isn’t captured, the system won’t see it.

The real innovation here is in the software interface. Configuring all of the parameters through a manual interface would be an arduous task. "The AI here is mostly a translator for humans," Byrne explained. "It takes human logic and turns it into computer logic. So, you can tell it, ‘Schedule my work, but prioritize these particular jobs, and deprioritize these orders.’ The system will factor in that logic, and it will tell you why certain orders are scheduled the way they are."

An Open Future

As a product, low-code platforms like Tangle are tough to pigeonhole. The idea is for these platforms to mutate into anything a fabricator or any other user needs them to be.

For instance, Tangle can work with existing ERP systems (including JobBoss), scheduling systems, or anything else, and build low-code apps around them to create a complete solution. Or, it can be used as a stand-alone system, offering the traditional functions of an ERP as well as quoting, scheduling, quality, production control, and customer-facing web portals.

Byrne added that the system can use what’s known as RPA, or robotic process automation. "If you’re trying to get information out of a system that doesn’t have an open API, you can make a bot that pretends to be a person." Use cases vary, but in effect, RPA acts as an API when no API exists, allowing different legacy platforms to shake hands and get along.

Think of the Potential

When everything connects, the potential abounds—especially with an AI interface that allows users to grab the information it needs. Imagine a shop with a machine monitoring platform. Because the company has older machines, getting job-specific data might not be easy, especially if the system runs batches of parts from different jobs (think of a laser cutting nest). The monitoring system shows uptime and downtime, but it doesn’t show what jobs ran and when.

But what if that machine monitoring data is time stamped? If it is, it could be correlated with clock-in clock-out data from the ERP or manufacturing execution system (that is, an operator clocks in and out of jobs on a separate computer terminal). That in turn could be correlated with actual-versus-estimated data, which in turn could be correlated with the mix of jobs on the floor at a particular time. This could help govern when orders are released and perhaps even how they’re sequenced.

Supplier metrics (cost and performance of material suppliers, heat treaters, custom powder coaters) could even be wrapped into the mix.

An assembly operation took longer than expected. Why? The custom coater didn’t return all the parts we sent them.

Also, what about demand predictability from customers? Does the customer give a good forecast and order at regular intervals, or does it send a massive PO out of the blue? The more predictable that demand is, the less costly serving that customer is likely to be. Interconnected data would detail what those costs really are and spur people to think of new ways to reduce them.

All that cost data could be compared with customer- and even sector-specific data. Are a shop’s margins low enough to be competitive for certain customers or sectors, but not so low that it’s leaving money on the table?

To be clear, much of this is hypothetical. But the data is there, all gathered in separate sandboxes: ERPs, MESs, CRMs, nesting software, production control software, machine monitoring software, warehouse management software, HR management software, compliance software—the list goes on. If there’s a function a manufacturer performs, you can bet there’s some software initialism or acronym associated with it. The trick will be tying it all together.

A Tapestry of Innovation

Years ago, Microsoft dominated the consumer software world and worked to squash the competition wherever it could. Today, the software giant behind the Windows operating system embraces open source code, even (gasp) Linux.

Software in metal fabrication might be following a similar path. A fabricator might work with one platform, if it so chooses, or a tapestry of new and legacy platforms. Whatever the approach, the system will be tied together with a human-friendly interface—AI-driven or otherwise—that can grab the right data it needs to optimize every process in the metal fabrication enterprise, from quote to cash.

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

Eci JobBoss,

jobboss.com

Tangle,

tangle.io

THERMA-TRON-X, INC.

Industrial Paint Finishing Systems

ECOAT | POWDER | LIQUID

SCAN ME

Your Best Finish Starts With Us!

Material Handling Innovations

Heat Processing Solutions

Water & Wastewater Treatment

Service and Spare Parts

Visit us at: HEAT TREAT | 2023

October 17-19