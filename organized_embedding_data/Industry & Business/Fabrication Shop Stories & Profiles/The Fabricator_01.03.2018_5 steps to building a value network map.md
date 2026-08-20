# 5 steps to building a value network map

[TARİH: 01.03.2018 The Fabricator]

Approach provides alternative to value stream mapping

By Shahrukh Irani

L

ean manufacturing has its roots in the Toyota Production System (TPS). But as most in custom fabrication know, the TPS that was designed for Toyota’s assembly lines doesn’t necessarily work for the high-product-mix, low-volume environment of the typical custom fabricator or, for that matter, any other job shop.

Of course, some lean tools are universally applicable and fit custom fabrication very well. Employee involvement in strategic planning, ergonomics, 5S, total productive maintenance, errorproofing, visual controls, standard work, machine setup reduction, and more can help a custom fabricator become better at what it does.

Some lean tools, though, don’t work so well in job shops’ high-mix, low-volume environment. A job shop has various customers that order different quantities of different products that all have different lead times, routings, bills of materials (BOMs), outside vendor operations, and due dates. TPS concepts like line balancing, level loading, right-sized machines, and single-piece part flow can be extraordinarily difficult or impossible to achieve, at least if one goes by their traditional definitions and uses. In particular, a lean tool borrowed from TPS that’s difficult, perhaps impossible, to adapt to the custom fabrication environment is value stream mapping (VSM). Because this tool—intended to highlight and help prioritize improvement opportunities that will eliminate waste and shorten lead times—does not work in any job shop, industry really needs a viable alternative.

Still, this doesn’t mean the concepts behind value stream mapping can’t be applied to a job shop. A job shop is a complicated entity that does not repeatedly produce orders for just one or even a handful of value streams, but instead a network of interconnected value streams that I call a value

network

map. The interconnectedness between the value streams exists because of the kind of BOMs a job shop has and the assembly requirements. Job shops also have part routings that share one or more common machines.

To implement lean manufacturing, you need to overcome two age-old "elephants in the room": creating an efficient factory layout and implementing effective scheduling of daily operations by taking into consideration capacity constraints, such as the constraints of machines, labor, materials, and tooling. Value network mapping (VNM) can help you tame both elephants effectively and efficiently.

Issues With VSM

VSM is a process of mapping material and information flows required to coordinate the activities performed by manufacturers, suppliers, and distributors to deliver products to customers. Manufacturers create "current-state" and "future-state" maps, and then build a production system around a "pacemaker" process of manufacturing. That is, everything is produced to a

takt

time—the drumbeat of each manufacturing step—determined by customer demand. This level-loads the shop floor so that everything flows.

But managing a custom fabrication operation, you know your shop doesn’t produce just one product or product family. (In fact, most will tell you that they wish they knew the product families that exist in their product mix.) A traditional VSM cannot handle product variety or demand variation. It cannot map a large number of dissimilar manufacturing routings involving dozens of different work centers. Nor can it map the complete multilevel BOM of any complex product. Worse yet, VSM provides a single day’s snapshot of part flow that, as anyone in custom fabrication knows, cannot represent the dynamic system that is their shop floor. Work loads and routings on the shop floor can look entirely different from one day to the next.

Creating a Value Network Map

How do you map and analyze many value streams on a single map to determine what improvements to make to your production system? This is where the VNM comes into play.

To create one, you can refer to the basic idea behind the steps used to create a VSM, but then take a different approach to each. This new approach helps account for the high-product-mix, low-volume reality of the job shop.

1. Identify all value streams

In the traditional VSM, a manufacturer simply specifies the value of each product family from the customer’s standpoint. The same thinking applies to VNM. In job shops, as it is for all manufacturers, it’s still about quality, cost, and delivery. However, unlike manufacturers that have high-volume, repetitive production, custom fabricators produce a wide variety of products and, hence, must be able to modify their facilities by product mix and demand changes, as well as adapt to changes in the customer base.

You can identify product or component families by analyzing how work flows through the shop by using the production flow analysis (PFA) method. PFA basically identifies similarities between multicomponent product assemblies, or a large product mix of individual components, by comparing their BOMs or manufacturing routings. This large-scale similarity analysis for product family formation can be done easily using statistical software like Minitab or SAS or application software like SIMOGGA and PFAST (Production Flow Analysis and Simplification Toolkit).

This is by far the most complicated step for any job shop. A full-blown statistical analysis is ideal, of course. But if resources aren’t available for this, your shop can simply identify a single product or product family, such as one that represents a common job the shop processes, like an enclosure—in the "sweet spot," a successful product that helped your shop get to where it is today.

Creating a map around the complete BOM and operations process chart for this product could help leverage the shop’s strengths for future growth. And, of course, the process can be repeated for other products using the software tools mentioned earlier.

Figure 1 To create a value network map, you need to extract a complete, indented BOM detailing every component that goes into a product or group of products. (A partial view of a multipage BOM is shown.)

Figure 2 This operations process chart shows how all the components in each of the three major subassemblies that constitute the final product flow from one process to the next.

To map a single product or product family, the analysis is much simpler. From your enterprise resource planning (ERP) system, you can start by simply extracting the BOM for a key bread-and-butter product. Note that you need to extract the

complete

, indented BOM of the product (see

Figure 1

).

2. Map the value stream

In traditional VSM, a manufacturer identifies all the steps in a value stream for each product family and, whenever possible, eliminates those steps that do not create value.

