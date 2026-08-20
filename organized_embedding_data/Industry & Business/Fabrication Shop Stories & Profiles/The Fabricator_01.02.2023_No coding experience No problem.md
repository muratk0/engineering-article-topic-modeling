# No coding experience? No problem

[TARİH: 01.02.2023 The Fabricator]

Software

How low-code apps could streamline the shop floor

By

Tim Heston

An Independent Rough Terrain Center LLC (IRTC) employee at a workstation uses a tablet in the company’s Work Center Alert System, a custom application built with Microsoft Power Apps.

Images: Independent Rough Terrain Center LLC

S

oft ware has made its mark in sheet metal fabrication, from quoting and CAD/CAM to programming and scheduling. All of it has brought a host of initialisms: enterprise resource planning (ERP), manufacturing execution systems (MES), customer relationship management (CRM), computerized maintenance management system (CMMS), product data management (PDM)—the list goes on.

Metal fabrication itself has changed too. Shops now aren’t really in the parts business. They’re in the information business. The better they process information, the more likely they’ll be fabricating the right quantity of parts at the right time in the right way.

When shops fail to do this effectively, they produce what the late Dick Kallage, a longtime industry consultant, called

information waste

. Someone doesn’t have the right information at the right time, so they waste time fabricating something incorrectly, at the wrong time, or at the wrong quantity. Or they waste time walking somewhere to ask questions. Or they mistype something or click the wrong menu, which sets off a cascade of events that throws yet another wrench into the system.

Small shops dominate metal fabrication, and order processing practices can vary greatly, from quoting through engineering to information posted on the paper (or virtual) job traveler. Responsibilities vary from shop to shop too.

All this makes it impractical for one off -the-shelf soft ware package to handle every aspect of a manufacturing business, no matter how small that business might be. On top of this, the state of soft ware in manufacturing resembles the state of machinery: Some systems are new, some are very old, and getting everything talking and on the same page is easier said than done.

Scott Clauss knows this scenario all too well. He’s business systems architect for Independent Rough Terrain Center LLC (IRTC). The 97-employee shop specializes in building and (especially) rebuilding massive rough-terrain container handlers for the Department of Defense and commercial industries. Based in Cibolo, Texas, the company isn’t a fabricator, but the operation has many of the same challenges a high-product-mix fab shop faces every day.

Clauss and other company managers knew they had an issue with information waste. The company had implemented plenty of visual controls, even

an-don

lights near workstations to notify others of an issue. Too oft en, workers had no choice but to leave their workstations to track down someone who could help. And those walks could take a while. The shop rebuilds massive container-lifting trucks, and there’s just no getting around it: People need a lot of space (a multifacility campus, in fact) to get the job done.

As Clauss recalled, "We knew we had a problem. How could we use the resources we currently have to allow people to communicate in a more consistent manner? We saw them using radios, using email. And they were continually walking across the floor to find someone.

"I realized that one resource everyone had on every electronic device is email. But we needed to be able to control the flow of information. Who gets what? What messages get sent to whom? That’s how it all started."

A section of a container handler undergoes a tear down. IRTC’s work involves massive components, hence the need for shop floor space.

In a previous system, users had to scroll through hundreds of drawings to find a part. Now, they navigate through a few menus and choose a specific zone of the machine. That narrows the choice to just a handful of drawings.

This led the company to explore a novel area of software: low-code apps. Numerous platforms have emerged in recent years from Google, Salesforce, and other marquee names in Big Tech. IRTC happens to be using Microsoft Power Apps. Such software gives a basic structure to build on top of—no coding experience required—to create custom applications that suit the needs of a particular business.

As Clauss described it, "It’s a program that makes programs."

No More Walking

Clauss isn’t a software engineer. In fact, he was initially hired as a senior technical writer, and part of his job was developing manufacturing work instructions for those on the plant floor.

As President and CEO Stephen Speakes recalled, "Scott identified a need. He saw people were having difficulty communicating. He knew we needed a way for people to communicate efficiently with the right person at the right time."

In manufacturing in general, minimizing the unknowns and pushing more authority to those on the front line are a core part of continuous improvement. A bending department lead might receive a job traveler showing a bend that can’t be made with available tooling or the specified tool setup. So, the department lead walks to the engineering department to hash out the issue. In this case, an efficient communication method between engineering and the brake department could help—people wouldn’t spend as much time walking—but it doesn’t get to the core of the issue:

Why weren’t parts designed with the shop’s available tooling in mind?

That said, some fabrication issues arise regardless, not because of a basic tooling error, but because the shop just hasn’t processed the job before.

