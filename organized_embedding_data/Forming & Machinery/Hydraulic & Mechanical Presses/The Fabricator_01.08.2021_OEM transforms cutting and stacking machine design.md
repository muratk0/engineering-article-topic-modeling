# OEM transforms cutting and stacking machine design, boosts throughput 55%

[TARİH: 01.08.2021 The Fabricator]

Technology Applications

Lamination coils of various widths can feed into the X-Shear, depending on transformer core sizes.

Beckhoff Automation

SITUATION

In transformer core manufacturing, efficiency gains in production cannot sacrifice part accuracy. Micro Tool & Machine Ltd. (MTM) made repeatability its top priority while working to increase throughput of its X-Shear machine.

"Higher production rates are the goal of every machine manufacturer," said Gord Atamanchuk, general manager. "Doing this without sacrificing processed part accuracy is critical to our success. Once processed, being able to assemble those parts into the final e-stacked core while minimizing gaps is more critical than ever because of the industry trends to reduce postprocessing time downstream." Based in Winnipeg, Man., MTM designs and manufactures systems for the manufacturing and distribution of medium-size power transformers and for the aerospace and medical industries. These systems integrate CNC, robotics, tooling, assembly, jigs, and fixtures. Since its founding in 1964, the company has offered high degrees of customization to accommodate the unique process flows or facility layouts of its global customers. The engineering team often re-evaluates technologies and components to provide the most robust capabilities, as the recent X-Shear redesign proves.

Based in Winnipeg The XS600-P20E X-Shear cuts, stacks, and assembles transformer laminations using PC-based automation and robotics. At one end, the machine uses an X-shaped blade configuration to cut any required geometry from coiled lamination of varying widths. After that, two articulated Kuka robots, in conjunction with two pick-and-place arms, assemble the core pieces.

The system is designed to cut and assemble up to four transformer cores at once in e-stacking modes and sort the cut laminations into 30 segment piles when not in e-stacking modes. However, it can scale up or down depending on product sizes. At 43 ft. long by 26 ft. wide, the machine’s footprint measures up to three times smaller than many competitors because of its space-saving grid format for loading/unloading.

In the redesign, MTM engineers focused on optimizing throughput, increasing cut accuracy, and reducing component and labor costs. They wanted to reduce wiring effort with distributed I/O modules. The machine needed to leverage IoT-ready technologies to offer customers opportunities to further enhance machine performance and to provide remote support, since the machine would eventually be installed in China. PLC cycles and scan times also needed to be shortened.

"One of the biggest keys was implementing a true multitasking controller. The previous control platform we used fell short of our runtime requirements. The system had limited capability to perform conditions or commands in parallel. This meant fewer parts per minute," said Eduard Streichert, electrical lead. "Switching to a standardized PLC program—specifically IEC 61131-3— would provide further gains. For electrical technicians, it’s easier to troubleshoot in standard PLC languages."

RESOLUTION

MTM engineers combined what they had learned from previous systems and customer feedback, then leveraged a new control platform for the X-Shear. In the five years leading up to this redesign, the engineering team had transitioned all other machines to PC-based control from Beckhoff Automation. Now they were ready to update the largest and most complex machine.

For the X-Shear, the company chose the TwinCAT 3 automation software and the C6930 control cabinet industrial PC (IPC) from Beckhoff. The multiple runtimes in the software enable deterministic control for parallel tasks, including high-velocity coordinated motion used with the X-shaped cutters. Through Visual Studio integration, the software enables programmers to use the best language for the project and the engineer, including IEC 61131-3 and its object-oriented extensions, predefined or custom function blocks, and computer science programming standards.

"Unlike the previous programming platform, TwinCAT helps technicians see potential issues faster and understand how to fix them," Streichert explained.

The IPC features a seventh-generation Intel Core i5 processor with four cores and a 2.7-GHz clock speed. The single PC-based controller handles control logic, IoT connectivity, and other functionality for the cutting and stacking cells.

"As a true multitasking controller, the C6930 reduces machine cycle times so that throughput is much higher," Streichert said. "The IPC offers one combined solution for PC and PLC technologies. This includes everything from connecting to higher-level systems and enabling remote support to storing recipes and running the HMI in Visual Basic."

For the operator interface, MTM selected a CP3921 multitouch control panel with custom push-button extensions. This IP65-rated, 21-in. touchscreen is pole-mounted on the cutting cell. The stacking cell features a built-in CP2912 multitouch control panel, which provides the same HMI experience scaled to a 12-in. touchscreen.

The fully integrated Beckhoff system enables motion design tools, realtime PLC, and a digital oscilloscope all inside the standard software. This helped with fine-tuning movements for highest accuracy, Streichert explained.

By transitioning to the Beckhoff platform, MTM boosted performance and functionality for the X-Shear. The machine’s maximum cutting speed increased to 34 sheets per minute—a 55% increase in speed compared to previous models with the legacy PLC. These gains resulted in part from the significantly faster PLC cycle time of 1 ms. Most important, the machine redesign accomplished its key goal: maintaining high cut accuracy.

