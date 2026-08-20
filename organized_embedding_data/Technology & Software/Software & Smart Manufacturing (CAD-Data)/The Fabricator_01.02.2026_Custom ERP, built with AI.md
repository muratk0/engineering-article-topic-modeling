# Custom ERP, built with AI

[TARİH: 01.02.2026 The Fabricator]

Software

Digitalization at a 10-employee fab shop

By

Tim Heston

J

eff West has spent the past two decades of his career as a hands-on welder and fabricator. In his 20s he helped build and maintain precipitators and other equipment at power plants across the country. He delved deep into pipe welding and spent time welding rail cars before landing a job at Cogbill Construction in Vidor, Texas. He’s now foreman of the company’s 10-person metal fabrication shop.

And, oh yeah, he also writes software and, with the help of AI, is building a custom enterprise resource planning (ERP) platform.

BIG SOFTWARE FOR A SMALL COMPANY

"I’m a welder, fabricator, and hobbyist programmer. I’ve never coded for a living or anything. I’ve just always had an interest in it, going back to the 1990s, I suppose." West reminisced, "I’ve used a variety of programming languages. Python’s my favorite. But for this app I’ve built here, this is all JavaScript."

He picked up his phone and showed an app, dubbed Cogbill ERP, which today helps the small job shop track orders and organize quality control documents, linking every piece in a job back to material test reports (MTRs) sent from the metal supplier. All that insight is now available with a few taps on a phone, tablet, or laptop.

"And now, AI has made everything go so much faster. Instead of manually writing thousands of lines of code, I just build a foundation, tell AI what I want, then modify it manually as needed."

Small metal fabrication shops have a common conundrum. In some ways, they’re simple and, hence, don’t need all the bells and whistles of many off-the-shelf ERP platforms. But in other ways they’re extremely complex, because every small operation has unique needs. Product mixes vary, as do project timelines and job requirements. So, instead of molding their own operation to fit an off-the-shelf ERP platform, they build a homegrown system, often based on spreadsheets.

A fabricator bump-bends a large radius on the shop’s press brake. He logs in and out of the job on the company’s custom ERP system using a large-button interface on his phone.

This approach historically has taken fabricators only so far. But as Cogbill’s story shows, the situation might be changing, AI has helped the fabricator build an ERP platform tailored to its unique needs. The story shows how AI tools are quietly reshaping how businesses, especially small ones, operate.

Jeff West has been a welder and fabricator for more than 20 years. He’s also coded as a hobby since the 1990s.

A SOFTWARE JOURNEY

Cogbill’s metal fabrication operation is about as custom and high-productmix as they come. Some jobs might involve a few pieces of angle iron cut on an ironworker; others, several dozen pieces cut on a plasma table, then formed on a press brake; still others involve welding and assembly. Some jobs cost less than a few hundred dollars; others cost several million. Some need to be delivered tomorrow; others ship specific components on a defined schedule spanning weeks or months.

When Hani Almufti, engineer and manager of strategic development, arrived at Cogbill 14 years ago, he joined a shop full of paperwork. "Back then, the owner would write on a sheet of paper what people in the shop needed to do. It was a list of instructions. Timesheets were done on paper too."

These would be typed into a spreadsheet, a homegrown system that detailed job averages and costs. That same information would be typed again into QuickBooks.

Several years later, Almufti developed another spreadsheet with functions that helped streamline order processing. Once someone input all the job information—customer name, billing address, location of job drawings—the system would automatically generate other sheets that the company needed to process an order. This included the shop work order, which described what needed to be done, where the material was, the ship date, and delivery method. All this fed into QuickBooks, too, eliminating double data entries and the potential for data-entry error.

"It would also create a quality check sheet, which each employee or the foreman would initial to signify each step had been complete: cutting, bending and rolling, welding, and so on," Almufti said. "Then, when the job was finished, [that original spreadsheet] would automatically generate the packing list and delivery ticket."

About a dozen years ago, the shop implemented a separate system that tracked all the MTRs for its inventory. Workers began scanning the MTRs and connecting them to specific jobs, tracked on a system built in Google Sheets and backed up by bound paper copies. "We now have almost 15 volumes of printed MTR sheets. Many MTRs are multiple pages," Almufti said, "and each volume has 1,000 pages. All of it has become difficult to manage. That’s why we’re pushing to go paperless."

