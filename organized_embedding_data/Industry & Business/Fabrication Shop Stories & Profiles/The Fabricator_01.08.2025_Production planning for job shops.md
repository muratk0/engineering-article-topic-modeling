# Production planning for job shops

[TARİH: 01.08.2025 The Fabricator]

Part Flow

Custom metal fabricators are not Toyota—and that’s a good thing

By

Gary Conner

АВТОр / iSTOCK / Getty Images Plus

I

’ve worked on lean manufacturing initiatives at more than 300 companies, most of them job shops, and over the years I’ve heard a familiar refrain:

We are not Toyota

. My response is: "Good! That would be boring!"

Many job shops have studied the Toyota production system. They appreciate its benefits but also question the applicability of one-piece flow in a high-mix, low-volume environment. And rightly so.

I count about 150 tools and techniques in what has evolved into a set of continuous improvement processes universally titled "lean manufacturing." One tool is value stream mapping (VSM), which aims to create a visual representation of a product or service flow. It identifies where

value

is being generated and where energy, labor, material, or any other resource is being expended without any value being generated. Waste in all its forms can be more easily identified (and then eliminated) with VSM.

Toyota manager Taiichi Ohno and engineer Shigeo Shingo identified seven primary forms of waste: transportation, overproduction, motion, overprocessing, waiting, defects, and excess inventory. VSM helps visualize where and when various forms of waste are generated.

Because of the nearly unlimited number of customers, product types, and part complexities found within a job shop, applying traditional tools like

kanban

(make or move signals) and

takt

time (manufacturing rhythm) can be difficult. Similar challenges apply to VSM.

Toyota makes a limited number of models of a single product type (automobiles). In contrast, a job shop might manufacture medical products, aerospace components, transportation equipment, and one-of-a-kind agricultural products all at the same time. To further complicate the process, make-to-order shops often act as research and development for their customers, helping to develop manufacturable designs for components that may never see a repeat order.

The differences between job shops and OEMs are obvious and significant, and they require a significantly different set of VSM tools.

A Review of the Lean Toolbox

First, let’s review several principle tools in the lean manufacturing toolbox. First is the

product-quantity-routing (PQR) analysis

, which basically answers the following question: "What do we make, how many do we make, and what processes are required to make it?"

Takt

time defines how often a product, unit, or service is required by your process, like producing one product every minute. In a job shop, of course, all products can have different processing times, and the

takt

time calculations need to account for this fact (more on this later).

Both the PQR and

takt

time analysis help build the VSM, long used in OEM environments. The challenge is to have a flexible, dynamic method that job shops can use when the workload changes by the day, sometimes by the hour.

Another lean tool is

line balancing

. This was first used in the automotive industry by Henry Ford, who had the luxury of making one type of product that allowed work to be divided equally among the appropriate number of workers. Line balancing is much more complex in a job shop, but it’s not impossible. I will demonstrate how a dynamic planning tool can help you know exactly how many operators are needed and where they are needed, in real time.

Standard work

is the result of line balancing. Each operator needs to know clearly what their assignment is during each

takt

time (manufacturing cycle). This is difficult to do using traditional VSM because most mapping methods are static. Job shop workers need a flexible, easy-to-use, dynamic tool for planning their day.

All this helps build an optimal

facility layout

, which is crucial to maintaining a flexible workforce and environment. People need to be able to quickly move to the work when the workload moves from one process to another.

A Deep Dive Into the PQR

Creating a PQR analysis is the first step in transforming a value stream. Knowing what you make, how many, and how you make them will determine all aspects of your VSM. You cannot identify

takt

time or standard work without knowing how the product is processed through your facility.

Imagine you work for Henry Ford and you need to produce 100 Model As. The Model A is the product (P); 100 is the quantity (Q). Pretty simple so far. The routing (R, or required processes) is a little more complicated. A highly simplified PQR chart for Ford’s production plan might look like

Figure 1.

The time required to assemble the frame, engine, and so forth will be gathered during the value stream observation. For now, it is just important to identify the required process steps.

The Model A will always require an engine, transmission, and body panels. Parts made in job shops may not require or use all the same processes. Some processes may run only occasionally for special jobs, yet the team still needs access to them.

Imagine you work in a sheet metal job shop that, for the sake of simplicity, makes only two products.

Figure 2

shows two different process routings. Part 1 requires welding; Part 2 doesn’t. Part 2 requires shearing and painting while Part 1 doesn’t.

Flow is not consistent. While this example shows the mix as 50%-50%, tomorrow the mix might be 80%-20%. This makes it hard to plan where the labor should be distributed and where equipment should be positioned to minimize distance traveled, motion, and waiting.