In this sense, IRTC shares the same challenges as a sheet metal job shop. For every truck it refurbishes, the company starts with a standard bill of material (BOM), but that’s just the beginning. Ed Ortiz, director of product development, explained it this way: "We know certain parts are going to go onto the truck at certain stations. But along the way you might find components that are corroded or have missing or broken components that need to be replaced. We call this additional work effort, or AWE."

The nature of rebuilding anything can be unpredictable. Workers know exactly what they need to complete the job

only

after they’ve inspected what they have. Certain rebuild elements might require someone from the quality department. Others might require expensive parts that need management approval. The potential scenarios are endless.

Parts are delivered, quality and managers inspect and sign off as needed, and the truck flows to subsequent workstations for rebuilding. Subassemblies that have been refurbished already—axles, engines, transmissions—are rebuilt onto the frame, which moves down the main production line.

Like in a sheet metal shop, the actual processes on IRTC’s floor flowed smoothly. Inefficient communication was the sticking point.

There’s a Custom App for That

In November 2021, Clauss began chatting about these issues with an intern in the company’s IT department. "He said, ‘Did you hear of this Microsoft program called Power Apps? It comes with the Office 365 standard business suite.’ We already had the program, so it was a resource we had available to us for free."

Again, Clauss is a technical writer, not a software programmer. But since he had been concentrating on developing work instructions, he knew the company’s processes inside and out. He just needed a more effective way for employees to communicate.

"These custom apps really shine when you don’t have an out-of-the-box software solution to use," he said, "especially for processes that meet a need unique to a certain company. That’s where these apps can really have an impact." In essence, Power Apps is a graphical front-end interface that draws from tables in the background. "Those tables could come from a SharePoint list, an Excel file, or SQL database that you already have, and you can build a table fairly easily," Clauss said. "It has a number of drop-down lists that you choose from, and that really is the only thing you program. The entire system is pretty simple."

To start developing, Clauss began with the one communication tool everyone had and knew how to use: email. It’s also accessible on any electronic device—computer terminal, laptop, phone, and tablet.

Thing is, email by itself is clunky and inefficient. If, say, an employee at a workcenter needs someone from the quality department, he doesn’t want to spend time drafting an email and sending it to a list of people. If that were the case, it might be faster to simply walk to the quality department and ask for help.

A customized Power Apps program—what the company calls the

Work Center Alert System

—helped streamline things. Imagine shop floor employees require someone from the quality department. They don’t spend time drafting emails. Instead, within their phone or iPad, they click a few buttons, which in turn automatically sends an email with applicable attachments (including images of the issue) to a defined group of people. The first to reply takes ownership of the problem, and the process moves forward from there. It’s like an

andon

light on steroids. There’s no time spent with excessive keystrokes, yet the email notifications and attachments still communicate what’s needed to the right people.

The shop used lights by each workstation to indicate status and the need for help. Despite the visual controls, response times were slow, and someone had to patrol the shop continually to check for issues. Now, a custom Power Apps application helps employees communicate issues immediately.

IRTC has a multifacility campus. The more effectively employees can communicate without hiking across the floor or between buildings, the more efficient the operation can be.

A rebuilt, unpainted rough-terrain container handler is tested on IRTC’s industrial campus.

Something similar happens during the AWE process, when someone at a workstation finds they need a part that costs more than $500. Previously, warehouse personnel manually looked at the cost of every part requested from the shop floor, then sent an email to the supervising manager for any part that exceeded $500. Warehouse personnel then had to wait for a response before entering the request in the ERP. Today, the Power Apps automatically sends an email to managers for any part that’s over $500. And with a click of a button, the manager now can approve or deny the request.

Ordering the parts is simpler too now. "Before, employees had to hand-write their orders and part numbers, then hand-deliver the paper to the person placing the order," Clauss said.

Now, using a Power Apps program, the process occurs electronically and in a much-improved fashion. Before, those ordering the parts had to scroll through dozens of pages to find the right drawings and part number. "We had 193 different drawings [for each truck], and we had to look through each of them, one at a time," Clauss said.

To streamline things, Clauss wrote a program that uses an exploded view showing exactly where on the truck the part is located. "This narrows the drawing list down to about three," he said. "So, we shortened our typical part-searching time from eight minutes down to just 30 seconds. When they find the part, they just hit a button, and the program fills in the required form and sends it directly to the person placing the order."

Speakes chimed in. "We’ve noticed a huge difference in employee engagement in the most important area, the people on the front lines." He described previous scenarios where people continually spent time looking for help. "Think about the guy on the floor. He needs a part. He needs help, and he can’t get it. We had signs. We had people assigned to patrol the hallway to see if there was an issue. But it was all terribly ineffective. It le" the person who needed help convinced that the organization didn’t care. Now, it’s just the opposite. He has the tool to request help, and he sees an immediate response."

The Value of Immediate Customization