The MTRs reveal a common conundrum among small job shops. As sources explained, only a small portion of Cogbill’s customers demand MTRs with their delivered orders. In fact, some of the shop’s largest customers don’t require one. In these cases, many shops with homegrown systems might choose to track MTRs on demand, not for every job. After all, scanning PDFs and managing a database can be a serious resource drain.

Both Almufti and West didn’t think this way. Housing and tracking MTRs help maintain traceability and standardize procedures, they said. Most important, building such traceability raises the bar for quality, preparing the small fabricator for customers that demand MTR and even more granular traceability. The challenge for very small operations, of course, is finding the resources to buy or build and then manage the system.

Here again, AI is changing the game. In the middle of 2025, West began building a custom ERP system that’s both simple for shop use and yet sophisticated enough to plan for growth.

JOB TRACKING AND TRACEABILITY

As anyone who works in the job shop world knows, rework is the worst kind of waste. What makes rework even more painful is when there’s no documentation that proves the root cause.

In the middle of last year, when Cogbill’s fabricators were forced to rebuild some handrails that were lost by an outside service provider (a galvanizer, in this case), the foreman didn’t just accept it as part of life in a job shop. He did something about it.

"We were told we miscounted the handrails," West said. "I knew we had fabricated them all, but I couldn’t prove it. I didn’t want to have that happen again. I wanted a tracking system where we’d have real documentation showing every fabrication step from cutting to bending to welding." This was the initial spark that pushed West to start applying his coding prowess. Using JavaScript, he built a basic job tracking system that incorporated a photo of the job work ticket and an image of the job, staged for shipping.

"As we’re building a job, I can link the MTRs to specific parts of a job, or a job as a whole," West said. "I’ll then link them to the part, so we can keep track in our inventory system. And when we ship, we attach a cover sheet that lists out all the parts and what MTR numbers each had. Then we attach a single copy of the MTR."

West held up his phone again. Next to him, Almufti opened his laptop. Each viewed the same screen with the same information: material type, country of origin, quantity in square feet, material grade (A36, A106, stainless 304, etc.), and even the heat number. Click on the material and you see a window showing a scanned PDF next to the MTR.

Each piece of received material is assigned a Cogbill number for internal tracking. MTRs from the mill are scanned (several document scanners sit next to the quality office). The material goes into numbered racks, and the location is recorded.

The employee receiving the material also writes the Cogbill number on multiple areas of the piece. Again, the fab shop runs low-quantity work and, hence, regularly deals with remnants. Those remnants are kept in the same inventory slot (stacked vertically, for easy access) until the plate is consumed entirely.

"That way," Almufti said, "we don’t have to keep updating the material location." He added that the simple strategy helps avoid two common productivity pitfalls: searching for material and tracking remnants.

A SOFTWARE FUTURE ACCELERATED BY AI

Today, besides MTRs, the system tracks jobs and hours worked on each job. Workers clock in and out for each manufacturing step, or stage, using their smartphones. Cogbill ERP shows active jobs in production, as well as the percentage complete for each order. It shows ready-to-ship jobs, as well as the number of stages in queue, giving an accurate view of the remaining work in the shop.

Soon, West and Almufti plan to make certain aspects of job tracking available for customers to view. Just as someone would log on to track an order from Amazon, customers will be able to log on to Cogbill’s system to see where their jobs stand.

Eventually, Almufti hopes to start digging into estimated versus actual costs and use that to drive the fabricator’s sales efforts and identify areas for potential improvement. "After the job ends, we want to know if we overbid on a job, or if we underbid on some parts of that job," he said. "With that, we can adjust the execution. This will help us run our operation by the numbers, by real data, not by someone’s experience."

Here again, AI is playing a key role. Years ago, a fabricator like Cogbill might have hired a software developer to build a custom system if the budget allowed, even if the shop had a foreman who knew how to code. The time commitment to develop a custom system would have been too great.

"Within just the past year, though, things have really changed," West said. "These AI engines have turned from being just a useful tool to a true software development tool. They used to just help write lines of code. Now, it can write the entire code base."

