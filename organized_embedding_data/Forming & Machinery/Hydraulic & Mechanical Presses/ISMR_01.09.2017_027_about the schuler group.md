# About the Schuler Group

[TARİH: 01.09.2017 ISMR]

After acquiring toolmaker AWEBA and the majority stake in Chinese press manufacturer Yadon, Schuler is present in 40 countries with around 6,600 employees. Schuler is majority-owned by the Austrian ANDRITZ Group See www.schulergroup.com

properties and characteristics which used to be regarded as contradictory. The result, Schuler told ISMR, is a range of benefits for the user which 'cannot be achieved with conventional press designs like greater eccentric

COIL PROCESSING; FOUR QUICK FORMULAS FOR PRODUCTION PLANNING

## Coil processing is gaining popularity because of the lean concepts it immediately introduces into the workshop. Here, various coil calculator formulas are introduced and explained to enable quick decisions to be made on the shop floor.

Coil processing is a way to introduce lean production concepts into sheet metal fabrication; in-line production, continuous processing, reduced WIP (Work In Progress) and minimum waste.

Four quick formulas can greatly help production planning as well as answer the simple questions below:

How can we calculate coil length from inner diameter, outer diameter and thickness?

How can we calculate the running time for a metal coil?

How can we calculate coil length from weight, material type, width and thickness?

How can we calculate coil weight from width, outer and inner diameter?

Four quick formulas can greatly help production planning

In this article, I will show how these formulas are obtained to provide tools that can be easily adapted to new materials and conditions.

Defining a metal coil First of all, let's answer the basic question: what is a metal coil?

The coil inner diameter (ID measured in mm) depends upon the type of re-coiler used in the slitting line. The most common bore size is 508mm, but 406mm and 610mm sizes are also used.

## By Andrea Dallan, CEO, Dallan SpA

The coil outer diameter (OD measured in mm) depends upon the capacity of the service centre. It must be also checked against the geometrical characteristics of the decoiler, where the metal coil will be processed.

In the following calculations, the thickness (T. measured in mm) of the metal coil means the total thickness - including paint, if present. For coated coils paint thickness can be between 0.03mm and 0.08mm; note that some producers of coated coils only indicate the metal thickness on the coil labels. The paint thickness can slightly influence the results of the formulas.

The coil width (W measured in mm) is the transversal dimension of the coil and, together with the previous data, enables the calculation of coil length (L measured in m), which is needed to calculate the quantities that can be produced from one coil.

The material type is important to define the density of the metal (D is measured in kg/dm^3). Here are some references for the most common materials:

Carbon Steel, Galvanized Steel and 
Aluzinc: 7.85kg/dm^3 
Stainless Steel: 8kg/dm^3 
Aluminium: 2.71kg/dm^3 
Lead: 11.3kg/dm^3

With the geometry of the coil defined, it is now easy to calculate the metal coil weight (measured in kg). Let's now see how to answer the following four questions.

## How can we calculate coil length from inner diameter, outer diameter and thickness?

Quite often, in the workshop, we may not have information on the coil weight or material type. In this situation, we can still calculate the coil length from the geometry of the coil. All we need to do is measure the coil outer diameter, inner diameter and thickness. With this information, we first calculate the Volume of the metal coil:

(Volume) = 3,14/4*(OD^2-ID^2)*W

Volume will be in cubic millimetres. To obtain the coil length, we have to divide the result by the section of the coil determined by the coil width and thickness.

L = (Volume)/(W*T*1000)

For coated coils, paint thickness can be between 0.03mm and 0.08mm

It's easy to see that the width of the coil is not needed, so the final formula becomes:

L = 3,14/4*(OD^2-ID^2)/(T*1000)

The coefficient 1000 is used to compensate for the dimensions in [mm] with the length in [m]. For example, a coil with OD = 1600mm, ID = 508mm and T = 0.6mm results in a length of 3010 metres.

This formula is extremely useful because it allows a quick calculation of the running metres on a coil being processed (for example, with a laser sensor that reads the coil diameter) and can therefore be used to calculate, with the following formula, the running time for the machine.

## How can we calculate the running time for a metal coil?

Starting from the length of the coil, with just two pieces of information it is possible to calculate the running autonomy for the machine. All we need to know is the part length and the cycle time.

