# What makes a factory smart?

[TARİH: 01.11.2019 The Fabricator]

Machine and software communication, without barriers

By Carlos García Villate

I

ndustry is changing at high speed, enabled by new technologies framed by Industry 4.0 and the industrial internet of things (IIoT). New approaches for software systems and machines are being unveiled all the time.

Driving it all has been mass customization. Consumers demand personalized products, but at the same time manufacturers must continue to produce at low costs despite new market demands. All this has forced a radical rethink of supply chains. Industries are relocating to take advantage of lower labor rates, cheaper and sustainable transport, and less regulation and taxation, among other reasons. But as machines, factories, and software become smarter, information-sharing and collaboration have stepped to the fore, and industry is rethinking supply chains once again.

Smart machines in a smart factory, collaborating in a network of smart factories, will be governed by a single brain that considers all aspects of production, such as the load of each plant, transport costs from the plant to the place of delivery, availability and cost of raw materials, and delivery dates. Artificial intelligence (AI), machine learning, and related models will create the intelligence necessary to make a smart factory possible.

In a truly smart factory, software and machines "talk" to one another seamlessly. These capabilities will usher in a new level of collaboration among machine builders, software providers, automation integrators, and other players in the sheet metal supply chain.

Evolution of Machine Communication

The need for machines to "talk" to software isn’t new. For years sheet metal industry stakeholders have integrated this ability in various scenarios, typically for an automated cell or line, such as when a sheet metal stacker loading a punch or laser machine forwarded cut parts to a panel bender. In these cases, machines had to inform software systems when they were ready to execute a new operation or when they had finished it. In this way the company could run a complete shift, usually at night, so that the line could work unattended. Such lights-out automation used a validation software system to control all the machinery involved, detecting when a machine finished its work and was ready to load the following process.

Common protocols such as OPC UA (Open Platform Communications, Unified Architecture) and MTConnect solve basic problems involving security and access to data, but they do not solve the problem of semantics. Despite these advances, it is still very difficult and sometimes impossible for systems to communicate. Different machines from different manufacturers, or even different models from the same manufacturer, can speak different languages.

Sometimes the machines in the shop are old and communication protocols are unwieldy. Connecting them can be difficult and expensive, and the cost of upgrading to modern equipment might be prohibitive. To move forward with digitalization, companies need to make sure that they have machinery that complies with the latest communication standards.

Enter the Universal Machine Tool Interface (UMATI) initiative. Launched in 2018, UMATI is a joint effort of VDW (the German machine tool manufacturer association) and 17 technological partners that aim to achieve ease and speed in machine integration. Up to now this could be achieved only with tailor-made projects that entailed high costs and long implementation times. With UMATI, all machines will speak the same language.

UMATI relies on OPC UA, which solves all the basic connectivity problems, like data access, data transfer methods, and security. This opens the door to resolving difficulties in IT/IIoT integration, key to Industry 4.0 and essential to building a smart factory.

These integration mechanisms allow any machine to communicate real-time production status data to other systems in the network. Once the operator has prepared the job on the machine, all events (such as "start," "pause," and "end of job") are transmitted to cooperating systems. In one sense, these mechanisms make it possible for a traditional machine to be converted into a cyberphysical system that "talks" to cooperating software like materials resource planning (MRP), manufacturing execution systems (MES), enterprise resource planning (ERP), and other systems that manage manufacturing processes.

These mechanisms will help the development of many different systems that monitor the machine status. They will, for example, show key process indicators in real time—including load capacity and overall equipment effectiveness (OEE)—monitor current load capacities, and produce quotations based on a machine’s situation and availability.

Machines will start fruitful communication with cooperating software that works with IIoT, advanced sensors, security, and other systems. These new resources present new opportunities not only for machine and cellular automation, but also for factory and even multifactory automation. New machines incorporate software layers that enable them to communicate with other software systems and applications in a sophisticated way, either locally or in the cloud.

The interconnection between the two worlds, the local and the cloud, will be critical, and it’s already possible thanks to mobile technologies like 5G. A new standard in communications, 5G will allow the cloud to become the default envi-ronment where data will be stored, processed, managed, and consumed at any time and from any device in a completely secure manner.

This also will change customer and supplier relationships as information systems throughout the value chain reveal previously untapped opportunities. The industry is moving from efficient machines to intelligent machines, and software will elevate these machines to a whole new level.

Data Security Vital for Digitalization

Connecting the plant to the IIoT has enormous and indisputable advantages, but it also can expose hidden elements to a new world full of cybersecurity threats. For reliable production and confidentiality, intelligent machines in an intelligent factory must be secured. In the smart factory, machines as well as local- and cloud-based software all cooperate, but such robust interoperability requires the latest security technologies.

The type of functions that need to be secured include data transfer (both real-time and batch), data retention, and flexibility when adding new information sources or destinations. With these types of security measures, cloud computing becomes a viable solution.