FIGURE 1 Highly oversimplified, these are the process steps required to make a Ford Model A.

FIGURE 2 This product-quantity-routing (PQR) analysis shows a hypothetical job shop that produces only two parts.

A traditional materials resource planning (MRP) system struggles with developing a daily or hourly production plan that fosters flow because those systems are designed, built, and sold on the premise that material will be batched among departments or processes. That concept worked for decades in departmentalized facility layouts designed for OEMs that build countless copies of the same product year after year. But companies interested in adopting flow in a flexible, lean-focused factory will need a much more flexible and dynamic tool.

FIGURE 3 This simple PQR analysis details the time each process requires to produce two parts.

FIGURE 4 This shows the number of operators required at each process to maintain the established

takt

time.

Finding Rhythm

Think about

takt

time as a heartbeat. Our heartbeat is based on our level of activity (demand).

Takt

time is the same, and it has a simple formula to determine it: available time divided by demand. Henry Ford could calculate

takt

very easily. If he wanted to produce 100 cars during each eight-hour (or 480-minute) shift, he’d simply divide 480 minutes (available time) by 100 (demand) to get 4.8. That shows he’d need to produce a vehicle every 4.8 minutes. Why is it important to know the

takt

time? Because Henry Ford had to determine how many people he needed to produce his vehicles.

To be clear, even this simple example has other considerations. People take breaks, and they need to eat lunch. Studies show that people are about 85% effective with their time, so a 480-minute day really has only about 408 minutes of "truly" available time. This would give us the following: 408/100 = 4.08. So, the true

takt

time is closer to four minutes per vehicle rather than 4.8.

We use a simple calculation to determine the ideal number of operators for any process: operator cycle time divided by

takt

time, or OCT/TT. Let’s imagine that one person building a car alone would require 50 hours (3,000 minutes). Here, we’d divide the OCT of 3,000 minutes by the

takt

time of 4.08 minutes. This gives us 735, the minimum number of operators we need to build a car every 4.08 minutes.

Henry Ford would have to hire at least 735 people and then make sure each person was assigned four minutes of work. If the process of installing an engine required 20 minutes of labor, then five people (20 OCT/4 TT) would need to be assigned to that operation to maintain the flow of vehicles. This is the essence of line balancing.

Takt

time within Henry Ford’s business is based on only two variables: available time and demand. Job shops and other make-to-order operations must add another variable:

complexity

. A Model A might have slight variations, but for the most part, a car is a car is a car. In the job shop world, the complexity of one work order may require 10 times the labor of the workorder ahead of it. This can create a huge imbalance in the labor content or machine requirement (run-time).

Figure 2 shows (by an X) that a particular process is required and thus shows the routing.

Figure 3

replaces X with a time value. This information helps identify bottlenecks or any process that might have unused capacity. Our quantity is 100, and we’re using the same eight-hour day (408 minutes) that we calculated for Henry Ford. In this case, our

takt

time also is 4.08 minutes per unit.

To determine the number of operators required, we again divide operator cycle time by the

takt

time (OCT/TT). In this example, the total OCT is 18.5 minutes. We divide this by the

takt

time of 4.08 minutes to get 4.53. This gives us the total number of people we need to maintain flow.

Next, we need to answer another important question:

How many people do we need at each process?

Figure 4

adds a row at the bottom showing the number of operators required at each process. Shearing is a very small requirement, so it doesn’t require a full-time operator. Here, we might consider assigning the punch operator, who has only a 75% workload, to the shear operation as well. We also will need two forming operators working on two press brakes. If we have only one press brake available, then we might need a second shift.

You can imagine how complicated this PQR analysis could become when a company has 2,000 or 3,000 unique part numbers. (Hold that thought. We’ll soon get to a way we can handle all that complexity.)

A Hybrid Approach

Make-to-order operations must deal with enormous variability in part complexity. This has been the overwhelming reason many job shops throw up their hands and utter those famous words:

We are not Toyota

. Takt

time does not work here because we never know what the workload or demand will be.

I try to be empathetic, but I started my career working in a sheet metal job shop. During my years as a lean manufacturing consultant, I knew there were solutions to clients’ problems, and I had an obligation to help them solve them.

FIGURE 5 Four part types are grouped together into one product family for a specific value stream.

Takt

times are calculated by using weighted average work units, not sales units.

I’ve worked on lean manufacturing initiatives at more than 300 companies, most of them job shops, and over the years I’ve heard a familiar refrain: We are not Toyota. My response is: "Good! That would be boring!"

