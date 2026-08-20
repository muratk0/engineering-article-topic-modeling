# The Southwest software meltdown

[TARİH: 01.03.2023 The Fabricator]

Tech Talk

Why Southwest’s holiday fiasco may be a warning sign for antiquated manufacturers

By

Caleb Chamberlain

For more content from

Caleb Chamberlain

, visit

www.thefabricator.com/author/caleb-chamberlain

.

Caleb Chamberlain

is CEO and co-founder of OSH Cut, 165 N. 1330 W #C4, Orem, UT 84057, 801-850-7584,

www.oshcut.com

.

D

uring Christmas and New Year’s, Southwest Airlines canceled almost 17,000 flights and stranded hundreds of thousands of people in airports across the U.S. The cost to the company’s reputation may be immeasurable, but Southwest estimated its immediate cost at a staggering $825 million.

Many factors contributed to the meltdown, but in the end, it boils down to poor software infrastructure. Flight scheduling is complicated generally, but particularly so for Southwest. Other airlines favor a hub-and-spoke model, bringing flights into major hubs like Detroit and then connecting to smaller airports on the spokes. In contrast, Southwest favors point-to-point flights, minimizing layovers. Crew members required to fly aircraft are dispersed across the country, and without a large hub, canceled flights are far more likely to strand personnel. A canceled flight in Dallas might mean that another flight in Los Angeles doesn’t have a pilot, and that might mean yet another flight in Las Vegas doesn’t have flight attendants. One canceled flight follows another like a row of dominoes. When poor weather slammed airports across the country on the week of Christmas, the entire house of cards came tumbling down.

No Surprise

This outcome wasn’t just predictable. It was predicted. In November last year, Casey Murray, president of the Southwest Airlines Pilots Association, said, "I fear that we are one thunderstorm, one [air traffic control] event, one router brownout from a complete meltdown. Whether that’s Thanksgiving or Christmas or New Year’s, that’s the precarious situation we are in."

His concern wasn’t new. Much has been written about this already, but one element of the entire fiasco stands out as something that lean-savvy fabricators would have noticed immediately: the complete disconnect between management priorities and on-the-ground reality.

One would think that Southwest’s scheduling systems could handle personnel management for canceled flights, but that isn’t the case. Instead, stranded crew must call a hotline to report where they are, arrange hotel accommodations, and reschedule manually. These service calls are ordinarily bad, with reported hold times measured in hours and call disconnects common. It’s bad enough that the Union of Southwest Airlines Flight Attendants recently prioritized upgraded scheduling and communication tools even above increased pay.

Despite ongoing poor worker experience, Southwest didn’t invest in new systems to improve scheduling efficiency. It shrugged off the need while simultaneously allocating hundreds of millions of dollars for dividends and billions in stock buybacks. Southwest was a money-making machine, made brittle by a misguided drive for fiscal efficiency that ignored realities on the ground. When everything dissolved into chaos last year, Southwest had no idea where its pilots and other crew members were, or whether they were fit to fly. The schedule had to be restarted from scratch by people using tools literally two decades old, tools originally designed to serve a much smaller airline.

In fairness, it’s easy to criticize. Southwest has shown phenomenal growth, an excellent balance sheet, and great investor return. Like a frog in a pot, Southwest might have been mildly irritated by its scheduling systems 20 years ago, only to be slowly boiled as the company grew too fast, not comprehending the extent of its infrastructure and process problems. Perhaps the issue was caused less by poor discipline and avarice, and more by unfortunate but predictable C-suite blind spots.

A Warning for Manufacturers

Manufacturers well-versed in lean might have coached the executive team at Southwest on the importance of "going to the

Gemba

," being on the ground (or in the air) where the real work happens. A few weeks in the weeds any time in the last decade might have prompted leadership to say, "Hey, we have a problem here." There’s nothing like pain to motivate change, and it seems that the company’s pain was felt by everyone except upper management.

All of this may serve as a warning for manufacturers stuck in the past. Southwest’s systems worked for decades with relatively minor interruptions. It was likely easy to say, "We’ve been running this way for years. Why change?" Experienced manufacturers may look sideways at modern software and ask the same questions. The answer is that software can improve both customer experience and employee quality of life now and prepare the company for growth.

With so many moving pieces, personnel management and scheduling are problems naturally difficult for people to tackle manually, but comparably are simple for a computer. In Southwest’s case, the difficulty has been to match crew to aircraft manually, a process described by Southwest COO Andrew Watterson as "extraordinarily difficult," a "tedious and long process." Imagine if during the past two decades Southwest invested a fraction of its $12 billion in share buybacks into custom scheduling and planning software that could automate the process. It’s certainly not an easy problem. Replacing active software is like changing a tire on a moving car. But a billion dollars is a lot of money, and a decade is a long time.

Automating the Information Pipeline

The problem is a little different for most manufacturers. Few operate at the scale of an airline, so the stakes are lower, and not every manufacturer has the cash and expertise required to write custom software in-house. Even so, off-the-shelf software can help automate tedious and difficult tasks company wide.