To illustrate, West walked through how he built the company’s MTR module. He used JavaScript as a foundation but then accelerated the development by working with Claude, an AI agent from Anthropic.

ENHANCED SOFTWARE, THREE BIG BENEFITS

Cogbill Construction’s Hani Almufti explained that the fabricator’s inhouse ERP system addresses three practical needs common to many small job shops:

1. Reduced communication errors –

Change orders, updated instructions, and the latest drawings are pushed into the same system for everyone to see, instead of being rewritten on paper, relayed verbally, or buried in long email threads.

2. Fast job closeouts –

In the past, employees gathered MTRs, QC check sheets, change orders, and other documents by hand, then copied, scanned, and archived them in a physical job folder along with drawings and job-related correspondence. Now, the system automatically exports all job documentation into a consolidated PDF package and saves it to the company server under a consistent, searchable name for long-term retrieval.

3. Less paper –

The shop still prints engineering drawings when needed, but MTRs and most job communications are now handled digitally instead of being printed and filed.

"You need to build in modules," he said. "The AI gets confused if you give it too much. So, for the MTRs, I described the material traceability we wanted and fed it the spreadsheet that we used in our original tracking program. This tells it what we need.

"At first, the AI usually overcomplicates things," West continued, explaining that for the MTR module, the AI drew from all the functionality it comes across on the internet—everything from general construction to medical devices and nuclear reactors. "Seeing this, I basically tell the AI, ‘I don’t need all this.’ So, you talk back and forth with it until it gets close to what you need. Then it says, ‘OK, let’s build it.’ And it builds the module in a branch that doesn’t affect your current code base. You see how it looks, and you go back and forth to perfect it."

On the near horizon, the company hopes to integrate AI tools that will ease the user experience. "We want to be able to verify our MTRs automatically," Almufti said, explaining that today, employees still need to verify that the system read the PDF files of those scanned MTRs correctly. Text recognition has come a long way, but it isn’t perfect. "We also want to be able to import customer-provided part lists and automatically rename products according to our own standard part names and numbers."

The current system has features entirely customized to the company’s needs: shipping insights; maintenance, including digital manuals and records; tracking for employee training and certifications; user-specific access and interfaces (people see the information they need to see); inventory management, including a digitized MTR database; QC package development; quote and job tracking—the list goes on.

"We want to be able to manage everything, from the initial phone call to quoting to the end of the job," West said. "We’ve got most of the pieces there. It’s now just a matter of putting it all together."

In all this, perhaps the most significant insight from AI has been developing the user interface (UI) and overall user experience (UX). In a sense, gathering and organizing the data AI needs to do its work is time-consuming, but it’s relatively straightforward. Getting people to

use the system regularly

is another matter, which is why UI and UX are so important.

Over the past several months, West has perfected the interface by telling AI how people use the platform. It knows it needs to account for people wearing gloves. So, on the phone screen, buttons appear large. The AI also knows how experienced people are with software and what information they access regularly throughout their workday. From this, West said, AI has helped build an intuitive, clean-looking system that has required minimal training. The design reflects how people work.

West summed it up this way: "The goal of software is to make the job easier for everybody, not more complicated." He added that AI really has made "giant leaps" in streamlining software development. Improving the platform now takes a matter of minutes or hours, not weeks or months.

"It’s really amazing. The technology has changed tremendously even over the past six months, when I started this project. AI is just getting better and better. Just imagine what it will be able to do a year from now."

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

Cogbill Construction,

cogbillconstruction.com

Claude by Anthropic,

claude.ai

ACHIEVE THE IMPOSSIBLE

SEPTEMBER 14-19, 2026 MCCORMICK PLACE, CHICAGO

Transforming Your Business Is an Adventure

"There are so many tools and processes I would never have known about; roaming the halls of IMTS has excited me to learn so much more.

Emerging technology is truly what’s at the forefront at IMTS.

"

Whether she’s sailing the Pacific or building wind turbines, curiosity drives Crystal Allen. And for this builder of the future,

IMTS-The International Manufacturing Technology Show

offers her new adventures to embrace - and exciting paths forward.

Chart your course at IMTS on Sept. 14-19, 2026, in Chicago.

SCAN TO

REGISTER