To do it, I used

weighted average

takt

and operator cycle times

. Discovering this was the tipping point for the sheet metal job shop I grew up in, and it worked for 100% of the clients I served while facilitating more than 1,500

kaizen

events. The idea sounds complex, but it all hinges on a simple concept: Find a common denominator.

Engineers, who generally think in numbers, want a perfect solution to a math problem. They do not like estimates or averages. But we must first acknowledge that no make-to-order environment can ever have a perfectly calculated

takt

time or labor content associated with a given set of random products. The best we can hope for is an accurate weighted average.

Consider a company that makes hospital beds, dishwashers, and vending machines. If the products all share operators and equipment, the level of complexity is enormous. Say the company needs to make 10 of each product in a given workday of eight hours, or 408 minutes—which, considering breaks and lunch, gives us a realistic amount of time available for operators to work. Ten hospital beds, 10 dishwashers, and 10 vending machines gives us 30 units. The required

takt

time over an eight-hour day would be 13.6 minutes per unit sold (408 divided by 30).

But alas, it’s not that simple, because the labor content is different. The hospital bed requires one hour of labor, the dishwasher requires three hours, and the vending machine requires seven hours. To produce one bed, one dishwasher, and one vending machine takes 11 hours (1 + 3 + 7). Repeating that 10 times gives us 110 hours. If it takes 110 hours to produce 30 units of mixed sales (10 dishwashers, 10 vending machines, and 10 hospital beds), that’s equivalent to the labor content needed to make 110 hospital beds—each of which takes just one hour of labor to produce.

Here, the hospital bed is our common denominator to develop a realistic

takt

time. By dividing 408 minutes by 110 (rather than 30), we get 3.71 minutes

per work unit

—not per sales unit. Because a vending machine requires seven times the labor of a hospital bed (one hour versus seven hours), the operators would be allowed seven times that 3.71-minute

takt

time, or 25.9 minutes (3.71 × 7) to produce one vending machine.

Identify Product or Part Types

Of course, the typical job shop makes hundreds or even thousands of different products. How on earth can you develop a

takt

time that accounts for all of them?

Here’s where the part type comes into play. Most sheet metal job shops produce a mix of products that share certain attributes. These could center on workpiece size or geometry, the end product (enclosures, for example), or another job characteristic.

A high-level PQR analysis can simplify the process by "dividing and conquering." Since most companies are set up in process-centric areas (cutting department, bending department, etc.), many find it difficult to think about value stream alignment rather than departmental alignment. I sometimes ask, "If you were forced to move from this building into three smaller buildings, how would you divide the work?" That usually gets at the answer of how many value streams they really have.

At this point, we are only looking for a thumbnail sketch of the product mix. Once we begin mapping the value stream and performing real-time observations, we will acquire more precise values. In the absence of hard data, I rely on expert opinion. It is remarkable how accurate experts are at estimating the relative complexities of their product families. Once you divide the company’s entire sales mix into logical product families (value streams), you can start working on developing your

takt

times.

Let’s say you’ve identified four part types that you’re grouping into one product family. We will assume that these components are a set of parts (kits) used in an assembly. We could perform this same analysis on every component, but in the interest of simplicity, we will study them as kits.

Figure 5

shows the completed analysis. It probably looks cryptic at this point, so let’s walk through the process step by step.

Again, we’ve identified our four different product types—Part Type ABC, XYZ, etc., in the table—that together use three different materials: aluminum, mild steel, and stainless. First, we estimate the complexity of processing each material type. This value could be expressed in how many hours are necessary to process the average type of product or simply a numeric value on a scale of one to five. For the rest of this example, we will use the simple numeric values shown in Figure 5.

As shown in the figure, aluminum products are given a complexity score of one while stainless steel has a score of five. Put another way, products made of aluminum are estimated to be 80% less complex than stainless steel. Here, we’ll use aluminum products as a common denominator equal to one unit of work. Stainless products require five times the effort or labor.

Populating the table with the day’s sales projections, we can determine the true labor requirement for 17 units sold. When we multiply the ABC mild steel kit of parts by three work unit equivalents, we get nine work units. When we add Part Type XYZ with two aluminum components (two parts × one work unit equivalent) and two stainless steel components (two parts × five work unit equivalents), we get 12 work unit equivalents. When we add up all the work unit equivalents for our four kits, we get 43. So, the mix of products (four part-type kits, in this case) that total 17 sales units gives us a weighted average work-unit equivalent of 43.