Beckhoff Automation

www.beckhoff.ca

OIROX Compact Cells

Your customised solution for automated small part welding

The QIROX Compact cells do not require much space and can be easily integrated into any production. From sensors to controller each compact cell or compact system is a tailor-made unit with components which match each other perfectly.

CLOGS

weld your way.

Mining equipment-maker improves productivity, safety with heavy-duty positioners

SITUATION

Joy Global Underground Mining LLC, a subsidiary of Komatsu Mining Corp., provides essential mining equipment and systems to companies worldwide to extract fundamental minerals for developing modern infrastructure, technology, and consumer products.

As a large company manufacturing large equipment and frames of different sizes, Komatsu needed a positioner with a heavy capacity. Turning the frames took a minimum of 30 min. and required three to four workers using cranes, so the company wanted to improve productivity as well as safety. In early 2019 Joe Nara, sales service manufacturing coordination manager for Komatsu’s crushing business, started searching for a positioner on the internet.

RESOLUTION

Nara found ALM just at the time ALM was developing its Heavy Duty (HD) line of positioners, with capacities from 75,000 to 125,000 lbs. Komatsu purchased two 100,000-lb. headstock with adjustable rail tailstock positioners.

Even with such a heavy capacity, the footprint of the positioner did not take up a lot of floor space. "The ALM positioner has a significantly smaller footprint than its competitors, even at such a high capacity," said Nara. "Since we did not have the required amount of concrete, we had to add a 3-in. plate to anchor the positioner directly to the floor. Even with that plate, the footprint is still small."

The positioners are structurally designed to a 3-to-1 safety factor and feature safety scanners that protect the operator while the machine is in motion. "The safety scanner is by far the top benefit. Using the Keyence safety scanners with the positioners has helped us tremendously," Nara explained.

"The next benefit would be that we can move frames through our line faster. The positioner keeps our cost down, and having a high-capacity positioner means that it can be used with the wide range of frames with which we work.

"It now takes about four minutes to lift the frame to the top and rotate it 360 degrees and back down," Nara continued. "The guys out in the shop feel much safer using the positioners instead of a crane. Plus, using positioners frees up the overhead crane for other parts of the facility." Nara said using the positioners has saved around 100 hours per frame, a significant improvement.

"We use these positioners as a part of our selling strategy, which in itself is important. We love bringing our customers into our facility to show them how the frame is coming out; they are instantly impressed. When they come in, they see the benefits of the positioners, particularly that their frames are getting completed faster," Nara said. "The president and vice president of our division were also very impressed when they came in for a tour. It was nice to see that their reaction was so positive. Showing them where we had made improvements, not only from a production standpoint but safety as well, made it clear that purchasing the positioners was worth the investment."

ALM Positioners

www.almmh.com

Visit us at

FABTECH Booth A3399

This webcast was recorded on July 26, 2021

How to reduce human error by using automation in your estimating and quoting process

paperless

PARTS

The guide to building guardrails that increase speed, profi tability, and scalability in sheet metal fabrication

One of the main challenges for every sheet metal fabricator is to balance the need for fast quotes with making sure they are consistent and mistake-free. Inconsistencies and mistakes come from manual estimating processes. These processes rely on Excel, tribal knowledge, and a team of estimators’ ability to approach every RFQ the same way. Anyone who has estimated jobs for an 8 hour day knows that at the end of the day their approach or perception can vary. Relying on estimators to catch all manufacturability issues is an unrealistic expectation without some level of automation. One mistake on a large quote usually means thousands of dollars in lost revenue. Inconsistencies on quotes to a longtime customer could mean losing the customer.

A buyer’s job is to manage risk, and if your shop sends inconsistent quotes or makes mistakes, you look risky. Estimating is one of the most challenging jobs in your shop and is critical to ensure profitability. Every job starts with a quote and this process is a bottleneck if you don’t give your team the right tools for the job.

Join this webinar with Jason Ray, Co-founder and CEO of Paperless Parts, to learn how you can leverage technology to:

Automate steps in the quoting process to improve the consistency of your quotes

Avoid mistakes with manufacturability warnings based on the geometry of the part

YOU’LL HEAR FROM:

Jason Ray

Co-Founder and CEO Paperless Parts

Jason Ray is the Co-Founder and CEO of Paperless Parts, the platform for manufacturing that enables machine shops to streamline communications, quote faster and more accurately, improve customer experience, and grow their business. Jason found his passion for manufacturing while serving at the Pentagon in the United States Navy as a supply and logistics officer, where he led advanced manufacturing implementation. Seeing the negative impacts associated with ineffective sourcing of short-run production components, Jason was determined to solve this critical problem that plagues manufacturing. Jason has a B.A. from Trinity College and MBA from Babson College.

This free webinar is brought to you by:

To access this webcast, please visit

www.thefabricator.com/webcast