# Should you top off the sheet?

[TARİH: 01.02.2023 The Fabricator]

Tech Talk

Maybe, but is it worth the wasted capacity?

By

Caleb Chamberlain

I

t’s great to know whether equipment is running, or why it isn’t. Most modern machines provide telemetry to indicate what they are doing at every moment. If you pair telemetry with software dashboards, cloud-connected equipment provides a wealth of insight into what happens on the shop floor. But even then, there is often one missing piece to the puzzle: It’s great to know that equipment is running, but it’s just as important to know whether it is generating value.

For example, here’s a nesting quandary for you. The nest shown in

Figure 1

has just enough room to add two more parts, but the work order doesn’t require that many. There are no other open orders requiring the material, no available filler parts, and no finished-goods inventory to produce. The customer may be willing to increase the quantity to top off the sheet, but with hundreds of other orders in the queue, there isn’t a lot of time to spare. Would you add two more parts to fill out the sheet?

The part only takes 15 seconds to cut, and all that area is just going to be scrapped anyway. Why not avoid the waste? If one part fails, there is no need to queue up a replacement. If not, the customer gets an extra part or two.

At our shop, that was the rationale for a while. It seemed such a shame to waste space on a sheet, so we’d top off one sheet, fill gaps in another with small parts, and even proactively cut extra on challenging jobs where we expected attrition. It felt good to use the full sheet, and customers were often delighted to receive extra parts. Meanwhile, we wasted less material and slightly reduced the need to requeue failed parts.

What we failed to realize was that the true cost wasn’t necessarily the material, the labor time, or the cost of running the equipment. The true cost was

wasted capacity

. One or two extras in a thousand-part order might not matter, but across hundreds of smaller orders in a week, that extra time added up.

That became immediately obvious when we started tracking not just laser ontime but

billed

laser time. We built a system that categorizes laser time based on outcomes:

this percentage

of parts cut today were shipped,

this many

were scrapped,

this many

were excess, and so on. The result was enlightening.

Figure 2

shows just how dramatically those extra parts soaked up laser time on some days. As much as 10% of available laser time in a shiftwas sometimes spent cutting parts that weren’t producing revenue. It’s possible to put a number on the actual cost of that laser time, in terms of labor, depreciation, gas usage, electricity, and material cost. Those figures matter, but they pale in comparison to the opportunity cost of working for free.

FIGURE 1 This nesting job has just enough room for two more parts.

FIGURE 2 We charted laser time as a percentage of available capacity, showing what happened to parts cut each day. The graph shows percent excess, scrapped, and shipped parts. It also shows the percentage of parts that were still in-process when the graph was created. This is a sample plot for illustrative purposes, but it roughly matches outcomes at our shop in 2021.

FIGURE 3 We charted material usage by month for 0.188-in.-thick 304 stainless steel, along with the min/max inventory levels that were configured automatically by our inventory systems.

On average, each of our lasers produces around $3,000 per hour of active operation. Sometimes it’s higher, sometimes it’s lower; it all depends on the product mix each month. That $3,000 figure incorporates all downstream revenue enabled by laser cutting, including material, bending, tapping, and powder coating. Based on that figure, we sometimes wasted nearly $5,000 of revenue capacity in a single eight-hour shift—simply by cutting extra parts.

The fix was simple. We asked our operators to stop adding extra parts, even if there was room for them. Yes, that’s sometimes a hard sell. Ignoring that one perfect spot for that one extra part is enough to drive meticulous operators crazy. It’s often the right decision anyway. Adding extra parts seemed innocuous enough, but it cost us a lot in wasted capacity. Classifying machine time as billed or waste enabled us to immediately reclaim as much as 10% of our laser capacity on some days.

As a result, we saw a minor decrease in cost of goods sold and a trivial increase in scrap sales. The long-term impact was more notable: We were able to drive more revenue through existing equipment before adding personnel, shop space, and new equipment. In a capital-intensive operation, that matters.

This lesson may or may not apply in shops with different product mixes and sales strategies. A few extra parts in 10,000 probably aren’t going to matter, and a shop that carries finished inventory has more flexibility, since extra parts will be sold eventually.

Savvy fabricators may also look at Figure 2 and see even more time to reclaim. Generally, time lost to excess parts is minor in comparison to time lost to laser downtime. That’s an excellent point, and one we’ll discuss at length in a future article. The biggest takeaway is that we were able to reclaim time lost to excess parts literally overnight, once we understood the scope of the problem.

