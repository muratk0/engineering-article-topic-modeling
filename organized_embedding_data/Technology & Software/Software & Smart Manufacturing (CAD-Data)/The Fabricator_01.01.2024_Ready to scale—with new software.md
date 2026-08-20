# Ready to scale—with new software

[TARİH: 01.01.2024 The Fabricator]

Tech Talk

Custom software can be both a blessing and a curse

Caleb Chamberlain

W

e’ve been working hard to overhaul our production management, inventory, and shipping systems. We launched OSH Cut as an online, on-demand sheet metal and tube cutting service five years ago. And from the start, we decided we’d write our own software instead of integrating with off-the-shelf ERP software.

That decision has proved both a blessing and a curse. On one hand, we’ve been able to build "perfect" software that fits narrowly and specifically to our own workflows. Because our software was written by us, for us, we’ve eliminated friction that plagues more generalized software.

On the other hand, the narrow scope of our in-house software has made it difficult to grow beyond our initial value offering. For example, we designed our production routing and shipping systems to support a very specific workflow: on-demand orders placed online, and billed and shipped immediately after completion. Our original software handles that particular workflow very well, automating everything from shipment quoting and purchasing, to label printing and packing list generation. But it also has real limitations. We never made parts to stock and rarely shipped partial orders. We couldn’t ship multiple orders together, support blanket POs, track inventory across multiple production sites, handle vendor-managed inventory, or even do basic job costing.

In a nutshell, we designed our first system to automate shipping, with no eye on work-in-process (WIP) or finished-goods inventory, correct accounting, job costing, or more general business workflows that normal ERP software would support out of the box.

In retrospect, that’s OK. Our first attempt was highly automated, and that allowed us to grow our business without much of the front office overhead that might normally have been required to fulfill a high volume of custom orders. Supported by our software, we’ve profitably scaled to more than 50 employees and served over 10,000 customers, most of them businesses. But the narrow scope of our software has prevented us from growing with our larger customers.

As I write this article, we are rolling out new production, inventory, and shipping systems to fix that problem. We could switch gears and integrate with a mature ERP package, and even I would say that would usually be advisable. But we’ve benefitted so much by automating business workflows that tying into an existing ERP would set us back in a major way. Without expensive and time-consuming customization, we’d have to hire four or five people just to manage data entry and babysit the new software. And that would just get us back to where we are today.

So instead, we are replacing our original system with new custom-designed software that handles normal ERP workflows correctly, without sacrificing the efficiency we gain through software automation.

Our software team has been working hard to make this happen. It’s been a challenge, because it involves gutting existing systems, migrating database tables, releasing new application program interfaces (APIs), and refactoring existing production consoles. And all that has to happen without interrupting production. We jokingly compare it to changing the tires on a moving car. The stakes are really high, and we can’t mess up.

So far this year, we’ve created a new "item" system, supporting production items with bills of materials, customizable routes, and work instructions. We developed a new inventory system that can track raw materials, consumables, WIP, and finished goods, and built out a new purchase order system for it. Those new systems saw some limited use, but they didn’t see prime time until recently. As I write this, it’s been less than a week since we launched new quality and shipping systems that fully leverage all that new ERP-friendly infrastructure. So far, so good!

FIGURE 1 A quality console simplifies final inspection. Parts in the final inspection step are listed with thumbnails and are automatically sorted by priority and due date. Additional filters can be applied to quickly search for and identify parts.

FIGURE 2 Interactive 3D models help workers check for accuracy and quality. After inspection, parts are labeled and placed in inventory so that they can be stored or shipped as needed.

FIGURE 3 Shipping orders identify parts that need to ship. Tools are provided to scan inventory into boxes, book shipments, and print shipping labels.

With these new systems, we had four major objectives:

1. The new quality and shipping consoles must integrate nicely with inventory management software. Finished parts must enter inventory, and the shipping system must pull parts from inventory.

2. We must keep automated workflows that help us ship over 100 orders per day.

3. We must be able to ship anything from inventory, whether we purchased it or made it ourselves, and whether we manufactured it a year ago or today.

4. We must have the ability to ship partial orders, combine multiple sales orders into one shipment to the same customer, and track all shipments against the sales orders they satisfy.

Production and Quality

These new features are enabled first by our new quality control production console, shown in

Figures 1

and

2.

Quality is naturally and ideally built into every production step, but we have a final step where parts are inspected, labeled, and (with this new system) scanned into inventory.

Final inspection completes the work order for that item, and all accumulated WIP value moves into finished-goods inventory. That value includes anything on the bill of materials, including measured labor, consumables, raw materials, and (where appropriate) standard costs including overhead. For the accounting gurus out there, our costing model is a hybrid of actual measured costs wherever possible and standard costs for things we can’t directly measure per job or per part.

Inventory and Shipping

After a completed work order moves parts into finished goods, those parts are managed by our inventory system in the same way that raw materials and consumables are managed. That’s standard for any ERP system, of course, but it’s a big step forward for us. The inventory system makes it possible to move, store, and adjust quantities of items.

And once parts are in inventory, they can be shipped at any time to fulfill a sales order.

In our new system, we trigger fulfillment by creating a "shipping order," as shown in

Figure 3.

Our shipping orders simply define what needs to be shipped, to whom, by what date, and by what method. We also use them to handle internal transfers between facilities and to track will-call orders.

Like our old system, shipping workstations allow workers to scan parts into boxes, print packing lists, quote and purchase shipping, and print shipping labels. Under the hood, customers are automatically notified whenever it is appropriate—for example, when they have parts ready to pick up in will call, or when their order is fully shipped. For most orders, credit cards are automatically charged prior to shipping. For net-terms customers, invoices will soon be automatically created and emailed, with easy links for payment.

We are passionate about user experience: Software design has come a long way since 90s-era internet and Windows 95. We are excited to provide our people with software that is both powerful and a joy to use.

What’s Next

Most of this functionality is pretty standard for off-the-shelf ERP. We are proud of our systems because they remain highly automated in spite of the newly added flexibility. We are also passionate about user experience: Software design has come a long way since 90s-era internet and Windows 95. We are excited to provide our people with software that is both powerful and a joy to use.

Our new quality and shipping systems represent a first big step. Our next big steps will be to migrate our routing systems, tie them together with production planning, implement time tracking and other automated costing systems, and automate accounts receivable and accounts payable workflows. We’ll be working on this at least through all of next year. In the end, this is all about getting our house in order. We’ll better understand costs, overhaul our automated quoting engine, leverage time and cost data to optimize production planning, and better serve our customers.

Our particular need for software automation is driven by custom highmix production. Most shops scale on the back of large production jobs or specialized work. In those cases, off-the-shelf ERP is probably more than suitable, and options abound. That’s great news for operations who have yet to modernize their software. In lieu of expensive in-house development, I’d recommend exploring the many possibilities and getting the process started.

Caleb Chamberlain

is CEO and co-founder of Orem, Utah-based OSH Cut,

www.oshcut.com

.

Discover the World of High-Productivity Double-Articulated Weld Booms

Double Articulation

Complete Area Coverage - No Dead Zones!

Effortlessly Move from Weld to Weld

Integrated Fume Extraction (option)

Robust Design-Built to Perform

Increased Safety

Increased Productivity

Andersen Industries •

www.andersenmp.com/weldpro-360

∗

m 760-246-8766