To create a VNM, start with a product-process matrix. This essentially maps the value streams for the products in the identified product family. With the BOM in hand, identify the components and subassemblies made in-house, which become the final product that ships out the door; then obtain the detailed routings for the components, subassemblies, and the final product from incoming raw materials to outgoing product.

Identify the specific stations on the final assembly line to which each of the in-house assemblies and subassemblies are delivered. With this information, develop an operations process chart that identifies how each and every component and subassembly flows from one work center to the next (see

Figure 2

).

Chart each part number in the assembly against the work centers they flow through. You’ll probably notice that a fair number of part numbers flow through the same machines (

Figure 3

). That is, they have similar, possibly identical, routings. This helps you identify part families, which in turn helps you to develop your future-state material flow in its entirety.

3. Create flow

You now have a good picture of how products flow between work centers, as well as the future state you want to achieve. For instance, this future state could come about by implementing multiple component-producing cells that replenish inventory in a supermarket from which the welders pull kits of parts to produce the subassemblies that go into the final product.

Armed with this information, your shop can now start modifying the existing facility layout—at least to the extent possible—to align it with the existing product flow (see

Figure 4

).

Consider some kind of cellular layout, such as one that produces the same product or a variant of the same product. Of course, some fabricators may have trouble moving away from their age-old process-focused layout that invariably results in a batch-and-queue production system. A punch press or press brake may process some parts but not others. If this is the case (and in custom fabrication, it’s certainly not unusual), excessive equipment sharing may occur—an operator in one cell walking over to another cell to use a press brake with the right bed length, for example. And some machines, like stamping presses, can be cost-prohibitive to move. In these cases, hybrid cellular layouts, cascading cellular layouts, or virtual cells may be preferable. The logistics to support each cell’s operation are managed by a single water spider who functions like a cell manager on wheels.

Figure 3 Components that have similar routings occur consecutively in adjacent rows. Work centers common to one or more similar/identical routings are circled and identified. This multiproduct process chart generated by the PFAST software helps create part families and forms the basis of a value network map.

Figure 4 This layout shows how parts would flow through a cascading cellular layout at a custom fabricator. For instance, a turret punch feeds a press brake, hardware insertion, spot welding, and grinding.

Figure 5 This Gantt chart is a visual depiction of the complete production schedule for an entire product. It shows the start and finish times of all part numbers in the product, which includes both in-house and outsourced processes. The longer the bar, the longer a process takes on that machine to complete that particular component, subassembly, or the final product. Commercial finite capacity schedulers like Tactic (

www.waterloo-software.com

), Preactor (

www.preactor.com

), and Schedlyzer (

www.optisol.biz

) can also invert the Gantt chart shown in this figure.

To implement lean manufacturing, fabricators need to overcome two elephants in the room: creating an efficient factory layout and implementing effective scheduling.

A cascading cellular layout is a combination of the traditional cellular and process layouts; however, it keeps different processes close together—eliminating excessive walking and transportation—but allows operators the freedom to choose machines that work best. In a virtual cell, machines that can’t be moved easily (so-called monuments) may still be far apart, but remain in a "virtual cell," meaning the tooling, fixtures, and support services for those machines are dedicated mainly to one product or a range of products.

Regardless of the layout you design for the upstream portion of your custom fabrication facility, when those components get delivered to the welding booths (or other departments that fabricate the subassemblies that go into each final product), be sure to designate locations that will receive components or subassemblies. Designating locations helps your shop to efficiently build the kits of components that must be delivered to the different welding cells.

4. Establish pull

In custom fabrication and elsewhere, production capacity is not infinite. This is where strategies like finite capacity scheduling and drum-buffer-rope (DBR) scheduling, based on the ideas behind the theory of constraints, can help. Regardless of the method, scheduling should always factor in the capacity of the bottleneck, or constraint, work centers.

From your ERP system you can extract the setup and cycle time for each value-added operation for the product you’re mapping. You then can use this data to generate a Gantt chart, which provides a visual production schedule that shows the start and finish time for every operation, subject to queuing delays at shared resources and finite capacity constraints at bottleneck resources. A Gantt chart helps to put constraint processes into stark relief, be it welding, outsourced plating or heat treating, or anything else. The Gantt chart is the multiproduct multimachine alternative to the single timeline that shows at the bottom of any VSM where a single product is always mapped (see

Figure 5

).

5. Seek perfection, and return to Step 1

As value is specified, value streams are identified, wasted steps are removed, and flow and pull systems are introduced. The process begins again until the state of perfection is reached in which perfect value is created with no waste. Of course, there is no such thing as the perfect job shop, which is why continuous improvement never stops for a custom fabricator whose product mix, workforce, customer base, vendor base, materials requirements, and manufacturing technology will change every year.

Taming the Elephants in the Room

Value network ma pping is an approach that can help to eliminate two age-old obstacles to improving operational performance in any high-mix, low-volume custom fabrication facility: the factory layout and the scheduling of daily operations. These two elephants in the room are one reason that so many job shops struggle to completely and comprehensively implement the principles of lean.

If a custom fabricator or job shop has reliable data available in their ERP system and the desire to grow more competitive and, ultimately, attain world-class delivery, they should give VNM a serious look.

▸ Shahrukh Irani, PhD, is president of Lean and Flexible LLC,

www.leanandflexible.com

, a consulting firm that focuses on adapting lean manufacturing for the high-product-mix, low-volume manufacturer.