We still have room to apply this kind of analysis in other ways. Suppose we were to consider the impact of sheet cuts or even slug-destructs? The laser time that truly produces value is the time required to cut the part profile. Sheet cuts and slug-destruct profiles help other downstream operations, but they also represent opportunity cost. At our shop, a slug-destruct profile that adds 10% more laser time costs $500 in opportunity cost per hour of operation. So instead, we use microjoints and plan on higher downstream labor for denesting, for a net improvement in efficiency.

Using microjoints instead of slug-destruct increases capacity at the expense of higher denesting labor. That only makes sense if there’s enough work to take advantage of improved machine capacity. If there is time to spare, slugdestruct might be the better option.

Inventory Management

In our early years, our raw material buying strategy was ad hoc and unplanned. If we found that we needed more material for a job, we’d order what was needed plus a little more that we’d keep on-hand. It was off the cuff, based on our personal perception of what our most-used materials were.

As we grew and added materials, that process became inefficient. Improper recordkeeping and controls meant that we sometimes double-ordered without realizing it, or ordered the wrong amount, or submitted a purchase order (PO) too late to fill an order on time. Meanwhile, the amount of cash tied up in inventory kept growing and growing. The situation produced an ironic combination of inefficiencies: Orders often shipped late because we had too much of the wrong kind of inventory.

Experienced fabricators might correctly point out that these are basic mistakes, easily solved with simple procedures. I agree! In our case, we implemented software to track and automate inventory management and purchasing. Collecting data about material usage allowed us to set minimum and maximum inventory levels automatically based on historical usage, automated scheduling and nesting processes allowed purchasing systems to adapt to changing demand, and automated PO generation took demand and min/max levels into account when creating POs for review (see

Figure 3

).

Setting min/max inventory levels based on historical usage, and then purchasing based on those targets, allowed us to reduce raw material inventory by more than 25%. Meanwhile, the number of orders shipping late due to missing materials dropped dramatically. This represented a win for cash flow and efficiency, and a win for customers.

What Does the Future Hold?

Good information, made available at the right time, can improve any business process. When we optimize inventory and nesting strategies with data, we improve cash flow and on-time delivery, and we make more efficient use of labor and expensive equipment. Collectively, these kinds of data-enabled optimizations improve the bottom line in a real and measurable way.

For shops not already taking advantage, most of these optimizations are imminently accessible. Raw inventory and PO management should be available in any manufacturingoriented ERP system worth its salt. Similarly, most modern equipment provides telemetry, or can be retrofitted to do so. It can be more difficult to determine automatically whether machine on-time corresponds to actual value (yes, the laser is cutting, but are we billing for it?). Instead, ensuring that equipment is generating revenue when it operates can be handled with good training and process management, even if data collection isn’t automated.

In the end, a connected shop can use data in myriad ways. Once you have the data, opportunities abound. I expect that new tools will emerge to help turn the mass of available data into actionable business intelligence. I can’t wait to see where it goes!

Caleb Chamberlain

is CEO and co-founder of OSH Cut, 165 N. 1330 W #C4, Orem, UT 84057, 801-850-7584,

www.oshcut.com

.

For more content from

Caleb Chamberlain

, visit

www.thefabricator.com/author/caleb-chamberlain

.

Turn-Key Batch & Automated Coating Systems

Finishing Systems

888-770-0021

reliantfinishingsystems.com

Porta Press

www.portapress.com

Toll Free: 1-800-668-4996 Email:

sales@punchtools.com

Your Neighbour in the North!

4 ROLL HYDRAULIC DOUBLE PINCH PLATE BENDING MACHINES

REAL WORK HORSES

FROM TENNESSEE • MADE IN USA

The 403 Series from WDM.

Over 40 years of experience with 3 generations working in the business.

Built in USA with American and global components.

30 gauge to 3″ thick, 1′ to 26′ wide.

Custom and built to order options available.

We are a dedicated business specializing in customer service and lasting customer relations.

From complete custom forming cells to many popular/standard machines In stock.

Waldemar Design & Machine LLC

900 Highland Drive

Spencer, TN 38585

931-946-8474, or 606-787-8474

Contact us direct, or contact your favorite machine tool distributor and ask about WDM Machine Tools.

3 & 4 Roll Hydraulic Double Pinch Plate Bending Machines • Initial Pinch Sheet & Plate Bending Rolls Cone Rolling Machines • Bending Systems & Complete Forming Cells