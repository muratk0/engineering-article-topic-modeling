# From shrink-wrapped boxes to the cloud

[TARİH: 01.12.2023 The Fabricator]

Tech Talk

AI is the next logical step in software development

Caleb Chamberlain

C

omputer software has changed a lot since the 80s and 90s. I remember when you could walk into a Barnes & Noble and browse through the software section, perusing shrink-wrapped boxes containing floppy disks or CDs. There was something nice about walking through the software aisle like that, everything in one place, imagining the possibilities. It was exciting.

In 2023, the internet has taken over the world and, with it, software distribution models. You don’t shop for software at a brick-and-mortar store anymore. Instead, most modern software is designed to run in a web browser: Your computer downloads and runs the app every time you visit the website. Instead of buying software once, installing it, and running it on your isolated computer, most software vendors are leaning hard into SaaS: software as a service. You’ll pay a monthly subscription, and in return you can use the most recent version of the software, from any computer, with your up-to-date data, anywhere in the world, at any time.

This is a big change, and not entirely positive. There’s something nice about being able to actually

own

software. Imagine losing access to your business’s financial information because your subscription expired. Subscriptions mean that the health and safety of your data is dependent on infrastructure and companies that you don’t control. And who knows where they’ll be in 10 years?

On the other hand, data and software in the cloud is inherently safer than data stored on your shop’s computer. You don’t have to worry about a crashed computer causing you to lose all your data. For better or worse, software is moving that direction, and there are definite advantages to using software in the cloud.

To the Cloud

For starters, web applications change the way software is developed, usually for the better. Old-fashioned software is usually built to run on a single operating system, like Windows or macOS, using programming tools that are often proprietary and tailored to the operating system. In practice, this means that it can be difficult to make customized user interfaces that are natural and easy to use. In contrast, web browsers use standardized languages that work mostly equivalently across all devices and operating systems, from your desktop PC to a designer’s MacBook to your mobile phone.

There are many, many different frameworks out there for building web applications, but in the end they all produce HTML to structure a web page, CSS to style it, and JavaScript to program it. Those tools together give developers the ability to make custom software that interacts in unique ways. For example, we’ve developed specialized tools to help run our shop, including software for inventory management, scheduling, and production. Web-based development makes designing custom user interfaces extremely easy compared to more traditional approaches.

But perhaps most important, web applications are built on a completely different and extremely powerful "tech stack." A tech stack is the collection of tools and technologies used to develop and deploy a web application. For traditional software from before the internet era, the tech stack was isolated and limited. Programmers would write code and build it with a compiler to convert that code to something your computer could run. You’d buy a set of floppy disks or a CD and install it on your computer, and that was that. The application may have relied on a local database, also installed on your computer.

Putilich / iStock / Getty Images Plus

There’s an API for That

In contrast, a web application usually features a lightweight front end running in a web browser. If you’ve ever logged into a web application like NetSuite, QuickBooks Online, or ProShop ERP, that’s what you are using: a front-end app that enables you to interact with the larger system. Data storage and most intensive processing is handled by the back end, which includes a server and usually a database of some kind.

If you create an invoice in your online ERP tool, the front end (running in your web browser) sends messages back and forth with the server in real time to keep things up to date: "Create this invoice, assign it to this vendor, add this line-item." In modern software, the discussion between your web browser and the server takes place over what’s called an API, or an application programming interface. An API is just an agreed-upon way for software to exchange information or initiate actions.

The API ecosystem is one of the most powerful, enabling tools accessible to internet-enabled software. There are tens of thousands of software companies online who don’t sell software per se; they sell services that other software developers can use on demand, accessible via API calls. The front-end app running in your web browser isn’t just restricted to talking to a single server maintained by the app’s developers. Instead, it can talk to hundreds of different services that provide advanced functionality, all through something as simple as a single line of code making an API request.

For example, at OSH Cut, we utilize many different third-party APIs to add advanced features to our tools. We needed to get accurate shipping rates from parcel and freight carriers: UPS, FedEx, USPS, and Old Dominion. It works out that there are multiple software companies who offer web APIs for doing precisely that: We can issue a single API call (something incredibly easy to do from a web server or a web app in a browser) and get rates from all carriers at once.

Instead of spending months figuring out how to estimate shipping costs, our developers were able to get accurate shipping rates with less than a day of development. We use other web-based APIs to determine whether shipping addresses are residential or commercial; to calculate, collect, and pay sales tax accurately across over 13,000 sales tax jurisdictions in the U.S.; to download and synchronize bank transactions; and to securely accept credit card payments without ever having actual card numbers exposed to our own software (a big win for security and compliance). And, of course, we’ve written our own APIs that allow our instant quoting app to perform manufacturability checks and quote parts through a web browser.

All of these tools have enabled us to tackle complex problems in a fraction of the time. And it barely scratches the surface. For example, Adobe and others offer tools that allow PDF documents to be automatically scanned and analyzed in a single API call. We are interested in that because it will allow us to write document automation tools that automatically tie bills of lading to inventory receipts and mill certs, streamlining and improving traceability workflows.

There are many more possibilities: If you can imagine it, there’s almost certainly an API that does it. While we don’t use them at OSH Cut, there are even web APIs to nest sheet metal parts, taking that complex operation and making it easily accessible with minimal development.

Making AI Easy

There has been a lot of buzz about AI recently, and for good reason. Large language models (LLMs) make computers seem convincingly intelligent, in ways previously only imagined in science fiction. AI feels like a technology that’s going to change everything, much like the internet has. It’s hard to see where it’s going (or whether it’ll be net positive for the world), but we should all buckle up.

From a practical standpoint, the incredible thing about these new LLMs (like ChatGPT from OpenAI) is that they are

extremely simple

to use. Why? Because they expose their functionality via web API, just like we’ve been discussing.

To be clear, this isn’t simple technology. AI models are no joke. They contain

trillions

of parameters, tuned and trained using what’s effectively the sum of human experience made available on the internet, at a cost of hundreds of millions of dollars. A simple request to ChatGPT revs up data centers in the cloud that house unimaginable computing power. LLMs are incomprehensibly complex, and only work at all because of a confluence of technologies that have only existed in their current form for the last decade or so.

The miracle is that a junior software developer can access all that capability in a single API call, making any web application smart enough to analyze complex data and extract patterns, and then have a convincing back-and-forth conversation about it. AI is impossibly complicated, but imminently accessible anyway. In a previous article, I wrote that I’m unsure how we could use AI to improve our manufacturing operation. But it costs almost nothing to try. I’ll let you know how it goes.

We’ve come a long way since you had to walk into a bookstore to find and buy software. Modern web applications make user experience better than ever. Web APIs make a vast collection of complex and powerful tools easily available. And AI tools are about to change how we interact with computers in ways impossible to foresee. This is an exciting time to be alive.

Caleb Chamberlain

is CEO and co-founder of Orem, Utah-based OSH Cut,

www.oshcut.com

.

FOR YOUR LARGEST PROJECTS, CHOOSE JUMBO HSS.

When it comes to industrial projects like manufacturing facilities, using structural steel with wider spans and high axial load capacities is essential.

Enter Jumbo HSS from Atlas Tube. Our HSS have a high strength-to-weight ratio, which means you can use less steel and lower your embodied carbon. Our products are also the largest domestically made HSS and have frequent rollings, making it even easier to meet your projects’ demands.

Go big with Jumbo HSS at

atlastube.com/jumbo