Quoting stands out as a possible easy win for many shops. Lengthy and inconsistent quoting practices from our vendors led my brother Jacom and I to start OSH Cut, a high-mix, on-demand online metal manufacturing company. We wrote software to enable customers to obtain instant pricing and manufacturability feedback online.

That software has allowed our shop to scale with zero quoting or engineering office staff. We don’t sell software, but there are multiple software companies that provide similar automated quoting tools for fabricators. That availability means that virtually overnight, shops can finish more bids, more accurately, and faster than ever before.

With many shops already moving that direction, it’s going to become more important to modernize quoting tools to remain competitive. Customers are growing to expect rapid quotes. It’s possible that shops that fail to modernize quoting infrastructure will see a slow erosion of business as others improve quoting efficiency and take market share.

Operational efficiency is also an area where manufacturers can benefit from modern software tools. At OSH Cut, we began with paper travelers and work orders. That worked fine at low order volume, but keeping track of many in-process orders—with all their exceptions, deficits, and schedules—quickly became unwieldy. Production deficits caused by scrapped or missing parts required new laser jobs to be requeued, and jobs requiring multiple parts in different stages of production constantly changed status in the production pipeline.

To figure out whether a job might not ship on time, we’d thumb through a paper traveler, review the work order, confirm with the laser programmer that a deficit was requeued, discuss the job with the laser and brake operators, and then try to figure out how the order fit in the schedule with a bunch of other orders. After all that work, the situation would change 10 minutes later, and we’d have to start all over again. It was "extraordinarily difficult," a "tedious and long process."

We ended up writing custom software to fix this problem too. We call it the

pipeline

, and it keeps track of the number of parts in every stage of production, with automation prioritizing jobs in every stage based on production requirements and job due date.

There are companies that sell similar manufacturing resource planning (MRP) software specifically for fabricators. Shops that track production manually may benefit greatly, and virtually overnight, with the right off-the-shelf software. The result is better quality of life for shop workers, less confusion, fewer missed deadlines, and happier customers.

Scheduling, nesting, and job prep is another tedious job that benefits from automation. We had automated quoting software early on, but converting sales orders into manufacturing jobs was still time-consuming. It required downloading customer files from our servers, importing them into third-party nesting and laser programming software (which often failed), copying part quantity and deadline info, prepping flat patterns, fixing design issues, figuring out what materials we had in stock, and then deciding what jobs to nest together.

This workflow was harder to fix, because it involved lots of different software tools that might usually be isolated, or "siloed." A laser vendor might provide nesting software, but it may not integrate with a quoting front-end, inventory management software, or smart scheduling tools. Our solution was to implement software of our own (one piece at a time) to do all of it, including nesting and laser programming.

Our scheduling engine knows when orders are due, what we have in inventory, what we need to order, and the status of every production step. It uses that information to drive nesting decisions. The result is that the first time we see a job, it is already prepped, nested, scheduled, and ready for review and release.

Again, fabrication equipment vendors provide software with this kind of allinclusive automation either baked in or available after integration with a shop’s existing enterprise resource planning (ERP) software. Custom software allows for solutions tailored to your shop’s needs, but it’s expensive and time-consuming. It’s cheaper and nearly as effective to buy off-the-shelf when you can, and powerful software is becoming more readily available as its benefits become more obvious.

Choosing the right software is a big decision, and it’s worth taking your time. Modernizing too fast may expose manufacturers to new risks, and choosing the wrong off-the-shelf software tools could have huge implications. It’s hard to switch to new software once you’ve committed.

The good news is that there is plenty of time. I don’t think a dramatic Southwest-style meltdown is the most likely outcome for manufacturers intent on running business as usual. It’s quite the opposite, in fact. I think that aging shops are more likely to see a slow erosion of business as other shops improve efficiency and take market share. If that’s true, there’s plenty of time to modernize, one disciplined step at a time.

Trust the leaders in Dust and Fume Extraction

Superior performance.

Proper engineering. Sensible pricing.

Get your dust and fume extraction solutions from one of Canada’s most trusted manufacturers with over 30 years of experience.

Industrial Vacuums

Dust Collectors

Wet Collectors

Downdraft Tables

Fume Arms

Vac Ready Welding/Tools

Contact us for a quote

1-800-365-DUST (3878)

info@eurovac.com

www.eurovac.com

Missing Production Due Dates?

"We change the game

when other efforts fail to solve the persistent problem of missed due dates in high mix manufacturing environments. Our proven Dynamic Production Method (DPM) & Protected Flow Manufacturing™ (PFM) technology makes mastering on-time-delivery an achievable goal."

Download White Paper

For more information, or to request a demo, visit

www.lillyworks.com

or call 603-926-9696.

Alert. Recommend. Do.

Protected Flow Manufacturing helps you drastically improve on-time delivery by prioritizing what needs to happen first, not what’s due first.

lillyworks.com