To uncover the production rates we need to maintain to ship 17 units a day, we first determine the available minutes per eight-hour shift. Again, eight hours is 480 minutes, but to account for breaks, we assume only 408 minutes are available. To uncover the

takt

time, we divide 408 minutes of available time by 43 work unit equivalents to get 9.5 minutes.

FIGURE 6 Here, we changed the demand (now, it’s all aluminum parts), and the rest of the chart recalculates the resources you need.

That 9.5-minute

takt

time applies to one kit of aluminum components, our common denominator. When we produce a stainless kit, the manufacturing team would have five times the baseline

takt

to produce it (9.5 × 5 = 47 minutes).

Next, we generate a flowchart identifying all the processes required to manufacture the product. Again, we’re simplifying the example with only two processes, cut and weld—shown by the final two columns in Figure 5.

If we assume every component gets every process, we will either over- or underestimate the labor content—hence the importance of the "precent required" columns in Figure 5. Notice that Part Type ABC made of mild steel requires cutting only 50% of the time, but Part Type XYZ requires cutting 100% of the time. This is another significant distinction between OEMs and make-to-order shops. At Ford Motor Co., every car gets an engine, doors, and seats. In the job shop world, material often goes around a process without any need for it.

Next, we go to the shop floor (or use historical data) to add operator cycle times to the table. Real-time observations are preferred because later we will capture setup data, machine cycle time data, and yield information as well. For this example, we will just focus on the operator.

You’ll notice in Figure 5 that the four different part types have different process-time requirements. That’s the result of multiplying OCT by the percent of parts requiring the process. For example, one minute of OCT at a 50% usage requirement is 0.5 minute, or 30 seconds.

When the OCT values (multiplied by the percent required) are added together, we get 11 minutes. This is our grand weighted average, because it is based on the percentage of sales, the complexity, the percentage utilized, and the average OCT. This value divided by

takt

time provides an ideal number of operators for each process. As shown in Figure 5 at the bottom, this particular product mix will require 1.2 operators cutting and 1.3 operators welding.

All this might seem like a lot of work, but keep this in mind: Now that the table is built, just a few small changes can provide you a real-time production planning tool. Being able to categorize any part as a Type ABC, 123, or XYZ can allow you to plan your day quickly and allocate labor purposefully instead of just guessing at it.

Notice in

Figure 6

, no other changes were made except the demand quantities. In this example, all the products are aluminum, and the quantities required for each product type are consistent. You can see immediately that now

only one person

is required at each process.

FIGURE 7 This linearity chart can show operators how many units should be processed at a certain time during a shift.

Tracking Progress

On a linearity chart, the team can plot their output and identify whether they are on the correct pace or not (see

Figure 7

). Anyone can walk by and check the linearity chart to see where they are in the schedule.

If operators are not on track, they can communicate those discrepancies. You then make appropriate changes with improvements to the

takt

time calculation, the process itself, or a combination of both. This all happens in conjunction with observation and actual cycle time measurement.

You probably know the adage:

You can’t improve what you don’t measure

. The job shop environment, however, involves so much variability that you can spend an entire career measuring and end up not changing anything—a classic case of analysis paralysis.

Again, experts on the floor can help. They can help you establish ballpark numbers that allow you to jumpstart your production planning. Once you implement it, you can continue your operator observations and actual cycle time measurements. In other words, don’t worry about absolute accuracy; you can perfect the numbers over time.

A Powerful Planning Tool

Note that how you apply this planning method really depends on your product mix. In some cases, job shops build a VSM based on every distinct part number. Other times, teams identify four or five product routing types and quickly determine the type of each daily (or weekly) job being released in the production process. They then populate the table and distribute labor according to the resulting calculations.

Regardless, this production planning tool has been a tipping point for hundreds of job shops and other high-product-mix operations. They use a simple spreadsheet to schedule their jobs, sometimes importing MRP data to populate the daily demand.

Day-to-day planning in a make-to-order environment often is better managed using a hybrid

takt

time and realistic labor content based on weighted averages. Again, it takes time to build the spreadsheet, but once it is created, it can save hours a day trying to run different production models in your head—which often leads to guessing wrong and falling short of the true production requirement.

Gary Conner

is an author, independent consultant, and two-time recipient of the Shingo Prize,

lean1mfg@gmail.com

. If you’re interested in obtaining a fully functional and editable version of the Excel spreadsheet discussed in this article, you can email

Tim Heston

at

theston@fmamfg.org

.

by BRADY

Make Marks with Meaning

Innovative solutions for world-class engraving, marking and cutting.

gravotech.us.com