Custom Power Apps programs can take advantage of technologies built into phones, tablets, and laptops. For instance, if an app were written to document standard work instructions, it can incorporate photos or videos. It can also turn someone’s smartphone into a barcode or QR code reader.

"In this way, it can help a warehouse with perpetual inventory," Clauss said. "You can take a picture of the barcode, input or select the quantity, and it automatically deducts from the inventory. When you refill stock, you can do the same thing but just select ‘in’ instead of ‘out.’"

It can also use a device’s GPS location and detect where and how a device is moving. Clauss described an-other company’s custom Power Apps program that shut down access when carried away from the building or if the phone moved beyond a certain velocity (say, if its owner was driving). He also mentioned certain tools that are in the works that might allow an electronic device to replace certain measurement tools used for quality.

MARK YOUR CALENDARS!

ADVANCED LASER APPLICATIONS WORKSHOP

NEW DATES NEW LOCATION

JUNE 13-15, 2023 NOVI, MICH.

Suburban Collection Showcase

Sponsored by:

Legacey Sponsor:

Gold Sponsor:

Space is limited.

Register |

alawlaser.org

ADVANCING MANUFACTURING TOGETHER.

BE PART OF IT.™

fmamfg

.org

"Think about the poor guy on the floor. He needs a part. He needs help, and he can’t get it. We had signs. We had people assigned to patrol the hallway to see if there was an issue. But it was all terribly ineffective. It left the person who needed help convinced that the organization didn’t care. Now, it’s just the opposite. He has the tool to request help, and he sees an immediate response."

— Stephen Speakes, Independent Rough Terrain Center LLC

And in the near future, the company hopes to use Power Apps to augment or even replace its inspection recordkeeping software. "[Our current software’s] greatest shortcoming is its inspection forms, which we use to inspect the vehicles and our work on them," Ortiz said. "All of the inspection information, including photographs, gets compiled into a library for each vehicle."

The program’s functionality isn’t the issue; it’s the lack of adaptability. If IRTC needs to change an inspection form, it can take six weeks or more for the software vendor to send an update and implement the change. "If Scott could do it," Ortiz said, "he’d likely have the change made in 20 minutes."

The Implications of Low-code Apps

Power Apps can connect to ERP platforms, though IRTC has yet to connect its custom apps directly. "It’s not difficult to learn, implement, or even maintain, once you have the connection in place," Clauss said, adding that the company is exploring how to implement that connection in the future.

Establishing connections and ridding the company of information silos is top of mind. As Speakes described: "We have our ERP system, our CAD system, our PDM system. How do we get all these systems talking to each other and sharing data in a cost-effective way? Now, we’re always needing to download data from the ERP into an Excel spreadsheet. How can we have our software communicate so we don’t have to manually manipulate the data?"

The free flow of information is the panacea for any business these days, of course. Information silos can wreak havoc on operational efficiency and even company culture. People work with their own metrics in mind, not considering how their actions affect the company as a whole. And who can blame them? They see their own metrics all the time, but they rarely see the big picture. Low-code apps might be one way for companies to connect the dots and share the right information at the right time.

That said, sources at IRTC emphasize that the greatest benefit to low-code apps is the fact they can be immediately customized by someone without coding experience. (Clauss was able to start writing apps after viewing a few online tutorials.) In this way, low-code apps could fit well in the sheet metal job shop full of flexible machines. Need to make something else?

Just retool

. Need software to do something else?

Just re-code

.

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

Independent Rough Terrain Center LLC,

www.irtc-tx.com

Microsoft Power Apps,

powerapps.Microsoft.com

THE TUNGSTEN ELECTRODE EXPERTS

DGP has been industry leader in tungsten and tungsten preparation since 1992. Visit our website to buy online from stock with same day shipping or call us for a free consultation today.

ARC SABER

TUNGSTEN STORAGE

REPLACEMENT

DIAMOND GRINDING WHEELS

WELDING

TORCHES & PARTS

RAW TUNGSTEN

INCLUDING NEW DGP TRI-MIX

MONSTER

TIG NOZZLE KITS

PIRANHA

TUNGSTEN GRINDERS

PRE & RE-GROUND

TUNGSTEN ELECTRODES

DIAMONDGROUND.COM

2651 Lavery Court • Newbury Park, CA • 91320 • 805.498.3837 •

sales@diamondground.com

PT Series Perfect grinding results!

• Deburring • Deslagging • Edge Rounding • Laser Oxide Removal • Surface Finishing

PT 3-4 stations / 103″ belt length

PT Compact / 85″ belt length

MRB brush system for perfect edge deburring

DR Planetary head

Optional vacuum table

Hans Weber Sales & Service

P 913.254.1611 • F 913.254.1582

sales@weberamerica.com

•

www.weberamerica.com