# ERP and the (Very) Small Shop

[TARİH: 01.03.2015 The Fabricator]

Chief Concerns

5 questions to ask before you upgrade

By Dave Lechleitner

I

f you’re reading this, there’s a very good chance you work at a small fab shop—perhaps a very small one. In other industries, a company with about 50 employees might be considered "small," but in metal fabrication and similar sectors, a typical "small" shop is actually much smaller. Job shops with a dozen or even fewer employees dot the country, and in aggregate, they make up a large portion of all the metal fabrication done in North America.

For decades now large OEMs and their top-tier suppliers have used enterprise resource planning (ERP) platforms to help streamline their operations and improve their efficiency. The small shop, though, has had a different story. For years many have run not on an integrated ERP platform, but instead on homegrown systems, often based on Microsoft Excel

®

, Access

®

, or similar programs, and a completely separate accounting program. Other shops may have a shop management program that’s extremely old, perhaps dating back to the days of MS-DOS.

With all these hurdles, small shops (and even a few larger ones) tend to shy away from ERP, thinking that making the transition is just too big of a task, more trouble than it’s worth. In addition, the transition isn’t always without its challenges. Today, however, making the upgrade usually isn’t as challenging as it used to be, especially considering some of the cloud-based platforms available. For a small shop, cloud-based systems might be very attractive, because they don’t require full-time IT resources or a costly infrastructure.

Of course, no matter how easy upgrading to and managing the new software may be, you should start your upgrade by asking the right questions.

1. What Data Do We Want to Migrate?

Before migrating your data to the new ERP system, first analyze what data you want to transfer. Reaching consensus here among your managers, supervisors, and employees can be critical. What is the real value of your historical data, and what do you need to migrate to the new system? Many often have a knee-jerk reaction and say they need every bit of data gathered over the past few decades.

Early in the process, when you’re evaluating your ERP options, meet with members of your team to determine the real value of your legacy data. If you have a large amount of legacy data organized and input in an unusual way, a new ERP platform needs to be built around those constraints effectively to mirror how you’ve used the data in the past. This can work fine in some cases, but in other cases it can limit a new ERP system’s more robust functions.

For instance, in the past you may have defined job routings a certain way, with every machine in the shop being a unique work center. Many newer ERP systems, though, also can use workcells—that is, it views a group of machines as an individual "work center." The bending department may have five press brakes, all very similar but each slightly different in their capabilities. For this reason, you may want the ERP system to view these machines as one "workcell," simply because 80 percent of the time it doesn’t matter which press a part needs to run on. New ERP scheduling algorithms can identify the preferred machine, but it also can name alternative machines in the workcell, depending on the current machine work load. For a job shop, this kind of flexibility can be extremely valuable.

Setting up your ERP to run this way can be straightforward, but again, if legacy data is built in an entirely different way, things can get complicated. Deciding which data points you really need can save a lot of time and headaches down the road.

Try categorizing your legacy in three ways: (1) data that absolutely needs to be in the new ERP platform, (2) data that would be nice to have, and (3) data that’s not needed at all.

Start with No. 3, which is usually the easiest. Right off the bat, you can eliminate the data that’s redundant, obsolete, or trivial. Next, tackle the information for those long-ago small jobs, such as a one-off that you fabricated five years ago and aren’t likely to see again. In the off chance the order does come up again, it wouldn’t take you long to re-create it. Next, move to No. 2, the nice-to-have data. This can include detailed transactional details, such as conversation records between the customer and client that may not relate directly to the job.

Finally, move to No. 1, the critical information. This includes basic job histories: the customer, the order date and job number, quantity, ship date, as well as details relating to price (revenue) and costs. It may also include more details for work from your core customers and long-term contracts, such as pricing and delivery agreements.

Ultimately, you need to ask yourself, What is the minimum amount of data I need to run my business? That answer depends on your situation and customer base. You may consider a small, old job something that is nice to have or not necessary at all, while another shop owner might consider it absolutely critical for the business. Regardless, asking these questions helps you draw your data-migration roadmap; without that roadmap, it’s easy to get lost.