(Number of parts) = L/(Part Length) (Coil running time in minutes) = (Number of parts)*(Seconds per part)/60

For example, with (part length) = 1.4m and (cycle time per part) = 12s, the formula results in:

(Number of parts) = 2150

(Running time) = 430 minutes = 7.2 hours

In the coil definition, I have determined the measuring unit with which the dimensions and density have to be used in the formulas; the final formulas have coefficients introduced to compensate for the different measuring units.

In my opinion, these two formulas remain, by far, the most useful in coil-fed production.

All measures are subject to tolerances (for example, sheet metal thickness). These tolerances will also influence the final result.

We assumed the use of coils with tight winds; if the coil is loose, this will result in lower weight and shorter lengths than the calculated outputs.

The coefficient 1000 is used, in this case, to compensate for the dimensions of Volume in [dm^3] and Length in [m].

Coil processing is gaining popularity because of the lean concepts it immediately introduces into the workshop. Moreover, metal coils make production planning easier, ensure long uptimes for processing lines and quite often have lower costs per ton than sheet metal.

## How can we calculate coil length from weight, material type, width and thickness?

To calculate the coil length (L), we start from the coil weight (W) and the material density (D)

(Weight in [kg]) = (Volume)*D (Volume) = (Weight)/D L = (Volume)*1000/(W*T) L = (Weight)*1000/(D*W*T)

In some cases, parts can have variable lengths and variable cycle times; we can therefore choose to use an average length and cycle time, or calculate the running time from the metres per minute produced by the line (for example, in roll forming lines).

For example, a steel coil with D = 7.81 kg/ dm^3 and weight 3000kg has a volume of 384dm^3 and a length of 2550m.

## How can we calculate coil weight from width, outer and inner diameters?

In production planning, sometimes decisions have to be made without having the physical coil available from which to take measurements. For example, we might only have the information about coil weight, width and thickness of the material.

The following formula can be used in production to estimate the weight of coils in production, starting from their geometry The calculation is pretty simple. It starts by calculating the Volume and multiplies the value by the Density of the material.

(Volume) = 3,14/4*(OD^2-ID^2)*W (Weight in [kg]) = (Volume) * D (Weight in [kg]) = 3,14/4*(OD^2- ID^2)*W*D/1000000

The coefficient of 1000000 is used to compensate for the dimensions of Volume (mm^3) and Density (kg/dm^3).

The graphic above is an interesting tool, showing the weight per millimetre of the width of a steel coil, with an ID (Inner Diameter) of 508mm. For example, the same steel coil with OD = 1600mm, ID = 508mm and W = 250mm has a weight of 3500kg.

Just by searching the Internet, you can find various coil calculators (e.g. search Google for "metal coil calculator").

I believe that it is important to understand how these formulas are obtained, since it allows us to adapt them to different practical situations and also helps us to take quick decisions in the workshop, thanks to a faster learning curve.

For further information, see www.dallan.com

## Conclusion

## FOCUS ON PUNCH PRESSES

UK subcontractor, Weldall (Cannock) Ltd., enjoyed a return on investment of just six months with new nesting software on its punch press.

W fabrication services. It has offered a specialist bespoke sheet metal welding and fabrication service for 25 years to different sectors of UK industry.

"We specialise in supporting the construction industry and have built a reputation for reliability, quality and competitiveness. All of our products are designed using the latest 3D packages and are fabricated using new CNC machinery. Our continuous investment in machines, software and knowledge keep us at the cutting edge of our industry to support our customers' needs. We generally work with materials such as aluminium, mild steel and stainless steel." it told ISMR.

The company decided to replace its ageing Haco punch press with a new Yawei Nisshinbo HPE punch press - the first of its kind in the UK.

## An eye on productivity

Weldall's older punch press, the company explained, was being driven by a CAM system which was 'cumbersome to use and had no automation features such as tool teach or nesting'

Ryan Blower, Operations Director, Weldall (Cannock) Ltd., explained further: "Automatic tooling was basically non-existent. With the old system, you had to tell it exactly what to do....

Complex tooling could be ‘learnt' by the system and then automatically reapplied to new parts