The Manufacturing Brain

Today most machine tools are subject to the demands of external software. They wait to receive a CNC program. With the right data and logic, external software determines what tasks machines execute and when they execute them. The machines send status information to external software while people monitor the operation with the machine control or via supervisory control and data acquisition (SCADA).

This is all going to change. A smart factory’s automation requires intelligently applied control that goes beyond the control loop implemented in a SCADA system. A smart factory effectively has a "brain" capable of orchestrating all the elements involved in production, from order entry through planning, purchasing, and execution.

A smart factory effectively has a "brain" capable of orchestrating all the elements involved in production, from order entry through planning, purchasing, and execution.

The manufacturing brain will change just about everything in the sheet metal factory. Consider computer-aided manufacturing. Any CAM system should minimize waste and inefficiency.

It should not only produce the best nest, but also generate the best processing method that satisfies quality requirements and minimizes processing time on the machine. Today, to maximize margins for each production order, a skilled programmer must generate the best possible nest, optimize material use, and select the most efficient cutting method.

The smart factory will challenge the traditional role of production engineers and change the relationship between CAM and machines. Machines and software will take on repetitive tasks that people currently perform. They need only know certain manufacturing parameters, such as quality, geometry, quantity of parts, the material, and thickness. With this information, the machine will generate the best nesting and processing method. AI and machine learning will be key, but exceptions will still need the supervision and knowledge of the production engineer.

The smart factory will change MESs too, reacting automatically to incidents like machine failure, absence of material, change in order priorities, and other events during production. Incorporating intelligence, MESs will determine the best time to perform a task, the best routing, and the best order of execution. And they will analyze order and customer characteristics, material availability, the required delivery date, and make immediate adjustments that consider the current work load—all in a matter of microseconds.

The Cloud’s Potential

With the help of AI, the manufacturing brain will select the best plant, the best routing, with the most appropriate machines. That said, the nature of AI makes the cloud essential. The cloud has created computing capacity that until now has been unimaginable.

Some purists will say that an MES can only be in the plant. Is it possible to solve production scheduling in the cloud only, and leave the control of production execution in each of the plants? These are some of the questions that need to be answered.

Regardless, the cloud’s potential is undeniable. Cloud-based MESs prepare the way for powerful manufacturing systems that make extensive use of new levels of computing capacity that can manage multiple plants at new levels of efficiency. For example, it will be able to make the decision to send part of the production to one plant or another based on information sent in real time from each plant. The MES in each plant will orchestrate production orders, and the MES in the cloud will orchestrate overall programming. And in all of this, 5G will play a pivotal role, handling the large flow of data between plants and the cloud.

The Future Requires Collaboration

The future will bring a machine that decides autonomously. It will do this based on its own status and information from a host of interconnected systems, including MES and CAM. Their interaction will be largely automatic. People will intervene only to handle the exceptions.

Fabricators will see more machines come with powerful software, both in the machine control and in the cloud. Using data and logic, intelligent systems will decide what to do next and what information to exchange with various machines. These machines will be immersed in a factory choreography, dancing their part while synchronized with the rest of the manufacturer’s systems.

Machines started to "talk" a long time ago, and they keep on learning more vocabulary and languages. Today machines and software are merging, and to function properly they need the right architecture based on solid protocols that support real-time interoperability. Above all this, a strategic approach for collaboration among machine tool builders, software developers, and system integrators will be essential to unleash the amazing concepts yet to be imagined. By working together, we will define the sheet metal factory of the future.

Carlos García Villate is research and development director at Lantek Sheet Metal Solutions in Miñano, Spain,

www.lantek.com

.

5 Elements of the Smart Factory

1. Digitization

Machines, software, customers, and suppliers interact and communicate electronically both locally and in the cloud. Built-in intelligence makes decisions to coordinate supply, production, and delivery of goods in a highly efficient way.

2. Automation

This optimizes machine and decision-making performance. It includes mechanical devices for handling raw material, components, and machine operation, as well as equipment such as robots for performing other operations. It also includes automated quotations, ordering, manufacturing planning, and similar activities.

The aim is to minimize human involvement, such as routine decision-making, and maximize machine utilization.

3. Provisioning

This ensures materials and resources are available when required. This can include product specifications, raw material, functioning machinery, CAM programs, manufacturing capacity, means of delivery, quality audits, and other factors necessary to complete production on time and to the desired quality and cost.

4. Intelligent Machines

Machines securely communicate with software systems around the factory and in the cloud to report their status, including the machine condition and what is being manufactured. Intelligent machines will make decisions and, rather than be told what to do by external systems, be part of the decision-making process, requesting information and equipment necessary to complete the job.

5. Dispatch

This coordinates manufacturing resources to achieve on-time delivery. Increasingly, companies have multiple manufacturing plants, and parts or assemblies can be produced at different locations. Customer delivery needs to be coordinated across multiple manufacturing sites so that products are delivered at the right time.