2. What Tools Can Help the Data Migration?

Once you decide on what data to migrate, now you will have to determine (probably with the help of your software vendor) how to migrate the data. If you need to transfer data in a raw format that’s not directly readable by the new ERP platform, you can export legacy data in comma separated values (CSV) format. Exporting information into a CSV template your new ERP system vendor provides is a common strategy for shops that have used Excel in the past.

This method does require some time to analyze and map, because CSV does not understand data hierarchy. Work orders, bills of material (BOMs), inventory locations, and the like are all exported as simple data points, so they have to be connected, or mapped, to show how each relates: this BOM to

that

work order to that inventory location. This usually requires someone to spend some time poring over data.

Asking the right questions helps you draw your datamigration roadmap; without that roadmap, it’s easy to get lost.

In recent years, though, new ways of migrating data have emerged, one of which is XML (Extensible Markup Language). Let’s take a look at a seemingly simple example. Say you try to migrate a list of customer addresses—some of which are invoice-only addresses, while others are shipping-only addresses— and within those addresses you have contacts that are associated with each address. Using CSV, you’d have to map each of those fields, instructing how each relates to the other, and fill in the gaps where necessary. Because CSV files don’t have information related in a data hierarchy, each set of data needs to be imported one at a time.

XML helps connect these missing links and clean up old data faster by applying business logic to fill in the blanks. Your ERP vendor can use standard XML templates that help migrate your data from any number of legacy formats.

Once the information reaches your new ERP platform, many systems now have intuitive find-and-replace functions to fill in the gaps and clean up your old data with consistent verbiage and item numbers. Certain platforms also can help eliminate and consolidate duplicative information (or "de-dupe"), such as item numbers that may have been input various ways over the years in the legacy system.

Of course, you may have implemented a system a long time ago—during the DOS era. Data in these systems can indeed be exported into CSV, though it’s not always a straightforward process, depending on how the software was written. Some old systems were written with proprietary databases (using COBOL or other legacy programming languages), and tools still are available that actually allow you to export that old data to CSV. This isn’t too arduous, but it does add another layer of complexity. In these cases, deciding which data points you need to migrate over is critical.

In rare cases, you may have a homegrown system that involves data that just can’t be exported or a database that has been "locked down" by the previous developer. So if you do upgrade, you may need to start with some manual data entry for critical accounts. Is it worth transitioning to the new system? In this case, you need to weigh the pros and cons. How much benefit will a new system give you, versus sticking with what you’ve got? If the legacy system is causing problems, the longer you wait to upgrade, the more data history you’ll have in your "data-locked" shop management system.

3. Does a Cloud-based ERP Platform Make Sense for Me?

Cloud-based systems and Software as a Service (Saas) have taken off in recent years. As Internet infrastructure improves, including its speed and uptime, ERP platforms that use data warehouses to manage both the ERP program and the data begin to make more sense. It also means that small operations need not invest in a server, network, high-powered client workstations, or the people to manage them.

Data security still continues to be a concern, but it turns out that information stored on data centers is probably more secure than data stored on local servers, which can be wiped out virtually by hackers or destroyed physically by a natural disaster. Cloud-based computing stores data at multiple sites, which have resources and redundancies to keep the servers on and running should a disaster strike.

On the other hand, cloud computing presents a wrinkle of complexity, particularly if you do work for customers with supplier-country-of-origin requirements. You may need to make sure that your cloud-based ERP provider has data centers in the United States and that it’s staffed by U.S. citizens.

This requirement can open up a gray area in certain circumstances, because some data centers operate in multiple countries. When you save to the cloud, data may be stored and backed up in data centers in the southeast U.S., as well as in Europe or elsewhere. Such arrangements work wonders for data security and service reliability, but they may present regulatory hurdles. The key is knowing to ask these questions from the get-go.