Weldall briefly considered other CAM systems but then quickly decided to purchase JETCAM software, which was being offered by Press and Shear (the UK distributor for Yawei Nisshinbo, manufacturer of Weldall's new punch press). It ordered the new machine and software, which was installed in November 2014.

"As JETCAM already had a postprocessor to drive the machine, no development was required with only minor tweaks needed during implementation to match its specific CNC hardware configuration. JETCAM Expert Lite was selected, which allowed Weldall to get up and running at low cost but with a clear upgrade path in the future to automatic nesting and integration into other systems, such as MRP," CAM software manufacturer, JETCAM, told ISMR.

Installation and training on the punch press and software took a week, with the software itself taking one day

"We were up and running very quickly. After the training, if I ever needed something, I would contact JETCAM support and it would produce a short video tutorial to show me what to do," added Ryan Blower.

Once the company started using the system, it 'quickly saw benefits'. Complex tooling could be 'learnt' by the system and then automatically reapplied to new parts. Parts could be auto-tooled with a single click, whereas previously users would have to manually place each tool. As a result, programming time dropped by at least 50%.

Currently, Weldall utilises a nesting capability in its guillotine software which generates an optimised nest pattern. Using JETCAM's bump nesting, these can be quickly replicated using drag and drop, with automatic spacing against parts and the sheet edge ensuring that there are no overlaps of either parts or tooling.

One feature designed to make instructions to the shop floor much clearer was the built-in Advanced Reports Designer, enabling Weldall to design a comprehensive works order report detailing parts required, tooling and material, as well as including images of parts and nests.

The report could be further customised to match the company's corporate identity giving a much more professional feel to the company.

## Looking to the future

In the two years since implementation, the company has seen an increase in turnover/ profitability in line with its ambitious business plan, which Ryan Blower cites is due to the increased capacity that the combination of machine and software have delivered.

With plans for a second machine within 12-18 months, Weldall also wishes to upgrade JETCAM to include automatic nesting with the capability to go from CAD file through to optimised nests and NC code within seconds.

"We saw an ROI (Return on Investment) on the machine within 12 months but, with JETCAM software, it was closer to six months. We've also seen a few updates to the software, specifically with the new interface, that have been beneficial. Our plan is to continue with our long term-growth through continued investment in plant, machinery and technology."

## JETCAM software highlights

■ ROI of six months, based on staff time alone

■ Tool teach allows complex tooling to be learnt and replicated automatically

■ Programming time was halved

■ Bump nesting allows for quick drag and drop nest creation

■ Advanced Reports Designer enables detailed FMS report

■ Full upgrade path to complete automation

■ Software recommended by machine vendor

■ New features seen through updates via maintenance

■ Fully trained in one day

Our plan is to continue with our long term-growth through continued investment in plant, machinery and technology

Press and Shear Ltd.   
14 Ninian Park   
Tamworth   
B77 5ES   
UK

www.pressandshear.com

EVENT PREVIEW

RUSSIA REVISITED

More than 550 companies from 32 countries are expected to exhibit at Metal-Expo 2017 in Russia.

The 23rd Metal-Expo International Industrial Exhibition will showcase a range of ferrous and non-ferrous products, equipment and solutions for steel industry development. Taking place from 14-17 November 2017 at the VDNkHa showground (Hall 75) in Moscow (Russia), Metal-Expo'2017 includes a conference programme with more than 40 events which will cover pressing issues facing steel and steel-related industries. The conference will be opened by Russian Metal and Steel Market and will highlight the latest trends and future prospects in Russian and international steel markets.

"According to Worldsteel, global steel use will grow 0.5% in 2017. Demand in Russia is also expected to grow 1.5%. Metal-Expo is a barometer for new market trends, indicating possible growth points," the show organiser told ISMR. "More than 550 companies from 32 countries are expected to participate in the event, while more than 30,000 professionals will attend. Steel product end-users from segments such as construction, heavy engineering, fuel and energy, transportation and logistics, as well as the steel trading segment, will visit the show this year.

ISMR SAYS:

"Don't miss Metal-Expo in Moscow from 14-17 November 2017"

METAL EXPO

Metal-Expo'2017 includes a conference programme with more than 40 events which will cover pressing issues facing steel and steel-related industries.