To deal with these issues in the years to come, some vendors may choose to allow their clients to deploy an ERP platform on a "private cloud." Instead of using all the data processing servers at a center for all clients, a private cloud has within the data center a designated server dedicated to one client, and the client takes on more responsibility for managing it. It isn’t in wide use yet, but down the road the private cloud could give manufacturers the benefit of using the security built into a large data center, while also meeting country-of-origin requirements to work with their customers.

4. Can the ERP Platform Support Our Job Shop?

OEMs and other manufacturers with set product lines operate efficiently in part because they minimize variability. If they’ve implemented components of lean manufacturing, they may have reorganized their shop floors into value streams and workcells dedicated to certain product lines that have fairly predictable demand levels, at least in comparison to the components made at a job shop.

Small job shops can be as individual as the people running them. They have their own way of doing things, which is why, if they have adopted an ERP system in the past that didn’t fit their manufacturing model, they may not have used all of its functions. This is particularly true for shop floor scheduling, which at small job shops can be intuitive for a manager who has run things for decades—but it may be difficult to mirror in an ERP system, depending on its functionality.

All the same, shops may benefit from finite capacity scheduling, or scheduling with multiple constraints. In fact, getting a handle on scheduling may be one reason that you want to upgrade your ERP system, to improve your on-timedelivery metric. Your on-time delivery may struggle for various reasons, and one may be measuring your actual available capacity, which isn’t that simple in a high-product-mix situation in which machine cycle times vary greatly from job to job.

Here, cloud-based ERPs are following Apple’s lead, with the use of apps. The iPhone

®

is a great phone, but it wouldn’t be what it is today without its app store. Today cloud-based ERP systems have the same potential. The core ERP platform may come with basic scheduling, but to expand the functionality, you can choose a scheduling app add-on that offers features very specific to your manufacturing model, like finite capacity scheduling.

Small job shops can be as individual as the people running them.

For this to work, the app and the app partner require careful vetting and quality control from the ERP vendor. App stores from Apple and Google have thousands of apps, so these companies have elaborate app partner programs to fully vet and test each application. In the ERP world, the ERP vendor is likely to have a more limited approach and may accept only so many apps to ensure the quality and performance of each app. Your Facebook app crashing on your phone is just an annoyance; your ERP’s scheduling app crashing is something else entirely.

Regardless, the cloud makes it much easier to adapt these third-party programs to ERP platforms. It also makes these platforms scalable, from the small fab shop to the large contract fabricator.

5. Does My Small Shop Really Need a New ERP Platform?

Some small shops have worked with only basic shop management systems for decades. In fact, many have survived just fine and have indeed run very efficient operations using Excel. So why upgrade? "Outgrowing Excel" is a common phrase in this business. But if you run a small operation, growth may not be your goal. You may have a dozen employees, and if you keep the business small, you keep things simpler—at least that’s the idea.

Your goals for the business, your customers, and the depth and breadth of your market demands play into the equation here. Your core customers may demand better on-time delivery and shorter lead times. An ERP upgrade may allow you to quote faster and streamline order processing, with deeper integration among sales, order processing, and the shop floor. Order generation and even scheduling can become more automated. With a better system, you may spend less time chasing the eight ball—selling, quoting, and processing orders—and more time improving the overall business.

You may already have good on-time delivery and short lead times, and so just want to become more efficient so you can work less. Will this happen with a new ERP platform? Quite often it does, but it really depends on your situation as well as your wants and needs. As with anything, you need to weigh the costs and benefits in terms of both the time and money spent adopting and transitioning to a new system.

Dave Lechleitner is chair of the Software Technology Council at the Fabricators & Manufacturers Association International and principal, product marketing, at Exact Online, 260 Charles St., Waltham, MA 02453, 855-359-9256,

www.exactonline.com

. For more on FMA’s technology councils, visit

www.fmanet.org/technology-councils

, or call 888-394-4362.